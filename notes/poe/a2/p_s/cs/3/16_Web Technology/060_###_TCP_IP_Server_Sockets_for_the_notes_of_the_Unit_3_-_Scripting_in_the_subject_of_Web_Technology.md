 Here is the content written in markdown format for the topic ### TCP/IP Server Sockets for the notes of the Unit 3 - Scripting in the subject of Web Technology:

### TCP/IP Server Sockets

- TCP/IP sockets are the endpoints of a communication channel used for network communications following the TCP/IP protocol suite.
- A socket is bound to an IP address and port number which identifies the application and its owner.
- Sockets are created using the socket API which provides functions to open, close, send and receive data through sockets.
- There are two types of sockets:
  - Server sockets - Used to listen for incoming connection requests from clients. A server application creates a server socket, binds it to a port and listens for connections from clients. When a connection is established, it creates a new socket for that client connection.
  - Client sockets - Used to initiate connections to server applications. A client application creates a socket, connects to a server socket at a given IP address and port and starts sending/receiving data.
- To create a TCP/IP server socket:
  1. Import the socket library
  2. Create a socket object using the socket.socket() function
  3. Bind the socket to an address using socket.bind() which takes a tuple of (host, port)
  4. Listen for incoming connections using socket.listen()
  5. Accept incoming connections using socket.accept() which returns a new socket and client address
- Advantages:
  - Supports reliable data transmission with error-checking and correction.
  - Provides flow control and congestion control to prevent fast senders from overwhelming slow receivers.
  - Supports multiplexing to allow multiple connections to coexist on the same network interface and port.
- Disadvantages:
  - Headers add overhead and reduce throughput for small packets.
  - Connection setup and termination requires additional time and resources.
  - Vulnerable to certain types of Denial of Service (DoS) attacks.
- Used in applications like web servers, mail servers, remote login, network file transfer, etc.