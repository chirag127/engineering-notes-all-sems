# Transport Layer Protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data is delivered from one process (application) to another process (application) on different hosts.
- Segmentation and reassembly: The transport layer divides the data into smaller segments and assigns sequence numbers to them for reordering at the destination.
- Flow control: The transport layer regulates the amount of data that can be sent by the sender and received by the receiver to avoid congestion and buffer overflow.
- Error control: The transport layer detects and corrects errors that may occur during the transmission of data.
- Multiplexing and demultiplexing: The transport layer allows multiple processes to share the same network connection by using port numbers to identify the source and destination processes.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and full-duplex communication between two hosts. TCP uses acknowledgments, timers, retransmission, and checksums to ensure error-free and in-order delivery of data. TCP also uses sliding window mechanism to implement flow control and congestion control.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and best-effort communication between two hosts. UDP does not guarantee the delivery, order, or integrity of data. UDP has low overhead and is suitable for real-time applications that can tolerate some data loss.

Some other transport layer protocols that have been defined and implemented are:

- Datagram Congestion Control Protocol (DCCP): It provides unreliable, connection-oriented, and congestion-controlled communication between two hosts. DCCP is designed for applications that need fast and timely delivery of data, such as streaming media and online games.
- Stream Control Transmission Protocol (SCTP): It provides reliable, connection-oriented, and message-oriented communication between two hosts. SCTP supports multiple streams of data within a single connection, which can improve the performance and reliability of applications that use multiple messages, such as voice over IP and web services.