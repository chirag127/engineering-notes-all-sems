## Unit 5 - Network Layer

The network layer is the third layer of the OSI model and is responsible for how a machine in a network can communicate with a machine in a different network. The network layer performs the following functions:

- **Addressing**: The network layer assigns a logical address to each device on the network, such as an IP address, and uses this address to identify the source and destination of the data packets. The network layer also translates the logical address into a physical address, such as a MAC address, using protocols such as ARP or RARP.
- **Routing**: The network layer determines the best path for the data packets to reach the destination, based on factors such as distance, cost, congestion, and reliability. The network layer uses routing protocols, such as RIP, OSPF, EIGRP, or BGP, to exchange routing information with other routers and update their routing tables.
- **Fragmentation and reassembly**: The network layer divides the data packets into smaller fragments if they are larger than the maximum transmission unit (MTU) of the underlying network, and adds a header to each fragment with information such as sequence number, offset, and identification. The network layer also reassembles the fragments into the original data packets at the destination, using the information in the header.
- **Error control and congestion control**: The network layer detects and corrects errors in the data packets, such as checksum errors, using protocols such as ICMP or IGMP. The network layer also monitors and controls the traffic flow on the network, and prevents congestion by adjusting the sending rate, window size, or buffer size, using protocols such as TCP or UDP.

Some of the common network protocols that operate at the network layer are:

- **IPv4**: Internet Protocol version 4 is the most widely used network protocol that provides logical addressing and routing for the data packets on the internet. IPv4 uses 32-bit addresses and can support up to 4.3 billion devices.
- **IPv6**: Internet Protocol version 6 is the successor of IPv4 that provides logical addressing and routing for the data packets on the internet. IPv6 uses 128-bit addresses and can support up to 3.4 x 10^38 devices.
- **ICMP**: Internet Control Message Protocol is a network protocol that sends and receives error and control messages, such as echo request and reply, destination unreachable, time exceeded, or parameter problem, between the devices on the network.
- **IGMP**: Internet Group Management Protocol is a network protocol that manages the membership of multicast groups, which are groups of devices that receive the same data packets from a source. IGMP allows a device to join or leave a multicast group, and informs the routers about the group membership.