### TCP

TCP (Transmission Control Protocol) is a connection-oriented protocol that operates at the transport layer of the OSI model. It provides reliable, ordered, and error-checked delivery of data between applications running on hosts communicating over an IP network.

TCP has the following features:

- **Connection-oriented**: Before data exchange, TCP establishes a connection between two endpoints. The connection is maintained until the end of data exchange, and then it is terminated.
- **Reliable**: TCP ensures that all the transmitted data is received correctly by the receiver. If any data packet is lost or damaged during transmission, TCP retransmits it until it is delivered successfully.
- **Ordered**: TCP guarantees that the data packets are delivered in the same order in which they were sent.
- **Flow control**: TCP uses a sliding window mechanism to control the flow of data between the sender and the receiver. This ensures that the receiver is not overwhelmed with data that it cannot process.
- **Congestion control**: TCP monitors the network for congestion and adjusts the rate of data transmission accordingly to avoid congestion.

TCP works by breaking the data into small packets, which are transmitted over the network. Each packet contains a sequence number, which helps the receiver to reorder the packets and detect any missing packets. The receiver sends an acknowledgment for each packet received, and the sender retransmits any packet for which an acknowledgment is not received.

TCP is widely used in the Internet Protocol (IP) suite and is the most commonly used transport protocol for applications such as web browsing, file transfer, and email. Its reliability and flow control mechanisms make it suitable for applications that require the delivery of large amounts of data without loss or corruption.