#### TCP Transport layer protocol

TCP (Transmission Control Protocol) is one of the core protocols of the Internet protocol suite. It operates at the transport layer of the OSI model and provides reliable, ordered, and error-checked delivery of data between applications running on hosts communicating over an IP network.

Here are some key points about TCP:

- TCP is a connection-oriented protocol, which means that it establishes a connection between two hosts before transmitting data.
- It uses a three-way handshake to establish the connection: SYN, SYN-ACK, and ACK.
- TCP provides a reliable transport service, which means that it ensures that all data sent is received by the destination host and that it is received in the correct order.
- TCP uses a flow control mechanism to ensure that the sender does not overwhelm the receiver with data.
- TCP uses a congestion control mechanism to ensure that the network is not overloaded with traffic.
- TCP supports full-duplex communication, which means that data can be sent in both directions simultaneously.
- TCP is a byte-stream protocol, which means that it transmits data as a series of bytes without any inherent message boundaries.
- TCP does not provide any error recovery mechanism; this is left to the application layer protocols.
- TCP is widely used by many applications, including web browsers, email clients, file transfer protocols, and network printing protocols.

In summary, TCP is an essential protocol that provides reliable and ordered delivery of data between applications running on different hosts over an IP network. Its features, such as connection-oriented communication, flow control, and congestion control, make it a popular choice for many network applications.