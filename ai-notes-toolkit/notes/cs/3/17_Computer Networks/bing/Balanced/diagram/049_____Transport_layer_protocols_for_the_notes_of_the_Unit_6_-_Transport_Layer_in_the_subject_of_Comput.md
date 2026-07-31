### Transport layer protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data is delivered from one process (application) to another process (application) on different hosts.
- Segmentation and reassembly: The transport layer divides the data into smaller segments and adds a header to each segment. The header contains information such as source and destination port numbers, sequence numbers, checksums, etc. The transport layer also reassembles the segments at the destination and checks for errors.
- Flow control: The transport layer regulates the amount of data that can be sent by the sender and received by the receiver. This prevents the sender from overwhelming the receiver with too much data at once.
- Error control: The transport layer detects and corrects errors that may occur during the transmission of data. This includes lost, duplicated, corrupted, or out-of-order segments. The transport layer can use techniques such as acknowledgments, timers, retransmissions, etc. to ensure reliable delivery of data.
- Multiplexing and demultiplexing: The transport layer allows multiple processes (applications) to share the same network connection. This is done by using port numbers to identify the source and destination processes. The transport layer also distributes the data to the appropriate processes based on the port numbers.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and byte-stream communication between two hosts. TCP establishes a logical connection between the sender and the receiver before exchanging data. TCP uses sequence numbers, acknowledgments, timers, and retransmissions to ensure that all the data is delivered correctly and in order. TCP also provides flow control and congestion control mechanisms to regulate the data transmission rate.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and datagram-oriented communication between two hosts. UDP does not establish a connection before sending data. UDP does not use sequence numbers, acknowledgments, timers, or retransmissions to ensure reliable delivery of data. UDP does not provide flow control or congestion control mechanisms. UDP is faster and simpler than TCP, but it does not guarantee the delivery, order, or integrity of the data.

Some other transport layer protocols that have been defined and implemented are:

- Datagram Congestion Control Protocol (DCCP): It provides unreliable, connection-oriented, and datagram-oriented communication between two hosts. DCCP is similar to UDP, but it adds congestion control mechanisms to avoid network congestion and packet loss.
- Stream Control Transmission Protocol (SCTP): It provides reliable, connection-oriented, and message-oriented communication between two hosts. SCTP is similar to TCP, but it supports multiple streams of data within a single connection. SCTP also provides features such as multihoming, partial reliability, and unordered delivery.