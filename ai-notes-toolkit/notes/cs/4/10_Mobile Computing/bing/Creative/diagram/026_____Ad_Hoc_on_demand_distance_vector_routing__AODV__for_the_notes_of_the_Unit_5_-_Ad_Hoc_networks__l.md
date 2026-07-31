### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is a loop-free routing protocol that uses sequence numbers to ensure freshness of routes .
- AODV uses three types of control messages: route request (RREQ), route reply (RREP) and route error (RERR)  .
- AODV operates as follows   :
  - When a source node wants to send a packet to a destination node, it checks its routing table for a valid route. If no route is found, it broadcasts a RREQ message to its neighbors.
  - The RREQ message contains the source and destination addresses, the source and destination sequence numbers, the broadcast ID and the hop count. The broadcast ID and the source address uniquely identify a RREQ message.
  - Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node and forwards the RREQ message to its neighbors, unless it has a valid route to the destination node with a higher sequence number than the one in the RREQ message.
  - When the RREQ message reaches the destination node or an intermediate node with a valid route to the destination node, it sends a RREP message back to the source node along the reverse route. The RREP message contains the destination and source addresses, the destination and source sequence numbers, the hop count and the lifetime of the route.
  - Each intermediate node that receives the RREP message updates its routing table with a forward route to the destination node and forwards the RREP message to the next hop towards the source node.
  - When the source node receives the RREP message, it establishes a route to the destination node and starts sending data packets.
  - If a link break occurs in the route, the upstream node of the broken link sends a RERR message to the source node, indicating the unreachable destinations. The RERR message contains the source and destination addresses, the destination sequence number and a list of unreachable destinations.
  - The source node, upon receiving the RERR message, invalidates the route to the destination node and initiates a new route discovery process if needed.