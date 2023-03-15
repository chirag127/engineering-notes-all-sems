### Process-to-process delivery

- The transport layer is the fourth layer of the OSI reference model that provides communication services between the computers connected in the network .
- The transport layer is mainly responsible for the process-to-process delivery of the entire message .
- A process is an application program that is running on the host . There might be more than one process running on the host.
- The transport layer uses port numbers to identify different processes on the same host and to deliver the message to the correct process .
- The transport layer can use different protocols to provide different levels of reliability, efficiency, and security for the process-to-process delivery .
- The Internet model has three protocols at the transport layer: UDP, TCP, and SCTP.
- UDP (User Datagram Protocol) is a connectionless and unreliable protocol that provides fast and simple delivery of datagrams without any error control or flow control .
- TCP (Transmission Control Protocol) is a connection-oriented and reliable protocol that provides error detection, error recovery, flow control, and congestion control for the delivery of segments .
- SCTP (Stream Control Transmission Protocol) is a connection-oriented and reliable protocol that provides multiple streams of data, message-oriented delivery, and protection against SYN flooding attacks for the delivery of chunks .