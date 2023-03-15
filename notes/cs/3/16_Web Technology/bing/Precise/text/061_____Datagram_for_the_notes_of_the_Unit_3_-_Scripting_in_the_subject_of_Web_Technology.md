### Datagram

- A datagram is a self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without reliance on earlier exchanges between this source and destination computer and the transporting network.
- It is used in connectionless networking, where each packet is treated as an independent unit of data.
- The term datagram is used in the context of the User Datagram Protocol (UDP) of the Internet Protocol Suite.
- UDP is a connectionless protocol that provides a datagram service for the application layer.
- Each UDP datagram contains information about the source and destination ports, the length of the data, and a checksum for error detection.
- UDP is considered an unreliable protocol because it does not provide any guarantees for the delivery of datagrams.
- However, it is useful for applications that require fast transmission of data and can tolerate some loss of data, such as online gaming or streaming media.
- In contrast, the Transmission Control Protocol (TCP) provides a reliable, connection-oriented service for the application layer, where data is transmitted in a continuous stream and packets are guaranteed to be delivered in the correct order.