### Datagram

- A datagram is a self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without reliance on earlier exchanges between this source and destination computer and the transporting network.
- It is used in connectionless networking, where each packet is treated as an independent unit of data.
- The term datagram is used in the context of the User Datagram Protocol (UDP) of the Internet Protocol Suite.
- UDP is a connectionless protocol that provides a datagram service for the application layer.
- Each UDP datagram contains a header and a payload. The header contains information such as the source and destination port numbers, the length of the datagram, and a checksum for error detection.
- UDP datagrams are sent over the network using the Internet Protocol (IP), which provides a best-effort delivery service.
- This means that there is no guarantee that the datagram will be delivered to its destination, or that it will arrive in the same order in which it was sent.
- Applications that use UDP must be able to handle lost, duplicated, or out-of-order datagrams.
- Examples of applications that use UDP include Domain Name System (DNS) queries, online gaming, and Voice over IP (VoIP) telephony.