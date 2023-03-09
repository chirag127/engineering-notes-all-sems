 Here is the content in markdown format for the given topic:

## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

### Socket Programming
Socket programming is a way of connecting two nodes on a network to communicate with each other. One node acts as a client and the other acts as a server. They can communicate using TCP or UDP protocols.

### TCP Sockets
TCP provides reliable, ordered, and error-checked delivery of transmitted data. Some key points about TCP sockets:

- A connection is established between the client and server before any data is exchanged.
- Data is transmitted in streams of bytes and received in-order.
- Data transmission is reliable and errors are detected and corrected.
- Throughput is lower than UDP but more reliable.

Examples of TCP sockets:
- Chat applications
- File transfer
- Web browsing

### UDP Sockets
UDP provides fast and efficient transmission of data without establishing a dedicated end-to-end connection. Some key points about UDP sockets:

- Data is transmitted in packets of bytes.
- Packets may be received out of order or lost.
- No connection setup is required.
- Higher throughput but less reliable than TCP.

Examples of UDP sockets:
- Video streaming
- Online games
- DNS lookups

#### Experiment Examples
Some examples of socket programming experiments:

- Simple DNS client/server: A DNS client sends a domain name to the server and the server returns the corresponding IP address.
- Data and time client/server: The time and date are fetched from the server and displayed on the client.
- Echo client/server: The client sends a message to the server, the server echoes it back to the client.
- Iterative and concurrent servers: Multiple clients can connect to a single server and send/receive data concurrently.

[Detailed diagrams, code examples, advantages, disadvantages, and applications can be added here for further understanding.]