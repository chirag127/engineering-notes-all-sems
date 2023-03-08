 Here is the content in markdown format for the given topics:

## Unit 3 - Network Layer in Computer Networks

The network layer is responsible for the following tasks:

1. Logical addressing - The network layer adds source and destination addresses to the packet headers, using logical addresses to identify the sending and receiving hosts.
2. Routing - The network layer performs routing, which involves selecting paths through an internetwork and forwarding packets among routers to reach the destination.
3. Fragmentation - The network layer can fragment packets into smaller packets to accommodate the maximum transmission unit (MTU) size of the network.
4. Congestion control - The network layer detects and helps avoid congestion in the network.

*Some key protocols at the network layer are IP, ICMP, ARP, RARP.*

IP (Internet Protocol) is the primary protocol that defines logical addressing and routing methods. ICMP (Internet Control Message Protocol) is used for diagnostics and reporting errors. ARP (Address Resolution Protocol) is used to map IP addresses to MAC addresses. RARP (Reverse Address Resolution Protocol) is used to map MAC addresses to IP addresses.

Advantages:

- Logical addressing enables efficient routing and delivery of packets.
- Routing enables optimal delivery paths to be selected based on Layer 3 (network layer) information.
- Fragmentation enables packets to be accommodated on networks with smaller MTUs.
- Congestion control helps avoid and recover from network congestion.

[Detailed diagrams and examples can be added here if required for learning]

### Coupling and Cohesion Measures for the notes of the Unit 3 - Software Design in the subject of Software Engineering

Coupling refers to the degree of interdependence between modules or components. High coupling means modules are heavily dependent on each other, which can make systems rigid, difficult to maintain and re-use modules.

Cohesion refers to the degree to which the elements inside a module belong together. High cohesion means elements strongly relate to the module's purpose, which makes modules more focused, reusable and maintainable.

[Continued...]