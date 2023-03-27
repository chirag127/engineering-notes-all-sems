### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

RPL (Routing Protocol for Low-Power and Lossy Networks) is a network layer protocol designed for resource-constrained and low-power devices in the Internet of Things (IoT) ecosystem. It is a standardized protocol that enables efficient and reliable routing of data packets in IoT networks.

Here are some key points to understand RPL:

- RPL is a distance-vector routing protocol that uses a Destination-Oriented Directed Acyclic Graph (DODAG) to represent the network topology. The DODAG is constructed by selecting a root node and adding nodes to the graph in a hierarchical manner.
- RPL uses a rank-based routing scheme, where each node is assigned a rank value based on its distance from the root node in the DODAG. The rank value determines the position of the node in the network topology and its role in forwarding data packets.
- RPL supports both proactive and reactive routing. In proactive routing, nodes periodically exchange control messages to maintain the network topology and update their routing tables. In reactive routing, nodes dynamically discover routes to the destination based on the current network topology.
- RPL supports multipath routing, where multiple paths can be used to transmit data packets to the destination. This improves the reliability of the network and reduces the risk of packet loss.
- RPL provides mechanisms for energy-efficient routing, such as selecting routes with low energy consumption and reducing the frequency of control message exchange to conserve energy.
- RPL is designed to work with a variety of data link layer protocols, including IEEE 802.15.4, which is commonly used in low-power wireless sensor networks.
- RPL is a standardized protocol, defined in RFC 6550, and is supported by several IoT platforms and operating systems, such as Contiki, RIOT, and TinyOS.

In summary, RPL is a network layer protocol that provides efficient and reliable routing for resource-constrained and low-power devices in IoT networks. It uses a hierarchical DODAG to represent the network topology, a rank-based routing scheme to determine the position of nodes in the topology, and supports both proactive and reactive routing. RPL also provides mechanisms for energy-efficient routing and works with a variety of data link layer protocols.