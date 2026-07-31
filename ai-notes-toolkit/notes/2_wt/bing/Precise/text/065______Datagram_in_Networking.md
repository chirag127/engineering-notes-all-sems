#### Datagram in Networking

- A datagram is a self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without reliance on earlier exchanges between this source and destination computer and the transporting network.
- It is a basic transfer unit associated with a packet-switched network.
- Datagrams are used in connectionless networking, where each packet is treated as an independent unit of data and is separately routed from the source to the destination.
- The term datagram is often used interchangeably with the term packet, although the two have slightly different meanings.
- In the context of the Internet Protocol (IP), a datagram is the basic unit of data that is transmitted over the network.
- Each IP datagram contains a header and a payload. The header contains information about the datagram, such as its source and destination addresses, while the payload contains the actual data being transmitted.
- The size of an IP datagram can vary, but it is typically limited to 65,535 bytes, including both the header and the payload.
- Since datagrams are treated as independent units of data, they may be delivered to the destination in a different order than they were sent, or they may be lost or corrupted during transmission.
- To ensure reliable delivery of data, higher-level protocols, such as the Transmission Control Protocol (TCP), may be used to provide error checking and retransmission of lost or corrupted datagrams.