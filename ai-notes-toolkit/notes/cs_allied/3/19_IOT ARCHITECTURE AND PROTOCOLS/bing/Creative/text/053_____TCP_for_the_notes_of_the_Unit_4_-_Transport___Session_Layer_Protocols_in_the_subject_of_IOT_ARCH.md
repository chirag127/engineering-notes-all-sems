### TCP

TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.

Some of the main features and functions of TCP are:

- **Reliability**: TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data. It resends the lost or corrupted packets to ensure the data integrity.
- **Segmentation**: TCP divides the data into segments of variable size and assigns a sequence number to each segment. This helps in reassembling the data in the correct order at the receiver side.
- **Congestion control**: TCP monitors the network congestion and adjusts the transmission rate accordingly. It uses various algorithms such as slow start, congestion avoidance, fast retransmit, and fast recovery to avoid or reduce the congestion.
- **Multiplexing**: TCP allows multiple applications to use the same network connection simultaneously. It uses port numbers to identify the source and destination applications of each segment.
- **Connection management**: TCP follows a three-way handshake process to establish and terminate the connection. The sender and receiver exchange SYN, ACK, and FIN packets to synchronize and finalize the connection parameters.

TCP is used by application protocols such as HTTP, FTP, SMTP, and Telnet that require reliable and ordered delivery of data.