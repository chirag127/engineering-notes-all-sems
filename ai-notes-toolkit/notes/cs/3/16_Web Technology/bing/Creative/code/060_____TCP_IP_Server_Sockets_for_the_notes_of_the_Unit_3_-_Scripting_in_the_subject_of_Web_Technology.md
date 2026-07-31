### TCP/IP Server Sockets

- TCP/IP server sockets are used to create servers that listen for either local or remote client programs to connect to them on published ports.
- TCP/IP server sockets use the Transmission Control Protocol (TCP), which is a connection-oriented protocol that ensures reliable and ordered delivery of data .
- TCP/IP server sockets require three steps to establish a connection with a client socket: 
  - The server socket creates a socket object and binds it to a specific port number.
  - The server socket calls the listen() method to start listening for incoming connection requests on the bound port.
  - The server socket calls the accept() method to accept a connection request from a client socket and returns a new socket object that represents the connection .
- TCP/IP server sockets can use the socket object returned by the accept() method to communicate with the client socket by sending and receiving data using the write() and read() methods .
- TCP/IP server sockets can handle multiple client connections by creating a new thread for each accepted connection and using the socket object in the thread to communicate with the client socket .
- TCP/IP server sockets can close the connection with a client socket by calling the close() method on the socket object .