### Transport layer protocols

Transport layer protocols are methods that provide end-to-end communication services for applications in the network stack.  They are responsible for ensuring reliable, ordered, and error-free delivery of data between different processes on different computers.  

Some of the main features and services of transport layer protocols are:

- Connection-oriented communication: Some transport layer protocols, such as TCP, establish a connection between the sender and the receiver before exchanging data. This connection is maintained until the data transfer is complete or the connection is terminated by either party.  
- Same order delivery: Transport layer protocols can ensure that the data segments are delivered in the same order as they were sent, by using sequence numbers and acknowledgements. This prevents the data from being corrupted or misinterpreted by the application.  
- Reliability: Transport layer protocols can detect and correct errors that may occur during data transmission, such as lost, duplicated, or corrupted segments. They use checksums to verify the integrity of the data, and retransmit the segments that are not acknowledged by the receiver.  
- Flow control: Transport layer protocols can regulate the rate of data transmission between the sender and the receiver, to avoid congestion and buffer overflow. They use mechanisms such as sliding window and congestion control to adjust the size of the data segments and the number of segments that can be sent at a time.  
- Multiplexing: Transport layer protocols can enable multiple applications to communicate with each other simultaneously, by using port numbers to identify the source and destination processes. Port numbers are part of the transport layer header, and are assigned by the operating system or the application.  

Some of the common transport layer protocols in the Internet protocol suite are:

- Transmission Control Protocol (TCP): TCP is the most widely used transport layer protocol, and provides connection-oriented, reliable, ordered, and error-free communication. TCP is used by many application layer protocols, such as HTTP, FTP, SMTP, and SSH. 
- User Datagram Protocol (UDP): UDP is a simpler and faster transport layer protocol, but provides connectionless, unreliable, unordered, and error-prone communication. UDP is used by applications that do not require reliability or order, such as DNS, DHCP, RTP, and online games. 
- Datagram Congestion Control Protocol (DCCP): DCCP is a newer transport layer protocol, and provides connection-oriented, unreliable, and congestion-controlled communication. DCCP is designed for applications that need timely delivery of data, such as streaming media and telephony. 
- Stream Control Transmission Protocol (SCTP): SCTP is another newer transport layer protocol, and provides connection-oriented, reliable, ordered, and error-free communication. SCTP is similar to TCP, but supports multiple streams of data within a single connection, and can handle network failures more gracefully. SCTP is used by applications that need high availability and performance, such as VoIP and web servers.