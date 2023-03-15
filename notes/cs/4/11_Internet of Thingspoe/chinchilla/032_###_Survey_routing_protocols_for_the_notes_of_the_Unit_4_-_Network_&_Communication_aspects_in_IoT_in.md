### Survey Routing Protocols for the Notes of the Unit 4 - Network & Communication Aspects in IoT in the Subject of Internet of Things

Routing protocols are essential for IoT networks to enable efficient data transmission between devices. Survey routing protocols refer to the process of selecting the best route for data transmission from a source device to a destination device. The following are some commonly used survey routing protocols in IoT networks:

1. RPL (IPv6 Routing Protocol for Low-power and Lossy Networks): RPL is a widely used routing protocol for IoT networks. It is designed specifically for low-power and lossy networks, making it suitable for IoT devices that have limited resources. RPL is based on the Distance Vector Routing Protocol (DVRP) and uses a Destination Oriented Directed Acyclic Graph (DODAG) to select the best route for data transmission.

2. AODV (Ad-hoc On-Demand Distance Vector): AODV is a reactive routing protocol that is commonly used in wireless ad-hoc networks. It is suitable for IoT networks that have dynamic topologies, where devices may join or leave the network frequently. AODV uses a route discovery process to find the best route between a source and a destination device.

3. DSDV (Destination-Sequenced Distance Vector): DSDV is a proactive routing protocol that is suitable for IoT networks that have a static topology. It uses a table-based approach to maintain a consistent view of the network topology and to select the best route for data transmission. DSDV is based on the Bellman-Ford algorithm and uses sequence numbers to avoid routing loops.

4. OLSR (Optimized Link State Routing): OLSR is a proactive routing protocol that is suitable for IoT networks with high mobility. It uses a table-based approach to maintain a consistent view of the network topology and to select the best route for data transmission. OLSR uses a Multi-Point Relays (MPR) mechanism to reduce the overhead of flooding routing information in the network.

5. PEGASIS (Power-Efficient Gathering in Sensor Information Systems): PEGASIS is a hierarchical routing protocol that is suitable for IoT networks with a large number of sensor nodes. It uses a chain-based approach to transmit data from one node to another until it reaches the sink node. PEGASIS reduces the energy consumption of sensor nodes by minimizing the distance they need to transmit data.

Mnemonics and learning tricks:
- To remember the characteristics of RPL, think of it as "Rapid and Power-saving Low-power" protocol.
- To remember the characteristics of AODV, think of it as "Ad-hoc On-Demand" protocol that discovers the best route dynamically.
- To remember the characteristics of DSDV, think of it as a "Destination-Sequenced" protocol that maintains a static view of the network topology.
- To remember the characteristics of OLSR, think of it as "Optimized Link State Routing" protocol that is suitable for highly mobile networks.
- To remember the characteristics of PEGASIS, think of it as "Power-Efficient Gathering in Sensor Information Systems" protocol that reduces energy consumption by using a chain-based approach.

In conclusion, survey routing protocols are essential for IoT networks to ensure efficient data transmission between devices. The selection of the appropriate routing protocol depends on the specific requirements of the IoT network, such as the network topology, device resources, and mobility. Understanding the characteristics and functionality of different routing protocols can help in selecting the best protocol for a given IoT network.