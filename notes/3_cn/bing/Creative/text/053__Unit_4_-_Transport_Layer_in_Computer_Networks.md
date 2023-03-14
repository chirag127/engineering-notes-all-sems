## Unit 4 - Transport Layer in Computer Networks

The transport layer is the fourth layer in the OSI model and the Internet protocol suite. It provides end-to-end communication services for applications running on different hosts. It also provides services such as connection-oriented communication, reliability, flow control, and multiplexing.  

Some of the main functions and services of the transport layer are:

- End-to-end delivery: The transport layer ensures that the entire message is delivered from the source to the destination, without any loss or corruption. It may use error detection and correction techniques, such as checksums and acknowledgments, to achieve reliable delivery.  
- Addressing: The transport layer uses port numbers to identify the source and destination application processes. Port numbers are 16-bit numbers that are appended to the IP addresses in the network layer. Port numbers allow multiple applications to use the same network layer protocol simultaneously.  
- Flow control: The transport layer regulates the amount of data that can be sent and received by the sender and receiver, respectively. Flow control prevents the sender from overwhelming the receiver or the network with too much data. It may use techniques such as sliding window, stop-and-wait, or backpressure to control the flow of data.  
- Multiplexing: The transport layer allows multiple application processes to share the same network layer connection. It does so by using port numbers to distinguish the data segments belonging to different processes. Multiplexing enables the efficient use of network resources and reduces the overhead of establishing and terminating connections.  

The transport layer protocols that are commonly used in the Internet are:

- Transmission Control Protocol (TCP): TCP is a connection-oriented, reliable, and full-duplex protocol that provides a byte-stream service to the application layer. TCP uses sequence numbers, acknowledgments, timers, and retransmissions to ensure reliable delivery of data. TCP also uses a sliding window mechanism to provide flow control and congestion control. TCP is suitable for applications that require reliable and ordered delivery of data, such as web browsing, email, file transfer, and remote login.  
- User Datagram Protocol (UDP): UDP is a connectionless, unreliable, and datagram-oriented protocol that provides a message service to the application layer. UDP does not use any error detection, correction, or flow control mechanisms. UDP is suitable for applications that can tolerate some loss or disorder of data, such as voice over IP, video streaming, online gaming, and domain name service.  

: Transport layer - Wikipedia
: Computer Network | Transport Layer - javatpoint
: What is the transport layer - tutorialspoint.com
: Transport Layer Introduction - tutorialspoint.com