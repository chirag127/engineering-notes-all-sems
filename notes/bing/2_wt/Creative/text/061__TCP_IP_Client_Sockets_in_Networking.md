#### TCP/IP Client Sockets in Networking

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet.
- A socket is one endpoint of a two-way communication link between two programs running on the network.
- A socket is defined by the IP address of the machine and the port it uses.
- A socket address is the combination of an IP address and a port number, much like one end of a telephone connection is the combination of a phone number and a particular extension.
- To create a TCP/IP client socket in Java, you need to use the java.net.Socket class.
- The constructor for the Socket class has parameters that specify the address family, socket type, and protocol type that the socket uses to make connections.
- When connecting a client socket to a server socket, the client will use an IPEndPoint object to specify the network address of the server.
- To send and receive data over TCP, you need to use the java.io.InputStream and java.io.OutputStream classes that are obtained from the socket object.
- To close a TCP/IP client socket, you need to call the close() method on the socket object.