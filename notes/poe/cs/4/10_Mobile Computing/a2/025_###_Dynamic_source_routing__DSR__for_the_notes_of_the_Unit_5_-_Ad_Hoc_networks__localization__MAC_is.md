 Here is the content in markdown format for the topic ### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Dynamic Source Routing (DSR)

- DSR is a simple and efficient routing protocol for wireless ad hoc networks.
- It is an on-demand routing protocol which means that it establishes a route only when it is required by the source node to transmit data.
- The key feature of DSR is that the source node determines and stores the complete route to the destination in its route cache. This route can then be used for future transmissions.
- The basic operations of DSR are:

1. Route Discovery: When a source node wants to send data to a destination node for which it does not already have a route, it initiates route discovery. It broadcasts a Route Request (RREQ) packet to its neighbors.

2. Route Reply: The destination node or any node that has a route to the destination, generates a Route Reply (RREP) packet and unicasts it to the originating node. The source node caches the discovered route in its route cache.

3. Route Maintenance: If a source node receives data packet transmission failure indication from MAC layer, it initiates route rediscovery by broadcasting a new RREQ to repair the broken link.

Advantages:

- Minimal routing overhead as routes are discovered only on demand.
- Loop-free routes.
- Supports unidirectional links.

Disadvantages:

- Large route cache is required to store source routes which increases memory overhead.
- All nodes must process all control packets which increases processing overhead.
- Does not scale well for large networks.

Applications: DSR can be used in ad hoc networks where topology changes frequently and bandwidth and power are constrained.