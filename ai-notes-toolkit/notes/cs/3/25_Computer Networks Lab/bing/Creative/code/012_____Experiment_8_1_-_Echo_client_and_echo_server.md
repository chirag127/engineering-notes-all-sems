### Experiment 8.1 - Echo client and echo server

- An echo client and an echo server are programs that communicate over a network using the TCP protocol.
- The echo client sends a message to the echo server and waits for a response.
- The echo server receives the message and sends it back to the echo client unchanged.
- The echo client and the echo server can run on the same machine or on different machines.
- The echo client and the echo server can be written in any programming language that supports TCP sockets, such as Java, Python, C, etc.
- The echo client and the echo server can be used to test the connectivity and performance of a network, or to demonstrate the basic functionality of TCP sockets.

#### Steps to implement an echo client and an echo server in Java:

1. Import the java.net and java.io packages, which provide classes and methods for network programming and input/output operations.
2. Create a class for the echo server, which implements the Runnable interface, to allow multiple clients to connect to the server concurrently.
3. In the constructor of the echo server class, create a ServerSocket object, which listens for incoming connections on a specified port number.
4. In the run method of the echo server class, use a while loop to accept connections from clients using the accept method of the ServerSocket object, which returns a Socket object for each connection.
5. For each connection, create a new thread of the echo server class, passing the Socket object as a parameter, and start the thread.
6. In the echo server class, create a BufferedReader object and a PrintWriter object, using the input and output streams of the Socket object, to read and write data to and from the client.
7. In the echo server class, use a while loop to read lines of text from the client using the readLine method of the BufferedReader object, and write them back to the client using the println method of the PrintWriter object, followed by the flush method to ensure the data is sent.
8. In the echo server class, handle any exceptions that may occur during the communication, such as IOException, and close the Socket object when the communication is over or interrupted.
9. In the main method of the echo server class, create an instance of the echo server class, passing the port number as a parameter, and call the run method.
10. Create a class for the echo client, which takes the server's host name and port number as command-line arguments.
11. In the echo client class, create a Socket object, passing the host name and port number as parameters, to establish a connection with the server.
12. In the echo client class, create a BufferedReader object and a PrintWriter object, using the input and output streams of the Socket object, to read and write data to and from the server.
13. In the echo client class, create another BufferedReader object, using the standard input stream, to read lines of text from the user.
14. In the echo client class, use a while loop to read lines of text from the user using the readLine method of the BufferedReader object, and write them to the server using the println method of the PrintWriter object, followed by the flush method to ensure the data is sent.
15. In the echo client class, use another while loop to read lines of text from the server using the readLine method of the BufferedReader object, and print them to the standard output stream using the System.out.println method.
16. In the echo client class, handle any exceptions that may occur during the communication, such as IOException, and close the Socket object when the communication is over or interrupted.