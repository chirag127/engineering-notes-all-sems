 Here is the content in markdown format for the topic ### Process-to-process delivery in transport layer:

### Process-to-process delivery in transport layer

The transport layer provides process-to-process delivery of the entire message. This means that the transport layer protocol headers include port numbers to identify the application process that each segment of the message should be delivered to. This allows multiple applications to use the network and the transport layer simultaneously.

Some key points about process-to-process delivery:

- The transport layer headers include source and destination port numbers. The port numbers are used to identify the sending and receiving applications.
- The transport layer assembles the segments into the original message and delivers the reassembled message to the receiving application process.
- The transport layer handles segmenting and reassembling the message. This shields the application layer protocols and processes from needing to deal with the packet size limitations of the network.
- The transport layer can provide mechanisms to ensure reliable delivery of messages and correct ordering of segments. These functions support the communication needs of applications.

Examples of transport layer protocols that provide process-to-process delivery:

- Transmission Control Protocol (TCP) provides reliable, in-order delivery of bytes between client and server processes.
- User Datagram Protocol (UDP) provides fast but unreliable delivery of packets between client and server processes.

Advantages:

- Allows multiple applications to use the network simultaneously.
- Shields applications from packet size limitations and reassembly details.
- Can provide reliable data delivery and ordering.

Disadvantages:

- Additional overhead for transport layer headers and trailers.
- Processing required to implement transport layer functions may introduce latency.

[Detailed diagrams and codes can be included here if required.]