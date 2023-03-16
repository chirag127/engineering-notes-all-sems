# Ad Hoc On-Demand Distance Vector Routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, where each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses three types of control messages: route request (RREQ), route reply (RREP) and route error (RERR)  .
- AODV operates in two phases: route discovery and route maintenance  .
- Route discovery is initiated when a source node needs to send a packet to a destination node and does not have a valid route to it  .
- The source node broadcasts a RREQ message to its neighbors, which contains the source and destination addresses, a sequence number and a hop count  .
- Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node and forwards the RREQ message to its neighbors, increasing the hop count by one  .
- If an intermediate node has a fresh route to the destination node (i.e., a route with a sequence number equal or higher than the one in the RREQ message), it sends a RREP message back to the source node along the reverse route  .
- If the destination node receives the RREQ message, it generates a RREP message with its own sequence number and the hop count set to zero  .
- The source node selects the route with the highest destination sequence number and the lowest hop count as the best route and starts sending data packets along it  .
- Route maintenance is performed when a link break occurs in an active route  .
- The node that detects the link break sends a RERR message to its upstream neighbors, informing them about the unreachable destinations  .
- The upstream nodes update their routing tables and propagate the RERR message to their upstream neighbors until the source node is reached  .
- The source node can either drop the packets destined to the unreachable destination or initiate a new route discovery  .
- AODV has some advantages, such as low overhead, loop-freeness, scalability and adaptability to dynamic network conditions .
- AODV also has some disadvantages, such as high latency, vulnerability to routing attacks, and dependence on reliable broadcast .