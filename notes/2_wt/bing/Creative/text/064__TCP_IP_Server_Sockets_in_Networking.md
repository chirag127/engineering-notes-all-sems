#### TCP/IP Server Sockets in Networking

- A network socket is a software structure within a network node of a computer network that serves as an endpoint for sending and receiving data across the network.
- A network socket is externally identified by its socket address, which is the triad of transport protocol, IP address, and port number.
- A TCP/IP server socket is a network socket that uses the Transmission Control Protocol (TCP) to establish and maintain a connection-oriented communication with a client socket .
- A TCP/IP server socket is defined by the IP address of the machine and the port it uses . For example, a web server socket may be 100.1.1.1:80, where 100.1.1.1 is the IP address and 80 is the port number.
- A TCP/IP server socket listens for incoming connection requests from client sockets on a specific port . When a connection request is received, the server socket accepts it and creates a new socket for the data exchange with the client socket .
- A TCP/IP server socket can handle multiple client sockets concurrently by using threads or processes . Each client socket is assigned a unique socket address by the server socket .
- A TCP/IP server socket provides reliable, ordered, and error-checked delivery of data to and from the client socket . It uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection .
- A TCP/IP server socket can send and receive data using the Socket class in .NET. The Socket class provides methods and properties for network communication, such as Bind, Listen, Accept, Send, and Receive.