 Here is the content in markdown format without any emojis or external links, written in a formal tone with points:

## Unit 4 - Transport Layer in Computer Networks

1. Introduction to Transport Layer
- The transport layer is responsible for delivering data between processes executing on different hosts.
- It provides logical communication between application processes running on different network hosts.
- It offers reliable data transmission with error correction and flow control.
- It supports multiplexing allowing multiple applications to use the network simultaneously.
- The two most common transport protocols are TCP and UDP.

2. Transmission Control Protocol (TCP)
- TCP provides reliable, ordered, and error-checked delivery of transmitted data.
- It is a connection-oriented protocol with a three-way handshake to establish a connection between two hosts.
- Data is transmitted in segments with sequence and acknowledgement numbers to ensure ordered delivery.
- Lost or corrupted segments are retransmitted.
- Congestion control is used to avoid overwhelming the network.
- Web transfers, email, and remote login use TCP.

3. User Datagram Protocol (UDP)
- UDP provides fast but unreliable data transmission without error correction or ordering.
- It is a connectionless protocol that does not establish a dedicated end-to-end connection.
- Data is transmitted in datagrams with source and destination port numbers.
- Lost or corrupted datagrams are not retransmitted.
- Streaming media and video conferencing use UDP to prioritize time over reliability.

4. Differences between TCP and UDP
- TCP is reliable, ordered, and error-checked while UDP is fast but unreliable.
- TCP uses a three-way handshake to establish a connection while UDP is connectionless.
- TCP uses sequence and acknowledgement numbers, retransmissions, and congestion control while UDP uses only port numbers and no error correction.
- TCP is typically used for web transfers and email while UDP is used for streaming media and video conferencing.