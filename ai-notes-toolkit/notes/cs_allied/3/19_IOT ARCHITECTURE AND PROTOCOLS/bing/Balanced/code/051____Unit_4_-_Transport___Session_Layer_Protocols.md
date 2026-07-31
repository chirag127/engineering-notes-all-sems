# Unit 4 - Transport & Session Layer Protocols

- The transport layer is the fourth layer in the OSI model, which provides end-to-end communication services for applications.
- The transport layer protocols are responsible for:
  - Establishing, maintaining, and terminating connections between hosts.
  - Segmenting and reassembling data into packets or datagrams.
  - Providing reliable or unreliable delivery of data, depending on the protocol.
  - Providing flow control and congestion control mechanisms to avoid network overload.
  - Providing error detection and correction mechanisms to ensure data integrity.
  - Providing port numbers to identify different applications or processes on the same host.
- The two most common transport layer protocols are TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
  - TCP is a connection-oriented, reliable, and stream-based protocol that guarantees the delivery of data in the same order as it was sent. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection. TCP also uses acknowledgments, sequence numbers, and timers to ensure reliability and avoid data loss or duplication. TCP provides flow control using a sliding window mechanism, and congestion control using algorithms such as slow start, congestion avoidance, fast retransmit, and fast recovery.
  - UDP is a connectionless, unreliable, and datagram-based protocol that does not guarantee the delivery or order of data. UDP does not use any handshakes, acknowledgments, or timers to establish or terminate a connection, or to ensure reliability. UDP does not provide any flow control or congestion control mechanisms, and relies on the application layer to handle these issues. UDP is suitable for applications that require low latency, high throughput, or real-time communication, such as voice over IP, video streaming, or online gaming.
- Some other transport layer protocols that have been defined and implemented include DCCP (Datagram Congestion Control Protocol) and SCTP (Stream Control Transmission Protocol).
  - DCCP is a connection-oriented, unreliable, and datagram-based protocol that provides congestion control for applications that use UDP. DCCP uses a four-way handshake to establish a connection, and a three-way handshake to terminate a connection. DCCP also uses acknowledgments, sequence numbers, and timers to provide feedback and control the sending rate. DCCP supports different congestion control algorithms, such as TCP-like, TCP-friendly, or delay-based, depending on the application requirements.
  - SCTP is a connection-oriented, reliable, and message-based protocol that provides multiple streams of data within a single connection. SCTP uses a four-way handshake to establish a connection, and a four-way handshake to terminate a connection. SCTP also uses acknowledgments, sequence numbers, and timers to ensure reliability and avoid data loss or duplication. SCTP provides flow control using a sliding window mechanism, and congestion control using algorithms similar to TCP. SCTP also provides features such as multihoming, partial reliability, and unordered delivery, which are not supported by TCP.

- The session layer is the fifth layer in the OSI model, which provides session management services for applications.
- The session layer protocols are responsible for:
  - Creating, maintaining, and terminating sessions between hosts.
  - Synchronizing the data exchange between hosts using checkpoints or tokens.
  - Managing the dialog control between hosts using modes such as simplex, half-duplex, or full-duplex.
  - Handling the authentication and authorization of hosts using passwords or certificates.
  - Providing security and encryption mechanisms to protect the data confidentiality and integrity.
- The session layer protocols are not widely used in the TCP/IP model, as most of these functions are either supported by the transport layer protocols, such as TCP or SCTP, or by the application layer protocols, such as HTTP, FTP, or SSH.
- Some examples of session layer protocols are RPC (Remote Procedure Call), NFS (Network File System), SQL (Structured Query Language), and X.225 (ISO Transport Service on top of TCP).