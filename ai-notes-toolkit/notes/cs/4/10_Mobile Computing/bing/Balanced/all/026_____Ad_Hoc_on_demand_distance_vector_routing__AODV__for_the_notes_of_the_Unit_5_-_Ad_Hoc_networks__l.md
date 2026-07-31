# Ad Hoc On-Demand Distance Vector Routing (AODV)

- AODV is a **reactive** routing protocol for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations **on demand** and supports both **unicast** and **multicast** routing .
- AODV uses **routing tables** with one entry for each destination and **sequence numbers** to validate routing information and prevent routing loops .
- AODV uses three types of control messages: **Route Request (RREQ)**, **Route Reply (RREP)** and **Route Error (RERR)**  .
- AODV operates as follows   :
  - When a source node wants to send a packet to a destination node, it first checks its routing table for a valid route. If no route is found, it broadcasts a RREQ message to its neighbors.
  - The RREQ message contains the source and destination addresses, the source and destination sequence numbers, a broadcast ID and a hop count. The broadcast ID and the source address uniquely identify a RREQ message.
  - Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node and forwards the RREQ message to its neighbors, unless it has a valid route to the destination node with a higher or equal sequence number than the one in the RREQ message. In that case, it unicasts a RREP message back to the source node along the reverse route.
  - The RREP message contains the source and destination addresses, the destination sequence number, a hop count and a lifetime. The destination sequence number indicates the freshness of the route and the lifetime indicates how long the route is valid.
  - When the source node receives the RREP message, it updates its routing table with a forward route to the destination node and starts sending data packets along the route.
  - If a link break occurs in the route, the upstream node that detects the link break sends a RERR message to the source node, indicating the unreachable destinations. The RERR message contains the source and destination addresses, the destination sequence number and a list of unreachable destinations.
  - When the source node receives the RERR message, it invalidates the route to the destination node and initiates a new route discovery process if needed.