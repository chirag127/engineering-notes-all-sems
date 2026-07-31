### RPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The network layer is responsible for routing packets from source to destination in an IoT network.
- The network layer is divided into two sublayers: routing layer and encapsulation layer.
- The routing layer handles the transfer of packets from source to destination, while the encapsulation layer forms the packets.
- RPL stands for Routing Protocol for Low-Power and Lossy Networks. It is a routing protocol designed for IoT networks that are resource-constrained, dynamic, and unreliable.
- RPL constructs a tree-like structure for the data transmission, where each node has a parent and zero or more children.
- RPL uses a metric called rank to measure the distance of a node from the root of the tree. The rank is based on various factors, such as hop count, energy consumption, link quality, etc.
- RPL defines three types of messages: DIO (DODAG Information Object), DAO (Destination Advertisement Object), and DIS (DODAG Information Solicitation).
- DIO messages are used to advertise the rank and other information of a node to its neighbors. DIO messages are also used to build and maintain the tree structure.
- DAO messages are used to propagate the destination information of a node to its parents. DAO messages are also used to enable downward routing, i.e., from the root to the nodes.
- DIS messages are used to request DIO messages from the neighbors. DIS messages are also used to discover new nodes or repair the tree structure.
- RPL supports multiple instances and multiple modes of operation. An instance is a set of nodes that use the same objective function and configuration parameters. A mode of operation is a set of rules that define how the nodes join and leave the tree, how the rank is computed, and how the routing is performed.
- RPL supports three modes of operation: storing mode, non-storing mode, and source routing mode.
- In storing mode, each node stores the routing information of its sub-tree in its routing table. This enables efficient downward routing, but requires more memory and bandwidth.
- In non-storing mode, each node only stores the routing information of its parent. This reduces the memory and bandwidth requirements, but requires the root to maintain the global routing information and forward the downward packets.
- In source routing mode, each node stores the routing information of its parent and its children. This enables the source node to include the complete path in the packet header, which eliminates the need for routing tables and global routing information. However, this increases the packet size and overhead.