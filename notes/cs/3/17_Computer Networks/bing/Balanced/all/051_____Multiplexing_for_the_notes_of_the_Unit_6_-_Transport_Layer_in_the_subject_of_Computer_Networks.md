# Multiplexing and Demultiplexing in Transport Layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Demultiplexing is the reverse process of multiplexing, where the data from the sender is extracted from the headers and delivered to the appropriate application processes of the receiver.
- Multiplexing and demultiplexing are the services facilitated by the transport layer of the OSI model, which provide end-to-end communication services for applications  .
- There are two types of multiplexing and demultiplexing: connectionless and connection-oriented.
- Connectionless multiplexing and demultiplexing use the combination of source IP address, source port number, destination IP address and destination port number to identify the sockets of the application processes.
- Connection-oriented multiplexing and demultiplexing use the combination of source IP address, source port number, destination IP address, destination port number and connection identifier to identify the sockets of the application processes.
- The transport layer protocols, such as UDP and TCP, use different fields in their headers to carry the information for multiplexing and demultiplexing .
- UDP uses only the source port number and destination port number fields in its header to identify the sockets of the application processes .
- TCP uses the source port number, destination port number and sequence number fields in its header to identify the sockets of the application processes .
- Multiplexing and demultiplexing are essential for enabling multiple applications to share the network resources and communicate with each other   .