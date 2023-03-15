# TCP/IP Server Sockets

- TCP/IP server sockets are used to create servers that listen for either local or remote client programs to connect to them on published ports.
- TCP/IP server sockets use the Transmission Control Protocol (TCP), which is a connection-oriented protocol that ensures reliable and ordered delivery of data .
- TCP/IP server sockets require three steps to establish a connection with a client socket: 
  - Create a ServerSocket object and bind it to a port number.
  - Call the accept() method of the ServerSocket object to wait for a client connection request. This method returns a Socket object that represents the connection with the client.
  - Use the getInputStream() and getOutputStream() methods of the Socket object to communicate with the client using input and output streams .
- TCP/IP server sockets can handle multiple client connections by creating a new thread for each client socket and using the synchronized keyword to avoid data inconsistency.
- TCP/IP server sockets can be closed by calling the close() method of the ServerSocket object and the Socket object .