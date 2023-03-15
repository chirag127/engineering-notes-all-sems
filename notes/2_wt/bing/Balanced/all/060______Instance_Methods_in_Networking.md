#### Instance Methods in Networking

- Instance methods are methods that are defined on an instance of a class, such as a socket, a server, or a client.
- Instance methods can be used to perform operations on the instance, such as sending and receiving data, closing the connection, or setting options.
- Instance methods are usually invoked by using the dot notation, such as `socket.send(data)` or `server.accept()`.
- Some common instance methods in networking are:

  - `socket.bind(address)`: This method binds the socket to a local address and port. The address argument is a tuple of (host, port), where host is a string representing the hostname or IP address, and port is an integer representing the port number. This method is usually used by servers to listen for incoming connections on a specific address and port.
  - `socket.listen(backlog)`: This method enables the socket to accept connections. The backlog argument specifies the maximum number of queued connections that can be waiting to be accepted. This method is usually used by servers after binding the socket to an address and port.
  - `socket.accept()`: This method waits for an incoming connection and returns a new socket object and the address of the client. The address is a tuple of (host, port), where host is a string representing the hostname or IP address of the client, and port is an integer representing the port number of the client. This method is usually used by servers to accept a connection from a client and create a new socket for communication.
  - `socket.connect(address)`: This method connects the socket to a remote address and port. The address argument is a tuple of (host, port), where host is a string representing the hostname or IP address of the server, and port is an integer representing the port number of the server. This method is usually used by clients to initiate a connection to a server.
  - `socket.send(data)`: This method sends data to the connected socket. The data argument is a bytes object containing the data to be sent. This method returns the number of bytes sent, which may be less than the length of the data. This method is usually used by both servers and clients to send data to each other.
  - `socket.recv(bufsize)`: This method receives data from the connected socket. The bufsize argument specifies the maximum number of bytes to be received. This method returns a bytes object containing the data received, which may be less than the bufsize. This method is usually used by both servers and clients to receive data from each other.
  - `socket.close()`: This method closes the socket and frees the resources associated with it. This method is usually used by both servers and clients to terminate the connection and release the socket.

- A possible mnemonic to remember some of the instance methods in networking is:

  - **B**ind, **L**isten, **A**ccept, **C**onnect, **S**end, **R**ecv, **C**lose
  - **BLAC SRC** (sounds like black source)