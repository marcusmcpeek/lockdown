# dalsp-2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Domain Lookup](#domain-lookup)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.0.12/24 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway | ND RA Disabled | ND RA RX Accept | ND Managed Config Flag | ND Other Config Flag | ND Cache | ND RA DNS Servers |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ | -------------- | --------------- | ---------------------- | -------------------- | -------- | ----------------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - | - | - | - | - | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 192.168.0.12/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 8.8.8.8 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
```

### Domain Lookup

#### DNS Domain Lookup Summary

| Source interface | vrf |
| ---------------- | --- |
| Management1 | MGMT |

#### DNS Domain Lookup Device Configuration

```eos
ip domain lookup vrf MGMT source-interface Management1
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

##### NTP Servers

NTP servers VRF: MGMT

| Server | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Source Address | Key |
| ------ | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | -------------- | --- |
| 0.pool.ntp.org | True | - | - | - | - | - | - | - | - |
| 1.pool.ntp.org | - | - | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 0.pool.ntp.org prefer
ntp server vrf MGMT 1.pool.ntp.org
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | UNIX-Socket | Default Services | Session Timeout |
| ---- | ----- | ----------- | ---------------- | --------------- |
| False | True | - | - | 1440 minutes |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ----------------- | --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | --- | --- | -------- | ------ | ------- |
| Ethernet1/1 | P2P_dalle-1_Ethernet50/1 | - | 172.16.30.2/31 | default | 1500 | False | - | - |
| Ethernet2/1 | P2P_dalle-2_Ethernet50/1 | - | 172.16.30.8/31 | default | 1500 | False | - | - |
| Ethernet3/1 | P2P_dalle-3_Ethernet50/1 | - | 172.16.30.14/31 | default | 1500 | False | - | - |
| Ethernet4/1 | P2P_dalle-4_Ethernet50/1 | - | 172.16.30.20/31 | default | 1500 | False | - | - |
| Ethernet5/1 | P2P_dalle-5_Ethernet50/1 | - | 172.16.30.26/31 | default | 1500 | False | - | - |
| Ethernet6/1 | P2P_dalle-6_Ethernet50/1 | - | 172.16.30.32/31 | default | 1500 | False | - | - |
| Ethernet7/1 | P2P_dalle-7_Ethernet50/1 | - | 172.16.30.38/31 | default | 1500 | False | - | - |
| Ethernet8/1 | P2P_dalle-8_Ethernet50/1 | - | 172.16.30.44/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description P2P_dalle-1_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.2/31
!
interface Ethernet2/1
   description P2P_dalle-2_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.8/31
!
interface Ethernet3/1
   description P2P_dalle-3_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.14/31
!
interface Ethernet4/1
   description P2P_dalle-4_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.20/31
!
interface Ethernet5/1
   description P2P_dalle-5_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.26/31
!
interface Ethernet6/1
   description P2P_dalle-6_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.32/31
!
interface Ethernet7/1
   description P2P_dalle-7_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.38/31
!
interface Ethernet8/1
   description P2P_dalle-8_Ethernet50/1
   no shutdown
   mtu 1500
   no switchport
   ip address 172.16.30.44/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 172.16.31.2/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Addresses |
| --------- | ----------- | --- | -------------- |
| Loopback0 | ROUTER_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 172.16.31.2/32
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | False |

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65100 | 172.16.31.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 256000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Maximum-accepted-routes | Maximum-advertised-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ----------------------- | ------------------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 172.16.30.3 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.9 | 65101 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.15 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.21 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.27 | 65103 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.33 | 65103 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.39 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.30.45 | 65104 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - | - | - |
| 172.16.31.5 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.6 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.7 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.8 | 65102 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.9 | 65103 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.10 | 65103 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.11 | 65104 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.31.12 | 65104 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Peer-tag In | Peer-tag Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ----------- | ------------ | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True | - | - | - | - | default | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65100
   router-id 172.16.31.2
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 256000
   neighbor 172.16.30.3 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.3 remote-as 65101
   neighbor 172.16.30.3 description dalle-1_Ethernet50/1
   neighbor 172.16.30.9 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.9 remote-as 65101
   neighbor 172.16.30.9 description dalle-2_Ethernet50/1
   neighbor 172.16.30.15 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.15 remote-as 65102
   neighbor 172.16.30.15 description dalle-3_Ethernet50/1
   neighbor 172.16.30.21 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.21 remote-as 65102
   neighbor 172.16.30.21 description dalle-4_Ethernet50/1
   neighbor 172.16.30.27 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.27 remote-as 65103
   neighbor 172.16.30.27 description dalle-5_Ethernet50/1
   neighbor 172.16.30.33 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.33 remote-as 65103
   neighbor 172.16.30.33 description dalle-6_Ethernet50/1
   neighbor 172.16.30.39 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.39 remote-as 65104
   neighbor 172.16.30.39 description dalle-7_Ethernet50/1
   neighbor 172.16.30.45 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.16.30.45 remote-as 65104
   neighbor 172.16.30.45 description dalle-8_Ethernet50/1
   neighbor 172.16.31.5 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.5 remote-as 65101
   neighbor 172.16.31.5 description dalle-1_Loopback0
   neighbor 172.16.31.6 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.6 remote-as 65101
   neighbor 172.16.31.6 description dalle-2_Loopback0
   neighbor 172.16.31.7 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.7 remote-as 65102
   neighbor 172.16.31.7 description dalle-3_Loopback0
   neighbor 172.16.31.8 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.8 remote-as 65102
   neighbor 172.16.31.8 description dalle-4_Loopback0
   neighbor 172.16.31.9 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.9 remote-as 65103
   neighbor 172.16.31.9 description dalle-5_Loopback0
   neighbor 172.16.31.10 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.10 remote-as 65103
   neighbor 172.16.31.10 description dalle-6_Loopback0
   neighbor 172.16.31.11 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.11 remote-as 65104
   neighbor 172.16.31.11 description dalle-7_Loopback0
   neighbor 172.16.31.12 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.31.12 remote-as 65104
   neighbor 172.16.31.12 description dalle-8_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.16.31.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 172.16.31.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
