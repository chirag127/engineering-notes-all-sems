 Here is the content in markdown format without any emojis or external links:

### Routing algorithms and protocols for the notes of the Unit 5 - Network Layer in the subject of Computer Networks.

1. Distance Vector Routing Protocol
- Each router maintains a table of minimum distances to every network.
- The router sends its table to neighboring routers periodically.
- Neighboring routers update their table and send updates to their neighbors.
- The table is updated until the routing tables at all routers converge to show the shortest path to every network.

2. Link State Routing Protocol
- Each router maintains a map of the network topology.
- The router sends update messages to neighboring routers when there is a change in the topology (link up/down).
- Neighboring routers update their map and generate a new map and send updates to their neighbors.
- The process continues until all routers have the latest map and can independently calculate the shortest path to every network.

3. Hierarchical Routing
- Networks are grouped into regions.
- Routing is done at multiple levels to reduce size of routing tables.
- Provides a scalable solution for large networks.
- Examples: RIP, OSPF, BGP.

The content is written in points in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.