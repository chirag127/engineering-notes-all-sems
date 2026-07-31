## Experiment 8 - Applications using TCP Sockets

TCP sockets are a type of network communication mechanism that allow two processes to exchange data using the Transmission Control Protocol (TCP). TCP is a reliable, connection-oriented protocol that ensures the data is delivered in order and without errors. TCP sockets are widely used for network applications that require reliable and bidirectional communication, such as web servers, chat applications, file transfer applications, etc.

In this experiment, you will learn how to use TCP sockets to implement some common network applications. You will need to use the socket programming interface, which provides the routines required for interprocess communication between applications, either on the same machine or across a network. You will also need to use the IP address and port number of the machines involved in the communication, as well as the socket type and protocol type that the socket uses to make connections.

Some of the applications that you will implement using TCP sockets are:

- Echo server and client: An echo server is a server that simply sends back whatever data it receives from a client. An echo client is a client that sends some data to an echo server and displays the response. This is a simple way to test the connectivity and functionality of TCP sockets.
- Web server and client: A web server is a server that responds to HTTP requests from clients and sends back the requested web resources, such as HTML files, images, etc. A web client is a client that sends HTTP requests to a web server and displays the received web resources. This is a common way to access the World Wide Web using TCP sockets.
- Chat server and client: A chat server is a server that allows multiple clients to join a chat room and exchange messages with each other. A chat client is a client that connects to a chat server and participates in the chat room. This is a common way to implement real-time communication using TCP sockets.
- File transfer server and client: A file transfer server is a server that allows clients to upload or download files from a shared directory. A file transfer client is a client that connects to a file transfer server and performs file operations, such as listing, uploading, or downloading files. This is a common way to implement file sharing using TCP sockets.

In order to implement these applications, you will need to follow these steps:

- Create a socket object using the constructor for the Socket class, which has parameters that specify the address family, socket type, and protocol type that the socket uses to make connections. For TCP sockets, you will use the AddressFamily.InterNetwork, SocketType.Stream, and ProtocolType.Tcp parameters, respectively.
- Bind the socket object to a local IP address and port number using the Bind method, which takes an IPEndPoint object as an argument. This is necessary for the server socket to listen for incoming connections from clients.
- Listen for incoming connections using the Listen method, which takes an integer argument that specifies the maximum number of pending connections that the socket can queue. This is necessary for the server socket to accept connections from clients.
- Accept a connection from a client using the Accept method, which returns a new socket object that represents the connection with the client. This is necessary for the server socket to communicate with the client socket.
- Connect to a server using the Connect method, which takes an IPEndPoint object as an argument. This is necessary for the client socket to establish a connection with the server socket.
- Send and receive data using the Send and Receive methods, which take a byte array as an argument and return an integer that indicates the number of bytes sent or received. This is necessary for both the server and client sockets to exchange data using TCP sockets.
- Close the socket using the Close method, which releases the resources associated with the socket. This is necessary for both the server and client sockets to terminate the connection gracefully.