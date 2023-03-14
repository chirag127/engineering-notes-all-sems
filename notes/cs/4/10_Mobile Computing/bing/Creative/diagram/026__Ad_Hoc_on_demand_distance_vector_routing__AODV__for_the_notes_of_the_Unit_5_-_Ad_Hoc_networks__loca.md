The following is a detailed ASCII diagram for Ad Hoc on demand distance vector routing (AODV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

AODV is a reactive routing protocol that establishes routes on demand between nodes in an ad hoc network. It uses control messages such as Route Requests (RREQs), Route Replies (RREPs), and Route Errors (RERRs) to discover and maintain routes. It also uses sequence numbers to ensure loop freedom and freshness of routes.

The diagram below shows an example of how AODV works. Suppose node S wants to send a packet to node D, but does not have a route to D. S broadcasts a RREQ message to its neighbors, which contains the source and destination addresses, the source and destination sequence numbers, and a hop count. The RREQ message is propagated by intermediate nodes until it reaches D or a node that has a fresh route to D. A node that receives a RREQ message updates its routing table with the reverse route to S, and then either forwards the RREQ or sends a RREP back to S. A RREP message contains the source and destination addresses, the destination sequence number, and the hop count to D. The RREP message is routed back to S along the reverse path established by the RREQ. When S receives the RREP, it updates its routing table with the forward route to D, and can start sending data packets to D. If a link break occurs along the route, the node that detects the link break sends a RERR message to its upstream neighbors, which then propagate the RERR to S. S then initiates a new route discovery process to find a new route to D.

The diagram uses the following symbols:

- S: source node
- D: destination node
- I: intermediate node
- RREQ: route request message
- RREP: route reply message
- RERR: route error message
- *: broadcast
- ->: unicast
- X: link break

```
+---+    +---+    +---+    +---+    +---+
| S |    | I |    | I |    | I |    | D |
+---+    +---+    +---+    +---+    +---+
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |*RREQ   |        |        |        |
  |------->|*RREQ   |        |        |
  |        |------->|*RREQ   |        |
  |        |        |------->|*RREQ   |
  |        |        |        |------->|
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |RREP    |
  |        |        |        |------->|
  |        |        |RREP    |        |
  |        |        |<-------|        |
  |        |RREP    |        |        |
  |        |<-------|        |        |
  |RREP    |        |        |        |
  |<-------|        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |DATA    |        |        |        |
  |------->|DATA    |        |        |
  |        |------->|DATA    |        |
  |        |        |------->|DATA    |
  |        |        |        |------->|
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |        |        |
  |        |        |X       |        |
  |        |        |        |        |
  |        |