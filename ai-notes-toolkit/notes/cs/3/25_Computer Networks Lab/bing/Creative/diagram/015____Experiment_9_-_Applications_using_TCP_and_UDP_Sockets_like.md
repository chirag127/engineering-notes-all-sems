## Experiment 9 - Applications using TCP and UDP Sockets

TCP and UDP are two protocols that are used for sending data over the Internet. They are both part of the transport layer of the Internet protocol suite, which means they are responsible for establishing connections, ensuring reliability, and managing congestion. However, they have different characteristics and use cases.

### TCP Sockets

TCP stands for Transmission Control Protocol. It is a connection-oriented protocol, which means that it establishes a logical connection between the sender and the receiver before exchanging data. This connection is maintained until the data transfer is complete or one of the parties closes it. TCP also provides reliability, which means that it ensures that all the data packets are delivered in the correct order and without errors. TCP does this by using acknowledgments, retransmissions, and checksums. TCP also implements flow control and congestion control, which means that it adjusts the rate of data transmission according to the network conditions and the receiver's capacity.

TCP sockets are used for applications that require reliable and ordered data delivery, such as web browsing, file transfer, email, and remote login. TCP sockets are created by specifying the TCP protocol and the destination IP address and port number. The socket then initiates a three-way handshake with the remote socket to establish the connection. Once connected, a TCP socket can only send and receive data to/from the remote socket. This means that each client in the application needs a separate TCP socket.

### UDP Sockets

UDP stands for User Datagram Protocol. It is a connectionless protocol, which means that it does not establish or maintain a logical connection between the sender and the receiver. UDP simply sends data packets, called datagrams, to the destination without waiting for acknowledgments or checking for errors. UDP does not provide reliability, ordering, flow control, or congestion control. UDP sockets are used for applications that do not require these features, but rather prefer speed and efficiency, such as video streaming, online gaming, voice over IP, and DNS. UDP sockets are created by specifying the UDP protocol and the destination IP address and port number. The socket then sends and receives datagrams to/from any socket that matches the destination address and port. This means that a single UDP socket can communicate with multiple sockets.

### Comparison

The main differences between TCP and UDP sockets are:

- TCP sockets are connection-oriented, while UDP sockets are connectionless.
- TCP sockets provide reliability, ordering, flow control, and congestion control, while UDP sockets do not.
- TCP sockets are used for applications that require reliable and ordered data delivery, while UDP sockets are used for applications that prefer speed and efficiency.
- TCP sockets can only communicate with one remote socket, while UDP sockets can communicate with multiple sockets.