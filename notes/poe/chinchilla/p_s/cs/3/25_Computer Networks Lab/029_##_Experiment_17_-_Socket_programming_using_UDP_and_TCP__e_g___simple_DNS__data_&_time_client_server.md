## Experiment 17 - Socket Programming using UDP and TCP

Socket programming is an essential part of network programming. It allows applications to communicate with each other over a network. In this experiment, we will learn about socket programming using UDP and TCP protocols. We will discuss various client/server applications such as simple DNS, data & time client/server, echo client/server, iterative & concurrent servers.

### Transmission Control Protocol (TCP)

TCP is a connection-oriented protocol that provides reliable and ordered delivery of data. It establishes a connection between two devices before data transmission. This protocol guarantees the delivery of data without any loss, duplication, or error. It uses a three-way handshake protocol to establish a connection. The three steps are:

1. SYN: The client sends a SYN to the server to initiate the connection.
2. SYN-ACK: The server responds with a SYN-ACK to acknowledge the request.
3. ACK: The client sends an ACK to confirm the connection.

TCP is used for applications where data integrity is critical, such as file transfer, email, and web browsing.

### User Datagram Protocol (UDP)

UDP is a connectionless protocol that provides unreliable and unordered delivery of data. It does not establish a connection before data transmission. This protocol does not guarantee the delivery of data, and data loss may occur. It is used for applications where speed and efficiency are critical, such as video streaming and online gaming.

### Simple DNS

DNS (Domain Name System) is a protocol used to map human-friendly domain names to IP addresses. In the simple DNS client/server application, the client sends a request to the server to resolve a domain name. The server then responds with the corresponding IP address.

### Data & Time Client/Server

The data & time client/server application is used to retrieve the current date and time from the server. The client sends a request to the server, and the server responds with the current date and time.

### Echo Client/Server

The echo client/server application is used to test the connectivity between two devices. The client sends a message to the server, and the server echoes the message back to the client. This application is useful for testing network latency and packet loss.

### Iterative & Concurrent Servers

Iterative servers handle one client at a time. They wait for the current client to finish before accepting new connections. Concurrent servers, on the other hand, can handle multiple clients simultaneously. They use threads or processes to handle each client separately.

#### Advantages of Iterative Servers

- Simple to implement
- Low resource usage
- Easy to debug

#### Disadvantages of Iterative Servers

- Slow response time for multiple clients
- Limited scalability

#### Advantages of Concurrent Servers

- High scalability
- Fast response time for multiple clients
- Can handle more clients than iterative servers

#### Disadvantages of Concurrent Servers

- Complex to implement
- High resource usage
- Difficult to debug

In conclusion, socket programming is an essential skill for network programmers. By learning about TCP and UDP protocols and various client/server applications, you can develop robust and efficient network applications. Understanding the differences between iterative and concurrent servers can help you choose the best approach for your application.