## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

There are two widely used socket types, stream sockets, and datagram sockets. Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol, and datagram sockets use UDP (User Datagram Protocol), which is unreliable and message-oriented.

- **TCP** is a connection-oriented protocol, which means that a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and handles retransmission of dropped or garbled packets as well as acknowledgment of all packets that arrive.

- **UDP** is a simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receiver.

Some examples of applications that use socket programming are:

- **Simple DNS**: DNS (Domain Name System) is used to translate human-readable domain names into IP addresses. A simple DNS application can be created using socket programming to send a domain name to a DNS server and receive the corresponding IP address.

- **Data & Time Client/Server**: A data and time client/server application can be created using socket programming, where the client sends a request to the server for the current date and time, and the server responds with the requested information.

- **Echo Client/Server**: An echo client/server application can be created using socket programming, where the client sends a message to the server, and the server responds by sending the same message back to the client.

- **Iterative & Concurrent Servers**: An iterative server handles one client at a time, while a concurrent server can handle multiple clients simultaneously. Both types of servers can be created using socket programming.

In summary, socket programming is a powerful tool for creating network-based applications using TCP and UDP protocols. It allows for the creation of a wide range of applications, from simple DNS and data & time client/server applications to more complex iterative and concurrent servers.