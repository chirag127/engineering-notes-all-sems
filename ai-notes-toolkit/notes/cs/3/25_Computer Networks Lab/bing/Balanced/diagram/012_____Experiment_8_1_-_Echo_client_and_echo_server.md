### Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network using sockets.
- A socket is an endpoint of a bidirectional communication channel between two processes running on different machines.
- An echo server is a server that receives data from a client and sends back an identical copy of the data to the client.
- An echo client is a client that sends data to an echo server and receives the same data back from the server.
- The purpose of this experiment is to demonstrate the basic concepts of socket programming in Java, such as creating, binding, listening, accepting, sending and receiving sockets.
- The steps of this experiment are as follows:

  1. Create a single-threaded TCP echo server that listens on a specific port for incoming connections from clients.
  2. Create a TCP echo client that connects to the echo server on the same port and sends a message to the server.
  3. The echo server receives the message from the client and echoes it back to the client.
  4. The echo client receives the echoed message from the server and prints it on the standard output.
  5. The echo client and server close their sockets and terminate.

- The code for the echo server and client can be found in the following sources  .