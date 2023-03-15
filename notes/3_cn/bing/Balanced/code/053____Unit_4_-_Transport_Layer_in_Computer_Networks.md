## Unit 4 - Transport Layer in Computer Networks

The transport layer is responsible for providing end-to-end communication between applications running on different hosts in a network. It offers services such as reliable data delivery, error detection and correction, flow control, congestion control, and multiplexing.

The transport layer uses two main protocols: Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).

TCP is a connection-oriented protocol that establishes a logical connection between the sender and the receiver before exchanging data. TCP ensures that the data is delivered reliably, in order, and without errors. TCP also implements flow control and congestion control mechanisms to avoid overloading the network or the receiver.

UDP is a connectionless protocol that does not establish a connection or guarantee reliable delivery of data. UDP simply sends datagrams to the destination without checking for errors or acknowledgments. UDP is faster and more efficient than TCP for applications that do not require reliability, such as streaming media or online gaming.

The transport layer uses port numbers to identify different applications running on the same host. A port number is a 16-bit number that is appended to the IP address of the host to form a socket. A socket is a unique identifier for a communication endpoint in a network. The transport layer header contains the source and destination port numbers, along with other fields such as sequence number, acknowledgment number, checksum, and flags.

The transport layer header is encapsulated inside the network layer header, which is then encapsulated inside the data link layer header, to form a packet. The packet is then transmitted over the physical layer to the destination host, where the headers are removed and the data is delivered to the application layer.