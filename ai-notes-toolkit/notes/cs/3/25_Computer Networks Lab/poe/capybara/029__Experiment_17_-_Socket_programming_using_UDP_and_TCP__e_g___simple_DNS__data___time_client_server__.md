## Experiment 17 - Socket programming using UDP and TCP

Socket programming is a way to allow communication between processes on different computers or devices. In this experiment, we will explore socket programming using both the UDP and TCP protocols. We will create several different types of servers and clients, including simple DNS, data & time client/server, echo client/server, and iterative & concurrent servers. Here are some key points to keep in mind when studying this topic:

- Socket programming is a way to allow communication between processes on different computers or devices.
- The User Datagram Protocol (UDP) is a connectionless protocol that does not guarantee delivery or order of messages. This makes it useful for applications that require fast transmission, such as online gaming or streaming video.
- The Transmission Control Protocol (TCP) is a connection-oriented protocol that guarantees delivery and order of messages. This makes it useful for applications that require reliable transmission, such as file transfer or email.
- DNS (Domain Name System) is a protocol used to translate domain names (such as www.google.com) into IP addresses (such as 172.217.6.68). In our simple DNS server, we will implement a basic version of this protocol.
- The data & time client/server will allow clients to request the current date and time from the server. The server will respond with the current date and time in a standard format.
- The echo client/server will allow clients to send messages to the server, which will then echo the message back to the client. This is a simple way to test the connection between the client and server.
- Iterative servers handle one client at a time, while concurrent servers can handle multiple clients at once. We will implement both types of servers and compare their performance.

Overall, socket programming using UDP and TCP is an important topic for anyone interested in network programming. By understanding the differences between these protocols and the different types of servers and clients that can be created, you will be well prepared to develop your own network applications.