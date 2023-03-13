#### Instance Methods in Networking

- Instance methods are methods that are defined on an instance of a class, such as a socket, a server, or a client.
- Instance methods can be used to perform various operations on the instance, such as sending and receiving data, closing the connection, or listening for incoming requests.
- Instance methods are usually invoked by using the dot notation, such as `socket.send(data)` or `server.accept()`.
- Some common instance methods in networking are:

  - `socket.bind(address)`: This method binds the socket to a specific address and port. The address can be a hostname, an IP address, or an empty string to accept connections from any interface. The port can be a number or a service name, such as 'http' or 'ftp'.
  - `socket.listen(backlog)`: This method enables the socket to accept incoming connections. The backlog argument specifies the maximum number of queued connections that can be waiting before the socket starts rejecting new ones.
  - `socket.accept()`: This method blocks until a new connection is established. It returns a pair of values: a new socket object that represents the connection, and the address of the client.
  - `socket.connect(address)`: This method connects the socket to a remote address and port. The address can be a hostname, an IP address, or a tuple of both. The port can be a number or a service name, such as 'http' or 'ftp'.
  - `socket.send(data)`: This method sends data to the connected socket. The data can be a string, a bytes object, or any object that supports the buffer protocol. The method returns the number of bytes sent, which may be less than the length of the data if the socket is non-blocking or the buffer is full.
  - `socket.recv(bufsize)`: This method receives data from the connected socket. The bufsize argument specifies the maximum number of bytes to read. The method returns a bytes object containing the data received, which may be empty if the socket is non-blocking or no data is available.
  - `socket.close()`: This method closes the socket and frees the resources associated with it. It also shuts down both ends of the connection, preventing any further data transmission. The method does not return any value.
  - `server.serve_forever()`: This method runs the server until it is stopped by calling `server.shutdown()` or by an exception. It handles incoming requests by creating a new thread for each one and calling the `server.handle_request()` method. The method does not return any value.