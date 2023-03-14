#### Datagram in Networking

- A datagram is a basic transfer unit associated with a packet-switched network.
- Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination.
- Datagrams provide a connectionless communication service across a packet-switched network. The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network.
- In a datagram network, each datagram is routed independently from the source to the destination even if they belong to the same message. The network treats the packet as if it exists alone.
- Since the datagrams are treated as independent units, no dedicated path is fixed for data transfer. Each datagram is routed by the intermediate routers using dynamically changing routing tables. So two successive packets from the source may follow completely separate routes to reach destination.
- In datagram networks, no prior resource allocation is done for the individual packets. This implies that no resources like buffers, processors, bandwidth, etc. are reserved before the communication commences. In datagram networks, resources are allocated on demand on a First−Come First−Serve (FCFS) basis.
- Datagram communication is generally guided by User Datagram Protocol or UDP.
- The following diagram shows datagram packets being sent by host H1 to host H2. The four datagram packets labelled as A, B, C and D, all belonging to same message are being routed separately via separate routes. The packets in the message arrive in the destination out of order. It is the responsibility of H2 to reorder the packets in order to retrieve the original message.

```
    H1
    | A
    |/
    R1
   /| B
  / |
 /  |
R2  R3
|  /| C
| / |
|/  |
R4  R5
|  /| D
| / |
|/  |
    H2
```

- Some advantages of datagram networks are:
  - They are more robust and fault-tolerant, as the failure of one node or link does not affect the entire network.
  - They are more scalable and flexible, as new nodes and links can be added or removed without disrupting the existing connections.
  - They are more efficient and fair, as the network resources are shared among all the packets on a FCFS basis, and no packet has to wait for a long time.
- Some disadvantages of datagram networks are:
  - They do not guarantee the reliable delivery, order, or integrity of the packets, as they may be lost, corrupted, duplicated, or reordered in transit.
  - They do not provide any flow control or congestion control mechanisms, as the network does not keep track of the state or the rate of the packets.
  - They do not support any quality of service or priority schemes, as the network does not differentiate between the packets based on their source, destination, or application.
- Some examples of datagram networks are:
  - The Internet, which uses the Internet Protocol (IP) as the datagram service for the network layer.
  - Local area networks (LANs), which use the Ethernet protocol as the datagram service for the data link layer.
  - Wireless networks, which use the IEEE 802.11 protocol as the datagram service for the physical and data link layers.
- Some applications of datagram networks are:
  - Real-time applications, such as voice over IP (VoIP) or video streaming, which can tolerate some packet loss or delay, but require low latency and jitter.
  - Interactive applications, such as online gaming or web browsing, which can tolerate some packet loss or reordering, but require fast response and feedback.
  - Broadcast or multicast applications, such as live events or group communication, which can benefit from the scalability and efficiency of datagram networks.

- A possible mnemonic to remember the characteristics of datagram networks is:

**D**ynamic routing
**A**llocation on demand
**T**ransfer unit
**A**rrival not guaranteed
**G**uided by UDP
**R**eordering by receiver
**A**dvantages and disadvantages
**M**any examples and applications