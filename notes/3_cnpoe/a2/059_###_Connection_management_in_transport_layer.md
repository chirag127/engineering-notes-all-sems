 Here is the content in markdown format for the topic -

### Connection management in transport layer

The transport layer is responsible for providing end-to-end communication between processes running on different hosts. It has to manage the connection between the hosts during data transfer. Some key points about connection management in the transport layer are:

1. Connection establishment - The transport layer protocols establish a logical connection between the hosts before the actual data transfer. This involves a 3-way handshake process to set up the connection. For example, TCP uses a 3-way handshake to establish a connection between the client and server.

2. Connection termination - The transport layer is also responsible for terminating the connection after the data transfer is complete. This is done through a 4-way termination process where both hosts acknowledge the termination of the connection. For example, TCP uses a 4-way termination to close the connection.

3. Connection orientation - Transport layer protocols can be either connection-oriented or connectionless. Connection-oriented protocols like TCP establish a dedicated end-to-end connection between hosts before data transfer. Connectionless protocols like UDP do not establish a dedicated end-to-end connection and have no connection establishment or termination process.

**Mnemonics** - A handy mnemonic to remember connection management in transport layer is -

> Establish connection, transfer data, terminate connection

**Advantages of connection-orientation** - Reliability, in-order delivery, congestion control.
**Disadvantages of connection-orientation** - Extra overhead of connection establishment and termination, slower start.

[Detailed diagrams and examples can be added here to aid understanding]

The transport layer connection management ensures smooth and efficient data transfer between hosts. It provides the necessary connection and disconnection processes to facilitate reliable end-to-end communication.