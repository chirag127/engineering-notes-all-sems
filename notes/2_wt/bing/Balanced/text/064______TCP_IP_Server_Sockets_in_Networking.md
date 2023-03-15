#### TCP/IP Server Sockets in Networking

- A socket is an endpoint of a communication between two processes running on different machines on a network.
- A TCP/IP server socket is a socket that listens for incoming connections from TCP/IP clients on a specific port and address.
- A TCP/IP server socket can accept multiple connections from different clients, but only one connection per client at a time.
- A TCP/IP server socket can perform the following steps to establish a communication with a client:
  - Create a socket object with a specific port and address, or let the system assign them automatically.
  - Bind the socket object to the port and address using the bind() method.
  - Listen for incoming connection requests from clients using the listen() method, specifying the maximum number of queued requests.
  - Accept a connection request from a client using the accept() method, which returns a new socket object for the communication with the client, and the client's address and port.
  - Send and receive data to and from the client using the send() and recv() methods, or other methods such as sendall() and recvfrom().
  - Close the connection with the client using the close() method, or let the system close it automatically when the socket object is destroyed.
  - Repeat steps 4 to 6 for other clients, or close the server socket using the close() method, or let the system close it automatically when the socket object is destroyed.

- A TCP/IP server socket can use either blocking or non-blocking mode to handle the connections from clients.
  - In blocking mode, the server socket waits until a connection request or data is available before returning from the accept() or recv() methods, respectively. This mode is simpler to implement, but may cause the server to be unresponsive to other clients or events while waiting.
  - In non-blocking mode, the server socket returns immediately from the accept() or recv() methods, even if no connection request or data is available. This mode allows the server to handle multiple clients or events concurrently, but requires more complex logic and error handling.