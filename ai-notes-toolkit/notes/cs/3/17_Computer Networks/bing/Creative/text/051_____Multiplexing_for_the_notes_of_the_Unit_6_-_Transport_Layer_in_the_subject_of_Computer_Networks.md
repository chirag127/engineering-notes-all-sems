### Multiplexing and Demultiplexing in Transport Layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver .
- Demultiplexing is the reverse process of multiplexing, where the data segments received from the network layer are extracted and delivered to the appropriate application processes of the receiver .
- Multiplexing and demultiplexing are the services facilitated by the transport layer of the OSI model.
- The transport layer uses port numbers to identify the application processes and to multiplex and demultiplex the data segments  .
- There are two types of multiplexing and demultiplexing: connectionless and connection-oriented.
- Connectionless multiplexing and demultiplexing use only the source and destination port numbers to identify the application processes. An example of a connectionless protocol is UDP (User Datagram Protocol) .
- Connection-oriented multiplexing and demultiplexing use the source and destination port numbers as well as the source and destination IP addresses to identify the application processes. An example of a connection-oriented protocol is TCP (Transmission Control Protocol) .
- Multiplexing and demultiplexing are the backbone transport services that enable end-to-end communication between applications running on different hosts .