### Connection management in transport layer

- The transport layer is responsible for creating and managing the end-to-end connections between hosts for data transmission.
- The transport layer uses two main protocols: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that uses a three-way handshake to establish a connection between two hosts. TCP ensures that the data is delivered in order and without errors, and provides flow control and congestion control mechanisms.
- UDP is an unreliable, connectionless protocol that does not guarantee the delivery, order, or integrity of the data. UDP is faster and simpler than TCP, and is used for applications that do not require reliability, such as streaming media or online games.
- Connection management involves three phases: connection establishment, data transfer, and connection termination.
- Connection establishment is the process of initiating a connection between two hosts. In TCP, this is done by exchanging SYN, SYN-ACK, and ACK messages. In UDP, there is no connection establishment, and the hosts can start sending data packets immediately.
- Data transfer is the process of sending and receiving data between two hosts. In TCP, this is done by using sequence numbers, acknowledgments, and sliding windows to ensure reliable and ordered delivery of data. In UDP, there is no data transfer protocol, and the hosts simply send and receive datagrams without any feedback or control.
- Connection termination is the process of closing a connection between two hosts. In TCP, this is done by exchanging FIN, FIN-ACK, and ACK messages. In UDP, there is no connection termination, and the hosts can stop sending data at any time.