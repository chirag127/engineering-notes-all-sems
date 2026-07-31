### Experiment 2.1 - Study of Socket Programming

Socket programming is a way of enabling communication between different processes or machines using network protocols. A socket is an endpoint of a connection that can send and receive data. Socket programming involves creating, binding, connecting, listening, sending and receiving sockets using a specific protocol, such as TCP or UDP.

The following are some of the steps involved in socket programming:

- Importing the socket library: The socket library provides the functions and constants for creating and manipulating sockets. For example, in Python, one can import the socket library using `import socket`.
- Creating a socket: A socket is created by specifying the address family, the socket type and the protocol. For example, in C, one can create a TCP socket using `int sockfd = socket(AF_INET, SOCK_STREAM, 0);`.
- Binding a socket: A socket is bound to a specific address and port using the bind function. This assigns a local name to the socket and allows it to receive connections or datagrams. For example, in C, one can bind a socket to the address 127.0.0.1 and port 8080 using `struct sockaddr_in servaddr; servaddr.sin_family = AF_INET; servaddr.sin_addr.s_addr = inet_addr("127.0.0.1"); servaddr.sin_port = htons(8080); bind(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));`.
- Connecting a socket: A socket can initiate a connection to another socket using the connect function. This establishes a TCP connection between the client and the server sockets. For example, in C, one can connect a socket to the address 127.0.0.1 and port 8080 using `struct sockaddr_in servaddr; servaddr.sin_family = AF_INET; servaddr.sin_addr.s_addr = inet_addr("127.0.0.1"); servaddr.sin_port = htons(8080); connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr));`.
- Listening and accepting a socket: A socket can listen for incoming connections using the listen function. This marks the socket as a passive socket that can accept connections from other sockets. For example, in C, one can listen for up to 10 connections using `listen(sockfd, 10);`. A socket can accept a connection from another socket using the accept function. This returns a new socket that represents the established connection. For example, in C, one can accept a connection and store the new socket in `int newsockfd` using `int newsockfd = accept(sockfd, NULL, NULL);`.
- Sending and receiving data: A socket can send and receive data using the send and recv functions for TCP sockets, or the sendto and recvfrom functions for UDP sockets. These functions take the socket descriptor, the buffer to store or send the data, the size of the buffer, and some flags as arguments. For example, in C, one can send a message "Hello" using `send(sockfd, "Hello", 6, 0);` and receive a message in a buffer `char buf[1024]` using `recv(sockfd, buf, 1024, 0);`.

The following are some of the advantages of socket programming:

- It allows communication between different processes or machines using a common protocol and format.
- It supports both connection-oriented and connectionless communication models, depending on the socket type and protocol.
- It is portable and compatible across different operating systems and platforms, as long as they support the socket API.
- It is flexible and extensible, as it can support various applications and services, such as web, email, chat, file transfer, etc.