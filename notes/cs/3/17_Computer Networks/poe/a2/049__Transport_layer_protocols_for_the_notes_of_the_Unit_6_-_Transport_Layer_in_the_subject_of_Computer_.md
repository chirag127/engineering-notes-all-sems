 Here is the content in Markdown format without any emotions or external links:

### Transport layer protocols

1. TCP (Transmission Control Protocol)
- Provides reliable, ordered and error-checked delivery of sent packets over IP networks.
- Uses a three-way handshake to establish a connection between two hosts.
- Uses sequence and acknowledgement numbers to provide reliability.
- Flow control avoids overwhelming the receiver.
- Congestion control avoids overloading the network.

2. UDP (User Datagram Protocol)
- Provides fast but unreliable datagram service.
- Does not establish a dedicated end-to-end connection.
- Does not provide the reliability features of TCP.
- Used for real-time applications where speed is more important than reliability, e.g. video streaming.

3. SCTP (Stream Control Transmission Protocol)
- Provides reliable, sequenced but message-oriented communication.
- Supports multi-homed hosts with multiple IP addresses.
- Connection-oriented but provides faster failover than TCP.
- Used for signaling and control information in telephony networks.

The above points cover the major transport layer protocols - TCP providing reliable data transfer, UDP providing fast but unreliable data transfer and SCTP providing reliable message-oriented data transfer with multi-homing support. These protocols run on top of IP and handle end-to-end connectivity and data transfer between applications on two hosts.