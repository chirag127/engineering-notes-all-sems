 Here is the content in markdown format for the topic - ### Temporary ordered routing algorithm (TORA) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Temporary Ordered Routing Algorithm (TORA)

- TORA is a reactive routing protocol for mobile ad hoc networks (MANETs).
- It is an on-demand routing protocol which builds routes only when required.
- TORA finds multiple loop-free and link-disjoint paths between a source and destination.
- TORA uses the concept of "height" associated with each node to establish the shortest path from source to destination. The height of a node increases monotonically as the node moves away from the destination.
- The key steps involved in TORA are:

1. Route Discovery: When a source node wants to send data to a destination node and does not have a valid route, it initiates a route discovery process by broadcasting a QUERY packet with height (HQ) set to 0.
2. Building Cloud: On receiving the QUERY packet, each intermediate node updates its height to be one greater than the height in the QUERY packet and rebroadcasts the QUERY packet. This results in the formation of a "directed cloud" leading to the destination.
3. Route Reply: The destination node or an intermediate node that has a fresh enough route to the destination generates a REPLY packet that traces back along the reverse path of the QUERY packet, establishing the route in the routing tables of the traversed nodes.
4. Route Maintenance: TORA performs local route repairs by using the concept of "height" whenever the network topology changes.

Advantages:
- Finds multiple loop-free and link-disjoint paths
- Incurs low overhead as it uses height increments instead of sequence numbers
- Performs local repairs to handle route failures

Disadvantages:
- Slow convergence
- Complex protocol
- Vulnerable to attacks like flooding, blackhole, etc.