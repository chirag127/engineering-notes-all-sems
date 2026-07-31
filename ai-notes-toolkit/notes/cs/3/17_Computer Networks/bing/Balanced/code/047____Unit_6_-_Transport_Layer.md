## Unit 6 - Transport Layer

The transport layer is the fourth layer of the OSI model. It is responsible for providing end-to-end communication between processes running on different hosts. It also offers various services such as data transfer, reliability, flow control, congestion control, error detection, and multiplexing/de-multiplexing. The transport layer uses different protocols to deliver these services, such as TCP, UDP, SPX, DCCP, and SCTP. 

Some of the main functions and protocols of the transport layer are:

- **Data transfer**: The transport layer transfers data from the application layer to the network layer and vice versa. It also segments the data into smaller units called segments or datagrams, and adds headers to them. The headers contain information such as source and destination port numbers, sequence numbers, checksums, and flags. The transport layer also reassembles the segments or datagrams at the destination host and delivers them to the application layer.

- **Reliability**: The transport layer ensures that the data is delivered correctly and in order to the destination host. It uses various mechanisms such as acknowledgments, retransmissions, timers, and windowing to achieve this. For example, TCP is a reliable protocol that uses a three-way handshake to establish a connection, and uses sequence numbers and acknowledgments to ensure that no data is lost or duplicated.

- **Flow control**: The transport layer regulates the rate of data transmission between the sender and the receiver. It prevents the sender from overwhelming the receiver or the network with too much data. It uses various techniques such as windowing, buffering, and backpressure to achieve this. For example, TCP uses a sliding window mechanism to adjust the size of the window based on the available buffer space and the network conditions.

- **Congestion control**: The transport layer detects and avoids congestion in the network. Congestion occurs when the network resources are insufficient to handle the traffic load. It causes delays, losses, and lower throughput. The transport layer uses various algorithms such as slow start, congestion avoidance, fast retransmit, and fast recovery to deal with congestion. For example, TCP uses these algorithms to adapt its window size and retransmission behavior based on the network feedback.

- **Error detection**: The transport layer detects and corrects errors in the data transmission. It uses various methods such as checksums, parity bits, and cyclic redundancy checks to detect errors. It also uses retransmissions, acknowledgments, and negative acknowledgments to correct errors. For example, TCP uses a checksum field in its header to verify the integrity of the data, and uses retransmissions and acknowledgments to recover from errors.

- **Multiplexing/de-multiplexing**: The transport layer enables multiple processes to share the same network connection. It uses port numbers to identify the source and destination processes. It also uses sockets to establish and manage the connections. Multiplexing is the process of combining data from multiple processes into a single stream for transmission. De-multiplexing is the process of separating data from a single stream into multiple streams for delivery. For example, TCP and UDP use port numbers and sockets to multiplex and de-multiplex data.

Some of the main protocols of the transport layer are:

- **TCP (Transmission Control Protocol)**: TCP is a connection-oriented, reliable, and full-duplex protocol. It provides reliable data transfer, flow control, congestion control, and error detection and correction. It is used by many applications such as HTTP, FTP, SMTP, and SSH.

- **UDP (User Datagram Protocol)**: UDP is a connectionless, unreliable, and datagram-based protocol. It provides fast and simple data transfer, but does not guarantee reliability, flow control, congestion control, or error detection and correction. It is used by applications that require low latency, high throughput, or real-time communication, such as DNS, DHCP, RTP, and VoIP.

- **SPX (Sequenced Packet Exchange)**: SPX is a connection-oriented, reliable, and packet-based protocol. It provides reliable data transfer, flow control, and error detection and correction. It is used by applications that run on the IPX/SPX network protocol suite, such as NetWare and Novell Directory Services.

- **DCCP (Datagram Congestion Control Protocol)**: DCCP is a connection-oriented, unreliable, and datagram-based protocol. It provides congestion control, but does not guarantee reliability, flow control, or error detection and correction. It is used by applications that require congestion control, but can tolerate some data loss, such as streaming media and online games.

- **SCTP (Stream