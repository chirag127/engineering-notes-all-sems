### TCP/IP Client Sockets

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet .
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- A TCP/IP client socket is a socket that initiates a connection to a server socket and exchanges data with it .
- A TCP/IP client socket is defined by the IP address and port number of the server socket that it connects to .
- A TCP/IP client socket requires three steps to establish a connection with a server socket :
  - Create a socket object with the desired address family, socket type, and protocol type.
  - Use the socket object's connect method to specify the network address and port number of the server socket.
  - Use the socket object's send and receive methods to exchange data with the server socket.
- A TCP/IP client socket can use either blocking or non-blocking mode to send and receive data .
  - Blocking mode means that the socket methods will wait until the operation is completed or an error occurs.
  - Non-blocking mode means that the socket methods will return immediately and indicate the status of the operation.
- A TCP/IP client socket can use either synchronous or asynchronous methods to send and receive data.
  - Synchronous methods mean that the program will wait for the socket methods to return before continuing.
  - Asynchronous methods mean that the program will register a callback function that will be invoked when the socket methods complete or fail.
- A TCP/IP client socket should close the connection with the server socket when it is no longer needed .
  - Closing the connection means sending a FIN packet to the server socket and waiting for an ACK packet in response.
  - Closing the connection will free the resources associated with the socket object and prevent data loss or corruption.