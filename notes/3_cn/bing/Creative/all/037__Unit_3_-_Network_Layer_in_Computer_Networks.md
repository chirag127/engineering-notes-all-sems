## Unit 3 - Network Layer in Computer Networks

The network layer is the third layer in the OSI model of computer networks. The OSI model is a conceptual framework that describes how a network functions by dividing it into seven layers, from the physical hardware up to the high-level software applications .

The main function of the network layer is to transfer network packets from the source to the destination across multiple links (networks) . The network layer is responsible for the following tasks:

- **Packetizing**: The network layer breaks the data received from the higher layers into smaller units called packets. Each packet contains a header with information such as the source and destination addresses, the packet sequence number, and the protocol type. The packet header helps the network layer to route the packet to the correct destination.
- **Routing**: The network layer determines the best path for each packet to reach the destination. The network layer uses routing algorithms and routing tables to find the optimal route for each packet. Routing can be static or dynamic, depending on whether the routing tables are fixed or updated periodically .
- **Forwarding**: The network layer forwards the packets to the next hop along the path to the destination. The network layer uses the packet header to identify the destination address and the next hop address. The network layer then passes the packet to the data link layer, which handles the physical transmission of the packet over the link.
- **Addressing**: The network layer assigns a unique address to each host and network in the network layer. The network layer address is also called the logical address or the IP address. The network layer address is used to identify the source and destination of each packet. The network layer address is independent of the physical address or the MAC address, which is used by the data link layer .
- **Subnetting and Internetworking**: The network layer manages the division of a large network into smaller sub-networks or subnets. Subnetting helps to reduce the network congestion and improve the network performance. The network layer also enables the communication between different subnets or different networks using devices such as routers. Routers operate at the network layer and connect different networks using a common protocol .

Some of the common protocols that operate at the network layer are:

- **Internet Protocol (IP)**: IP is the most widely used network layer protocol that provides connectionless and unreliable packet delivery service. IP supports both IPv4 and IPv6 addressing schemes. IP is responsible for packetizing, routing, and forwarding the packets in the Internet .
- **Internet Control Message Protocol (ICMP)**: ICMP is a network layer protocol that provides error reporting and diagnostic functions for IP. ICMP sends and receives messages such as echo request and echo reply, destination unreachable, time exceeded, and parameter problem. ICMP helps to troubleshoot the network problems and test the network connectivity .
- **Internet Group Management Protocol (IGMP)**: IGMP is a network layer protocol that supports multicast communication in IP networks. IGMP enables a host to join or leave a multicast group, and a router to maintain a list of multicast group members. IGMP helps to reduce the network traffic and bandwidth consumption for multicast applications such as video streaming and online gaming .

Some of the mnemonics and learning tricks for the network layer are:

- To remember the main functions of the network layer, use the acronym **PARFS** (Packetizing, Addressing, Routing, Forwarding, Subnetting).
- To remember the common network layer protocols, use the acronym **I3C** (IP, ICMP, IGMP, and some other protocols that start with C, such as CLNP, CDP, and CARP).
- To remember the difference between static and dynamic routing, use the analogy of a map and a GPS. Static routing is like using a map that shows the fixed routes and distances between places. Dynamic routing is like using a GPS that updates the routes and distances based on the current traffic and road conditions.