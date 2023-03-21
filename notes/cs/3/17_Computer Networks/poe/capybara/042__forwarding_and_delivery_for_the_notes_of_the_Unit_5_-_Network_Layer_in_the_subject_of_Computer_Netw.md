

### Forwarding and Delivery for the Notes of Unit 5 - Network Layer in the Subject of Computer Networks

The Network Layer is responsible for the delivery of packets from the source to the destination. It provides the necessary infrastructure for moving data across network boundaries. In this unit, we will discuss the forwarding and delivery process in the Network Layer.

#### Forwarding

Forwarding is the process of transferring a packet from an input port to an output port on a router. The router looks up the destination address in the packet header and forwards the packet to the next hop. The forwarding process involves the following steps:

- The router receives a packet on an input port.
- The router examines the destination address in the packet header to determine the output port.
- The router looks up the forwarding table to find the next hop for the destination address.
- The router forwards the packet to the next hop on the appropriate output port.

#### Delivery

Delivery is the process of ensuring that a packet reaches its intended destination. The delivery process involves the following steps:

- The source host encapsulates the data in a packet and sends it to the first router in the path to the destination.
- Each router in the path examines the destination address in the packet header and forwards the packet to the next hop.
- The packet is forwarded from router to router until it reaches the destination host.
- The destination host receives the packet, extracts the data, and delivers it to the appropriate application.

#### Routing

Routing is the process of determining the best path for a packet to reach its destination. The routing process involves the following steps:

- The router receives a packet on an input port.
- The router examines the destination address in the packet header to determine the best path to the destination.
- The router consults its routing table to find the next hop on the best path.
- The router forwards the packet to the next hop on the appropriate output port.

#### Conclusion

The Network Layer is responsible for the delivery of packets from the source to the destination. The forwarding and delivery process involves the transfer of packets from one router to another until it reaches the destination host. Routing is the process of determining the best path for a packet to reach its destination. Understanding the forwarding and delivery process is crucial for network engineers to design and troubleshoot networks.