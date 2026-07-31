## Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of enabling two programs to communicate over a network using a well-established protocol.
- A socket is a communication channel that connects a client and a server, allowing them to exchange data in both directions.
- A client is a program that requests a service or resource from a server, which is a program that provides the service or resource.
- The client-server model is a distributed application structure that partitions tasks between the providers of a service (servers) and the requesters of a service (clients).
- There are two types of sockets: stream sockets and datagram sockets.
  - Stream sockets, also known as connection-oriented sockets, establish a connection before transferring data. They are reliable, in-order, and use Transmission Control Protocol (TCP).
  - Datagram sockets, also known as connectionless sockets, do not require a connection before transferring data. They are unreliable, out-of-order, and use User Datagram Protocol (UDP).
- To create a socket, we need to specify the domain, the type, and the protocol of the socket.
  - The domain specifies the address family of the socket, such as IPv4, IPv6, or Unix domain.
  - The type specifies the communication semantics of the socket, such as stream or datagram.
  - The protocol specifies the protocol to be used by the socket, such as TCP or UDP.
- To use a socket, we need to perform some steps to establish a connection between the client and the server.
  - The server needs to bind the socket to an address that clients can use to find the server.
  - The server needs to listen for incoming connection requests from clients on the socket.
  - The server needs to accept a connection request from a client and create a new socket for the communication.
  - The client needs to connect to the server's socket using the server's address.
  - The client and the server can then send and receive data using the socket.
  - The client and the server need to close the socket when the communication is finished.