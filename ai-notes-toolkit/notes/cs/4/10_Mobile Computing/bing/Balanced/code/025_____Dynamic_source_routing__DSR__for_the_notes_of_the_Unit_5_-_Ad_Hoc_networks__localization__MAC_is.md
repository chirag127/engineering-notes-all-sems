Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on dynamic source routing (DSR) for the unit 5 of mobile computing.

### Dynamic source routing (DSR)

- Dynamic source routing (DSR) is a routing protocol for wireless mesh networks. It is similar to AODV in that it forms a route on-demand when a transmitting node requests one. However, it uses source routing instead of relying on the routing table at each intermediate device .
- Source routing means that the sender of a packet determines the complete sequence of nodes through which the packet has to pass. The sender explicitly lists this route in the packet's header, identifying each forwarding hop by the address of the next node to which to transmit the packet on its way to the destination host.
- DSR consists of two main mechanisms: route discovery and route maintenance. Route discovery is the process by which a node S wishing to send a packet to a destination node D obtains a source route to D. Route maintenance is the process of detecting and repairing route errors.
- Route discovery works as follows:
  - S initiates route discovery by broadcasting a route request (RREQ) packet to its neighbors. The RREQ contains the address of S, the address of D, and a unique identification number.
  - Each node receiving the RREQ appends its own address to the route record in the RREQ and forwards the packet to its neighbors, unless it is the destination or it has a route to D in its route cache.
  - If the node has a route to D in its route cache, it returns a route reply (RREP) packet to S, containing the copy of the route record from the RREQ along with the route from its cache.
  - If the node is the destination D, it returns a RREP to S, containing the route record from the RREQ, which is the complete source route from S to D.
  - S can receive multiple RREPs from different nodes and can choose the best route based on some criteria, such as the shortest route or the most reliable route.
  - S caches the routes learned from the RREPs for future use.
- Route maintenance works as follows:
  - When a node encounters a transmission error at its data link layer along a source route, it removes the link from its cache and generates a route error (RERR) packet, which contains the addresses of the two ends of the failed link.
  - The RERR is sent back to the source S, which then removes the failed link from its cache and initiates a new route discovery if necessary.
  - Alternatively, S can use another route from its cache or try to salvage the packet by finding a route to the next hop in the source route.
- DSR has some advantages and disadvantages :
  - Advantages:
    - It eliminates the need for periodic route advertisements and neighbor detection packets, which reduces the network overhead and saves bandwidth.
    - It allows multiple routes to be learned and cached, which increases the route availability and robustness.
    - It supports unidirectional links and asymmetric routes, which are common in wireless networks.
    - It adapts quickly to the topology changes and node mobility, as the routes are maintained only when needed.
  - Disadvantages:
    - It incurs high latency and overhead during route discovery, especially for large networks or high traffic loads.
    - It consumes more bandwidth and energy due to the source routing overhead, which increases with the route length and the number of intermediate nodes.
    - It suffers from the stale route problem, as the cached routes may become invalid due to the topology changes or node failures.
    - It is vulnerable to malicious nodes that can alter, drop, or misroute the packets.