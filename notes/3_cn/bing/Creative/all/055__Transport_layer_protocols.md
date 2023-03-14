### Transport layer protocols

Transport layer protocols are the methods that provide end-to-end communication services for applications in the network stack. They are responsible for ensuring reliable, ordered, and error-free delivery of data from one process to another across different hosts. 

Some of the main transport layer protocols are:

- **Transmission Control Protocol (TCP)**: This is a connection-oriented protocol that establishes a virtual circuit between the sender and the receiver before transmitting data. TCP uses sequence numbers, acknowledgements, checksums, and timers to ensure that all the data segments are delivered correctly and in order. TCP also provides flow control and congestion control mechanisms to regulate the rate of data transmission and avoid network overload. TCP is used by many application layer protocols, such as HTTP, FTP, SMTP, and SSH.  

- **User Datagram Protocol (UDP)**: This is a connectionless protocol that does not establish a virtual circuit or guarantee reliable delivery of data. UDP simply sends datagrams to the destination without waiting for acknowledgements or retransmitting lost or corrupted segments. UDP is faster and more efficient than TCP for applications that do not require reliability or ordering, such as real-time audio and video streaming, online gaming, and DNS.  

- **Datagram Congestion Control Protocol (DCCP)**: This is a connection-oriented protocol that provides unreliable delivery of data with congestion control. DCCP is designed for applications that need to avoid congesting the network but can tolerate some loss or reordering of data, such as voice over IP (VoIP) and media streaming. DCCP uses a handshake mechanism similar to TCP to establish a connection, and then uses acknowledgements and feedback messages to adjust the sending rate according to the network conditions. 

- **Stream Control Transmission Protocol (SCTP)**: This is a connection-oriented protocol that provides reliable delivery of data with multiple streams and multihoming. SCTP allows a single connection to have multiple independent streams of data, each with its own sequence numbers and acknowledgements. This enables parallel transmission of data and reduces head-of-line blocking. SCTP also supports multihoming, which means that a connection can have multiple IP addresses for each endpoint, providing redundancy and fault tolerance. SCTP is used for applications that need high performance and reliability, such as telephony and web services. 

Some mnemonics and learning tricks for the transport layer protocols are:

- TCP is like a telephone call: you need to dial and wait for the other person to answer before you can talk, and you need to say goodbye when you are done. TCP is reliable and orderly, but slow and heavy.

- UDP is like a postcard: you just write the address and the message and send it without knowing if it will reach the destination or not. UDP is fast and light, but unreliable and unordered.

- DCCP is like a walkie-talkie: you need to press a button and wait for a signal before you can talk, and you need to adjust the volume according to the noise level. DCCP is unreliable and orderly, but avoids congestion.

- SCTP is like a train: you can have multiple cars with different passengers and destinations, and you can switch tracks if there is a problem. SCTP is reliable and orderly, but supports multiple streams and multihoming.