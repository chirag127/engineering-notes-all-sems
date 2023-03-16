# RPL for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- RPL stands for Routing Protocol for Low-Power and Lossy Networks (LLNs).
- LLNs are networks that consist of resource-constrained devices (such as sensors, actuators, smart meters, etc.) that communicate over unreliable and low-bandwidth links (such as wireless, power-line, etc.).
- RPL is designed to enable scalable, efficient, and reliable routing in LLNs, which are often used for Internet of Things (IoT) applications.
- RPL is based on the concept of a Destination Oriented Directed Acyclic Graph (DODAG), which is a tree-like structure that defines the routing paths from the nodes to a common destination (such as a gateway or a sink).
- RPL uses a metric called rank to determine the position of a node in the DODAG. The rank is a function of the node's distance to the destination and other parameters (such as energy, hop count, link quality, etc.).
- RPL operates in two modes: storing mode and non-storing mode. In storing mode, each node maintains a routing table that contains the next hop information for all the destinations in the DODAG. In non-storing mode, only the root node maintains a routing table, and the other nodes forward the packets based on the source routing information carried in the packets.
- RPL uses three types of control messages to construct and maintain the DODAG: DODAG Information Object (DIO), Destination Advertisement Object (DAO), and DODAG Information Solicitation (DIS).
- DIO messages are used to advertise the DODAG configuration and the rank of the sender. DAO messages are used to propagate the destination information from the nodes to the root. DIS messages are used to request DIO messages from the neighbors.
- RPL supports multiple DODAGs within the same network, each with a different objective function (OF) that defines how the rank is calculated. RPL also supports multiple instances of the same DODAG with different configurations.
- RPL provides mechanisms for loop detection and avoidance, local repair, global repair, and mobility support.
- RPL faces several security challenges, such as rank attacks, version number (VN) attacks, DAO inconsistency attacks, DIO suppression attacks, sinkhole attacks, wormhole attacks, etc.
- RPL security can be enhanced by using cryptographic techniques (such as digital signatures, message authentication codes, encryption, etc.), trust management schemes, anomaly detection methods, secure routing metrics, etc.