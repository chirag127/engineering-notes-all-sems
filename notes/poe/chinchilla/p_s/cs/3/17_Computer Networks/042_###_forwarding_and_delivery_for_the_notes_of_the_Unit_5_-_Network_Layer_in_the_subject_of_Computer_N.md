### Forwarding and Delivery

The network layer is responsible for forwarding and delivering packets across a network. In this section, we will discuss the concepts of forwarding and delivery in detail.

#### Forwarding

Forwarding is the process of sending a packet from one router to another router along a path to its destination. The forwarding process is based on the destination address in the packet's header. When a router receives a packet, it examines the destination address and determines the next hop to which the packet should be forwarded. The next hop is the router that is closest to the destination network.

The forwarding table is used by routers to determine the next hop for a packet. The forwarding table contains information about the destination network addresses and the next-hop router addresses. The forwarding table is built dynamically by using routing protocols such as OSPF, ISIS, and BGP.

#### Delivery

Delivery is the process of getting a packet to its final destination. Delivery involves the following steps:

1. Routing: The network layer selects the best path to deliver the packet to its destination. Routing can be static or dynamic.

2. Forwarding: The packet is forwarded from one router to another router along the path to its destination.

3. Error detection and correction: The network layer performs error detection and correction to ensure that the packet is delivered without errors.

4. Fragmentation and reassembly: The network layer can fragment a packet into smaller packets if the packet is too large to be transmitted over the network. The network layer can also reassemble the smaller packets at the destination.

5. End-to-end delivery: The network layer ensures that the packet is delivered to the correct destination and that the packet arrives in the correct order.

Delivery can be accomplished using two different approaches: connectionless and connection-oriented.

#### Connectionless Delivery

In connectionless delivery, each packet is treated as an independent entity and is forwarded to its destination based on the destination address in the packet header. Connectionless delivery does not require the establishment of a dedicated path between the source and destination. The Internet Protocol (IP) is an example of a connectionless protocol.

Advantages of connectionless delivery:

- No setup or teardown of a connection is required.
- It is suitable for applications that require low delay, such as real-time streaming applications.

Disadvantages of connectionless delivery:

- There is no guarantee of delivery.
- Packets can be lost, duplicated, or delivered out of order.

#### Connection-oriented Delivery

In connection-oriented delivery, a dedicated path is established between the source and destination before any data is transmitted. The path remains active until all data has been transmitted. Connection-oriented delivery provides reliable delivery of data by using error detection and correction, flow control, and congestion control mechanisms. The Transmission Control Protocol (TCP) is an example of a connection-oriented protocol.

Advantages of connection-oriented delivery:

- Guaranteed delivery of packets.
- Packets are delivered in the correct order.
- Error detection and correction are performed.

Disadvantages of connection-oriented delivery:

- A setup and teardown of a connection are required, which introduces delay.
- It is not suitable for real-time applications that require low delay.

In conclusion, forwarding and delivery are critical processes in the network layer. Forwarding involves the process of sending a packet from one router to another router along a path to its destination. Delivery involves the process of getting a packet to its final destination. Both connectionless and connection-oriented delivery approaches have their advantages and disadvantages, and the choice of approach depends on the requirements of the application.