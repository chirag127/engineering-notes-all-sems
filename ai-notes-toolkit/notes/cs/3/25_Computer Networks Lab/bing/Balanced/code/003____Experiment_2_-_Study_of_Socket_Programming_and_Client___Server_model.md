## Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of enabling communication between two processes over a network.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- A client is a process that initiates a connection to a server and requests a service or resource.
- A server is a process that listens for incoming connections and provides a service or resource to the clients.
- The client-server model is a distributed application structure that partitions tasks between the providers of a service (servers) and the requesters of a service (clients).
- The client-server model can be implemented using different types of sockets, such as stream sockets and datagram sockets.
- Stream sockets, also known as connection-oriented sockets, establish a reliable and ordered connection between the client and the server before transferring data. They use the Transmission Control Protocol (TCP) as the underlying protocol.
- Datagram sockets, also known as connectionless sockets, do not require a connection between the client and the server and can send or receive data individually. They use the User Datagram Protocol (UDP) as the underlying protocol.
- The steps involved in socket programming are:

  - Socket creation: The client and the server create a socket using the `socket()` function, which returns a socket descriptor, an integer that identifies the socket.
  - Socket binding: The server binds the socket to a specific address and port using the `bind()` function, which associates the socket with the address and port that the clients can use to find the server.
  - Socket listening: The server listens for incoming connection requests from the clients using the `listen()` function, which specifies the maximum number of connections that the server can queue.
  - Socket connection: The client connects to the server using the `connect()` function, which specifies the address and port of the server. The server accepts the connection request from the client using the `accept()` function, which returns a new socket descriptor for the communication with the client.
  - Socket communication: The client and the server can send and receive data using the `send()` and `recv()` functions (or `write()` and `read()` functions) on the socket descriptors. The data can be in the form of bytes, strings, or structures.
  - Socket closing: The client and the server can close the connection using the `close()` function, which releases the socket descriptor and the associated resources.