### Routing in network layer

- Routing is the process of finding a path from a source to a destination in a network of nodes, such as routers, switches, or hosts.
- Routing is performed by the network layer, which is responsible for delivering packets across different networks.
- Routing can be classified into two types: static routing and dynamic routing.
- Static routing is when the routes are manually configured by the network administrator and do not change unless updated manually.
- Dynamic routing is when the routes are automatically learned and updated by the routers using routing protocols, such as RIP, OSPF, EIGRP, BGP, etc.
- Routing protocols can be further classified into two types: distance vector and link state.
- Distance vector protocols are based on the principle of exchanging distance information (such as hop count or cost) with neighboring routers. Each router maintains a routing table that contains the best known distance to each destination and the next hop to reach it. Examples of distance vector protocols are RIP and EIGRP.
- Link state protocols are based on the principle of exchanging topology information (such as link status, bandwidth, delay, etc.) with all routers in the network. Each router maintains a link state database that contains the complete map of the network and uses a shortest path algorithm (such as Dijkstra's or Bellman-Ford) to compute the best path to each destination. Examples of link state protocols are OSPF and IS-IS.
- Routing can also be classified into two types: unicast and multicast.
- Unicast routing is when a packet is sent from a single source to a single destination. Unicast routing can use any of the routing protocols mentioned above.
- Multicast routing is when a packet is sent from a single source to a group of destinations that share a common interest in the packet. Multicast routing requires special protocols that can build and maintain multicast trees, such as DVMRP, PIM, MOSPF, etc.