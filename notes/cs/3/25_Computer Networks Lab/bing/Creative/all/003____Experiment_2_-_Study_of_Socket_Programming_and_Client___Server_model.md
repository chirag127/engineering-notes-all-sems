# Experiment 2 - Study of Socket Programming and Client – Server model

## Objective
To understand the concept of socket programming and client-server model in network communication.

## Theory
- A socket is a simple communication channel through which two programs communicate over a network.
- A socket supports two-way communication between a client and a server, using a well-established protocol.
- A protocol is a set of rules and behavior that both the server and client must follow in order to establish two-way communication.
- A common protocol for socket communication is the Transmission Control Protocol (TCP), which provides reliable, in-order and error-free delivery of data .
- A socket is identified by a combination of an IP address and a port number.
- An IP address is a unique identifier for a device on a network, and a port number is a logical identifier for a specific process or service on that device.
- A socket on the server process waits for requests from a client, and binds an address that clients can use to find the server.
- A socket on the client process initiates a connection request to the server, and sends or receives data through the established connection.
- A socket can be either stream-oriented or datagram-oriented.
- A stream-oriented socket, also known as a connection-oriented socket, establishes a connection before transferring data, and ensures that the data is delivered reliably and in order.
- A datagram-oriented socket, also known as a connectionless socket, does not require a connection, and each packet sent or received on a datagram socket is individually addressed and routed.
- Socket programming is the process of creating and using sockets to enable communication between processes.
- Socket programming can be done in various programming languages, such as C, C++, Java, Python, etc .
- Socket programming involves the following steps :
  - Socket creation: A socket is created using the socket() function, which takes the domain, type and protocol as parameters, and returns a socket descriptor, an integer that identifies the socket.
  - Socket options: The socket options can be manipulated using the setsockopt() function, which takes the socket descriptor, the level, the option name and the option value as parameters, and allows changing the behavior of the socket.
  - Socket binding: The socket is bound to an address using the bind() function, which takes the socket descriptor and the address structure as parameters, and assigns a local protocol address to the socket.
  - Socket listening: The socket is set to listen for incoming connection requests using the listen() function, which takes the socket descriptor and the backlog as parameters, and marks the socket as a passive socket that can accept connections.
  - Socket connection: The socket is connected to a remote address using the connect() function, which takes the socket descriptor and the address structure as parameters, and initiates a connection to the specified address.
  - Socket acceptance: The socket accepts a connection request from a client using the accept() function, which takes the socket descriptor and the address structure as parameters, and returns a new socket descriptor for the accepted connection.
  - Socket communication: The socket can send or receive data using the send() and recv() functions, which take the socket descriptor, the buffer, the length and the flags as parameters, and transfer data between the connected sockets.
  - Socket closure: The socket is closed using the close() function, which takes the socket descriptor as a parameter, and releases the resources associated with the socket.

## References
: http://www.csce.uark.edu/~mqhuang/courses/3613/s2023/lectures/Lecture_3_socket.pdf
: https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Java_Java_Java_-_Object-Oriented_Programming_(Morelli_and_Walde)/15%3A_Sockets_and_Networking/15.06%3A_Client_Server_Communication_via_Sockets
: https://www.ibm.com/docs/en/i/7.3?topic=programming-how-sockets-work
: http://www.csce.uark.edu/~mqhuang/courses/3613/s2022/lectures/Lecture_3_socket.pdf
: