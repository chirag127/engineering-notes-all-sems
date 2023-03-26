### Temporary Ordered Routing Algorithm (TORA)

- TORA is a distributed routing protocol used in mobile ad hoc networks (MANETs).
- It is a reactive protocol, which means that it only establishes routes when needed.
- TORA is based on the concept of using height as a metric for routing.
- Nodes in the network are assigned a height value, which indicates their position in the network.
- The height value is used to determine the shortest path to a destination node.
- TORA uses three types of packets: query, update, and control.
- When a node needs to send a packet to a destination node, it broadcasts a query packet.
- The destination node responds with an update packet containing its height value.
- The node then broadcasts a control packet to inform the other nodes of the new route.
- TORA is capable of handling network partitions and is resilient to node failures.
- It is also able to adapt to changes in network topology and can quickly establish new routes when needed.
- TORA has been shown to perform well in dense networks with high mobility.
- However, it can suffer from high overhead and can be inefficient in sparse networks.
- TORA is a useful protocol for MANETs and provides a reliable and efficient way of establishing routes in dynamic networks.