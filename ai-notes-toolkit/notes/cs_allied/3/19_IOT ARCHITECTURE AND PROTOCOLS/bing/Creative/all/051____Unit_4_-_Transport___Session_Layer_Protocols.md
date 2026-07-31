# Unit 4 - Transport & Session Layer Protocols

The transport layer and the session layer are two of the seven layers of the Open Systems Interconnection (OSI) model. They are responsible for providing reliable and efficient communication between applications and hosts on a network.

## Transport Layer

The transport layer is the fourth layer of the OSI model. It provides end-to-end data transfer services to the upper layers, such as the session, presentation, and application layers. The transport layer can be either connection-oriented or connectionless, depending on the type of protocol used.

- Connection-oriented protocols establish a logical connection between the source and destination hosts before sending any data. They also provide reliable data delivery, error detection and correction, flow control, and congestion control. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP).
- Connectionless protocols do not require a logical connection between the source and destination hosts. They send data as independent packets, without any guarantee of delivery, order, or integrity. An example of a connectionless protocol is the User Datagram Protocol (UDP).

Some of the functions of the transport layer are:

- Multiplexing and demultiplexing: The transport layer can use port numbers to identify different applications or processes on the same host and deliver data to the correct destination.
- Segmentation and reassembly: The transport layer can divide a large message into smaller segments and add headers to each segment. The segments are then reassembled at the destination host by using sequence numbers and acknowledgment messages.
- End-to-end communication: The transport layer can provide end-to-end communication between applications on different hosts, regardless of the underlying network layer protocols or physical media.

Some of the protocols that operate at the transport layer are:

- Transmission Control Protocol (TCP): TCP is a connection-oriented, reliable, and full-duplex protocol that provides reliable data delivery, error detection and correction, flow control, and congestion control. TCP uses a three-way handshake to establish a connection, a sliding window mechanism to regulate the data flow, and a four-way handshake to terminate a connection.
- User Datagram Protocol (UDP): UDP is a connectionless, unreliable, and best-effort protocol that provides fast and efficient data transfer for applications that do not require reliability or order. UDP does not provide any error detection, correction, or flow control. UDP uses a simple header that contains the source and destination port numbers, the length, and the checksum of the data.
- Stream Control Transmission Protocol (SCTP): SCTP is a connection-oriented, reliable, and message-oriented protocol that provides multiple streams of data within a single connection. SCTP also provides features such as multihoming, path selection, and partial reliability. SCTP uses a four-way handshake to establish a connection, a selective acknowledgment mechanism to regulate the data flow, and a shutdown procedure to terminate a connection.
- Datagram Congestion Control Protocol (DCCP): DCCP is a connection-oriented, unreliable, and congestion-controlled protocol that provides efficient data transfer for applications that can tolerate some data loss, such as multimedia streaming or online gaming. DCCP also provides features such as congestion control, acknowledgment feedback, and security. DCCP uses a four-way handshake to establish a connection, a congestion control mechanism to regulate the data flow, and a close procedure to terminate a connection.

## Session Layer

The session layer is the fifth layer of the OSI model. It provides session management and synchronization services to the upper layers, such as the presentation and application layers. The session layer can establish, maintain, and terminate sessions between applications on different hosts. It can also coordinate the exchange of data and synchronize the communication between the applications.

Some of the functions of the session layer are:

- Session establishment: The session layer can initiate a session between two or more applications by using a session identifier, a session token, or a session key. The session layer can also negotiate the parameters and options for the session, such as the protocol, the encryption, or the compression methods.
- Session maintenance: The session layer can monitor and control the session by using checkpoints, timers, or heartbeat messages. The session layer can also handle errors, interruptions, or timeouts that may occur during the session.
- Session termination: The session layer can end a session gracefully by using a session close message or abruptly by using a session abort message. The session layer can also release the resources and data associated with the session.

Some of the protocols that operate at the session layer are:

- Session Initiation Protocol (SIP): SIP is a signaling protocol that is used to establish, maintain, and terminate multimedia sessions, such as voice, video, or instant messaging. SIP uses a