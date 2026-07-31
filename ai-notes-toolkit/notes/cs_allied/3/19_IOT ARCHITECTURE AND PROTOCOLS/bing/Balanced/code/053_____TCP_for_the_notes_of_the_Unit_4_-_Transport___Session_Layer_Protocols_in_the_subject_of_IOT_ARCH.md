### TCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- TCP stands for Transmission Control Protocol and it is a transport layer or routing protocol that works with the Internet Protocol (IP) to provide reliable and ordered data delivery over the Internet .
- TCP guarantees the ordered data delivery by using an acknowledgment function that requires the receiver to send back a confirmation message to the sender for each packet received.
- TCP also performs retransmission of lost packets, error control and flow control to ensure the data integrity and avoid congestion .
- TCP is best suited whenever a program wants to send a lot of data because TCP does fragmentation of data and sends it in the form of small packets that can be reassembled at the destination.
- TCP supports both IPv4 and IPv6, which are network layer or adaption layer protocols that define the addressing and routing of packets across the Internet .
- TCP is traditionally neglected as a transport-layer protocol for the Internet of Things (IoT) because of its perceived complexity, overhead and unsuitability for constrained-node networks (CNNs) that have limited resources and capabilities .
- However, recent trends and industry needs are favoring TCP presence in IoT environments, such as cloud computing, edge computing, fog computing, web services, remote management, firmware updates, security and privacy .
- TCP can be implemented and used in IoT scenarios with some adaptations and optimizations, such as lightweight TCP stacks, TCP header compression, TCP option negotiation, TCP congestion control algorithms, TCP timeout estimation and TCP proxying  .
- TCP can also coexist and interoperate with other transport-layer protocols for IoT, such as UDP, CoAP, MQTT and QUIC, depending on the application requirements and network conditions  .