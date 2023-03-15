### TCP/IP Server Sockets

- TCP/IP server sockets are used to create servers that listen for either local or remote client programs to connect to them on published ports.
- TCP/IP server sockets use the Transmission Control Protocol (TCP), which is a connection-oriented protocol that ensures reliable and ordered delivery of data .
- TCP/IP server sockets require three steps to establish a connection with a client socket: 
  - The server socket creates a socket object and binds it to a specific port number.
  - The server socket calls the listen() method to start listening for incoming connection requests on the port.
  - The server socket calls the accept() method to accept a connection request from a client socket and returns a new socket object that represents the connection .
- TCP/IP server sockets can send and receive data over the connection using the read() and write() methods of the socket object.
- TCP/IP server sockets can close the connection with the client socket by calling the close() method of the socket object.
- TCP/IP server sockets are different from UDP sockets, which are connectionless and do not guarantee reliable and ordered delivery of data.