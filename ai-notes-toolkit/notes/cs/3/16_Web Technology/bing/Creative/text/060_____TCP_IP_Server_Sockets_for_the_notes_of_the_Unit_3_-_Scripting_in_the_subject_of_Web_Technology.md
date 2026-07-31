### TCP/IP Server Sockets

- TCP/IP server sockets are used to create servers that listen for either local or remote client programs to connect to them on published ports.
- TCP/IP server sockets use the Transmission Control Protocol (TCP), which is a connection-oriented protocol that ensures reliable and ordered delivery of data .
- To create a TCP/IP server socket in Java, the ServerSocket class is used, which has a constructor that takes a port number as an argument.
- The ServerSocket class has methods such as accept(), close(), and getInetAddress() to manage the connections with the clients.
- The accept() method blocks until a client connects to the server socket, and returns a Socket object that represents the connection.
- The close() method closes the server socket and releases the port.
- The getInetAddress() method returns the IP address of the server socket.
- To send and receive data over TCP, the Socket class has methods such as getInputStream(), getOutputStream(), and close() to access the input and output streams of the socket and to close the socket.
- The input and output streams of the socket can be used to read and write bytes, characters, or objects, depending on the application logic.
- The close() method of the Socket class closes the socket and the associated streams.
- A TCP socket is defined by the IP address and the port of the machine that it uses to communicate .
- A TCP socket requires a three-way handshake to establish a connection: the SYN packet, the SYN-ACK packet, and the ACK packet .
- A TCP socket has built-in error checking and will retransmit missing or corrupted packets .
- A TCP socket is suitable for applications that require reliable and ordered data transfer, such as web, email, or file transfer .