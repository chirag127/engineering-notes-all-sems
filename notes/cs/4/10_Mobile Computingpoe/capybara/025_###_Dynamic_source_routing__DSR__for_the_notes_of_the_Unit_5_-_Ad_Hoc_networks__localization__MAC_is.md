### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

Dynamic Source Routing (DSR) is a reactive routing protocol for mobile ad hoc networks (MANETs). It is a type of on-demand routing protocol that uses source routing to forward packets. Here are the key points to know about DSR:

- **Route Discovery**: When a node wants to send a packet to a destination node, it first broadcasts a Route Request (RREQ) message. The RREQ contains the source node's address, the destination node's address, and a unique identifier. Each intermediate node that receives the RREQ checks its routing table to see if it has a route to the destination node. If the node does not have a route, it rebroadcasts the RREQ to its neighbors. This process continues until the RREQ reaches the destination node, or a node that has a route to the destination node.
- **Route Reply**: When the destination node receives the RREQ, it sends a Route Reply (RREP) message back to the source node. The RREP contains the destination node's address, the source node's address, the unique identifier from the RREQ, and the sequence numbers of the nodes along the path from the source to the destination. The intermediate nodes along the path also cache the route information contained in the RREP.
- **Route Maintenance**: When a node on the path moves or fails, the nodes on either side of the broken link detect the failure and initiate a new Route Discovery process to find an alternate path. The failed link is marked as invalid in the routing tables of the nodes that know about it, and the nodes that have cached the route information for the broken path delete it from their caches.

Here are some advantages and disadvantages of DSR:

**Advantages:**
- DSR is a reactive protocol, which means it only discovers routes when they are needed. This reduces the overhead of maintaining routing tables for every node in the network.
- DSR supports multiple routes to a destination, which increases the reliability of the network.
- DSR is flexible and can adapt to changes in the network topology.

**Disadvantages:**
- DSR relies on source routing, which means that each packet contains the entire route from the source to the destination. This can increase the size of the packets and reduce the efficiency of the network.
- DSR can suffer from the "route discovery storm" problem, where multiple nodes simultaneously initiate Route Discovery processes for the same destination node. This can cause congestion and reduce the performance of the network.

In summary, Dynamic Source Routing (DSR) is an on-demand routing protocol that uses source routing to forward packets in mobile ad hoc networks (MANETs). It is flexible and can adapt to changes in the network topology, but it can also suffer from performance issues under certain conditions.