#### TCP/IP Client Sockets in Networking

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet.
- TCP socket is a connection-oriented socket that uses the Transmission Control Protocol (TCP). It requires three packets to set up a connection: the SYN packet, the SYN-ACK packet, and the ACK packet.
- TCP socket is defined by the IP address of the machine and the port it uses. A socket address is the combination of an IP address and a port number.
- A socket is one endpoint of a two-way communication link between two programs running on the network. The socket mechanism provides a means of inter-process communication (IPC) by establishing named contact points between which the communication take place.
- A socket programming interface provides the routines required for interprocess communication between applications, either on the local system or spread in a distributed, TCP/IP-based network environment.
- A TCP/IP client socket is a socket that initiates a connection to a server socket and sends or receives data over the established connection .
- A TCP/IP client socket can be created using the Socket class in Java or the System.Net.Sockets.Socket class in .NET .
- A TCP/IP client socket can use an IPEndPoint object to specify the network address of the server. It can also use a hostname and a port number to resolve the server address using the DNS service.
- A TCP/IP client socket can use the connect method to establish a connection to the server socket . It can also use the beginConnect and endConnect methods to perform asynchronous connection operations.
- A TCP/IP client socket can use the getInputStream and getOutputStream methods in Java or the getStream method in .NET to obtain the input and output streams for sending and receiving data over the connection .
- A TCP/IP client socket can use the close method to terminate the connection and release the resources associated with the socket . It can also use the shutdown method to disable sending or receiving data on the socket.