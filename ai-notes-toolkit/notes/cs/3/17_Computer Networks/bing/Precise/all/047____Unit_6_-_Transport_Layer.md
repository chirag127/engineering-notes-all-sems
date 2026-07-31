## Unit 6 - Transport Layer

The transport layer is responsible for providing end-to-end communication services for applications. It is the fourth layer in the OSI model and the third layer in the TCP/IP model. Some of the key functions of the transport layer include:

1. **Connection-oriented communication:** The transport layer can establish a logical connection between the sending and receiving hosts to ensure reliable data transfer.

2. **Reliable data transfer:** The transport layer can provide reliable data transfer by implementing error detection and correction mechanisms, such as retransmission of lost or corrupted packets.

3. **Flow control:** The transport layer can regulate the flow of data between the sending and receiving hosts to prevent network congestion.

4. **Multiplexing:** The transport layer can multiplex multiple application-layer connections onto a single transport-layer connection.

5. **Segmentation and reassembly:** The transport layer can divide long messages into smaller segments for transmission and reassemble them at the receiving end.

Two of the most commonly used transport layer protocols are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP). TCP provides connection-oriented, reliable data transfer, while UDP provides connectionless, unreliable data transfer. The choice of protocol depends on the requirements of the application. For example, applications that require reliable data transfer, such as file transfers or email, typically use TCP, while applications that can tolerate some data loss, such as online gaming or video streaming, may use UDP.