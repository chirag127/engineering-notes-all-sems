### Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing instead of relying on the routing table at each intermediate node .
- Source routing means that the source node specifies the complete sequence of nodes to the destination in the packet header .
- DSR consists of two main mechanisms: route discovery and route maintenance .
- Route discovery is the process of finding a route from the source to the destination when there is no cached route available .
- Route discovery involves sending a route request packet that is flooded through the network until it reaches the destination or a node with a cached route .
- The route request packet contains the source and destination addresses, a unique request ID, and a list of nodes visited so far .
- The destination or the intermediate node with a cached route sends a route reply packet back to the source along the reverse path of the route request .
- The route reply packet contains the source and destination addresses, a unique request ID, and a list of nodes forming the route .
- The source node caches the route and uses it to send data packets to the destination .
- Route maintenance is the process of detecting and repairing link failures along the route .
- Route maintenance involves sending route error packets when a node detects a link failure or receives a packet with an unknown destination .
- The route error packet contains the source and destination addresses, the broken link, and the list of nodes forming the route .
- The node that receives the route error packet removes the broken link from its cache and propagates the route error packet to the source node .
- The source node initiates a new route discovery if it still needs to communicate with the destination .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages:
  - It reduces the overhead of periodic route updates and table maintenance .
  - It allows multiple routes to be cached and used for load balancing and fault tolerance .
  - It supports asymmetric and unidirectional links .
- Disadvantages:
  - It increases the packet header size due to source routing .
  - It may cause stale routes to be cached and used due to mobility and topology changes .
  - It may suffer from network congestion and collisions due to route request flooding .

: Dynamic Source Routing - Wikipedia
: Dynamic Source Routing - Wikipedia
: Dynamic Source Routing Protocol - Carnegie Mellon University