### Ad Hoc on demand distance vector routing (AODV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Ad Hoc on demand distance vector routing (AODV) is a routing protocol designed for wireless and mobile ad hoc networks .
- Ad hoc networks are networks that do not have any fixed infrastructure or centralized administration, and consist of mobile nodes that communicate with each other over wireless links .
- AODV establishes routes to destinations on demand, that is, only when a source node needs to send data to a destination node, it initiates a route discovery process  .
- AODV supports both unicast and multicast routing, and can handle dynamic network topology changes, such as node mobility, link failures, and network partitioning  .
- AODV uses two types of messages for route discovery and maintenance: route request (RREQ) and route reply (RREP)  .
- When a source node wants to send data to a destination node, it first checks its routing table to see if it has a valid route to the destination. If not, it broadcasts a RREQ message to its neighbors, which contains the source and destination addresses, a sequence number, and a hop count  .
- Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node, and then forwards the RREQ message to its neighbors, increasing the hop count by one  .
- If an intermediate node has a valid route to the destination, or if it is the destination itself, it sends a RREP message back to the source node, along the reverse route. The RREP message contains the destination address, the sequence number, and the hop count to the destination  .
- When the source node receives the RREP message, it updates its routing table with a forward route to the destination node, and starts sending data packets along the route  .
- AODV uses sequence numbers to ensure the freshness of routes and to avoid loops. A node maintains a sequence number for itself and for each destination it knows. A higher sequence number indicates a more recent route  .
- AODV uses route error (RERR) messages to notify the source node and other affected nodes of a link breakage or a node failure along an active route. The source node can then initiate a new route discovery process if needed  .
- AODV uses periodic hello messages to detect the connectivity of neighboring nodes. If a node does not receive a hello message from a neighbor for a certain time, it assumes that the link to that neighbor is broken  .
- AODV has some advantages and disadvantages as a routing protocol for ad hoc networks  :
  - Advantages:
    - It is adaptive to dynamic network conditions, such as node mobility, link failures, and network partitioning.
    - It is efficient in terms of network bandwidth and node resources, as it only creates routes on demand and does not rely on periodic advertisements.
    - It can handle both unicast and multicast routing, and can support multiple routes to a destination.
    - It can prevent routing loops and stale routes by using sequence numbers.
  - Disadvantages:
    - It may incur high latency and overhead for route discovery, especially for large and dense networks, or for high mobility scenarios.
    - It may suffer from congestion and collisions due to the broadcast nature of RREQ messages.
    - It may not be able to find the shortest or the most optimal route, as it depends on the first RREP message received by the source node.
    - It may not be able to cope with high traffic load or frequent route changes, as it may cause frequent route discoveries and route errors.

- A possible mnemonic to remember the main features of AODV is:

  - **A**daptive to dynamic network conditions