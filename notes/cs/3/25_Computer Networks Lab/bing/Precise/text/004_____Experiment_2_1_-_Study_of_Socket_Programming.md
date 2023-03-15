### Experiment 2.1 - Study of Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

Here are some key points to remember when studying socket programming:

1. Sockets are the endpoints of a bidirectional communications channel.
2. Sockets may communicate within a process, between processes on the same machine, or between processes on different machines.
3. Socket programming is the core API for inter-process communication.
4. The socket API is based on the Berkeley sockets interface, which was developed in the early 1980s.
5. The most common types of sockets are stream sockets and datagram sockets.
6. Stream sockets provide a reliable, connection-oriented service, while datagram sockets provide an unreliable, connectionless service.
7. Socket programming is used in many applications, including web browsers, email clients, and instant messaging programs.
