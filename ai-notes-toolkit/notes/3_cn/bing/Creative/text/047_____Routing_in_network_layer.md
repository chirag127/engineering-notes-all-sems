### Routing in network layer

- Routing is the process of finding a path from a source to a destination in a network of nodes, such as routers, switches, or hosts.
- Routing is performed by network layer protocols, such as IP, that operate on logical addresses, such as IP addresses, rather than physical addresses, such as MAC addresses.
- Routing can be classified into two types: static routing and dynamic routing.
- Static routing is when the routes are manually configured by the network administrator and do not change unless updated manually. Static routing is simple, secure, and predictable, but it is not scalable, adaptable, or efficient.
- Dynamic routing is when the routes are automatically learned and updated by the network devices using routing protocols, such as RIP, OSPF, or BGP. Dynamic routing is scalable, adaptable, and efficient, but it is more complex, less secure, and less predictable.
- Routing protocols can be further classified into two types: distance vector protocols and link state protocols.
- Distance vector protocols are based on the principle of exchanging distance information, such as hop count or cost, with neighboring nodes. Each node maintains a routing table that contains the best known distance and next hop for each destination. Examples of distance vector protocols are RIP and BGP.
- Link state protocols are based on the principle of exchanging topology information, such as link status and cost, with all nodes in the network. Each node maintains a link state database that contains the complete network topology. Each node then runs a shortest path algorithm, such as Dijkstra's algorithm, to compute the best path for each destination. Examples of link state protocols are OSPF and IS-IS.