### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of enabling communication between different processes or machines using network protocols.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol, such as TCP or UDP.
- Socket programming involves creating, configuring, and using sockets to establish connections and exchange data.
- Socket programming can be done in various programming languages, such as C, Python, Java, etc.
- Socket programming can be used for various applications, such as web servers, chat applications, file transfer, etc.

Some basic steps involved in socket programming are:

- Create a socket using the socket() function, specifying the address family, socket type, and protocol.
- Bind the socket to a local address and port using the bind() function.
- Listen for incoming connections using the listen() function (for server sockets) or connect to a remote address and port using the connect() function (for client sockets).
- Accept a connection request from a client using the accept() function (for server sockets) or send and receive data using the send() and recv() functions (for client sockets).
- Close the socket using the close() function when the communication is over.