# Unit 5 - Network Layer

The network layer is the third layer of the OSI model and the layer that provides data routing paths for network communication. The network layer is responsible for how a machine in a network can communicate with a machine in a different network. Some of the main functions of the network layer are:

- Addressing: The network layer assigns logical addresses to the devices in the network, such as IP addresses. These addresses are used to identify the source and destination of the data packets and to route them through the network.
- Routing: The network layer determines the best path for the data packets to reach the destination, based on factors such as distance, congestion, cost, etc. The network layer uses routing protocols, such as RIP, OSPF, EIGRP, BGP, etc., to exchange routing information with other routers and to update their routing tables.
- Fragmentation and reassembly: The network layer may divide the data packets into smaller fragments if the maximum transmission unit (MTU) of the underlying network is smaller than the packet size. The network layer also reassembles the fragments at the destination and checks for errors and missing fragments.
- Congestion control: The network layer monitors the network traffic and tries to avoid or reduce congestion by regulating the flow of data packets. The network layer may use techniques such as buffering, queuing, dropping, or feedback to control congestion.
- Error control: The network layer detects and corrects errors that may occur during the transmission of data packets. The network layer may use checksums, acknowledgments, timers, or retransmission to ensure reliable delivery of data.

Some of the common network layer protocols are:

- Internet Protocol (IP): IP is the most widely used network layer protocol that provides connectionless and best-effort delivery of data packets across the internet. IP supports both IPv4 and IPv6 addressing schemes and defines the format and structure of the IP datagrams.
- Internet Control Message Protocol (ICMP): ICMP is a network layer protocol that provides error and diagnostic messages for IP. ICMP is used to report network problems, such as unreachable hosts, network congestion, time exceeded, etc. ICMP also supports ping and traceroute utilities that test the connectivity and trace the route of data packets.
- Internet Group Management Protocol (IGMP): IGMP is a network layer protocol that manages multicast groups on the internet. IGMP allows hosts to join or leave multicast groups and routers to exchange multicast group information and forward multicast packets to the appropriate hosts.
- Address Resolution Protocol (ARP): ARP is a network layer protocol that maps the network layer addresses (IP addresses) to the data link layer addresses (MAC addresses). ARP is used to find the MAC address of a host or a router that has a specific IP address. ARP uses ARP requests and ARP replies to exchange address information.