### Quality of service in transport layer

- Quality of service (QoS) is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity.
- The transport layer is responsible for enhancing the QoS provided by the network layer by offering reliable and efficient end-to-end data transmission between application processes.
- The transport layer can provide QoS in terms of:
  - Throughput: the amount of data transferred per unit time.
  - Delay: the time taken for a packet to travel from the source to the destination.
  - Jitter: the variation in delay of packets.
  - Reliability: the probability of successful delivery of packets.
  - Security: the protection of data from unauthorized access or modification.
- The transport layer can use different protocols and techniques to achieve QoS, such as:
  - TCP: a connection-oriented, reliable, and congestion-controlled protocol that uses acknowledgments, retransmissions, and window-based flow control to ensure data integrity and efficiency.
  - UDP: a connectionless, unreliable, and best-effort protocol that does not use any error or flow control mechanisms and is suitable for real-time applications that can tolerate some packet loss or delay.
  - SCTP: a connection-oriented, reliable, and message-oriented protocol that supports multiple streams, multihoming, and partial reliability to provide flexibility and resilience for applications that require both reliability and timeliness.
  - RTP: a protocol that works on top of UDP and provides end-to-end delivery services for real-time applications that involve audio and video data, such as VoIP and video conferencing. RTP provides features such as sequence numbers, timestamps, payload type identification, and source identification to enable synchronization, jitter compensation, and quality monitoring.
  - RSVP: a protocol that works on both the network and the transport layer and enables applications to reserve network resources along a path from the source to the destination to guarantee QoS parameters such as bandwidth, delay, and reliability. RSVP uses signaling messages to establish, maintain, and tear down reservations and to communicate QoS requirements and availability.
- The transport layer can also cooperate with other layers to achieve QoS, such as:
  - The application layer: the transport layer can use the information provided by the application layer about the QoS requirements and preferences of the application to select the appropriate protocol and parameters for data transmission.
  - The network layer: the transport layer can use the feedback provided by the network layer about the network conditions and congestion to adjust the transmission rate and window size of the transport protocol to avoid congestion and packet loss.
  - The link layer: the transport layer can use the services provided by the link layer to ensure reliable and efficient data transmission over the physical medium, such as error detection and correction, framing, and medium access control.