# Sensor deployment & Node discovery

Sensor deployment and node discovery are two important aspects of IoT sensing capabilities. Sensor deployment refers to the process of placing sensor nodes in the environment to monitor physical phenomena, such as temperature, humidity, light, sound, etc. Node discovery refers to the process of identifying and locating sensor nodes in the network, and establishing communication links among them.

## Sensor deployment

Sensor deployment can be done in various ways, depending on the application requirements, the environment characteristics, and the sensor node capabilities. Some of the common methods of sensor deployment are:

- **Random deployment**: Sensor nodes are scattered randomly in the area of interest, without any prior knowledge of the environment or the node locations. This method is suitable for large-scale and dynamic scenarios, where precise node placement is not feasible or necessary. However, random deployment may result in uneven node distribution, coverage holes, and connectivity issues.
- **Deterministic deployment**: Sensor nodes are placed in predefined locations, based on some optimization criteria, such as coverage, connectivity, energy efficiency, etc. This method is suitable for small-scale and static scenarios, where precise node placement is possible and desirable. However, deterministic deployment may require more planning, coordination, and resources than random deployment.
- **Hybrid deployment**: Sensor nodes are deployed in a combination of random and deterministic methods, to balance the trade-offs between them. For example, some nodes may be placed randomly to provide initial coverage and connectivity, while some nodes may be placed deterministically to enhance the network performance or reliability.

## Node discovery

Node discovery is essential for sensor nodes to form a network and exchange data. Node discovery can be done in various ways, depending on the network architecture, the communication protocol, and the node capabilities. Some of the common methods of node discovery are:

- **Broadcasting**: Sensor nodes broadcast their presence and information to their neighbors, and listen for broadcasts from other nodes. This method is simple and robust, but may cause high overhead and interference in dense networks.
- **Beaconing**: Sensor nodes periodically send beacons to announce their presence and information, and listen for beacons from other nodes. This method is more efficient and scalable than broadcasting, but may cause synchronization and latency issues in dynamic networks.
- **Querying**: Sensor nodes send queries to request information from other nodes, and reply to queries from other nodes. This method is more selective and adaptive than beaconing, but may cause more complexity and overhead in large networks.