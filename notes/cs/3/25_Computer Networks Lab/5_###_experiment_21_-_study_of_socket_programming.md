### Experiment 2.1 - Study of Socket Programming

Experiment 2.1 - Study of Socket Programming covers the following topic:

1. Socket Programming:
Socket programming is a method of communication between two processes over a network. It involves creating a socket on one end of the communication, and connecting to the socket on the other end.

2. How it works:
In socket programming, the processes communicate by sending messages to each other over the network. The messages are sent and received using the sockets.

The process that initiates the communication creates a socket and binds it to a specific port on the network. The other process connects to the socket using the IP address of the computer that created the socket and the port number.

Once the connection has been established, the processes can send and receive messages using the sockets. The messages are sent using the send() function, and received using the recv() function.

3. Advantages:
Socket programming has several advantages, including:
1. Flexibility: Socket programming allows for communication between processes running on different operating systems and platforms.
2. Scalability: Socket programming can handle multiple connections, allowing for scalability and the ability to support large numbers of clients.
3. Performance: Socket programming provides a fast and efficient means of communication between processes.

In conclusion, Experiment 2.1 - Study of Socket Programming is an important aspect of network programming. By understanding the basics of socket programming, developers can create efficient and scalable applications that can communicate over a network.
