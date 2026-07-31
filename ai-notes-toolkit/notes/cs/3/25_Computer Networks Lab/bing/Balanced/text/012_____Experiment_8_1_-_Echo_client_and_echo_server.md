### Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that communicate over a network using sockets.
- An echo client sends a message to an echo server, and the echo server receives the message and sends back an identical copy of the message to the echo client.
- The purpose of this experiment is to demonstrate the basic concepts of socket programming in Java, such as creating, binding, listening, accepting, reading, and writing sockets.
- The steps of this experiment are as follows:

  1. Create a single-threaded TCP echo server that listens on a specific port and prints out the received messages on the standard output.
  2. Create a TCP echo client that connects to the echo server, reads a line of input from the keyboard, and sends it to the echo server.
  3. Run the echo server and the echo client on the same or different machines, and observe the communication between them.
  4. Modify the echo server and the echo client to handle multiple messages and close the connection gracefully.
  5. Experiment with different types of messages, such as empty, long, or binary messages, and see how the echo server and the echo client handle them.
  6. Optionally, create a UDP echo server and a UDP echo client, and compare the differences between TCP and UDP sockets.