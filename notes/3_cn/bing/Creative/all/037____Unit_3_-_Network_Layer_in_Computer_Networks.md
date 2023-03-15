## Unit 3 - Network Layer in Computer Networks

- The network layer is the third layer in the OSI model and the Internet layer in the TCP/IP model.
- The network layer is responsible for transmitting data segments between networks in the form of packets.
- The network layer assigns source and destination IP addresses to the packets and determines the best paths for data delivery using routing protocols.
- The network layer also manages sub-networks, internetworking, quality of service, load balancing, link management and security.
- The network layer can interrelate different protocols and subnets with different schemas and provide different logical network designs over the physical network design.
- The network layer works with routers, which are devices that move data packets across multiple networks.
- The network layer can be divided into two sub-layers: the logical network sub-layer and the physical network sub-layer.
- The logical network sub-layer deals with the logical addressing and routing of packets, while the physical network sub-layer deals with the physical addressing and transmission of packets.

Some of the main concepts and protocols related to the network layer are:

- IP (Internet Protocol): The main protocol that defines the format and structure of packets and how they are routed across networks.
- ICMP (Internet Control Message Protocol): A protocol that sends error and control messages between hosts and routers.
- ARP (Address Resolution Protocol): A protocol that maps IP addresses to MAC addresses of devices on the same network.
- RARP (Reverse Address Resolution Protocol): A protocol that maps MAC addresses to IP addresses of devices on the same network.
- DHCP (Dynamic Host Configuration Protocol): A protocol that assigns IP addresses and other network parameters to devices dynamically.
- NAT (Network Address Translation): A technique that allows multiple devices to share a single public IP address by modifying the source and destination addresses of packets.
- IPv4 (Internet Protocol version 4): The most widely used version of IP that uses 32-bit addresses and can support up to 4.3 billion devices.
- IPv6 (Internet Protocol version 6): The latest version of IP that uses 128-bit addresses and can support up to 3.4 x 10^38 devices.
- Subnetting: A technique that divides a network into smaller sub-networks by using a subnet mask.
- CIDR (Classless Inter-Domain Routing): A technique that allows more flexible allocation of IP addresses by using a prefix length instead of a class-based system.
- Routing: The process of finding the best path for a packet to reach its destination using routing algorithms and routing tables.
- Routing Protocols: The rules and procedures that routers use to exchange routing information and update their routing tables.
- Static Routing: A type of routing that uses manually configured routes that do not change unless the network administrator changes them.
- Dynamic Routing: A type of routing that uses routing protocols to automatically update routes based on network conditions and topology changes.
- Distance Vector Routing: A type of dynamic routing that uses the distance (number of hops) and the direction (next hop) to find the best route for a packet.
- Link State Routing: A type of dynamic routing that uses the state (cost, bandwidth, delay, etc.) of each link to find the best route for a packet.
- RIP (Routing Information Protocol): A distance vector routing protocol that uses hop count as the metric and has a maximum of 15 hops.
- OSPF (Open Shortest Path First): A link state routing protocol that uses cost as the metric and supports hierarchical routing and load balancing.
- BGP (Border Gateway Protocol): A distance vector routing protocol that is used to exchange routing information between autonomous systems (networks under different administrative domains).
- Multicast Routing: A type of routing that delivers a packet to multiple destinations that belong to a multicast group.
- IGMP (Internet Group Management Protocol): A protocol that manages the membership of multicast groups and communicates with multicast routers.
- PIM (Protocol Independent Multicast): A protocol that supports multicast routing across different network protocols and topologies.

Some of the mnemonics and learning tricks for the network layer are:

- To remember the sub-layers of the network layer, use the acronym LNP (Logical Network, Physical Network).
- To remember the main functions of the network layer, use the acronym ARQILS (Addressing, Routing, Quality of service, Internetworking, Load balancing, Security).
- To remember the main protocols of the network layer, use the acronym IIAARND (IP, ICMP, ARP, RARP, DHCP, NAT).
- To remember the difference between IPv4 and IPv6, use the acronym BALS (Bits, Addresses, Length,