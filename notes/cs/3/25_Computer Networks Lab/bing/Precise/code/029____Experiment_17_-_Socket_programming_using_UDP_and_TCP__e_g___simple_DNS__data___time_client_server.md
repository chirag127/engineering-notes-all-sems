## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

There are two widely used socket types, stream sockets, and datagram sockets. Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol, and datagram sockets use UDP (User Datagram Protocol), which is unreliable and message-oriented.

- **TCP** is a connection-oriented protocol, which means that a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and handles retransmission of dropped or garbled packets as well as acknowledgment of all packets that arrive.

- **UDP** is a simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receiver.

Some common applications of socket programming are:

- **Simple DNS:** Domain Name System (DNS) is a distributed database that translates domain names to IP addresses. A simple DNS server can be implemented using socket programming to listen for DNS queries and respond with the corresponding IP address.

- **Data & Time Client/Server:** A time server can be implemented using socket programming to listen for time requests and respond with the current date and time. A time client can also be implemented to send time requests to the server and display the received date and time.

- **Echo Client/Server:** An echo server is a server that simply sends back any data it receives. An echo client can be implemented to send data to the server and display the received echoed data.

- **Iterative & Concurrent Servers:** An iterative server handles one client at a time, processing each request before moving on to the next. A concurrent server, on the other hand, can handle multiple clients simultaneously, processing each request concurrently using threads or processes.

In summary, socket programming using UDP and TCP allows for the implementation of various network applications, including simple DNS, data & time client/server, echo client/server, and iterative & concurrent servers. These applications can be implemented using either the reliable, connection-oriented TCP or the simpler, connectionless UDP, depending on the requirements of the application.