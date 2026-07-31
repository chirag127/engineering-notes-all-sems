### Flow control in transport layer

- Flow control is the mechanism that regulates the rate of data transmission between two nodes in a network.
- Flow control is needed in transport layer because it prevents data loss due to buffer overflow or underflow, and improves the efficiency and reliability of data transmission.
- Flow control in transport layer is different from flow control in data link layer, because it operates end-to-end, not just across a single link.
- Flow control in transport layer can be implemented by using feedback-based or rate-based techniques.
- Feedback-based flow control uses acknowledgments and windowing to adjust the sender's transmission rate according to the receiver's buffer capacity and network congestion.
- Rate-based flow control uses a predefined transmission rate that is agreed upon by both sender and receiver, and does not depend on feedback.
- Some examples of transport layer protocols that use flow control are TCP, UDP, and SCTP.