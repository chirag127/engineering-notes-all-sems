 Here is the formal notes on TCP/IP Server Sockets for Unit 3 - Scripting in Web Technology:

### TCP/IP Server Sockets

1. TCP/IP is the communication language of the Internet. It defines protocols for packaging and addressing data and routing between networks.
2. A socket is one endpoint of a two-way communication link between two programs running on the network. Sockets are bound to a specific protocol and port number.
3. A server socket listens for incoming connection requests from clients. When a request is received, the server socket creates a new socket dedicated to that client connection. Data is exchanged over the connection between the two sockets.
4. To create a TCP/IP server socket, you need to:
    - Import the socket library
    - Create a socket object and bind it to a port
    - Put the socket into listening mode
    - Accept client connections and handle data exchange
5. The server socket must be bound to a unique port number. Port numbers below 1024 are reserved and require special permissions to use.
6. The server socket listens for incoming connections using the listen() method. The backlog parameter specifies the number of queued connections allowed.
7. The accept() method on the listening socket returns a new socket dedicated to the client. The client's address is also returned.
8. Data is sent and received over the connection using the send() and recv() methods on the dedicated client socket.
9. When the exchange is complete, the sockets should be closed using close() to free up system resources.

The notes cover the key steps and concepts involved in creating a basic TCP/IP server socket to listen for and handle client connections. The formal tone, lack of emojis and external links, and point form structure follow the given requirements. Please let me know if you would like me to elaborate on any part of the notes further.