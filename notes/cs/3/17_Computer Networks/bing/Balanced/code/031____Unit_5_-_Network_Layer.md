## Unit 5 - Network Layer

The network layer is the third layer of the OSI model, which is responsible for how a machine in a network can communicate with a machine in a different network. The network layer performs the following functions:

- **Addressing**: The network layer assigns a logical address to each device in the network, such as an IP address, which is used to identify the source and destination of the data packets. The network layer also performs address translation, such as NAT, which maps private IP addresses to public IP addresses.
- **Routing**: The network layer determines the best path for the data packets to reach the destination, based on factors such as distance, cost, congestion, and reliability. The network layer uses routing protocols, such as RIP, OSPF, EIGRP, and BGP, to exchange routing information with other routers and update their routing tables.
- **Fragmentation and reassembly**: The network layer divides the data packets into smaller fragments if they are larger than the maximum transmission unit (MTU) of the underlying network. The network layer also reassembles the fragments at the destination and checks for errors and missing fragments.
- **Congestion control and quality of service**: The network layer monitors the traffic load on the network and adjusts the transmission rate and priority of the data packets to avoid congestion and ensure quality of service. The network layer uses techniques such as queuing, scheduling, dropping, and marking to manage the network resources and traffic.

Some of the common network layer protocols are:

- **Internet Protocol (IP)**: IP is the most widely used network layer protocol, which provides connectionless and unreliable delivery of data packets across the internet. IP supports two versions: IPv4 and IPv6, which differ in their address format, header structure, and features.
- **Internet Control Message Protocol (ICMP)**: ICMP is a network layer protocol that is used to send error and control messages between devices on the internet, such as ping, traceroute, and destination unreachable.
- **Internet Group Management Protocol (IGMP)**: IGMP is a network layer protocol that is used to manage multicast groups on the internet, such as video streaming and online gaming. IGMP enables devices to join and leave multicast groups and routers to forward multicast traffic efficiently.
- **Address Resolution Protocol (ARP)**: ARP is a network layer protocol that is used to map a network layer address, such as an IP address, to a data link layer address, such as a MAC address, on a local area network (LAN). ARP enables devices to communicate with each other on the same network segment.