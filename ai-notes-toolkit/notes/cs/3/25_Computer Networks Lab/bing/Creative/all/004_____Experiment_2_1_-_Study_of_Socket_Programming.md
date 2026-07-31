# Experiment 2.1 - Study of Socket Programming

## Objective
To learn the basics of socket programming and how to write client/server applications using sockets.

## Theory
- A socket is an endpoint of communication between two processes or machines on a network.
- Socket programming is the process of creating and using sockets to send and receive data over a network.
- Sockets can be classified into two types: stream sockets and datagram sockets.
- Stream sockets use TCP as the transport protocol and provide reliable, ordered, and error-free communication.
- Datagram sockets use UDP as the transport protocol and provide unreliable, unordered, and error-prone communication.
- Sockets can also be classified into two domains: Internet domain and Unix domain.
- Internet domain sockets use IP addresses and port numbers to identify the endpoints of communication.
- Unix domain sockets use file system paths to identify the endpoints of communication.
- Sockets are supported by various operating systems, such as Unix, Windows, Mac, etc.
- Sockets can be created and manipulated using various programming languages, such as C, Python, Java, etc.

## Steps
- To create a socket, we need to specify the domain, the type, and the protocol of the socket.
- To use a socket, we need to perform the following steps:
  - Bind the socket to a local address and port using the bind() function.
  - Listen for incoming connections using the listen() function (for server sockets only).
  - Accept a connection from a remote socket using the accept() function (for server sockets only).
  - Connect to a remote socket using the connect() function (for client sockets only).
  - Send and receive data using the send() and recv() functions (for stream sockets) or the sendto() and recvfrom() functions (for datagram sockets).
  - Close the socket using the close() function.
- To use sockets in different programming languages, we need to import the socket library and use the appropriate functions and methods provided by the library.