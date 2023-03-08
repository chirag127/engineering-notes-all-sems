### Experiment 2.1 - Study of Socket Programming

Socket Programming is a technique of networking programming that allows two or more nodes (devices) to communicate with each other. In this experiment, we will learn the basics of Socket Programming, its types, and how to use it to establish communication between two nodes.

#### What are Sockets?

A socket is an endpoint of a two-way communication link between two nodes on a network. It is a combination of an IP address and a port number that uniquely identifies a process running on a device. Sockets are used for inter-process communication (IPC) within a single device or inter-network communication between multiple devices.

#### Types of Sockets

There are two types of sockets: 

1. Stream Sockets (TCP)
2. Datagram Sockets (UDP)

##### Stream Sockets (TCP)

Stream sockets provide a reliable, connection-oriented communication channel between two nodes. It ensures that data is delivered in the same order in which it was sent and without any errors. It uses the Transmission Control Protocol (TCP) as the underlying protocol for communication.

##### Datagram Sockets (UDP)

Datagram sockets provide an unreliable, connectionless communication channel between two nodes. It does not guarantee that data will be delivered in the same order in which it was sent or without any errors. It uses the User Datagram Protocol (UDP) as the underlying protocol for communication.

#### How to Use Sockets

Using sockets in programming involves creating a socket, binding it to an IP address and port number, and then either listening for incoming connections or connecting to a remote socket.

Here are the basic steps to use sockets:

1. Create a socket using the `socket()` function.
2. Bind the socket to an IP address and a port number using the `bind()` function.
3. Listen for incoming connections using the `listen()` function (for server applications).
4. Accept incoming connections using the `accept()` function (for server applications).
5. Connect to a remote socket using the `connect()` function (for client applications).
6. Send and receive data using the `send()` and `recv()` functions.

#### Advantages of Socket Programming

- Allows communication between different devices on a network.
- Provides a reliable and efficient method of data transfer.
- Supports different types of communication protocols (TCP, UDP, etc.).
- Can be used for various applications such as file transfer, email, chat, etc.

#### Disadvantages of Socket Programming

- Requires knowledge of networking concepts and protocols.
- Can be complex to implement and debug.
- Security concerns such as data encryption and authentication must be addressed.

#### Examples of Socket Programming

- Chat applications
- Online gaming
- File transfer applications
- Email clients
- Web browsers

Overall, Socket Programming is an essential concept in networking programming, and understanding it is crucial for developing various network applications.