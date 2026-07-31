# Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network using sockets.
- A socket is an endpoint of a bidirectional communication channel between two processes running on different machines.
- An echo server is a server that receives data from a client and sends back an identical copy of the data to the client. This is useful for testing the connectivity and performance of the network.
- An echo client is a client that connects to an echo server, sends some data, and waits for the server to echo it back. The client can then compare the sent and received data to verify the integrity and reliability of the network.
- To create an echo client and echo server using Java, the following steps are required:
  - Import the java.net and java.io packages, which provide classes and methods for network programming and input/output operations.
  - Create a ServerSocket object on the server side, which listens for incoming connections on a specified port number.
  - Create a Socket object on the client side, which connects to the server's IP address and port number.
  - Create input and output streams on both the server and the client sides, which allow reading and writing data to and from the sockets.
  - Use a loop on the server side to accept connections from multiple clients, and create a new thread for each client to handle the communication.
  - Use a loop on the client side to read data from the standard input, write it to the output stream of the socket, read the echoed data from the input stream of the socket, and print it to the standard output.
  - Close the sockets and the streams when the communication is done.