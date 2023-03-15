# Unit 5 - Network Layer

The network layer is the third layer of the OSI model and the layer that provides data routing paths for network communication. Data is transferred in the form of packets via logical network paths in an ordered format controlled by the network layer. The network layer is also responsible for logical addressing, fragmentation and reassembly, and error control functions.

Some of the functions of the network layer are:

- **Logical addressing**: The network layer assigns a unique address to each device on the network, which is used to identify the source and destination of the data packets. The most common logical addressing scheme is the Internet Protocol (IP) address.
- **Routing**: The network layer determines the best path for data to reach its destination, based on factors such as network topology, traffic, and cost. The network layer uses routing protocols, such as Routing Information Protocol (RIP), Open Shortest Path First (OSPF), and Border Gateway Protocol (BGP), to exchange routing information and update routing tables .
- **Fragmentation and reassembly**: The network layer divides large data packets into smaller fragments that can be transmitted more efficiently across different types of networks. The network layer also reassembles the fragments at the destination and checks for errors and missing pieces.
- **Error control**: The network layer detects and corrects errors that may occur during data transmission, such as packet loss, duplication, or corruption. The network layer uses checksums, acknowledgments, and timers to ensure reliable data delivery.

Some of the protocols that operate at the network layer are:

- **Internet Protocol (IP)**: IP is the main protocol that provides logical addressing and routing for data packets across the internet. IP can be divided into two versions: IPv4 and IPv6. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses. IPv4 is the most widely used version, but IPv6 is gradually replacing it due to the shortage of IPv4 addresses .
- **Internet Control Message Protocol (ICMP)**: ICMP is a protocol that sends and receives error and control messages between network devices. ICMP is used for diagnostic purposes, such as ping and traceroute, to test the connectivity and reachability of network hosts. ICMP also reports network problems, such as destination unreachable, time exceeded, or parameter problem .
- **Internet Group Management Protocol (IGMP)**: IGMP is a protocol that manages multicast groups on a network. Multicast is a method of sending data to multiple destinations simultaneously, using a single source address and a group address. IGMP allows network devices to join or leave multicast groups, and informs routers about the membership status of the groups .