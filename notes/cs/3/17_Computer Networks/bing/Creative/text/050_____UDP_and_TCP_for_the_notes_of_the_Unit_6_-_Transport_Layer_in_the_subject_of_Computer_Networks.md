### UDP and TCP

- UDP and TCP are two protocols used for sending data packets over the Internet.
- UDP stands for User Datagram Protocol, and TCP stands for Transmission Control Protocol.
- UDP is a connectionless protocol, meaning it does not establish a connection before sending data packets.
- TCP is a connection-oriented protocol, meaning it establishes a connection before sending data packets and maintains it until the data transfer is complete.
- UDP is faster than TCP, as it does not perform error-checking, retransmission, or flow control.
- TCP is slower than UDP, as it performs error-checking, retransmission, and flow control to ensure reliable and ordered delivery of data packets.
- UDP is suitable for applications that require speed, efficiency, and real-time communication, such as video streaming, online gaming, and voice over IP (VoIP).
- TCP is suitable for applications that require reliability, accuracy, and data integrity, such as web browsing, email, file transfer, and remote access.
- UDP and TCP have different header formats and port numbers.
- UDP header consists of four fields: source port, destination port, length, and checksum.
- TCP header consists of six fields: source port, destination port, sequence number, acknowledgment number, header length, and flags.
- UDP port numbers range from 0 to 65535, and TCP port numbers range from 0 to 65535.
- UDP and TCP use different algorithms to handle congestion and flow control.
- UDP does not have any congestion or flow control mechanism, and relies on the application layer to handle these issues.
- TCP uses a sliding window mechanism to control the amount of data sent and received, and uses various algorithms to avoid and recover from congestion, such as slow start, congestion avoidance, fast retransmit, and fast recovery.