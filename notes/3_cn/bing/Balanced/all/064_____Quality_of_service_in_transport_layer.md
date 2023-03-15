### Quality of service in transport layer

- Quality of service (QoS) is the use of mechanisms or technologies that work on a network to control traffic and ensure the performance of critical applications with limited network capacity.
- The transport layer is responsible for enhancing the QoS provided by the network layer by offering reliable and efficient end-to-end data delivery between application processes.
- The transport layer can provide QoS by using the following methods:
  - Establishing transport connections by sending requests and specifying the required QoS parameters, such as throughput, delay, jitter, and reliability.
  - Using transport addresses to identify the end points of a connection, such as port numbers in the internet.
  - Providing flow control and congestion control to regulate the rate of data transmission and avoid network overload.
  - Providing error control and retransmission to ensure data integrity and reliability.
  - Providing multiplexing and demultiplexing to allow multiple applications to share the same network resources.
  - Providing segmentation and reassembly to divide large data units into smaller ones for efficient transmission and recombine them at the destination.
- The transport layer can use different protocols to provide different levels of QoS, such as TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) in the internet.
  - TCP is a connection-oriented, reliable, and full-duplex protocol that provides flow control, congestion control, error control, and retransmission.
  - UDP is a connectionless, unreliable, and simplex protocol that provides minimal QoS and is suitable for real-time applications that can tolerate some data loss.
- A mnemonic to remember the main functions of the transport layer is **FECMSS** (Flow control, Error control, Congestion control, Multiplexing, Segmentation, and Synchronization).