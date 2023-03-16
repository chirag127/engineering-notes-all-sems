Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on Dynamic Source Routing (DSR) for the Unit 5 of Mobile Computing.

# Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing instead of relying on the routing table at each intermediate node .
- Source routing means that the source node specifies the complete sequence of nodes to the destination in the packet header .
- DSR consists of two main mechanisms: route discovery and route maintenance .
- Route discovery is the process of finding a route from the source to the destination when there is no cached route available .
- Route discovery involves broadcasting a route request (RREQ) packet by the source node, which is forwarded by the intermediate nodes until it reaches the destination or a node with a cached route to the destination .
- The destination or the intermediate node then sends a route reply (RREP) packet back to the source node along the reverse path of the RREQ packet .
- The source node then caches the route in its route cache and uses it to send data packets .
- Route maintenance is the process of detecting and repairing link failures along the route .
- Route maintenance involves sending route error (RERR) packets by the node that detects a link failure, which are propagated back to the source node .
- The source node then removes the broken route from its route cache and initiates a new route discovery if needed .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages include:
  - No periodic routing updates, which reduces the control overhead and bandwidth consumption .
  - No need to maintain routing tables at each node, which saves memory and processing power .
  - Loop-free routes, since the source node specifies the entire route in the packet header .
  - Support for multiple routes to the same destination, which increases the reliability and load balancing .
- Disadvantages include:
  - Large packet header size, which increases the transmission delay and consumes more bandwidth .
  - Route cache inconsistency, which may lead to stale or invalid routes due to network topology changes .
  - Vulnerability to malicious nodes, which may alter or drop the packets or the route information .
