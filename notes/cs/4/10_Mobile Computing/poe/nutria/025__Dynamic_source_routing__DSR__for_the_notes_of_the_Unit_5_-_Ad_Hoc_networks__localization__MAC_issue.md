

### Dynamic Source Routing (DSR)

* DSR is a routing protocol used in mobile ad hoc networks (MANETs). It is a reactive routing protocol, meaning that it only establishes routes when needed. 
* DSR is based on source routing, meaning that the sender of a packet specifies the route that the packet should take through the network. 
* DSR uses two main types of messages: Route Request (RREQ) and Route Reply (RREP). 
* When a node needs to send a packet, it sends a RREQ to discover a route to the destination. All nodes that receive the RREQ will record the route in their route cache and then forward the RREQ to their neighbors. 
* When the destination node receives the RREQ, it sends a RREP back to the source node, which contains the route from the destination to the source. 
* The source node then caches the route and sends the packet along the route. 
* DSR also supports route caching and route maintenance. When a node sends a packet and receives a RREP, the node stores the route in its route cache. When the node needs to send a packet again, it can use the cached route instead of sending a RREQ. 
* If a node detects a link failure while sending a packet, it can send a Route Error (RERR) message to the source node. The source node can then use its route cache to find an alternate route. 
* DSR is an efficient and scalable protocol, but it is also vulnerable to certain attacks, such as routing loops and malicious nodes.