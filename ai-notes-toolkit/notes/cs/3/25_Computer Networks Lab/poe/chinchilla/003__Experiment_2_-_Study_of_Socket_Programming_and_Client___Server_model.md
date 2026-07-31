## Experiment 2 - Study of Socket Programming and Client – Server model

In this experiment, we aim to study the basics of socket programming and the client-server model. The following points will cover the important aspects of this topic:

1. **Socket programming:** Socket programming is a way of creating network applications that communicate with each other using a socket. A socket is a virtual endpoint of a two-way communication link between two programs running on the network. It allows two or more processes to communicate with each other, both locally and over a network.

2. **Client-server model:** The client-server model is a way of structuring network applications where one program, the client, requests information or services from another program, the server. The server responds to the client's request and provides the requested information or service. This model is commonly used in web applications, where a web browser acts as the client and a web server provides the requested web pages.

3. **Types of sockets:** There are two types of sockets in socket programming: Stream sockets and Datagram sockets. Stream sockets provide a reliable, connection-oriented service, while Datagram sockets provide an unreliable, connectionless service.

4. **TCP and UDP:** TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are the most commonly used protocols in socket programming. TCP provides a reliable, connection-oriented service, while UDP provides an unreliable, connectionless service.

5. **Socket API:** Socket programming is done using the Socket API, which is a set of functions and data structures that provide an interface for creating and using sockets. The Socket API is platform-independent and can be used on any operating system that supports sockets.

6. **Socket address:** A socket address is a combination of an IP address and a port number. It uniquely identifies a socket on the network.

7. **Socket programming in Python:** Python provides a built-in module called `socket` that can be used for socket programming. The `socket` module provides functions for creating, binding, connecting, and sending/receiving data over sockets.

8. **Server programming in Python:** To create a server using Python, we need to create a socket object and bind it to a specific address and port number. We then listen for incoming connections and accept them using the `accept()` method. Once a connection is established, we can send and receive data using the socket object.

9. **Client programming in Python:** To create a client using Python, we need to create a socket object and connect it to a specific address and port number. We can then send and receive data using the socket object.

10. **Common socket errors:** There are several common errors that can occur when working with sockets, such as "Address already in use", "Connection refused", and "Socket timeout". These errors can be handled using exception handling in Python.

In conclusion, socket programming and the client-server model are important concepts in network programming. Understanding these concepts and the Socket API will allow us to create network applications that can communicate with each other over a network.