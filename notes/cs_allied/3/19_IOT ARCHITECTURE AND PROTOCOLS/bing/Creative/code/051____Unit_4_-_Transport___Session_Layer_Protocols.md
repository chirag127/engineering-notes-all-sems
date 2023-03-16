## Unit 4 - Transport & Session Layer Protocols

The transport layer and the session layer are two of the seven layers of the Open Systems Interconnection (OSI) model. They are responsible for providing reliable and efficient communication between applications on different hosts.

### Transport Layer

The transport layer is the fourth layer of the OSI model. It provides end-to-end data transfer services to the upper layers, such as the session, presentation, and application layers. The transport layer can be either connection-oriented or connectionless, depending on the protocol used.

- Connection-oriented protocols establish a logical connection between the source and destination hosts before exchanging data. They ensure reliable and ordered delivery of data, and can also provide flow control and congestion control mechanisms. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP).
- Connectionless protocols do not require a logical connection between the source and destination hosts. They send data as independent packets, called datagrams, without guaranteeing reliability or order. They are faster and more efficient than connection-oriented protocols, but they may also lose or duplicate data. An example of a connectionless protocol is the User Datagram Protocol (UDP).

Some of the functions of the transport layer are:

- Multiplexing and demultiplexing: The transport layer can use port numbers to identify different applications or processes on the same host, and to direct data to the appropriate upper layer protocol.
- Segmentation and reassembly: The transport layer can divide a large message into smaller segments, and add headers to each segment. The headers contain information such as sequence numbers, checksums, and flags. The transport layer can also reassemble the segments into the original message at the destination host, and check for errors and missing data.
- Error detection and correction: The transport layer can use checksums or other methods to detect errors in the data, and request retransmission or correction of the corrupted segments.
- Flow control: The transport layer can use techniques such as sliding window or stop-and-wait to regulate the amount of data sent by the sender, and to prevent the receiver from being overwhelmed by too much data.
- Congestion control: The transport layer can use algorithms such as additive increase multiplicative decrease (AIMD) or slow start to adjust the sending rate of the sender, and to avoid network congestion and packet loss.

Some of the transport layer protocols that have been defined and implemented are:

- TCP: A connection-oriented, reliable, and full-duplex protocol that provides byte-stream service to the upper layers. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP also uses acknowledgments, timers, sequence numbers, and window sizes to ensure reliable and ordered delivery of data. TCP also provides flow control and congestion control mechanisms.
- UDP: A connectionless, unreliable, and best-effort protocol that provides datagram service to the upper layers. UDP does not guarantee delivery, order, or integrity of data. UDP is faster and more efficient than TCP, but it may also lose or duplicate data. UDP is suitable for applications that require low latency and high throughput, such as streaming media or online gaming.
- Datagram Congestion Control Protocol (DCCP): A connection-oriented, unreliable, and congestion-controlled protocol that provides datagram service to the upper layers. DCCP is similar to UDP, but it also provides congestion control mechanisms to avoid network congestion and packet loss. DCCP is suitable for applications that require low latency and high throughput, but can tolerate some loss of data, such as voice over IP (VoIP) or video conferencing.
- Stream Control Transmission Protocol (SCTP): A connection-oriented, reliable, and message-oriented protocol that provides multiple streams of data to the upper layers. SCTP is similar to TCP, but it also supports multiple streams of data within a single connection, and can handle multiple IP addresses for each endpoint. SCTP also provides features such as multihoming, partial reliability, and unordered delivery. SCTP is suitable for applications that require reliable and flexible data transfer, such as telephony or web services.

### Session Layer

The session layer is the fifth layer of the OSI model. It provides session management and synchronization services to the upper layers, such as the presentation and application layers. The session layer can establish, maintain, and terminate sessions between different applications or processes on different hosts.

Some of the functions of the session layer are:

- Session establishment: The session layer can use protocols such as the Session Initiation Protocol (SIP) or the Hypertext Transfer Protocol (HTTP) to initiate a session between two or more parties, and to negotiate the parameters and rules of the session