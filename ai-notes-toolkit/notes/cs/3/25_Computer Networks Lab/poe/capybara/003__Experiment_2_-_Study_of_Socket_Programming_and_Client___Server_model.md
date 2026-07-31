## Experiment 2 - Study of Socket Programming and Client – Server model

In this experiment, we will study the basics of socket programming and the client-server model. Here are the key points to keep in mind:

- Socket programming is a way of communicating between two computers over a network. It involves using sockets, which are endpoints of a two-way communication link.
- There are two types of sockets: client sockets and server sockets. Client sockets are used to initiate a connection to a server socket, while server sockets wait for incoming client connections.
- The client-server model is a way of organizing computer applications that involves a client program that requests services from a server program.
- The basic steps involved in socket programming include creating a socket, binding the socket to a specific address and port, listening for incoming connections (in the case of a server socket), accepting incoming connections, sending data over the connection, and receiving data over the connection.
- In the client-server model, the server program typically runs continuously and waits for incoming connections from client programs. When a client connects, the server creates a new thread or process to handle the client's request.
- Some common protocols used in socket programming include TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). TCP provides reliable, ordered, and error-checked delivery of data, while UDP provides faster but less reliable delivery of data.
- Socket programming can be used for a variety of applications, including web servers, email servers, chat applications, and online games.

Overall, socket programming and the client-server model are essential concepts for anyone interested in network programming or building distributed systems. By understanding the basics of socket programming, you can create powerful and scalable applications that can communicate with other computers over a network.