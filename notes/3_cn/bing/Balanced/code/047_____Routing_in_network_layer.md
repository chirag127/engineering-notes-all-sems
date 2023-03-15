### Routing in network layer

Routing is the process of finding the best path for a packet to reach its destination in a network. Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model. A router forwards the packet based on the information available in the packet header and forwarding table. The routing algorithms are used for routing the packets.

There are different types of routing in computer networks, such as:

- Static routing: The routes are manually configured and rarely changed.
- Dynamic routing: The routes are automatically updated depending on the network conditions.
- Unicast routing: The packet is sent to a single destination.
- Multicast routing: The packet is sent to a group of destinations.
- Broadcast routing: The packet is sent to all the destinations in the network.
- Anycast routing: The packet is sent to the nearest destination among a group of destinations.

Routing can be classified into two categories based on the scope of the network:

- Interior routing: The routing within a single autonomous system (AS), which is a group of routers under the same administrative control. Examples of interior routing protocols are RIP, OSPF, and EIGRP.
- Exterior routing: The routing between different autonomous systems. Examples of exterior routing protocols are BGP and EGP.

Routing can also be classified into two categories based on the information used for routing decisions:

- Distance vector routing: The router maintains a vector of distances to each destination and exchanges it with its neighbors periodically. The router chooses the shortest path based on the distance vector. Examples of distance vector routing protocols are RIP and EIGRP.
- Link state routing: The router maintains a map of the entire network and calculates the shortest path to each destination using an algorithm such as Dijkstra's or Bellman-Ford. The router updates its map whenever there is a change in the network topology. Examples of link state routing protocols are OSPF and IS-IS.