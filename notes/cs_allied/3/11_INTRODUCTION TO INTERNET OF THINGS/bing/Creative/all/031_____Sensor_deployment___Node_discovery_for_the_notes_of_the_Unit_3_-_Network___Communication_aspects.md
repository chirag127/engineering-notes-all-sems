# Sensor deployment & Node discovery

Sensor deployment and node discovery are two important aspects of IoT sensing capabilities. Sensor deployment refers to the process of placing sensor nodes in the environment to monitor physical phenomena, such as temperature, humidity, light, sound, etc. Node discovery refers to the process of identifying and locating sensor nodes in the network, as well as establishing communication links among them.

## Sensor deployment

Sensor deployment can be done in various ways, depending on the application requirements, the environment characteristics, and the sensor node capabilities. Some of the common methods of sensor deployment are:

- **Random deployment**: Sensor nodes are scattered randomly in the area of interest, without any prior knowledge of the environment or the node locations. This method is suitable for large-scale and dynamic scenarios, where precise node placement is not feasible or necessary. However, random deployment may result in uneven node distribution, coverage holes, and connectivity issues.

- **Deterministic deployment**: Sensor nodes are placed in predefined locations, based on the environment layout and the application objectives. This method can ensure optimal node placement, coverage, and connectivity, but it requires more planning and coordination, and it may not be adaptable to changes in the environment or the application.

- **Self-deployment**: Sensor nodes are equipped with mobility mechanisms, such as wheels, legs, or propellers, and they can move autonomously to adjust their positions according to the environment conditions and the application goals. This method can achieve adaptive and flexible sensor deployment, but it also introduces more complexity and cost, and it may raise security and privacy concerns.

## Node discovery

Node discovery is essential for establishing and maintaining the network topology, routing, and data aggregation in IoT. Node discovery can be classified into two types:

- **Neighbor discovery**: Sensor nodes discover their immediate neighbors within their communication range, and exchange information such as node ID, location, energy level, etc. Neighbor discovery can be done periodically or on-demand, using broadcast or unicast messages, and using various protocols and algorithms.

- **Network discovery**: Sensor nodes discover the whole network structure, and learn the routes to other nodes or the gateway. Network discovery can be done proactively or reactively, using flooding or routing tables, and using various protocols and algorithms.

Some of the challenges and issues of node discovery in IoT are:

- **Scalability**: Node discovery should be able to handle large-scale and dynamic networks, where nodes may join, leave, or move frequently.

- **Energy efficiency**: Node discovery should minimize the energy consumption of sensor nodes, by reducing the communication overhead, the computation complexity, and the idle listening time.

- **Security**: Node discovery should prevent malicious attacks, such as node impersonation, node replication, node compromise, etc., by using authentication, encryption, and verification techniques.

- **Accuracy**: Node discovery should provide accurate and reliable information about the node locations, the node capabilities, and the network topology, by using localization, calibration, and synchronization techniques.