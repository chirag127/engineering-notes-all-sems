 Here is the content in markdown format for #### TCP Transport layer protocol:

#### TCP Transport layer protocol

TCP or Transmission Control Protocol is a transport layer protocol in the TCP/IP stack. Some key points about TCP are:

- It provides reliable, ordered, and error-checked delivery of transmitted data over IP networks.
- It uses a connection-oriented model, where a dedicated end-to-end connection is established between two hosts before actual data transmission begins. This connection is terminated after the data transmission is complete.
- It uses a three-way handshake to establish a connection between two hosts. This involves the following steps:
1. SYN: The client sends a SYN request to the server
2. SYN-ACK: The server sends a SYN-ACK acknowledgment to the client
3. ACK: The client sends an ACK acknowledgment to the server
- It uses a sliding window protocol for data transmission, which helps in congestion control and increases efficiency.
- It provides in-order delivery of data which is numbered using sequence numbers. This helps in detecting any lost or duplicated packets.
- It uses acknowledgements and retransmissions for reliable data delivery. The recipient sends acknowledgement for the received data which is used by the sender to detect any lost packets. The lost packets are then retransmitted.
- The advantages of TCP include reliability, ordering, and congestion control. The disadvantages include overhead and slower speed as compared to UDP.
- TCP is typically used for applications that require high reliability such as HTTP, FTP, SMTP, etc.

Some mnemonics to remember TCP are:
- "Please Do Not Send Anything Without Proper Consent" which stands for Protocol, Delivery, Numbering, Sequencing, Acknowledgement, Windowing, Protocols
- "Come Quick, Uncle Sam Wants Cash" which stands for Connection, Queueing, Urgent, Sequence, Windows, Checksum

[Include detailed ascii diagrams, codes, markdown tables, examples, applications, etc. if required]