### Transport layer protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data is delivered from one process (application) to another process (application) on different hosts.
- Segmentation and reassembly: The transport layer divides the data into smaller segments and assigns sequence numbers to them for reordering at the destination.
- Flow control: The transport layer regulates the rate of data transmission between the sender and the receiver to avoid congestion and buffer overflow.
- Error control: The transport layer detects and corrects errors that may occur during the data transmission.
- Multiplexing and demultiplexing: The transport layer allows multiple processes to share the same network connection by using port numbers to identify the source and destination processes.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and full-duplex communication between two hosts. TCP uses acknowledgments, timers, and retransmissions to ensure error-free and in-order delivery of data. TCP also uses sliding window mechanism to implement flow control and congestion control.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and best-effort communication between two hosts. UDP does not use acknowledgments, timers, or retransmissions to ensure data delivery. UDP does not provide any flow control or congestion control. UDP is suitable for real-time applications that can tolerate some data loss.

Additional transport layer protocols that have been defined and implemented include:

- Datagram Congestion Control Protocol (DCCP): It provides unreliable, connection-oriented, and congestion-controlled communication between two hosts. DCCP is designed for applications that need low-latency and low-overhead data transmission, such as multimedia streaming and online gaming.
- Stream Control Transmission Protocol (SCTP): It provides reliable, connection-oriented, and message-oriented communication between two hosts. SCTP supports multiple streams of data within a single connection, which allows for better utilization of network resources and higher performance. SCTP also supports multihoming, which enables a host to have multiple IP addresses and switch between them in case of network failure.