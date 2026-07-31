## Unit 5 - Network Layer

The network layer is the third layer of the OSI model, which is responsible for how a machine in a network can communicate with a machine in a different network. The network layer performs the following functions:

- **Addressing**: The network layer assigns a logical address to each device on the network, such as an IP address, which is used to identify the source and destination of the data packets.
- **Routing**: The network layer determines the best path for the data packets to reach the destination, based on factors such as distance, traffic, cost, etc. The network layer uses routing protocols, such as RIP, OSPF, EIGRP, etc., to exchange routing information with other routers.
- **Fragmentation and reassembly**: The network layer divides the data packets into smaller fragments if they are larger than the maximum transmission unit (MTU) of the underlying network, and adds a header to each fragment with information such as sequence number, offset, etc. The network layer also reassembles the fragments at the destination and checks for errors.
- **Congestion control**: The network layer monitors the network traffic and adjusts the transmission rate of the data packets to avoid congestion and packet loss. The network layer uses congestion control algorithms, such as TCP, to regulate the flow of data.

Some of the common network protocols that operate at the network layer are:

- **Internet Protocol (IP)**: IP is the most widely used network protocol, which provides the basic functionality of addressing and routing. IP can be divided into two versions: IPv4 and IPv6, which differ in the format and size of the addresses.
- **Internet Control Message Protocol (ICMP)**: ICMP is a protocol that is used to send error and control messages between network devices, such as ping, traceroute, etc. ICMP helps to diagnose network problems and test connectivity.
- **Internet Group Management Protocol (IGMP)**: IGMP is a protocol that is used to manage multicast groups, which are groups of devices that receive the same data packets simultaneously. IGMP allows a device to join or leave a multicast group, and informs the routers about the group membership.
- **Address Resolution Protocol (ARP)**: ARP is a protocol that is used to map a network layer address, such as an IP address, to a data link layer address, such as a MAC address. ARP helps to find the physical address of a device on the same network, which is needed for data transmission.