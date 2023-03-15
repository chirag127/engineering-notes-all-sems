## Unit 5 - Network Layer

The network layer is the third layer of the OSI model and the layer that provides data routing paths for network communication. Data is transferred in the form of packets via logical network paths in an ordered format controlled by the network layer. The network layer is also responsible for logical addressing, fragmentation and reassembly, and error control functions.

Some of the main functions of the network layer are:

- **Logical addressing**: The network layer assigns a unique logical address to each device on the network, such as an IP address. This address is used to identify the source and destination of the packets and to route them through the network.
- **Routing**: The network layer determines the best path for sending the packets from the source to the destination, based on factors such as distance, cost, congestion, and reliability. The network layer uses routing protocols, such as RIP, OSPF, EIGRP, and BGP, to exchange routing information and update routing tables.
- **Fragmentation and reassembly**: The network layer divides the packets into smaller fragments if they are larger than the maximum transmission unit (MTU) of the underlying network. The network layer also reassembles the fragments at the destination and checks for errors and missing fragments.
- **Error control**: The network layer detects and corrects errors that may occur during the transmission of the packets. The network layer uses checksums, sequence numbers, and acknowledgments to ensure the integrity and reliability of the data.

Some of the common network layer protocols are:

- **Internet Protocol (IP)**: IP is the most widely used network layer protocol that provides connectionless and unreliable delivery of packets across the internet. IP supports both IPv4 and IPv6 addressing schemes and handles the fragmentation and reassembly of packets.
- **Internet Control Message Protocol (ICMP)**: ICMP is a network layer protocol that provides error and diagnostic messages for IP. ICMP is used to report network problems, such as unreachable hosts, network congestion, and time exceeded.
- **Internet Group Management Protocol (IGMP)**: IGMP is a network layer protocol that manages the membership of multicast groups on a network. IGMP allows a host to join or leave a multicast group and informs the routers about the group membership status.
- **Address Resolution Protocol (ARP)**: ARP is a network layer protocol that maps a logical address, such as an IP address, to a physical address, such as a MAC address. ARP is used to find the MAC address of a host or a router on a local network.