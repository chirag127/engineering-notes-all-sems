### Multiplexing for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Demultiplexing is the reverse process of multiplexing, where the data segments received from the sender are extracted and delivered to the corresponding application processes of the receiver.
- Multiplexing and demultiplexing are the services facilitated by the transport layer of the OSI model, which extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts .
- There are two types of multiplexing and demultiplexing: connectionless and connection-oriented.
- Connectionless multiplexing and demultiplexing use the combination of source IP address, source port number, destination IP address and destination port number to identify the sockets and deliver the segments.
- Connection-oriented multiplexing and demultiplexing use the connection identifier (CID) field in the segment header to identify the sockets and deliver the segments.
- The transport layer protocols, such as TCP and UDP, provide different methods of multiplexing and demultiplexing, depending on their characteristics and functionalities.
- TCP is a connection-oriented protocol that uses the four-tuple of source IP address, source port number, destination IP address and destination port number to identify the sockets and deliver the segments.
- UDP is a connectionless protocol that also uses the four-tuple of source IP address, source port number, destination IP address and destination port number to identify the sockets and deliver the segments, but it does not establish or maintain any connection state between the sender and receiver.
- Multiplexing and demultiplexing are essential for the transport layer to provide end-to-end communication services for applications, such as web browsing, email, file transfer, etc.