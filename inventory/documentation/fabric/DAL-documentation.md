# DAL

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DAL_DC1 | l3leaf | dalle-1 | 192.168.0.14/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-2 | 192.168.0.15/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-3 | 192.168.0.16/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-4 | 192.168.0.17/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-5 | 192.168.0.18/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-6 | 192.168.0.19/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-7 | 192.168.0.20/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | l3leaf | dalle-8 | 192.168.0.21/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | spine | dalsp-1 | 192.168.0.11/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | spine | dalsp-2 | 192.168.0.12/24 | vEOS-LAB | Provisioned | - |
| DAL_DC1 | spine | dalsp-3 | 192.168.0.13/24 | vEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | --------- | -------------- |
| l3leaf | dalle-1 | Ethernet49/1 | spine | dalsp-1 | Ethernet1/1 |
| l3leaf | dalle-1 | Ethernet50/1 | spine | dalsp-2 | Ethernet1/1 |
| l3leaf | dalle-1 | Ethernet51/1 | spine | dalsp-3 | Ethernet1/1 |
| l3leaf | dalle-1 | Ethernet55/1 | mlag_peer | dalle-2 | Ethernet55/1 |
| l3leaf | dalle-1 | Ethernet56/1 | mlag_peer | dalle-2 | Ethernet56/1 |
| l3leaf | dalle-2 | Ethernet49/1 | spine | dalsp-1 | Ethernet2/1 |
| l3leaf | dalle-2 | Ethernet50/1 | spine | dalsp-2 | Ethernet2/1 |
| l3leaf | dalle-2 | Ethernet51/1 | spine | dalsp-3 | Ethernet2/1 |
| l3leaf | dalle-3 | Ethernet49/1 | spine | dalsp-1 | Ethernet3/1 |
| l3leaf | dalle-3 | Ethernet50/1 | spine | dalsp-2 | Ethernet3/1 |
| l3leaf | dalle-3 | Ethernet51/1 | spine | dalsp-3 | Ethernet3/1 |
| l3leaf | dalle-3 | Ethernet55/1 | mlag_peer | dalle-4 | Ethernet55/1 |
| l3leaf | dalle-3 | Ethernet56/1 | mlag_peer | dalle-4 | Ethernet56/1 |
| l3leaf | dalle-4 | Ethernet49/1 | spine | dalsp-1 | Ethernet4/1 |
| l3leaf | dalle-4 | Ethernet50/1 | spine | dalsp-2 | Ethernet4/1 |
| l3leaf | dalle-4 | Ethernet51/1 | spine | dalsp-3 | Ethernet4/1 |
| l3leaf | dalle-5 | Ethernet49/1 | spine | dalsp-1 | Ethernet5/1 |
| l3leaf | dalle-5 | Ethernet50/1 | spine | dalsp-2 | Ethernet5/1 |
| l3leaf | dalle-5 | Ethernet51/1 | spine | dalsp-3 | Ethernet5/1 |
| l3leaf | dalle-5 | Ethernet55/1 | mlag_peer | dalle-6 | Ethernet55/1 |
| l3leaf | dalle-5 | Ethernet56/1 | mlag_peer | dalle-6 | Ethernet56/1 |
| l3leaf | dalle-6 | Ethernet49/1 | spine | dalsp-1 | Ethernet6/1 |
| l3leaf | dalle-6 | Ethernet50/1 | spine | dalsp-2 | Ethernet6/1 |
| l3leaf | dalle-6 | Ethernet51/1 | spine | dalsp-3 | Ethernet6/1 |
| l3leaf | dalle-7 | Ethernet49/1 | spine | dalsp-1 | Ethernet7/1 |
| l3leaf | dalle-7 | Ethernet50/1 | spine | dalsp-2 | Ethernet7/1 |
| l3leaf | dalle-7 | Ethernet51/1 | spine | dalsp-3 | Ethernet7/1 |
| l3leaf | dalle-7 | Ethernet55/1 | mlag_peer | dalle-8 | Ethernet55/1 |
| l3leaf | dalle-7 | Ethernet56/1 | mlag_peer | dalle-8 | Ethernet56/1 |
| l3leaf | dalle-8 | Ethernet49/1 | spine | dalsp-1 | Ethernet8/1 |
| l3leaf | dalle-8 | Ethernet50/1 | spine | dalsp-2 | Ethernet8/1 |
| l3leaf | dalle-8 | Ethernet51/1 | spine | dalsp-3 | Ethernet8/1 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.30.0/24 | 256 | 48 | 18.75 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dalle-1 | Ethernet49/1 | 172.16.30.1/31 | dalsp-1 | Ethernet1/1 | 172.16.30.0/31 |
| dalle-1 | Ethernet50/1 | 172.16.30.3/31 | dalsp-2 | Ethernet1/1 | 172.16.30.2/31 |
| dalle-1 | Ethernet51/1 | 172.16.30.5/31 | dalsp-3 | Ethernet1/1 | 172.16.30.4/31 |
| dalle-2 | Ethernet49/1 | 172.16.30.7/31 | dalsp-1 | Ethernet2/1 | 172.16.30.6/31 |
| dalle-2 | Ethernet50/1 | 172.16.30.9/31 | dalsp-2 | Ethernet2/1 | 172.16.30.8/31 |
| dalle-2 | Ethernet51/1 | 172.16.30.11/31 | dalsp-3 | Ethernet2/1 | 172.16.30.10/31 |
| dalle-3 | Ethernet49/1 | 172.16.30.13/31 | dalsp-1 | Ethernet3/1 | 172.16.30.12/31 |
| dalle-3 | Ethernet50/1 | 172.16.30.15/31 | dalsp-2 | Ethernet3/1 | 172.16.30.14/31 |
| dalle-3 | Ethernet51/1 | 172.16.30.17/31 | dalsp-3 | Ethernet3/1 | 172.16.30.16/31 |
| dalle-4 | Ethernet49/1 | 172.16.30.19/31 | dalsp-1 | Ethernet4/1 | 172.16.30.18/31 |
| dalle-4 | Ethernet50/1 | 172.16.30.21/31 | dalsp-2 | Ethernet4/1 | 172.16.30.20/31 |
| dalle-4 | Ethernet51/1 | 172.16.30.23/31 | dalsp-3 | Ethernet4/1 | 172.16.30.22/31 |
| dalle-5 | Ethernet49/1 | 172.16.30.25/31 | dalsp-1 | Ethernet5/1 | 172.16.30.24/31 |
| dalle-5 | Ethernet50/1 | 172.16.30.27/31 | dalsp-2 | Ethernet5/1 | 172.16.30.26/31 |
| dalle-5 | Ethernet51/1 | 172.16.30.29/31 | dalsp-3 | Ethernet5/1 | 172.16.30.28/31 |
| dalle-6 | Ethernet49/1 | 172.16.30.31/31 | dalsp-1 | Ethernet6/1 | 172.16.30.30/31 |
| dalle-6 | Ethernet50/1 | 172.16.30.33/31 | dalsp-2 | Ethernet6/1 | 172.16.30.32/31 |
| dalle-6 | Ethernet51/1 | 172.16.30.35/31 | dalsp-3 | Ethernet6/1 | 172.16.30.34/31 |
| dalle-7 | Ethernet49/1 | 172.16.30.37/31 | dalsp-1 | Ethernet7/1 | 172.16.30.36/31 |
| dalle-7 | Ethernet50/1 | 172.16.30.39/31 | dalsp-2 | Ethernet7/1 | 172.16.30.38/31 |
| dalle-7 | Ethernet51/1 | 172.16.30.41/31 | dalsp-3 | Ethernet7/1 | 172.16.30.40/31 |
| dalle-8 | Ethernet49/1 | 172.16.30.43/31 | dalsp-1 | Ethernet8/1 | 172.16.30.42/31 |
| dalle-8 | Ethernet50/1 | 172.16.30.45/31 | dalsp-2 | Ethernet8/1 | 172.16.30.44/31 |
| dalle-8 | Ethernet51/1 | 172.16.30.47/31 | dalsp-3 | Ethernet8/1 | 172.16.30.46/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.16.31.0/24 | 256 | 11 | 4.3 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DAL_DC1 | dalle-1 | 172.16.31.5/32 |
| DAL_DC1 | dalle-2 | 172.16.31.6/32 |
| DAL_DC1 | dalle-3 | 172.16.31.7/32 |
| DAL_DC1 | dalle-4 | 172.16.31.8/32 |
| DAL_DC1 | dalle-5 | 172.16.31.9/32 |
| DAL_DC1 | dalle-6 | 172.16.31.10/32 |
| DAL_DC1 | dalle-7 | 172.16.31.11/32 |
| DAL_DC1 | dalle-8 | 172.16.31.12/32 |
| DAL_DC1 | dalsp-1 | 172.16.31.1/32 |
| DAL_DC1 | dalsp-2 | 172.16.31.2/32 |
| DAL_DC1 | dalsp-3 | 172.16.31.3/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 172.16.32.0/24 | 256 | 8 | 3.13 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DAL_DC1 | dalle-1 | 172.16.32.5/32 |
| DAL_DC1 | dalle-2 | 172.16.32.5/32 |
| DAL_DC1 | dalle-3 | 172.16.32.7/32 |
| DAL_DC1 | dalle-4 | 172.16.32.7/32 |
| DAL_DC1 | dalle-5 | 172.16.32.9/32 |
| DAL_DC1 | dalle-6 | 172.16.32.9/32 |
| DAL_DC1 | dalle-7 | 172.16.32.11/32 |
| DAL_DC1 | dalle-8 | 172.16.32.11/32 |
