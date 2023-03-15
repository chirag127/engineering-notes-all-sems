### Multiplexing for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Multiplexing in the transport layer extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts.
- Multiplexing in the transport layer requires that sockets have unique identifiers, and each segment have special fields that indicate the sockets to which the segment is to be delivered.
- There are two types of multiplexing in the transport layer: connectionless multiplexing and connection-oriented multiplexing.
- Connectionless multiplexing uses the User Datagram Protocol (UDP) and relies on the source and destination port numbers to identify the sockets.
- Connection-oriented multiplexing uses the Transmission Control Protocol (TCP) and relies on the source and destination port numbers as well as the source and destination IP addresses to identify the sockets.
- Demultiplexing is the reverse process of multiplexing, where the transport layer receives the segments from the network layer, extracts the data and delivers them to the appropriate application processes.
- Demultiplexing in the transport layer uses the port numbers and IP addresses in the segment headers to determine the destination sockets.
- Demultiplexing in the transport layer can be done in two ways: exclusive demultiplexing and inclusive demultiplexing.
- Exclusive demultiplexing means that a segment is delivered to one and only one socket.
- Inclusive demultiplexing means that a segment can be delivered to more than one socket.
- Inclusive demultiplexing is used for multicast or broadcast applications, where a segment can be received by multiple processes on the same or different hosts.