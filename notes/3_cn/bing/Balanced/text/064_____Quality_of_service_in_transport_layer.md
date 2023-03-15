### Quality of service in transport layer

- Quality of service (QoS) is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity.
- The transport layer is responsible for enhancing the QoS provided by the network layer by offering reliable and efficient end-to-end data delivery.
- The transport layer can provide QoS in terms of:
  - Throughput: the rate of data transfer between the sender and the receiver.
  - Delay: the time it takes for a packet to travel from the sender to the receiver.
  - Jitter: the variation in delay of packets.
  - Reliability: the probability of successful delivery of packets.
  - Security: the protection of data from unauthorized access or modification.
- The transport layer can use different protocols and techniques to achieve QoS, such as:
  - Transport Control Protocol (TCP): a connection-oriented protocol that provides reliable, ordered, and error-free data delivery. TCP uses mechanisms such as flow control, congestion control, and error recovery to ensure QoS.
  - User Datagram Protocol (UDP): a connectionless protocol that provides fast and efficient data delivery. UDP does not guarantee reliability, ordering, or error-free delivery, but it has lower overhead and latency than TCP. UDP is suitable for real-time applications that can tolerate some packet loss.
  - Stream Control Transmission Protocol (SCTP): a connection-oriented protocol that provides reliable, unordered, and error-free data delivery. SCTP supports multiple streams of data within a single connection, which can reduce jitter and improve QoS for multimedia applications.
  - Transport Layer Security (TLS): a protocol that provides security and encryption for data transmitted over TCP. TLS can protect data from eavesdropping, tampering, and impersonation attacks.
  - Quality of Service Transport Protocol (QSTP): a protocol that provides QoS for wireless sensor networks. QSTP uses a cross-layer approach that integrates the transport layer and the network layer to achieve QoS in terms of throughput, delay, reliability, and energy efficiency.