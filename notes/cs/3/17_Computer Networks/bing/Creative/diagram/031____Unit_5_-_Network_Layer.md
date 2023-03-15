## Unit 5 - Network Layer

The network layer is the third layer of the OSI model and the layer that provides data routing paths for network communication. Data is transferred in the form of packets via logical network paths in an ordered format controlled by the network layer. The network layer is also responsible for logical addressing, fragmentation and reassembly, and error control functions.

Some of the main functions of the network layer are:

- **Logical addressing**: The network layer assigns a unique logical address to each device on the network, such as an IP address. This address is used to identify the source and destination of the packets and to route them through the network.
- **Routing**: The network layer determines the best path for sending the packets from the source to the destination, based on factors such as distance, cost, congestion, and reliability. The network layer uses routing protocols, such as RIP, OSPF, EIGRP, and BGP, to exchange routing information and update routing tables.
- **Fragmentation and reassembly**: The network layer divides the packets into smaller fragments if they are larger than the maximum transmission unit (MTU) of the underlying network. The network layer also reassembles the fragments at the destination and checks for errors and missing fragments.
- **Error control**: The network layer detects and corrects errors that may occur during the transmission of the packets. The network layer uses checksums, sequence numbers, and acknowledgments to ensure the integrity and reliability of the data.

Some of the common network layer protocols are:

- **Internet Protocol (IP)**: IP is the most widely used network layer protocol that provides connectionless and unreliable datagram service. IP is responsible for logical addressing, routing, fragmentation and reassembly, and error control functions. IP has two versions: IPv4 and IPv6, which differ in the address format, header structure, and features.
- **Internet Control Message Protocol (ICMP)**: ICMP is a network layer protocol that provides error reporting and diagnostic functions for IP. ICMP sends and receives messages, such as echo request and reply, destination unreachable, time exceeded, and parameter problem, to inform the source or the destination about the status of the packets.
- **Internet Group Management Protocol (IGMP)**: IGMP is a network layer protocol that manages multicast groups on IP networks. IGMP enables hosts to join or leave multicast groups and routers to maintain multicast group membership information and forward multicast packets accordingly.
- **Address Resolution Protocol (ARP)**: ARP is a network layer protocol that maps the logical address (IP address) of a device to its physical address (MAC address) on a local area network (LAN). ARP enables devices to communicate with each other on the same network segment without the need for a router.