### Transport layer protocols

- Transport layer protocols are responsible for providing end-to-end communication services for applications over a network.
- Transport layer protocols lie between the user applications and the network layer, and use the network layer protocols (such as IP) to send and receive packets.
- Transport layer protocols can offer different types of services, such as reliable or unreliable, connection-oriented or connectionless, stream-oriented or message-oriented, etc.
- The most common transport layer protocols in the Internet are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) .
- TCP is a reliable, connection-oriented, stream-oriented protocol that ensures the correct delivery of packets in the same order as they were sent . TCP uses mechanisms such as sequence numbers, acknowledgments, timers, and retransmissions to deal with packet loss, duplication, corruption, and reordering. TCP also provides flow control and congestion control to regulate the rate of data transmission and avoid network congestion.
- UDP is an unreliable, connectionless, message-oriented protocol that does not guarantee the delivery or ordering of packets . UDP does not use any mechanisms to recover from packet loss, duplication, corruption, or reordering. UDP also does not provide any flow control or congestion control, and relies on the application layer to handle these issues. UDP is suitable for applications that require low latency, high throughput, or real-time communication, such as voice over IP, video streaming, online gaming, etc.
- Other transport layer protocols that have been defined and implemented include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP).
- DCCP is a connection-oriented, message-oriented protocol that provides unreliable delivery with congestion control. DCCP is designed for applications that can tolerate packet loss, but need to avoid network congestion, such as multimedia streaming, telephony, etc.
- SCTP is a connection-oriented, message-oriented protocol that provides reliable delivery with multiple streams and multihoming. SCTP allows multiple messages to be sent and received concurrently over different streams within a single connection, and also supports multiple network addresses for each endpoint. SCTP is designed for applications that need high availability, fault tolerance, and load balancing, such as web servers, telecommunication systems, etc.

Some possible mnemonics and learning tricks for the transport layer protocols are:

- TCP: **T**ransport **C**ontrol **P**rotocol -> **T**rustworthy, **C**onnected, **P**ersistent
- UDP: **U**ser **D**atagram **P**rotocol -> **U**nreliable, **D**isconnected, **P**erformance
- DCCP: **D**atagram **C**ongestion **C**ontrol **P**rotocol -> **D**rop **C**apable, **C**ongestion **C**autious, **P**acketized
- SCTP: **S**tream **C**ontrol **T**ransmission **P**rotocol -> **S**imultaneous, **C**onnected, **T**ransportable, **P**lural