 Here is the content in markdown format for the topic - ### Temporary ordered routing algorithm (TORA) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Temporary Ordered Routing Algorithm (TORA)

- TORA is a link-state routing protocol for mobile ad-hoc networks.
- It is an on-demand routing protocol which establishes routes quickly when required.
- TORA uses the concept of directed acyclic graph (DAG) for efficient route establishment.
- The main goals of TORA are to establish routes quickly and to maintain routing information efficiently.

**How TORA Works?**

1. When a source node wants to send data to a destination node and does not have a route, it initiates a route discovery process by broadcasting a QUERY packet to its neighbors.
2. Each intermediate node receiving the QUERY packet sets up a reverse route towards the source node and forwards the QUERY packet to its neighbors.
3. When the QUERY packet reaches the destination, the destination node sends a REPLY packet along the reverse route set up by the QUERY packet.
4. Each intermediate node receiving the REPLY packet directs the link towards the destination node to establish a forward route and forwards the REPLY packet towards the source node.
5. Once the source node receives the REPLY packet, it can send data along the established route.

**Features of TORA**

- TORA is a reactive routing protocol and establishes routes on-demand.
- TORA supports multiple paths to the destination using the concept of directed acyclic graph.
- TORA uses the height metric to find the shortest path to the destination. The height indicates the number of hops to the destination.
- The control messages are localized to a small set of nodes thereby reducing the routing overhead.
- TORA performs well even with high mobility and can quickly adapt to changing network topology.

**Advantages and Disadvantages of TORA**

Advantages:
- On-demand route establishment leading to reduced routing overhead
- Support for multiple paths
- Effective in highly dynamic networks

Disadvantages:
- Complex protocol
- Slow convergence
- Excessive flooding of control packets can lead to congestion