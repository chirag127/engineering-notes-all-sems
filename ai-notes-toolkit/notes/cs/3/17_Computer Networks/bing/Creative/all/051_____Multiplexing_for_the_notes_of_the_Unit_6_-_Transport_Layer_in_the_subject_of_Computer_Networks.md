# Multiplexing and Demultiplexing in Transport Layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Demultiplexing is the reverse process of multiplexing, where the data from the sender is extracted from the headers and delivered to the corresponding application processes of the receiver.
- Multiplexing and demultiplexing are the services facilitated by the transport layer of the OSI model, which extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts .
- There are two types of multiplexing and demultiplexing: connectionless and connection-oriented.
- Connectionless multiplexing and demultiplexing use the combination of source IP address, destination IP address, source port number and destination port number to identify the sockets to which the segments are to be delivered.
- Connection-oriented multiplexing and demultiplexing use the connection identifier, which is a unique value assigned to each connection, to identify the sockets to which the segments are to be delivered.
- The transport layer protocols, such as TCP and UDP, provide different mechanisms for multiplexing and demultiplexing, depending on their characteristics and functionalities.
- TCP uses connection-oriented multiplexing and demultiplexing, where each connection is identified by a 4-tuple of source IP address, destination IP address, source port number and destination port number.
- UDP uses connectionless multiplexing and demultiplexing, where each datagram is identified by a 4-tuple of source IP address, destination IP address, source port number and destination port number.
- The transport layer headers contain the fields that indicate the sockets to which the segments or datagrams are to be delivered, such as port numbers and connection identifiers .
- The transport layer multiplexing and demultiplexing service is essential for all computer networks, as it enables multiple applications to communicate simultaneously and efficiently over the same network .