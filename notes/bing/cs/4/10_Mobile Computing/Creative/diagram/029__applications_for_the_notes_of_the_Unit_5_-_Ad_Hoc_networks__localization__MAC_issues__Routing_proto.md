An ad hoc network is a wireless network that does not rely on any fixed infrastructure or centralized administration. It consists of a collection of nodes that can communicate with each other directly or through intermediate nodes. Ad hoc networks can be used for various applications, such as military, vehicular, sensor, and smartphone networks   .

The following diagram illustrates the basic architecture of an ad hoc network:

```
    +-----+     +-----+     +-----+     +-----+
    |  A  |-----|  B  |-----|  C  |-----|  D  |
    +-----+     +-----+     +-----+     +-----+
       |           |           |           |
       |           |           |           |
       |           |           |           |
    +-----+     +-----+     +-----+     +-----+
    |  E  |-----|  F  |-----|  G  |-----|  H  |
    +-----+     +-----+     +-----+     +-----+
       |           |           |           |
       |           |           |           |
       |           |           |           |
    +-----+     +-----+     +-----+     +-----+
    |  I  |-----|  J  |-----|  K  |-----|  L  |
    +-----+     +-----+     +-----+     +-----+
```

Each node (A-L) represents a device that can send and receive data packets over wireless links. The links between the nodes indicate the possible communication paths. For example, node A can communicate directly with nodes B and E, but not with nodes C, D, H, or L. To communicate with node L, node A has to use intermediate nodes, such as B, C, G, and K. This is called multi-hop routing.

Some of the challenges and issues in ad hoc networks are:

- Localization: How to determine the position of the nodes in the network without relying on GPS or other external sources.
- MAC (Medium Access Control): How to coordinate the access to the shared wireless channel among the nodes and avoid collisions and interference.
- Routing: How to find and maintain the optimal paths between the source and destination nodes in a dynamic and decentralized network.
- Global State Routing (GSR): A routing protocol that uses periodic exchange of network topology information among the nodes to update the routing tables. It is suitable for small and stable networks, but suffers from high overhead and scalability issues in large and dynamic networks.