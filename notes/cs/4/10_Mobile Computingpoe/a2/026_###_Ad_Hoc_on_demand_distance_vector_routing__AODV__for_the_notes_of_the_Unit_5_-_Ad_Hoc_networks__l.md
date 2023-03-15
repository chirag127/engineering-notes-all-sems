 Here are the notes for ### Ad Hoc on demand distance vector routing (AODV) for the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Ad Hoc on demand distance vector routing (AODV)

- AODV is a reactive routing protocol for mobile ad hoc networks (MANETs).
- It uses distance vectors to determine the shortest path between nodes.
- Route discovery is on-demand, meaning routes are only determined when needed.
- Route maintenance is achieved through the use of hello messages and sequence numbers.

#### Route Discovery

- When a source node wants to send data to a destination node, it initi Swiss the route discovery process if it does not already have a valid route to that destination.
- The source node broadcasts a ROUTE REQUEST (RREQ) packet to its neighbors.
- Each neighboring node receiving the RREQ rebroadcasts it to its neighbors, and so on, until either:
- The RREQ reaches the destination node. The destination node then unicasts a ROUTE REPLY (RREP) packet back to the source node.
- The RREQ reaches an intermediate node that has a fresh enough route to the destination. This intermediate node then unicasts a RREP packet back to the source node.

#### Route Maintenance

- To maintain active routes, each node periodically broadcasts HELLO messages to detect and inform neighbors of any changes in link state (up/down).
- A sequence number is associated with each route to identify the freshness of the route. The destination node includes the sequence number for the destination in the RREP.
- When a link break occurs (detected via HELLO messages), the node upstream of the break increments its sequence number and broadcasts a RERR (ROUTE ERROR) message to all nodes that use the broken link. These nodes then invalidate the routes using the broken link and re-initiate route discovery if the route is still needed.

Advantages:
- Reactive: routes are only determined on demand, reducing overhead and resource utilization.
- Loop-free: the sequence number mechanism avoids routing loops.
Disadvantages:
- Slow convergence: route discovery can lead to latency in delivering data packets.
- Overhead: the periodic HELLO messages and route error messaging lead to extra network traffic.