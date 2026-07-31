### RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks (LLNs), which are networks composed of resource-constrained devices that communicate over unreliable and low-bandwidth links  .
- RPL is designed to support a variety of IoT applications, such as smart grid, industrial automation, environmental monitoring, and home automation.
- RPL operates on top of the IPv6 protocol and uses the 6LoWPAN adaptation layer to compress and fragment IPv6 packets for transmission over IEEE 802.15.4 links  .
- RPL organizes the network into a Destination Oriented Directed Acyclic Graph (DODAG), which is a tree-like structure rooted at a destination node, such as a gateway or a sink  .
- RPL uses a metric called rank to measure the distance of a node from the DODAG root. The rank is calculated based on various parameters, such as hop count, link quality, energy consumption, and latency  .
- RPL uses two types of control messages to build and maintain the DODAG: DIO (DODAG Information Object) and DAO (Destination Advertisement Object). DIO messages are broadcasted by nodes to advertise their rank and DODAG configuration. DAO messages are unicast by nodes to inform their parents about their downstream routes  .
- RPL supports two modes of operation: storing mode and non-storing mode. In storing mode, each node maintains a routing table with entries for all its descendants. In non-storing mode, only the root maintains a routing table with entries for all the nodes in the DODAG  .
- RPL also supports local repair mechanisms to cope with link failures and topology changes. These include poison reverse, local rerouting, and global repair  .
- RPL faces several security challenges due to the characteristics of IoT networks, such as resource limitations, dynamic topology, and heterogeneous devices  .
- RPL security requirements include confidentiality, integrity, availability, authentication, authorization, and non-repudiation  .
- RPL security threats include external attacks, such as eavesdropping, replay, spoofing, and denial of service, and internal attacks, such as rank, version number, DAO inconsistency, and DIO inconsistency attacks  .
- RPL security solutions include cryptographic mechanisms, such as symmetric and asymmetric encryption, digital signatures, and message authentication codes, and non-cryptographic mechanisms, such as trust management, intrusion detection, and secure routing metrics  .