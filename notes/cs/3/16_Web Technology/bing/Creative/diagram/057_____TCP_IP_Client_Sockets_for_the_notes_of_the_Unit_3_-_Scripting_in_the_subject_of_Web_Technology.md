### TCP/IP Client Sockets

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet .
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- TCP socket is defined by the IP address of the machine and the port it uses. A port is a 16-bit number that identifies a specific application or service on a host.
- TCP socket is connection-oriented, which means it requires three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet. This is also known as the three-way handshake.
- TCP socket has built-in error checking and will retransmit missing or corrupted packets. It also provides flow control and congestion control mechanisms to ensure data delivery and avoid network congestion.
- To create a TCP client socket in Java, we need to use the Socket class . The constructor for the Socket class has parameters that specify the host name or IP address and the port number of the server socket.
- To create a TCP client socket in C or C++, we need to use the socket(), connect(), send(), and recv() functions. The socket() function creates a socket and returns a file descriptor. The connect() function establishes a connection with the server socket. The send() and recv() functions send and receive data over the socket.
- To close a TCP client socket, we need to use the close() function in C or C++, or the close() method in Java . This will terminate the connection and release the socket resources.