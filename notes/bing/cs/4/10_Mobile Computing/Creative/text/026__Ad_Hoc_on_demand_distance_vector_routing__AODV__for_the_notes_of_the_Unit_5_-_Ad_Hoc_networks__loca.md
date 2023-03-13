### Ad Hoc On Demand Distance Vector Routing (AODV)

- AODV is a routing protocol for mobile ad hoc networks (MANETs) and other wireless ad hoc networks.
- AODV is intended for use by mobile nodes in an ad hoc network. It offers quick adaptation to dynamic link conditions, low processing and memory overhead, low network utilization, and determines unicast routes to destinations within the ad hoc network   .
- AODV operates as follows :
  - Each node maintains a routing table that contains the next hop node and the destination sequence number for each destination.
  - When a node wants to send a packet to a destination, it checks its routing table. If it has a valid route, it uses it. Otherwise, it initiates a route discovery process by broadcasting a route request (RREQ) message.
  - The RREQ message contains the source and destination addresses, the source and destination sequence numbers, and a broadcast ID that uniquely identifies the RREQ.
  - Each node that receives the RREQ checks if it is the destination or if it has a valid route to the destination. If so, it sends a route reply (RREP) message back to the source. Otherwise, it rebroadcasts the RREQ after increasing the hop count.
  - The RREP message contains the source and destination addresses, the destination sequence number, the hop count, and the lifetime of the route.
  - The source node receives the RREP and updates its routing table with the new route. It then sends the packet to the destination using the next hop node.
  - Each node also periodically sends a hello message to its neighbors to maintain local connectivity. If a node does not receive a hello message from a neighbor for a certain time, it assumes that the link is broken and sends a route error (RERR) message to the nodes that use that link.
  - The RERR message contains the unreachable destination and the destination sequence number. The nodes that receive the RERR update their routing tables and propagate the RERR if necessary.
  - AODV uses sequence numbers to avoid loops and stale routes. A node always chooses the route with the highest destination sequence number and the lowest hop count. A node increments its own sequence number whenever it initiates a route discovery or receives a RREQ with a higher sequence number. A node also updates its sequence number when it receives a RREP or a RERR with a higher sequence number.