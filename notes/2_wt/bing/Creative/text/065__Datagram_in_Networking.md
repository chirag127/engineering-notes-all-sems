#### Datagram in Networking

- A datagram is a basic transfer unit associated with a packet-switched network.
- Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination.
- Datagrams provide a connectionless communication service across a packet-switched network. The delivery, arrival time, and order of arrival of datagrams need not be guaranteed by the network.
- In a datagram network, each datagram is routed independently from the source to the destination even if they belong to the same message. The network treats the packet as if it exists alone.
- Since the datagrams are treated as independent units, no dedicated path is fixed for data transfer. Each datagram is routed by the intermediate routers using dynamically changing routing tables. So two successive packets from the source may follow completely separate routes to reach destination.
- In a datagram network, no prior resource allocation is done for the individual packets. This implies that no resources like buffers, processors, bandwidth, etc. are reserved before the communication commences. In datagram networks, resources are allocated on demand on a First−Come First−Serve (FCFS) basis.
- Datagram communication is generally guided by User Datagram Protocol or UDP.
- The following diagram shows datagram packets being send by host H1 to host H2. The four datagram packets labelled as A, B, C and D, all belonging to same message are being routed separately via separate routes. The packets in the message arrives in the destination out of order. It is the responsibility of H2 to reorder the packets in order to retrieve the original message.

![Diagram of datagram network](https://www.tutorialspoint.com/datagram-network/images/datagram_network.jpg)