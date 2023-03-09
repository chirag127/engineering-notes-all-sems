 Here is the content written in markdown format:

### Experiment 2.1 - Study of Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. It allows us to create client-server applications.

* Socket - An endpoint for communication between two machines. It consists of an IP address and a port number.
* Server Socket - A socket that listens for connections from clients. It has to be bound to a port number and listen for connections. Once a connection is established, it creates a new socket for that client connection.
* Client Socket - A socket that initiates a connection to a server socket. It also needs to specify a port number and IP address of the server.

Steps to create a socket program:

1. Import socket library
2. Create a socket object
3. Specify the address family - AF_INET for IPv4 addresses
4. Bind the socket to an address and port number
5. For server socket, put the socket into listening mode. For client socket, connect to the server socket
6. Send and receive data
7. Close the socket

Advantages:

* Socket programming allows communication between processes on different machines.
* It is a lightweight mechanism and efficient method for IPC (Inter-Process Communication).
* It enables the creation of client-server applications. The server can handle multiple clients simultaneously.

Disadvantages:

* Complex to program and debug.
* Security issues like DoS (Denial of Service) attacks if not secured properly.
* Reliability issues if the network is unreliable. Data packets may get lost or corrupted.

Applications:

* Chat applications
* Email
* Web browsing
* Multiplayer games

[Detailed diagrams and code examples can be added here for better understanding]