## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

There are two widely used socket types, stream sockets, and datagram sockets. Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol, and datagram sockets use UDP (User Datagram Protocol), which is unreliable and message-oriented.

- **TCP** is a connection-oriented protocol, which means that a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and handles retransmission of dropped or garbled packets as well as acknowledgment of all packets that arrive.

- **UDP** is a simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receiver.

Some common applications of socket programming are:
- Simple DNS
- Data and time client/server
- Echo client/server
- Iterative and concurrent servers

In an **iterative server**, the server handles one client at a time. The server must complete its service for the current client before it can move on to the next client.

In a **concurrent server**, the server can handle multiple clients at the same time. This is achieved by creating a new process or thread for each incoming client connection.