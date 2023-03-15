### Multiplexing in transport layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Multiplexing in transport layer means extending the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts.
- A multiplexing-demultiplexing service is needed for all computer networks, because a host can run multiple processes that need to communicate with processes on other hosts.
- Multiplexing in transport layer requires that sockets have unique identifiers, and each segment have special fields that indicate the sockets to which the segment is to be delivered.
- There are two types of multiplexing in transport layer: connectionless multiplexing and connection-oriented multiplexing.
- Connectionless multiplexing uses the UDP protocol, which does not establish a connection before sending data. The sender adds the destination port number to the segment header, and the receiver uses the port number to deliver the segment to the correct socket.
- Connection-oriented multiplexing uses the TCP protocol, which establishes a connection before sending data. The sender and the receiver exchange segments with source and destination port numbers, as well as sequence and acknowledgment numbers, to identify and order the segments belonging to the same connection.
- Multiplexing in transport layer allows multiple applications to share the network resources and communicate with each other efficiently and reliably.