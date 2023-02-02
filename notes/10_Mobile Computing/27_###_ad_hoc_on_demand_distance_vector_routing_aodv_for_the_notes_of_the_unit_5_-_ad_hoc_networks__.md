### Ad Hoc on demand distance vector routing (AODV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing
Ad Hoc On Demand Distance Vector Routing (AODV) is a reactive routing protocol used in mobile ad hoc networks. It is designed to work in dynamic network environments where the network topology changes frequently. AODV operates on demand and only establishes routes when they are needed, reducing the overhead of maintaining unused routes.

AODV uses distance-vector algorithms to determine the best path between nodes. It maintains a routing table that contains the next hop and distance to each destination. When a node needs to send a packet, it broadcasts a route request (RREQ) to its neighbors. The RREQ is propagated through the network until it reaches the destination or an intermediate node with a fresh route to the destination. The intermediate node then sends a route reply (RREP) back to the source node along the reverse path.

AODV has several advantages over other routing protocols, including low overhead, fast route discovery, and efficient use of network resources. However, it is also susceptible to routing loops and black holes, which can cause significant performance degradation.

Overall, AODV is a popular choice for ad hoc networks due to its simplicity and effectiveness in dynamic network environments.
