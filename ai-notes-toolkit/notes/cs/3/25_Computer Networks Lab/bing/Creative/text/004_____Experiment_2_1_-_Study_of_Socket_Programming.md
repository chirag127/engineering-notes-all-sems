### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A node represents a computer or a physical device with an internet connection.
- A socket is the endpoint used for connecting to a node. It is created by the combination of the IP address and port number of the software.
- Socket programming tells us how we can use socket API for creating communication between local and remote processes.
- Socket programming can be done in different languages, such as C, C++, Python, Java, etc. Each language has its own socket library and functions .
- Socket programming can be classified into two types: TCP and UDP. TCP stands for Transmission Control Protocol and UDP stands for User Datagram Protocol. TCP is reliable, ordered and error-checked, while UDP is unreliable, unordered and not error-checked.
- Socket programming can be used for various applications, such as web browsing, email, chat, file transfer, remote login, etc.
- Socket programming can be learned by following some steps, such as:
  - Understanding the basic concepts of network communication, such as IP addresses, ports, protocols, etc.
  - Choosing a programming language and a socket library to work with.
  - Creating a socket using the socket function and specifying the domain, type and protocol.
  - Setting the socket options using the setsockopt function to manipulate the socket behavior.
  - Binding the socket to a specific address and port using the bind function.
  - Listening for incoming connections using the listen function (for server sockets) or connecting to a remote socket using the connect function (for client sockets).
  - Accepting a connection from a client socket using the accept function (for server sockets) or sending and receiving data using the send and recv functions (for client sockets).
  - Closing the socket using the close function when the communication is over.