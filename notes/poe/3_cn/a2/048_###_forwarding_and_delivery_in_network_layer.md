 Here is the content in markdown format for the topic ### Forwarding and Delivery in Network Layer:

### Forwarding and Delivery in Network Layer

The network layer is responsible for forwarding packets across networks and delivering them to the correct destination. Some key points to understand forwarding and delivery in the network layer are:

1. Routing: The process of determining the path taken by packets to reach the destination is called routing. Routing algorithms determine the optimal path based on metrics like hop count, bandwidth, delay, load, etc. Popular routing algorithms are link-state routing and distance-vector routing.
2. Forwarding table: The routing algorithms populate a forwarding table (or routing table) which contains the optimal next-hop for a destination network. The forwarding table is used by the forwarding process to determine where to forward the packets to.
3. Forwarding: The process of transferring packets from one interface to the next based on the forwarding table is called packet forwarding. The destination IP address is used to lookup the forwarding table and determine the next-hop to forward the packet to.
4. TTL: To prevent packets from endlessly circulating within the network, a time-to-live (TTL) field is decremented at each hop. If the TTL reaches 0, the packet is discarded. This avoids routing loops and other delivery failures.
5. Fragmentation: If the packet size exceeds the MTU (maximum transmission unit) of the next network, the packet is fragmented into smaller pieces for forwarding. The fragments are reassembled at the destination.
6. Reassembly: The network layer at the destination host reassembles the fragmented packets and passes the reassembled datagram to the higher layers.

Some mnemonics for remembering the network layer functions:
- Routing: Right Path, hop by hop
- Forwarding: Next hop lookup
- Delivery: Reassemble packets

Advantages of network layer:
- Hiding network details ( IP addresses) from upper layers
- Enabling communication across different network technologies (Ethernet, WiFi, etc.)
- Allowing scalable internetworks through hierarchy and aggregation

Disadvantages:
- Increased overhead (headers)
- Latency due to routing/forwarding process
- Complexity of routing algorithms and tables

[Include diagrams/images/codes/tables if required to explain the concepts]