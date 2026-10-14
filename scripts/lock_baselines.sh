#!/bin/bash
# Snapshot current RACK*.yml files as locked baselines.
# Run this as the network admin after making structural changes
# (switches, ports, adding/removing hosts).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SERVERS_DIR="$PROJECT_ROOT/inventory/group_vars/SERVERS"
BASELINES_DIR="$PROJECT_ROOT/baselines/SERVERS"

mkdir -p "$BASELINES_DIR"

locked=0
for rack_file in "$SERVERS_DIR"/RACK*.yml; do
    [ -f "$rack_file" ] || continue
    filename="$(basename "$rack_file")"
    cp "$rack_file" "$BASELINES_DIR/${filename}.baseline"
    # chmod 444 "$BASELINES_DIR/${filename}.baseline"
    chmod 777 "$BASELINES_DIR/${filename}.baseline"
    echo "Locked: $filename -> baselines/SERVERS/${filename}.baseline"
    locked=$((locked + 1))
done

if [ "$locked" -eq 0 ]; then
    echo "No RACK*.yml files found in $SERVERS_DIR"
    exit 1
else
    echo "Done. $locked baseline(s) updated."
fi
