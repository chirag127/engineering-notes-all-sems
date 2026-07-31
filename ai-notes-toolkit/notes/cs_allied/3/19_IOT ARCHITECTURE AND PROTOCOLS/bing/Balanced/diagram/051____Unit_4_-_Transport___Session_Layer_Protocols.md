## Unit 4 - Transport & Session Layer Protocols

The transport layer is the fourth layer of the OSI model and the third layer of the TCP/IP model. It provides end-to-end communication services for applications, such as error detection, flow control, congestion control, reliability, and multiplexing. The transport layer protocols lie between user applications and the network, and they offer user-oriented services based on the network characteristics.

Some of the common transport layer protocols are:

- **Transmission Control Protocol (TCP)**: TCP is a connection-oriented, reliable, and full-duplex protocol that establishes a logical connection between two endpoints and ensures that the data is delivered in the same order and without errors. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP also uses a sliding window mechanism to control the flow and congestion of data. TCP is used by many application layer protocols, such as HTTP, FTP, SMTP, and Telnet.

- **User Datagram Protocol (UDP)**: UDP is a connectionless, unreliable, and datagram-based protocol that does not guarantee the delivery, order, or integrity of the data. UDP does not establish or terminate a connection, and it does not use any flow or congestion control mechanisms. UDP is used for applications that require speed, efficiency, or real-time communication, such as DNS, DHCP, RTP, and VoIP.

- **Datagram Congestion Control Protocol (DCCP)**: DCCP is a connection-oriented, unreliable, and datagram-based protocol that provides congestion control for applications that use UDP. DCCP uses a feature negotiation mechanism to allow the endpoints to choose the appropriate congestion control algorithm for their application. DCCP is used for applications that require low latency and high bandwidth, such as streaming media, online gaming, and telephony.

- **Stream Control Transmission Protocol (SCTP)**: SCTP is a connection-oriented, reliable, and message-based protocol that provides multiple streams of data within a single connection. SCTP also provides features such as multihoming, path selection, and partial reliability. SCTP is used for applications that require high availability, fault tolerance, and message orientation, such as signaling, web services, and file transfer.

The session layer is the fifth layer of the OSI model and it is not present in the TCP/IP model. It provides services for establishing, maintaining, and terminating sessions between applications. The session layer protocols manage the synchronization, coordination, and dialog control of the data exchange. The session layer protocols also provide security, authentication, and encryption for the sessions.

Some of the common session layer protocols are:

- **Session Initiation Protocol (SIP)**: SIP is a signaling protocol that is used to create, modify, and terminate multimedia sessions, such as voice and video calls, over the Internet. SIP uses a request-response mechanism to exchange messages between the endpoints, and it supports various features such as call transfer, call hold, call forwarding, and conferencing.

- **Remote Procedure Call (RPC)**: RPC is a protocol that allows a program to execute a procedure or a function on a remote system, as if it were a local system. RPC uses a client-server model to exchange messages between the systems, and it abstracts the details of the network communication. RPC is used for distributed computing, such as in NFS, NIS, and LDAP.

- **Secure Shell (SSH)**: SSH is a protocol that provides secure and encrypted communication between two systems over an insecure network. SSH uses a client-server model to establish a secure channel, and it supports various features such as remote login, remote command execution, file transfer, and port forwarding.

- **AppleTalk Session Protocol (ASP)**: ASP is a protocol that provides session management and communication services for AppleTalk applications. ASP uses a client-server model to establish a session, and it supports various features such as request-response, attention, and write-continue. ASP is used for file sharing, printing, and remote access in AppleTalk networks.