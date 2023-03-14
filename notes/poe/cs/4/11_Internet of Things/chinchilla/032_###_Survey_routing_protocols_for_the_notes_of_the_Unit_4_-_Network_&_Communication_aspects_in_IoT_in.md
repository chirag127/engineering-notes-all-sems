### Survey Routing Protocols for the Notes of Unit 4 - Network & Communication Aspects in IoT in the Subject of Internet of Things

Routing protocols play a crucial role in the efficient functioning of networks, including IoT networks. In IoT, routing protocols determine the path that data should take through the network, which is crucial for the successful delivery of data to its intended destination. In this article, we will survey some of the different routing protocols commonly used in IoT networks.

#### 1. RPL (Routing Protocol for Low-Power and Lossy Networks)

RPL is a widely used routing protocol in IoT networks. It is designed to work in low-power and lossy networks, where nodes have limited energy and bandwidth. RPL uses a proactive approach to routing, which means that it builds a routing table in advance and maintains it even if there is no data to be sent. This ensures that the network is always ready to send data when required. RPL also supports multipath routing, which means that it can use multiple paths to send data to the destination node.

#### 2. AODV (Ad hoc On-Demand Distance Vector)

AODV is another popular routing protocol used in IoT networks. It is designed for mobile ad hoc networks, where nodes can move around and join or leave the network at any time. AODV uses a reactive approach to routing, which means that it only builds a routing table when there is data to be sent. This saves energy and bandwidth, as nodes do not have to constantly update their routing tables. AODV also supports multicast routing, which means that it can send data to multiple nodes at the same time.

#### 3. DSR (Dynamic Source Routing)

DSR is a simple and efficient routing protocol that is commonly used in IoT networks. It is designed for mobile ad hoc networks and is based on the concept of source routing. In DSR, the source node determines the entire route that data should take through the network and includes this information in the data packet itself. This reduces the amount of overhead required for routing, as nodes do not have to maintain routing tables. DSR also supports multicast routing and can send data to multiple nodes at the same time.

#### 4. OLSR (Optimized Link State Routing)

OLSR is a proactive routing protocol that is commonly used in wireless mesh networks. It is designed to optimize the use of network resources, including bandwidth and energy. OLSR builds a complete topology of the network and uses this information to determine the most efficient paths for data to take. OLSR also supports multipath routing and can use multiple paths to send data to the destination node.

#### 5. PEGASIS (Power-Efficient Gathering in Sensor Information Systems)

PEGASIS is a hierarchical routing protocol that is commonly used in wireless sensor networks. It is designed to save energy by reducing the amount of data that nodes have to send. PEGASIS works by organizing nodes into a chain and passing data along this chain until it reaches the base station. This reduces the amount of data that has to be transmitted wirelessly, saving energy and reducing the risk of data loss.

#### Conclusion

Routing protocols are a crucial part of IoT networks, and choosing the right protocol can have a significant impact on network performance. In this article, we have surveyed some of the different routing protocols commonly used in IoT networks, including RPL, AODV, DSR, OLSR, and PEGASIS. Each protocol has its own strengths and weaknesses, and choosing the right protocol will depend on the specific requirements of the network. By understanding the different routing protocols available, network administrators can make informed decisions when designing and deploying IoT networks.