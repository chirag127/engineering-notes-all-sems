#### TCP/IP Client Sockets in Networking

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet.
- A socket is one endpoint of a two-way communication link between two programs running on the network .
- A socket is externally identified by its socket address, which is the combination of transport protocol, IP address, and port number.
- A TCP/IP client socket is a socket that initiates a connection to a server socket and sends or receives data over the network .
- To create a TCP/IP client socket in Java, the following steps are required :
  - Import the java.net package, which contains the classes and interfaces for networking.
  - Create an instance of the Socket class, passing the host name and port number of the server socket as parameters to the constructor.
  - Obtain the input and output streams of the socket using the getInputStream() and getOutputStream() methods.
  - Use the input and output streams to send and receive data over the network, following the protocol agreed with the server.
  - Close the socket and the streams when the communication is finished, using the close() method.