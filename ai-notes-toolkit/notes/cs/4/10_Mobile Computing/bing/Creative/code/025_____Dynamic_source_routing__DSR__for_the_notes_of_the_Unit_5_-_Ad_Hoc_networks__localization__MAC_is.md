Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on dynamic source routing (DSR) for the unit 5 of mobile computing.

### Dynamic source routing (DSR)

- Dynamic source routing (DSR) is a routing protocol for wireless mesh networks. It is similar to AODV in that it forms a route on-demand when a transmitting node requests one. However, it uses source routing instead of relying on the routing table at each intermediate device .
- Source routing means that the sender of a packet determines the complete sequence of nodes through which the packet has to pass. The sender explicitly lists this route in the packet's header, identifying each forwarding hop by the address of the next node to which to transmit the packet on its way to the destination host.
- DSR consists of two main mechanisms: route discovery and route maintenance. Route discovery is the process by which a node S wishing to send a packet to a destination node D obtains a source route to D. Route maintenance is the process of detecting and repairing route errors.
- Route discovery works as follows:
  - S initiates route discovery by broadcasting a route request (RREQ) packet to its neighbors. The RREQ contains the address of S, the address of D, and a unique identification number.
  - Each node receiving the RREQ appends its own address to the route record in the RREQ and forwards the packet to its neighbors, unless it is the destination or it has a route to D in its route cache.
  - If the node is the destination or has a route to D, it sends a route reply (RREP) packet back to S along the reverse path of the RREQ. The RREP contains the route record accumulated in the RREQ.
  - S receives the RREP and caches the route to D in its route cache. It can then send packets to D using this route.
- Route maintenance works as follows:
  - Each node forwarding a packet to the next hop along the source route is responsible for confirming that the packet has been received by the next hop. This can be done by using link-layer acknowledgments or passive acknowledgments (by overhearing the next hop forwarding the packet).
  - If the node does not receive an acknowledgment, it retransmits the packet until a maximum number of attempts is reached. If the packet is still not acknowledged, the node returns a route error (RERR) packet to the original sender of the packet, indicating the link that failed.
  - The sender of the packet receives the RERR and removes the broken link from its route cache. It can then try to send the packet using another route in its cache or initiate a new route discovery.
- DSR has some advantages and disadvantages :
  - Advantages:
    - It eliminates the need for periodic route advertisements, which reduces the network overhead and saves bandwidth and energy.
    - It allows multiple routes to be learned and cached, which increases the route availability and robustness.
    - It supports unidirectional links and asymmetric routes, which are common in wireless networks.
    - It allows nodes to learn routes opportunistically by snooping on the source routes of the packets they overhear.
  - Disadvantages:
    - It adds the source route to each packet header, which increases the packet size and may cause fragmentation.
    - It may not scale well to large networks, as the route discovery may flood the network and the route caches may become stale or inconsistent.
    - It may suffer from the route cache poisoning problem, where malicious nodes can inject false routes into the caches of other nodes.