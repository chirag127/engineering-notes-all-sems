#### Learning bridge algorithms in local area network

A learning bridge is a device that connects two or more local area networks (LANs) and forwards frames based on the destination address of the frames. A learning bridge learns the location of the hosts by observing the source address of the incoming frames and builds a bridging table that maps each host address to the corresponding network interface. A learning bridge uses this table to forward frames to the appropriate interface or to flood them to all interfaces if the destination is unknown. A learning bridge can also implement the spanning tree protocol (STP) to avoid loops in the network topology and to create a tree-like structure of the connected LANs.

A learning bridge algorithm is a set of rules or procedures that a learning bridge follows to perform its functions. There are different learning bridge algorithms that can be used in different scenarios, such as transparent bridging, source routing, or adaptive routing. Here, we will focus on the transparent bridging algorithm, which is the most common and widely used learning bridge algorithm.

The transparent bridging algorithm consists of the following steps:

1. Initialization: When a bridge is powered on, it initializes its bridging table to be empty and sets all its ports to the forwarding state.
2. Learning: When a bridge receives a frame on one of its ports, it checks the source address of the frame and updates its bridging table with the entry (source address, port number, timestamp). If the entry already exists, it updates the timestamp. If the entry does not exist, it adds a new entry. The timestamp is used to age out the entries that are not updated for a long time.
3. Forwarding: After updating the bridging table, the bridge checks the destination address of the frame. If the destination address is a broadcast or a multicast address, or if the destination address is not found in the bridging table, the bridge floods the frame to all its ports except the one on which the frame was received. If the destination address is found in the bridging table, the bridge forwards the frame to the port indicated by the entry, unless it is the same as the incoming port, in which case the frame is discarded.
4. Loop prevention: To prevent loops in the network, the bridge implements the STP, which is a distributed algorithm that elects a root bridge among all the bridges in the network and computes a spanning tree of the LANs that minimizes the path cost from each bridge to the root bridge. The STP also assigns a role to each port of each bridge: root port, designated port, or blocked port. A root port is the port that connects a bridge to the root bridge or to the bridge that is closest to the root bridge. A designated port is the port that connects a bridge to a LAN segment and provides the best path from that segment to the root bridge. A blocked port is a port that is neither a root port nor a designated port and is disabled to avoid loops. The STP uses special frames called bridge protocol data units (BPDUs) to exchange information among the bridges and to determine the root bridge, the port roles, and the spanning tree. The STP also adapts to changes in the network topology, such as link failures or additions, by recomputing the spanning tree and the port roles.

The following diagram illustrates the basic architecture of a transparent bridging network with four LANs (A, B, C, and D) and three bridges (1, 2, and 3). The diagram also shows the bridging tables of each bridge, the port roles of each port, and the spanning tree of the network. The root bridge is bridge 1, and the root ports are marked with R, the designated ports are marked with D, and the blocked ports are marked with B.

```
    +-----+     +-----+     +-----+
    |  A  |-----|  1  |-----|  B  |
    +-----+     +-----+     +-----+
                 |   |
                 |   |       +-----+
                 |   |       |  C  |
                 |   |       +-----+
                 |   |         |
                 |   |         |
                 |   |         |
                 |   |         |
                 |   |       +-----+
                 |   |       |  3  |
                 |   |       +-----+
                 |   |         |
                 |   |         |
                 |   |         |
                 |   |         |
                 |   |       +-----+
                 |   |       |  D  |
                 |   |       +-----