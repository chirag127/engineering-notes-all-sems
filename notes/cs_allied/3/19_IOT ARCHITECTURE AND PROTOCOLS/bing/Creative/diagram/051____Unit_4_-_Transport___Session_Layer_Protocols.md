## Unit 4 - Transport & Session Layer Protocols

The transport layer and the session layer are two of the seven layers of the Open Systems Interconnection (OSI) model. They are responsible for providing reliable and efficient communication between applications on different hosts in a network.

### Transport Layer

The transport layer is the fourth layer of the OSI model. It provides end-to-end data transfer services to the upper layers, such as the session, presentation, and application layers. The transport layer can be either connection-oriented or connectionless, depending on the protocol used.

- Connection-oriented protocols establish a logical connection between the source and destination hosts before exchanging data. They ensure reliable and ordered delivery of data, and can handle flow control, congestion control, and error recovery. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP).
- Connectionless protocols do not require a logical connection between the source and destination hosts. They send data as independent packets, without guaranteeing reliability, order, or delivery. They are faster and more efficient than connection-oriented protocols, but they may lose or duplicate data, or deliver it out of order. An example of a connectionless protocol is the User Datagram Protocol (UDP).

Some of the functions of the transport layer are:

- Multiplexing and demultiplexing: The transport layer can use port numbers to identify different applications or processes on the same host, and to multiplex or demultiplex data streams accordingly.
- Segmentation and reassembly: The transport layer can divide a large data stream into smaller segments, and add headers to each segment for identification and error detection. The transport layer can also reassemble the segments into the original data stream at the destination host.
- Flow control: The transport layer can regulate the rate of data transmission between the source and destination hosts, to avoid overwhelming the receiver or the network resources.
- Congestion control: The transport layer can monitor the network conditions and adjust the data transmission rate accordingly, to avoid congestion and packet loss.
- Error detection and recovery: The transport layer can use checksums or other methods to detect errors in the data segments, and request retransmission or correction of the corrupted segments.

Some of the transport layer protocols that have been defined and implemented are:

- TCP: The most widely used transport layer protocol, which provides connection-oriented, reliable, and ordered data transfer services. TCP is used by many applications, such as web browsing, email, file transfer, and remote login.
- UDP: A transport layer protocol that provides connectionless, unreliable, and unordered data transfer services. UDP is used by applications that require speed and efficiency, such as video streaming, voice over IP, online gaming, and DNS queries.
- SCTP: A transport layer protocol that provides connection-oriented, reliable, and unordered data transfer services. SCTP supports multiple streams of data within a single connection, and can handle network failures and mobility. SCTP is used by applications that require high availability and security, such as telephony, signaling, and web conferencing.
- DCCP: A transport layer protocol that provides connection-oriented, unreliable, and unordered data transfer services. DCCP supports congestion control mechanisms for applications that generate bursty or variable-rate traffic, such as multimedia streaming, interactive gaming, and chat.

### Session Layer

The session layer is the fifth layer of the OSI model. It provides session management services to the upper layers, such as the presentation and application layers. The session layer enables applications to establish, maintain, and terminate sessions, and to synchronize the sessions.

A session is a logical association between two or more applications or processes that communicate over a network. A session can be used to exchange data, control information, or commands. A session can also support security, authentication, and encryption features.

Some of the functions of the session layer are:

- Session establishment: The session layer can initiate a session request, negotiate the session parameters, and confirm the session acceptance between the source and destination applications.
- Session maintenance: The session layer can monitor the session status, handle session interruptions, and resume or restart the session if needed.
- Session termination: The session layer can end the session gracefully, or abort the session in case of an error or timeout.
- Session synchronization: The session layer can coordinate the data exchange between the source and destination applications, and ensure that they are in sync. For example, the session layer can use checkpoints or markers to divide the data stream into logical units, and to recover from failures or interruptions.

Some of the session layer protocols that have been defined and implemented are:

- RPC: A session layer protocol that allows a client application to invoke a procedure or a function on a remote server application