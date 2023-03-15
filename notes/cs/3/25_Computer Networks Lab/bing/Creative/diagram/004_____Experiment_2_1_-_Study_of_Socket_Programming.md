### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A node represents a computer or a physical device with an internet connection.
- A socket is the endpoint used for connecting to a node. It is created by the combination of the IP address and port number of the software.
- Socket programming tells us how we can use socket API for creating communication between local and remote processes.
- Socket programming can be done in different languages, such as C, C++, Python, Java, etc.
- Socket programming can be classified into two types: stream sockets and datagram sockets.
- Stream sockets use TCP (Transmission Control Protocol) for reliable and ordered data transfer.
- Datagram sockets use UDP (User Datagram Protocol) for fast and connectionless data transfer.
- Socket programming involves the following steps :
  - Socket creation: We use a function to create a socket object with a specific address family, socket type and protocol.
  - Socket binding: We use a function to bind the socket object to a specific IP address and port number on the local machine.
  - Socket listening: We use a function to make the socket object listen for incoming connections from other nodes.
  - Socket accepting: We use a function to accept a connection request from another node and return a new socket object for communication.
  - Socket connecting: We use a function to initiate a connection to another node by specifying its IP address and port number.
  - Socket sending and receiving: We use functions to send and receive data through the socket objects.
  - Socket closing: We use a function to close the socket objects and release the resources.