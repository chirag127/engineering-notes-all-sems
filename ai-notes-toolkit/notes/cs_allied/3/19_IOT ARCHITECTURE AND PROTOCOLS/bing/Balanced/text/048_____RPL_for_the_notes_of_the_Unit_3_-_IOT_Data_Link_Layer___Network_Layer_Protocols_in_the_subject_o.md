### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The network layer is responsible for routing packets from source to destination in an IoT network.
- The network layer is divided into two sublayers: routing layer and encapsulation layer.
- The routing layer handles the transfer of packets from source to destination, while the encapsulation layer forms the packets.
- RPL stands for Routing Protocol for Low-Power and Lossy Networks. It is a routing protocol designed for IoT networks that are resource-constrained, dynamic, and unreliable.
- RPL constructs a tree-like topology for the data transmission, where each node has a rank that indicates its position in the tree.
- RPL uses two types of messages: control messages and data messages.
- Control messages are used to build and maintain the topology, while data messages are used to carry the application data.
- Control messages include DIO (DODAG Information Object), DAO (Destination Advertisement Object), DIS (DODAG Information Solicitation), and DAO-ACK (DAO Acknowledgment).
- DIO messages are used to advertise the rank and other information of a node to its neighbors.
- DAO messages are used to inform the parent node about the destination nodes that are reachable through the sender node.
- DIS messages are used to request DIO messages from the neighbors.
- DAO-ACK messages are used to acknowledge the receipt of DAO messages.
- Data messages include ICMPv6 (Internet Control Message Protocol version 6) and UDP (User Datagram Protocol) packets.
- ICMPv6 packets are used to perform diagnostic functions, such as ping and traceroute.
- UDP packets are used to carry the application data, such as sensor readings or actuator commands.
- RPL supports two modes of operation: storing mode and non-storing mode.
- In storing mode, each node maintains a routing table that contains the next hop information for all the destinations in the network.
- In non-storing mode, each node only maintains the next hop information for its parent node, and the source node includes the entire path information in the data packet.