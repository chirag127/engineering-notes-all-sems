### TCP/IP Client Sockets

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet .
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- A TCP/IP client socket is a socket that initiates a connection to a server socket and exchanges data with it .
- A TCP/IP client socket is defined by the IP address and port number of the server socket, as well as the local port number of the client socket .
- To create a TCP/IP client socket in Java, the following steps are required  :
  - Import the `java.net` and `java.io` packages.
  - Create an instance of the `Socket` class, passing the server IP address and port number as arguments to the constructor.
  - Obtain the input and output streams of the socket using the `getInputStream()` and `getOutputStream()` methods.
  - Use the input and output streams to read and write data to and from the server socket, following the protocol defined by the server application.
  - Close the socket and the streams when the communication is finished, using the `close()` method.
- A TCP/IP client socket can also be created in other languages, such as C, C++, Python, etc., using similar steps and functions  .
- A TCP/IP client socket can communicate with multiple server sockets, as long as they use different port numbers .
- A TCP/IP client socket can also use the `connect()` method to establish a connection to a server socket, instead of passing the server IP address and port number to the constructor.
- A TCP/IP client socket can handle errors and exceptions using the `try-catch-finally` blocks or the `throws` clause in Java, or the `errno` variable or the `perror()` function in C and C++ .
- A TCP/IP client socket can use the `setSoTimeout()` method to specify a timeout value for the socket operations, such as reading and writing data .