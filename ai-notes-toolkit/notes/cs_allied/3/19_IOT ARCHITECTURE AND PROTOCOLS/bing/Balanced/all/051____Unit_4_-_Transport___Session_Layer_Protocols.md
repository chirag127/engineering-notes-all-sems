## Unit 4 - Transport & Session Layer Protocols

The transport layer and the session layer are two of the seven layers of the Open Systems Interconnection (OSI) model. They are responsible for providing reliable and efficient communication between applications on different devices.

- The transport layer (layer 4) is the lowest layer that deals with end-to-end communication. It provides services such as error detection, flow control, congestion control, and segmentation of data. It also ensures that data is delivered in the correct order and without duplication. The transport layer can be either connection-oriented or connectionless, depending on the protocol used. The most common transport layer protocols are:

  - Transmission Control Protocol (TCP): A connection-oriented protocol that establishes a virtual circuit between two endpoints and guarantees reliable and ordered delivery of data. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate it. TCP also uses acknowledgments, sequence numbers, and sliding window mechanism to ensure reliability and flow control. TCP is suitable for applications that require high reliability and data integrity, such as web browsing, email, and file transfer.

  - User Datagram Protocol (UDP): A connectionless protocol that sends datagrams without establishing a connection or ensuring reliability. UDP does not use acknowledgments, sequence numbers, or flow control. UDP is suitable for applications that require low latency and high speed, such as voice over IP, video streaming, and online gaming.

  - Stream Control Transmission Protocol (SCTP): A connection-oriented protocol that supports multiple streams of data within a single connection. SCTP provides reliable and ordered delivery of data, as well as congestion control and error detection. SCTP also supports multihoming, which allows a device to have multiple IP addresses and switch between them in case of failure. SCTP is suitable for applications that require high availability and flexibility, such as telephony and signaling.

  - Datagram Congestion Control Protocol (DCCP): A connection-oriented protocol that provides congestion control for unreliable datagrams. DCCP does not guarantee reliable or ordered delivery of data, but it allows applications to choose the level of reliability they need. DCCP also supports features such as multipath, encryption, and authentication. DCCP is suitable for applications that require congestion control and adaptability, such as multimedia and interactive applications.

- The session layer (layer 5) is the layer that manages the sessions between applications. It provides services such as session establishment, maintenance, and termination, as well as synchronization, dialog control, and security. The session layer can use different protocols depending on the application and the transport layer protocol. Some of the session layer protocols are:

  - Session Initiation Protocol (SIP): A protocol that initiates, modifies, and terminates multimedia sessions over the Internet. SIP uses a request-response model and supports features such as caller ID, call forwarding, call transfer, and conferencing. SIP can use TCP, UDP, or SCTP as the transport layer protocol.

  - Remote Procedure Call (RPC): A protocol that allows a program to execute a procedure on a remote device. RPC uses a client-server model and supports features such as authentication, encryption, and compression. RPC can use TCP or UDP as the transport layer protocol.

  - Network File System (NFS): A protocol that allows a device to access files on a remote device. NFS uses a client-server model and supports features such as caching, locking, and permission control. NFS can use TCP or UDP as the transport layer protocol.

  - Simple Network Management Protocol (SNMP): A protocol that allows a device to monitor and manage other devices on a network. SNMP uses a manager-agent model and supports features such as polling, traps, and configuration. SNMP can use TCP or UDP as the transport layer protocol.