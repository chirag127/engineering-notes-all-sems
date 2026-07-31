### Experiment 2.1 - Study of Socket Programming

1. **Introduction:** Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection.

2. **Socket Types:** There are two main types of sockets: stream sockets and datagram sockets. Stream sockets use TCP (Transmission Control Protocol) for data transmission, while datagram sockets use UDP (User Datagram Protocol).

3. **Socket Creation:** In order to create a socket, the `socket()` function is used. This function takes in two arguments: the address family and the socket type. The address family specifies the protocol to be used, while the socket type specifies the type of socket.

4. **Socket Binding:** After creating a socket, it needs to be bound to an IP address and port number. This is done using the `bind()` function, which takes in the socket, the address to bind to, and the length of the address as arguments.

5. **Socket Listening:** Once the socket is bound, it can start listening for incoming connections. This is done using the `listen()` function, which takes in the socket and the maximum number of queued connections as arguments.

6. **Socket Accepting:** When a connection is received, the socket can accept it using the `accept()` function. This function returns a new socket object and the address of the client.

7. **Socket Closing:** After the communication is complete, the socket can be closed using the `close()` function. This function takes in the socket as an argument and closes the connection.

8. **Conclusion:** Socket programming is an essential part of networking and is used to establish connections between nodes on a network. It involves creating, binding, listening, accepting, and closing sockets. Understanding socket programming is important for developing network-based applications.