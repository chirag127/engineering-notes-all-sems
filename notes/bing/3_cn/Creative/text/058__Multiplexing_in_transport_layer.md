### Multiplexing in transport layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Multiplexing at the transport layer involves adding transport headers to the data chunks received from different sockets and passing them to the network layer.
- The transport headers contain information such as source port number, destination port number, sequence number, acknowledgment number, etc. that help to identify the corresponding application processes at the receiver side.
- The transport layer can use either connection-oriented or connectionless multiplexing, depending on the protocol used (TCP or UDP).
- Connection-oriented multiplexing requires establishing a connection between the sender and the receiver before exchanging data, and maintaining the state of the connection throughout the communication.
- Connectionless multiplexing does not require any connection establishment or state maintenance, and relies on the port numbers to deliver the data to the correct socket.
- Demultiplexing is the reverse process of multiplexing, which is delivering the data to the correct socket by the transport layer at the receiver side.
- Demultiplexing at the transport layer involves extracting the transport headers from the segments received from the network layer, and using the information in the headers to direct the data to the appropriate socket.
- The transport layer can use either connection-oriented or connectionless demultiplexing, depending on the protocol used (TCP or UDP).
- Connection-oriented demultiplexing uses the source and destination port numbers, as well as the source and destination IP addresses, to identify the correct socket.
- Connectionless demultiplexing uses only the destination port number to identify the correct socket.
- Multiplexing and demultiplexing are the services facilitated by the transport layer to extend the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts.