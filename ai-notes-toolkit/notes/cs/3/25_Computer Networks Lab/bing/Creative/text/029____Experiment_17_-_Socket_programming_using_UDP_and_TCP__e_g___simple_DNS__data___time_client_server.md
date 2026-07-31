## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a protocol such as TCP or UDP.
- TCP (Transmission Control Protocol) is a connection-oriented, reliable, and stream-based protocol that ensures the delivery and ordering of data packets.
- UDP (User Datagram Protocol) is a connectionless, unreliable, and datagram-based protocol that does not guarantee the delivery and ordering of data packets.
- Stream sockets, datagram sockets, and raw sockets are the three types of socket programming interfaces.
- Stream sockets use TCP and provide a reliable and ordered stream of bytes between the nodes.
- Datagram sockets use UDP and provide an unreliable and unordered exchange of messages between the nodes.
- Raw sockets allow direct access to the network layer protocols and can be used to create custom protocols.
- Simple DNS (Domain Name System) is an application that translates domain names to IP addresses and vice versa using UDP sockets.
- Data and time client/server is an application that allows a client to request the current date and time from a server using TCP or UDP sockets.
- Echo client/server is an application that allows a client to send a message to a server and receive the same message back using TCP or UDP sockets.
- Iterative server is a server that handles one client request at a time in a sequential manner.
- Concurrent server is a server that handles multiple client requests at the same time using processes or threads.