### Transport layer protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data is delivered from one process (application) to another process (application) on different hosts.
- Segmentation and reassembly: The transport layer divides the data into smaller segments and assigns sequence numbers to them. The segments are then reassembled at the destination based on the sequence numbers.
- Flow control: The transport layer regulates the amount of data that can be sent by the sender and received by the receiver, to avoid congestion and buffer overflow.
- Error control: The transport layer detects and corrects errors that may occur during the transmission of data. It also handles lost, duplicated, or out-of-order segments.
- Multiplexing and demultiplexing: The transport layer uses port numbers to identify different processes (applications) on the same host and to deliver the data to the correct process. Multiplexing is the process of combining data from multiple processes into one segment, while demultiplexing is the process of separating data from one segment into multiple processes.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and byte-stream communication between two hosts. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP uses acknowledgments, timers, retransmission, and windowing to ensure error-free and in-order delivery of data. TCP also provides congestion control mechanisms to avoid network overload.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and message-oriented communication between two hosts. UDP does not use any handshaking, acknowledgment, retransmission, or windowing to ensure reliability or flow control. UDP is faster and simpler than TCP, but it does not guarantee the delivery of data. UDP is suitable for real-time applications that can tolerate some loss or delay of data.

Additional transport layer protocols that have been defined and implemented include:

- Datagram Congestion Control Protocol (DCCP): It provides unreliable, connection-oriented, and message-oriented communication between two hosts. DCCP uses a four-way handshake to establish a connection, and a three-way handshake to terminate a connection. DCCP uses acknowledgments, timers, and congestion control mechanisms to avoid network overload, but it does not use retransmission or windowing to ensure reliability or flow control. DCCP is suitable for multimedia applications that require congestion control but can tolerate some loss or delay of data.
- Stream Control Transmission Protocol (SCTP): It provides reliable, connection-oriented, and message-oriented communication between two hosts. SCTP uses a four-way handshake to establish a connection, and a four-way handshake to terminate a connection. SCTP uses acknowledgments, timers, retransmission, and windowing to ensure error-free and in-order delivery of data. SCTP also provides congestion control mechanisms to avoid network overload. SCTP supports multiple streams of data within a single connection, and allows partial reliability and unordered delivery of data. SCTP is suitable for applications that require multiple streams of data, such as voice over IP (VoIP).