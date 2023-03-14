### Forwarding and delivery in network layer

The network layer is responsible for source-to-destination or host-to-host delivery of packets across multiple networks. It takes the data from the transport layer, adds its header, and forwards it to the data link layer. The network layer also determines the best route for the packets to travel from the source to the destination among the multiple routes available in a network. This process is called routing. The network layer uses a forwarding table to decide which output link interface to use for each incoming packet. The forwarding table is configured by the routing algorithm.

The following diagram illustrates the basic architecture of the network layer:

```
+------+     +------+     +------+     +------+
| Host |     |Router|     |Router|     | Host |
|  H1  |-----|  R1  |-----|  R2  |-----|  H2  |
+------+     +------+     +------+     +------+
```

The network layer at H1 receives a packet from the transport layer, adds a header with the source address (H1) and the destination address (H2), and delivers the packet to the data link layer. The data link layer encapsulates the packet in a frame and sends it to R1. The network layer at R1 receives the frame, decapsulates the packet, and looks up the destination address (H2) in its forwarding table. The forwarding table tells R1 to forward the packet to the output link interface connected to R2. The network layer at R1 delivers the packet to the data link layer, which encapsulates the packet in a new frame and sends it to R2. The same process is repeated at R2, which forwards the packet to H2. The network layer at H2 receives the frame, decapsulates the packet, and delivers it to the transport layer.