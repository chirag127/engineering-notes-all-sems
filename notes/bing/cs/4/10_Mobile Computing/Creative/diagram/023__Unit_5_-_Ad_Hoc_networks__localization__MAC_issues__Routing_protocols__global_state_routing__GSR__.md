## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over a shared wireless channel. Localization is the process of determining the position of a node in an ad hoc network, which is useful for many applications and services. MAC issues refer to the challenges of coordinating the access to the wireless channel among the nodes, such as avoiding collisions, maximizing throughput, and minimizing energy consumption. Routing protocols are the algorithms that enable the nodes to discover and maintain routes to other nodes in the network. Global state routing (GSR) is a proactive routing protocol that extends the link state routing of wired networks to ad hoc networks.

The following diagram illustrates the basic architecture of an ad hoc network and the components of GSR:

```
    +-----+     +-----+     +-----+     +-----+
    | A   |-----| B   |-----| C   |-----| D   |
    +-----+     +-----+     +-----+     +-----+
      |           |           |           |
      |           |           |           |
      |           |           |           |
    +-----+     +-----+     +-----+     +-----+
    | E   |-----| F   |-----| G   |-----| H   |
    +-----+     +-----+     +-----+     +-----+

    A, B, C, D, E, F, G, H: mobile nodes
    -----: wireless link
    |: wireless range

    GSR components:

    - Link state table: each node maintains a table of its current links and their costs (e.g., hop count, signal strength, etc.)
    - Neighbor table: each node maintains a table of its current neighbors and their link state sequence numbers
    - Topology table: each node maintains a table of the entire network topology based on the link state information received from other nodes
    - Routing table: each node maintains a table of the best routes to all other nodes based on the topology table and a shortest path algorithm (e.g., Dijkstra's algorithm)
```