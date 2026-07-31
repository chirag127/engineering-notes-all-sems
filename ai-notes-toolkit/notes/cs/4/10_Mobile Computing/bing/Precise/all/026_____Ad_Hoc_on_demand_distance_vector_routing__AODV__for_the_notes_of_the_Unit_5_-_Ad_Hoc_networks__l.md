# Ad Hoc on demand distance vector routing (AODV)

Ad Hoc on demand distance vector routing (AODV) is a routing protocol for ad hoc mobile networks. It is part of Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing. Here are some key points to note about AODV:

1. AODV is an on-demand routing protocol, meaning that routes are established only when needed.
2. It uses a destination sequence number to ensure loop-free and up-to-date routes.
3. Route discovery in AODV is done through the use of Route Request (RREQ) and Route Reply (RREP) messages.
4. When a node needs to establish a route to a destination, it broadcasts a RREQ message to its neighbors.
5. The RREQ message is propagated through the network until it reaches the destination or a node with a fresh enough route to the destination.
6. The destination or the intermediate node with a fresh enough route then sends a RREP message back to the source, establishing the route.
7. Route maintenance is done through the use of Route Error (RERR) messages and HELLO messages.
8. If a link break is detected, a RERR message is sent to the affected upstream nodes to inform them of the link break.
9. HELLO messages are used to detect link breaks between neighbors.
10. AODV has low overhead and is scalable to large networks.
