#### Spanning Tree Algorithms in Local Area Network

- Spanning tree algorithms are used to eliminate loops in a bridged Ethernet local area network (LAN) by creating a logical tree topology that connects all the nodes without cycles .
- The most common spanning tree algorithm is the Spanning Tree Protocol (STP), which was invented by Dr. Radia Perlman, distinguished engineer at Sun Microsystems.
- STP works by electing a root bridge among all the bridges in the network, and then determining the best path from the root bridge to each node based on the link costs and bridge identifiers.
- STP uses special messages called Bridge Protocol Data Units (BPDUs) to exchange information among the bridges and to detect topology changes .
- STP assigns different states to each port of a bridge, such as blocking, listening, learning, forwarding, or disabled, to prevent loops and ensure connectivity .
- STP has some issues, such as performance, scalability, unidirectional links, and root bridge placement, that can affect the network efficiency and reliability.
- STP can be improved by using variants or extensions, such as Rapid Spanning Tree Protocol (RSTP), Multiple Spanning Tree Protocol (MSTP), or Per-VLAN Spanning Tree Protocol (PVSTP).
- A simple mnemonic to remember the port states of STP is BLFD: Blocking, Listening, Forwarding, Disabled.
- A simple mnemonic to remember the order of criteria for selecting the root bridge of STP is BPR: Bridge Priority, then MAC address.
- A simple mnemonic to remember the order of criteria for selecting the root port of STP is RPC: Root Path Cost, then Bridge Priority, then Port Priority, then Port Number.
- A simple mnemonic to remember the order of criteria for selecting the designated port of STP is RPC: Root Path Cost, then Bridge Priority, then Port Priority, then Port Number.
- A simple ASCII diagram of a spanning tree topology is shown below:

```
    +-----+      +-----+      +-----+
    |  A  |------|  B  |------|  C  |
    +-----+      +-----+      +-----+
      |            |            |
      |            |            |
      |            |            |
    +-----+      +-----+      +-----+
    |  D  |------|  E  |------|  F  |
    +-----+      +-----+      +-----+
```

- In this example, suppose bridge B has the lowest bridge identifier and is elected as the root bridge. Then, the ports connecting to the root bridge are the root ports for the other bridges (A, C, D, E, F). The ports connecting to the non-root bridges are the designated ports for the segments (A-B, B-C, D-E, E-F). The ports that are not root or designated are blocked to prevent loops (A-D, C-F, B-E). The resulting spanning tree is shown below with the port states:

```
    +-----+      +-----+      +-----+
    |  A  |---F--|  B  |---F--|  C  |
    +-----+      +-----+      +-----+
      |            |            |
      |            |            |
      |            |            |
    +-----+      +-----+      +-----+
    |  D  |---F--|  E  |---F--|  F  |
    +-----+      +-----+      +-----+

    F: Forwarding
    B: Blocking
```