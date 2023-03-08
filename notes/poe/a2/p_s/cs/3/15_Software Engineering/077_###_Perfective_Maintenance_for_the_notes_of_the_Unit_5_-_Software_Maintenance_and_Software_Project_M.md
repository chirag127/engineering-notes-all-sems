 Here is the content written in markdown format on the topic ## Unit 4 - Transport Layer in Computer Networks:

## Unit 4 - Transport Layer in Computer Networks

The transport layer is responsible for delivering data between processes running on different hosts. Some key responsibilities of the transport layer are:

1. Providing process-to-process delivery: The transport layer transfers data between processes running on different hosts, not just between hosts. It uses port numbers to identify sending and receiving processes.
2. Segmentation and reassembly: The transport layer divides application layer data into segments and reassembles segments into data at the destination.
3. Reliable data transfer: The transport layer provides reliable data transfer through error checking and correction. Data delivery can be guaranteed with acknowledgments and retransmissions.
4. Flow control: The transport layer regulates the rate at which data is sent to prevent overflow. The sender will not send data faster than the receiver can handle.
5. Congestion control: The transport layer reduces congestion in the network through techniques like slow start and avoidance of excessive retransmissions.

Two protocols that operate at the transport layer are:

- Transmission Control Protocol (TCP): A connection-oriented, reliable protocol that provides in-order delivery of bytes. TCP uses a 3-way handshake to establish connections and provides congestion control and flow control.
- User Datagram Protocol (UDP): A connectionless, unreliable protocol that provides fast delivery of datagrams. UDP is used for applications that do not require the level of service of TCP.

[Detailed diagrams, examples, codes, advantages, disadvantages, and applications of TCP and UDP can be added here if required for exam preparation.]