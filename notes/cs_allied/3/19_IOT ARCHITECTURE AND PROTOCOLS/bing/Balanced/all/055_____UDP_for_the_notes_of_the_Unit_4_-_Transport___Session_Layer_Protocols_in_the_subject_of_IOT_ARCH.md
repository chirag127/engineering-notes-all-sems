# UDP

UDP stands for User Datagram Protocol. It is one of the core communication protocols of the Internet protocol suite used to send messages (transported as datagrams in packets) to other hosts on an Internet Protocol (IP) network.

Some of the main features and characteristics of UDP are:

- UDP is a simple message-oriented transport layer protocol that is documented in RFC 768.
- UDP provides integrity verification (via checksum) of the header and payload, but it provides no guarantees to the upper layer protocol for message delivery and the UDP layer retains no state of UDP messages once sent.
- UDP is a connectionless protocol, which means that there is no need to establish a connection prior to data transfer.
- UDP is suitable for applications that require low-latency and loss-tolerating connections, such as streaming media, online gaming, voice over IP, etc.
- UDP provides a mechanism to detect corrupt data in packets, but it does not attempt to solve other problems that arise with packets, such as lost or out of order packets.
- UDP has a fixed header size of 8 bytes, which consists of four fields: source port, destination port, length, and checksum.
- UDP does not provide any flow control, congestion control, or error recovery mechanisms, which are left to the application layer to handle.
- UDP can support both one-to-one and one-to-many communication modes, such as unicast, multicast, and broadcast.