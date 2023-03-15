

#### TCP Transport Layer Protocol

- TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating over an IP network.
- TCP is a reliable transport layer protocol because it uses acknowledgements and flow control to ensure that data is received in the same order in which it was sent.
- TCP is also a connection-oriented protocol, which means that a connection is established between two applications before any data can be exchanged.
- TCP uses a three-way handshake to establish a connection between two applications. The three-way handshake consists of a SYN, SYN-ACK, and an ACK.
- TCP uses a sliding window flow control mechanism to ensure that the sender does not overwhelm the receiver with data. This flow control mechanism allows the receiver to specify the amount of data it is willing to accept from the sender.
- TCP also provides error detection and correction by using checksums. Checksums are used to detect errors in the data that is being transmitted.
- TCP also provides congestion control, which is used to prevent network congestion. Congestion control allows the sender to adjust its transmission rate in order to prevent network congestion.
- Mnemonics: 
  - SYN: Start Your Network
  - SYN-ACK: Send Acknowledgement
  - ACK: Acknowledge