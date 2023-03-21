 Here is the formal notes in Markdown format on the topic of TCP/IP Client Sockets without any emojis or external links:

### TCP/IP Client Sockets

1. TCP/IP is a protocol suite that defines how computers communicate over a network. It includes protocols such as IP, UDP, TCP, etc.
2. A socket is one endpoint of a two-way communication link between two programs running on the network.
3. A client socket is created by a client application to connect to a server socket. For example, a web browser creates a client socket to connect to a web server.
4. To create a TCP/IP client socket, we need to know:
- The server IP address or domain name
- The server port number

Steps to create a TCP/IP client socket:

1. Import the socket library
2. Create the socket object by calling the socket() method. Pass socket.AF_INET for IPv4 and socket.SOCK_STREAM for TCP.
3. Call the connect() method on the socket object passing the server hostname/IP and port number.
4. Send and receive data through the socket using send() and recv() methods.
5. Close the socket using close() when done.

This covers the key points regarding TCP/IP Client Sockets. Let me know if you would like me to elaborate on any of the points or add more details to the notes.