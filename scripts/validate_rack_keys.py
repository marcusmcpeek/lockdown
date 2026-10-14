#!/usr/bin/env python3
"""Validate RACK endpoint files against locked baselines.

Only adapter-level keys in ALLOWED_ADAPTER_KEYS may differ from the baseline.
All other keys (host-level and adapter-level) are locked. Structural changes
(adding/removing hosts or adapters) are also violations.

Exit 0 = validation passed, exit 1 = violations found.
"""

import argparse
import glob
import os
import sys

import yaml

ALLOWED_ADAPTER_KEYS = {"vlans", "enabled", "port_channel", "mode", "speed"}


def validate_file(baseline_path, live_path):
    violations = []

    with open(baseline_path) as f:
        baseline = yaml.safe_load(f)
    with open(live_path) as f:
        live = yaml.safe_load(f)

    if baseline is None:
        violations.append("Baseline file is empty or unparseable")
        return violations
    if live is None:
        violations.append("Live file is empty or unparseable")
        return violations

    for top_key in baseline:
        if top_key not in live:
            violations.append(f"Top-level key '{top_key}' was removed")
            continue

        baseline_hosts = baseline[top_key]
        live_hosts = live[top_key]

        if not isinstance(baseline_hosts, list) or not isinstance(live_hosts, list):
            if baseline_hosts != live_hosts:
                violations.append(f"Top-level key '{top_key}' value changed")
            continue

        if len(live_hosts) != len(baseline_hosts):
            violations.append(
                f"'{top_key}': host count changed from {len(baseline_hosts)} "
                f"to {len(live_hosts)} (adding/removing hosts is restricted)"
            )
            continue

        for host_idx, (b_host, l_host) in enumerate(zip(baseline_hosts, live_hosts)):
            host_name = b_host.get("name", f"index-{host_idx}")

            for key in b_host:
                if key == "adapters":
                    continue
                if key not in l_host:
                    violations.append(f"Host '{host_name}': locked key '{key}' was removed")
                elif b_host[key] != l_host[key]:
                    violations.append(
                        f"Host '{host_name}': locked key '{key}' changed: "
                        f"{b_host[key]!r} -> {l_host[key]!r}"
                    )

            for key in l_host:
                if key in ("adapters",) or key in b_host:
                    continue
                violations.append(
                    f"Host '{host_name}': new locked key '{key}' added (not in baseline)"
                )

            b_adapters = b_host.get("adapters", [])
            l_adapters = l_host.get("adapters", [])

            if len(l_adapters) != len(b_adapters):
                violations.append(
                    f"Host '{host_name}': adapter count changed from "
                    f"{len(b_adapters)} to {len(l_adapters)}"
                )
                continue

            for adp_idx, (b_adp, l_adp) in enumerate(zip(b_adapters, l_adapters)):
                adp_label = f"Host '{host_name}', adapter #{adp_idx + 1}"

                for key in b_adp:
                    if key in ALLOWED_ADAPTER_KEYS:
                        continue
                    if key not in l_adp:
                        violations.append(f"{adp_label}: locked key '{key}' was removed")
                    elif b_adp[key] != l_adp[key]:
                        violations.append(
                            f"{adp_label}: locked key '{key}' changed: "
                            f"{b_adp[key]!r} -> {l_adp[key]!r}"
                        )

                for key in l_adp:
                    if key in ALLOWED_ADAPTER_KEYS or key in b_adp:
                        continue
                    violations.append(
                        f"{adp_label}: new locked key '{key}' added (not in baseline)"
                    )

    for top_key in live:
        if top_key not in baseline:
            violations.append(f"New top-level key '{top_key}' added (not in baseline)")

    return violations


def main():
    parser = argparse.ArgumentParser(
        description="Validate RACK files against locked baselines"
    )
    parser.add_argument(
        "--baselines-dir", default="baselines/SERVERS/",
        help="Directory containing *.yml.baseline files",
    )
    parser.add_argument(
        "--servers-dir", default="inventory/group_vars/SERVERS/",
        help="Directory containing live RACK*.yml files",
    )
    args = parser.parse_args()

    all_violations = {}
    baseline_files = sorted(glob.glob(os.path.join(args.baselines_dir, "*.yml.baseline")))

    if not baseline_files:
        print("WARNING: No baseline files found. Skipping validation.")
        sys.exit(0)

    for bp in baseline_files:
        filename = os.path.basename(bp).replace(".baseline", "")
        live_path = os.path.join(args.servers_dir, filename)

        if not os.path.exists(live_path):
            all_violations[filename] = [f"Live file '{live_path}' is missing"]
            continue

        violations = validate_file(bp, live_path)
        if violations:
            all_violations[filename] = violations

    # Flag RACK files that exist without a corresponding baseline
    live_rack_files = sorted(glob.glob(os.path.join(args.servers_dir, "RACK*.yml")))
    baseline_filenames = {
        os.path.basename(bp).replace(".baseline", "") for bp in baseline_files
    }
    for lf in live_rack_files:
        fn = os.path.basename(lf)
        if fn not in baseline_filenames:
            all_violations.setdefault(fn, []).append(
                f"No baseline exists for '{fn}'. "
                f"A network admin must run lock_baselines.sh first."
            )

    if all_violations:
        print("=" * 60)
        print("VALIDATION FAILED: Restricted keys were modified")
        print("=" * 60)
        for filename, violations in sorted(all_violations.items()):
            print(f"\n  {filename}:")
            for v in violations:
                print(f"    - {v}")
        print(
            "\nBuild aborted. Contact the network admin to update "
            "baselines if structural changes are intended."
        )
        sys.exit(1)
    else:
        print("Baseline validation passed: no restricted keys were modified.")
        sys.exit(0)


if __name__ == "__main__":
    main()
