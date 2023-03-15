### Datagram

- A datagram is a self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without reliance on earlier exchanges between this source and destination computer and the transporting network.
- It is used in connectionless networking, where each packet is treated as an independent unit of data, unrelated to any other data.
- The term datagram is used in the context of the User Datagram Protocol (UDP) of the Internet Protocol Suite.
- UDP is a connectionless protocol that provides a datagram service for the application layer.
- A datagram sent using UDP is not guaranteed to arrive at its destination, nor is it guaranteed to arrive in the same order as other datagrams sent from the same source.
- The size of a datagram is limited by the underlying network technology. For example, the maximum size of an IPv4 datagram is 65,535 bytes, while the maximum size of an IPv6 datagram is 65,535 bytes.
- Applications that use datagrams must be able to handle lost, duplicate, and out-of-order datagrams.
- Examples of applications that use datagrams include Domain Name System (DNS) and Simple Network Management Protocol (SNMP).