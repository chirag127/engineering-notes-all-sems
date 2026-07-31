### Transport layer protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data is delivered from one process (application) to another process (application) on different hosts.
- Segmentation and reassembly: The transport layer divides the data into smaller segments and assigns sequence numbers to them. The segments are then reassembled at the destination based on the sequence numbers.
- Flow control: The transport layer regulates the rate of data transmission between the sender and the receiver to avoid congestion and buffer overflow.
- Error control: The transport layer detects and corrects errors that may occur during the data transmission. It also handles retransmission, acknowledgement, and timeout mechanisms.
- Multiplexing and demultiplexing: The transport layer uses port numbers to identify different processes (applications) on the same host and to multiplex (combine) or demultiplex (separate) the data streams accordingly.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and byte-stream communication between two hosts. TCP uses a three-way handshake to establish a connection, a sliding window protocol to control the flow and error, and a four-way handshake to terminate a connection.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and datagram communication between two hosts. UDP does not use any handshake, flow control, or error control mechanisms. It is faster and simpler than TCP, but less reliable and more prone to data loss.

Additional transport layer protocols that have been defined and implemented include:

- Datagram Congestion Control Protocol (DCCP): It provides unreliable, connection-oriented, and datagram communication between two hosts. DCCP uses a handshake to establish a connection, a congestion control mechanism to regulate the data rate, and a reset packet to terminate a connection.
- Stream Control Transmission Protocol (SCTP): It provides reliable, connection-oriented, and message-oriented communication between two hosts. SCTP uses a four-way handshake to establish a connection, a selective acknowledgement mechanism to control the flow and error, and a shutdown procedure to terminate a connection. SCTP also supports multiple streams, multihoming, and partial reliability.