### Forwarding and Delivery for the Notes of the Unit 5 - Network Layer in the Subject of Computer Networks

- The network layer is responsible for the delivery of packets from the source host to the destination host across one or more networks.
- The network layer supervises the handling of the packets by the underlying physical networks, which may have different characteristics and technologies.
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer provides two main functions: **forwarding** and **routing**.
- **Forwarding** is the process of moving a packet from an input link interface to the appropriate output link interface of a router based on the destination address of the packet.
- **Routing** is the process of finding the best path from the source to the destination in the network, which involves multiple routers and networks.
- The network layer uses different protocols to perform forwarding and routing, such as IP, IPsec, ICMP, IGMP, and GRE.
- IP (Internet Protocol) is the main protocol that defines the format and structure of packets, and how they are addressed and forwarded in the network layer.
- IPsec (Internet Protocol Security) is a protocol that provides security services such as encryption, authentication, and integrity for IP packets.
- ICMP (Internet Control Message Protocol) is a protocol that allows routers and hosts to exchange control and error messages in the network layer, such as ping and traceroute.
- IGMP (Internet Group Management Protocol) is a protocol that enables hosts to join and leave multicast groups, and routers to maintain multicast forwarding tables.
- GRE (Generic Routing Encapsulation) is a protocol that allows encapsulation of packets of one protocol type within another protocol type, creating a virtual point-to-point connection.