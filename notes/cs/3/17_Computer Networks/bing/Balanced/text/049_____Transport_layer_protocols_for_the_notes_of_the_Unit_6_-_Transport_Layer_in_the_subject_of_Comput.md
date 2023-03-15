### Transport layer protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data is delivered from one process (application) to another process (application) on different hosts.
- Segmentation and reassembly: The transport layer divides the data into smaller segments that can be transmitted over the network layer, and reassembles them at the destination host.
- Flow control: The transport layer regulates the rate of data transmission between the sender and the receiver, to avoid congestion and buffer overflow.
- Error control: The transport layer detects and corrects errors that may occur during the data transmission, such as lost, duplicated, or corrupted segments.
- Multiplexing and demultiplexing: The transport layer allows multiple processes to share the same network connection, by assigning a unique identifier (port number) to each segment. The transport layer also delivers the segments to the correct processes based on the port numbers.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and byte-stream communication between two hosts. TCP establishes a logical connection before sending the data, and uses acknowledgments, sequence numbers, timers, and retransmission to ensure the data is delivered correctly and in order. TCP also implements flow control and congestion control mechanisms to adjust the data rate according to the network conditions.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and datagram communication between two hosts. UDP does not establish a connection before sending the data, and does not use acknowledgments, sequence numbers, timers, or retransmission to ensure the data delivery. UDP also does not implement flow control or congestion control mechanisms, and relies on the application layer to handle the errors and congestion. UDP is faster and simpler than TCP, but less reliable and more prone to data loss.

Additional transport layer protocols that have been defined and implemented include:

- Datagram Congestion Control Protocol (DCCP): It provides unreliable, connection-oriented, and datagram communication between two hosts. DCCP is similar to UDP, but it implements congestion control mechanisms to avoid overloading the network.
- Stream Control Transmission Protocol (SCTP): It provides reliable, connection-oriented, and message-oriented communication between two hosts. SCTP is similar to TCP, but it supports multiple streams within a single connection, and allows partial reliability and unordered delivery of messages. SCTP also provides features such as multihoming, path selection, and security.