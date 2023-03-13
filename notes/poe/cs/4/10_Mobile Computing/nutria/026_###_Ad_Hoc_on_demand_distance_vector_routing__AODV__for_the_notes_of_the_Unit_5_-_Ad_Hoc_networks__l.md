
### Ad Hoc on demand distance vector routing (AODV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

AODV is a routing protocol designed for mobile ad-hoc networks (MANETs). It is a reactive routing protocol, meaning that it only establishes routes when needed. AODV is an on-demand routing protocol, meaning that it only establishes routes when needed. It is a distance-vector routing protocol, meaning that it uses hop-counts to determine the best route between two nodes.

AODV works by flooding the network with route request (RREQ) packets. When a node receives an RREQ packet, it will broadcast it to its neighbors. The neighbors will then forward the packet to their neighbors, and so on, until the packet reaches its destination. When the destination node receives the RREQ packet, it will generate a route reply (RREP) packet and send it back to the source node. The RREP packet contains information about the route from the destination node to the source node.

AODV has several advantages over other routing protocols. It is easy to implement, and it is relatively efficient in terms of bandwidth and memory usage. AODV also provides loop-free routing, meaning that it avoids the creation of loops in the network. It also supports multicast routing, meaning that it can be used to send data to multiple nodes at the same time.

In terms of mnemonics and learning tricks, one way to remember AODV is to think of it as an "On Demand Distance Vector" routing protocol. This will help you to remember the basic characteristics of AODV. Additionally, you can use the acronym "RREQ" to remember the Route Request packet, and "RREP" to remember the Route Reply packet.