### Transport layer protocols

The transport layer is responsible for providing end-to-end communication services for applications. It provides logical communication between application processes running on different hosts. Some of the key transport layer protocols are:

1. **Transmission Control Protocol (TCP)**: TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data between applications. It uses a three-way handshake to establish a connection between two hosts and employs flow control, congestion control, and error recovery mechanisms to ensure reliable data transfer.

2. **User Datagram Protocol (UDP)**: UDP is a connectionless protocol that provides a simple, unreliable datagram service. It is used for applications that do not require the reliability of TCP, such as real-time audio and video streaming, online gaming, and DNS queries.

3. **Stream Control Transmission Protocol (SCTP)**: SCTP is a connection-oriented protocol that provides reliable, ordered delivery of data. It is similar to TCP, but also supports multihoming and multistreaming, which allows multiple network paths and multiple streams of data to be used simultaneously.

4. **Datagram Congestion Control Protocol (DCCP)**: DCCP is a connection-oriented protocol that provides unreliable, congestion-controlled delivery of data. It is used for applications that require congestion control, but do not require the reliability of TCP, such as real-time multimedia streaming.

These are some of the key transport layer protocols that provide different levels of reliability, ordering, and congestion control to meet the needs of various applications.