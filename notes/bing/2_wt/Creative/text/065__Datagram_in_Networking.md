#### Datagram in Networking

- A datagram is a basic transfer unit associated with a packet-switched network.
- Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination.
- Datagrams provide a connectionless communication service across a packet-switched network. This means that there is no need to establish or terminate a connection before or after sending data.
- In a datagram, data is frequently divided and transmitted from source to destination without a predefined route. The order of delivery to the receiver end is not guaranteed.
- Datagrams are typically structured in header and payload sections. The header contains information such as the source and destination addresses, the protocol type, the length, and the checksum. The payload contains the actual data to be transmitted.
- Datagrams are suitable for applications that require fast and efficient data transfer, such as video streaming, voice over IP, and online gaming. However, datagrams may also suffer from packet loss, duplication, delay, or corruption due to network congestion or errors.
- Datagrams are used by protocols such as the Internet Protocol (IP), the User Datagram Protocol (UDP), and the Internet Control Message Protocol (ICMP).