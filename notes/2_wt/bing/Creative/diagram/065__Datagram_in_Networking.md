A datagram is a basic transfer unit associated with a packet-switched network. Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination. Datagrams provide a connectionless communication service across a packet-switched network. The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network .

#### Datagram in Networking

The following diagram illustrates the basic architecture of a datagram network using ASCII characters:

```
    +----+    +----+    +----+    +----+
    | H1 |----| R1 |----| R2 |----| H2 |
    +----+    +----+    +----+    +----+
       |        |        |        |
       |        |        |        |
       |        |        |        |
    +----+    +----+    +----+    +----+
    | H3 |----| R3 |----| R4 |----| H4 |
    +----+    +----+    +----+    +----+
```

In this diagram, H1, H2, H3, and H4 are hosts that send and receive datagrams. R1, R2, R3, and R4 are routers that forward datagrams based on their header information. The lines between the hosts and routers represent physical links that can carry one or more datagrams at a time.

Suppose H1 wants to send a message to H4. The message is divided into four datagrams, labeled as A, B, C, and D. Each datagram has a header that contains the source address (H1) and the destination address (H4). The datagrams are sent one by one over the network, but they may take different paths to reach H4. For example, datagram A may go through R1, R2, and R4, while datagram B may go through R1, R3, and R4. The routers use routing tables to decide which link to forward each datagram to.

The datagrams may arrive at H4 in any order, or some of them may be lost or corrupted along the way. It is the responsibility of H4 to reorder the datagrams and check for errors. If any datagram is missing or damaged, H4 may request H1 to resend it. This is done by using a reliable transport protocol, such as TCP, on top of the datagram network service. Alternatively, H4 may accept the message as it is, without requesting retransmission. This is done by using an unreliable transport protocol, such as UDP, on top of the datagram network service.