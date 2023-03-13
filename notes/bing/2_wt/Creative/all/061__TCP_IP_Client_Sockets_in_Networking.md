#### TCP/IP Client Sockets in Networking

- TCP/IP sockets are used to implement reliable, bidirectional, persistent, point-to-point, stream-based connections between hosts on the Internet.
- A socket can be used to connect Java’s I/O system to other programs that may reside either on the local machine or on any other machine on the Internet.
- A TCP socket is defined by the IP address of the machine and the port it uses. The TCP socket guarantees that all data is received and acknowledged.
- For example, we are sending an HTTP request from our client at 120.1.1.1 to the website at 189.1.1.1. The client socket is 120.1.1.1:1234 and the server socket is 189.1.1.1:80.
- Before you can initiate a conversation through a socket, you create a data pipe between your app and the remote destination. TCP/IP uses a network address and a service port number to uniquely identify a service.
- The constructor for the Socket class has parameters that specify the address family, socket type, and protocol type that the socket uses to make connections. When connecting a client socket to a server socket, the client will use an IPEndPoint object to specify the network address of the server.
- A socket is one endpoint of a two way communication link between two programs running on the network. The socket mechanism provides a means of inter-process communication (IPC) by establishing named contact points between which the communication take place.
- In the standard Internet protocols TCP and UDP, a socket address is the combination of an IP address and a port number, much like one end of a telephone connection is the combination of a phone number and a particular extension.

- A possible mnemonic to remember the features of TCP/IP sockets is: **R**eal **B**oys **P**lay **S**occer **G**reatly.

  - **R**eal: Reliable
  - **B**oys: Bidirectional
  - **P**lay: Persistent
  - **S**occer: Stream-based
  - **G**reatly: Guaranteed

- A possible learning trick to understand the concept of sockets is to use an analogy of a telephone call. A socket is like a phone that can make and receive calls. A socket address is like a phone number and an extension. A socket connection is like a phone line that connects two phones. A socket communication is like a conversation that takes place over the phone line.