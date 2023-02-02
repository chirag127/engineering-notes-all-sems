### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing
Dynamic Source Routing (DSR) is a routing protocol for ad hoc networks, which allows nodes to dynamically discover a route between nodes without the need for a centralized infrastructure.

DSR operates on a "on-demand" basis, meaning it only searches for routes when a node needs to send data. Each node maintains a route cache, which stores the routes it has discovered. When a node needs to send data, it first checks its cache for a valid route to the destination node. If a route is found, the data is sent along that route. If no route is found, the node initiates a route discovery process.

DSR has two main components: route discovery and route maintenance. In route discovery, a node broadcasts a route request (RREQ) to its neighbors, which then forward the RREQ to their neighbors, and so on, until the destination node is reached. The destination node then sends a route reply (RREP) back to the source node along the reverse path.

In route maintenance, DSR uses "acknowledgement" packets to detect broken links and update the route cache accordingly. If a node does not receive an expected acknowledgement, it assumes the link is broken and removes that link from its cache.

DSR has the advantage of being simple and scalable, but it can suffer from high overhead and long latencies in large networks.
