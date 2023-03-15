### Survey routing protocols for the notes of the Unit 4 - Network & Communication aspects in IoT in the subject of Internet of Things

Routing protocols are essential for efficient communication in IoT networks. These protocols determine the path taken by data packets from the source to the destination. In this section, we will survey some of the commonly used routing protocols in IoT networks.

#### 1. Routing Protocol for Low-Power and Lossy Networks (RPL)

RPL is an IPv6-based routing protocol that is specifically designed for low-power and lossy networks (LLNs) in IoT. It uses a directed acyclic graph (DAG) to represent the network topology and supports both storing and non-storing modes of operation. The protocol is highly scalable and energy-efficient, making it suitable for IoT networks with limited resources.

#### 2. Constrained Application Protocol (CoAP)

CoAP is a lightweight application-layer protocol that is designed for resource-constrained IoT devices. It uses UDP as the underlying transport protocol and supports RESTful interactions between devices. CoAP can be used with RPL to enable efficient communication in IoT networks.

#### 3. Message Queuing Telemetry Transport (MQTT)

MQTT is a publish-subscribe messaging protocol that is widely used in IoT applications. It is designed for low-bandwidth, high-latency networks and supports QoS levels to ensure reliable message delivery. MQTT can be used with CoAP and RPL to enable efficient and reliable communication in IoT networks.

#### 4. Border Gateway Protocol (BGP)

BGP is an inter-domain routing protocol that is commonly used in large-scale IoT networks. It is a path-vector protocol that uses TCP as the underlying transport protocol and supports policy-based routing. BGP can be used to enable communication between different IoT networks and to provide a scalable and flexible routing solution.

#### 5. ZigBee Routing Protocol (ZRP)

ZRP is a hybrid routing protocol that is used in ZigBee networks. It combines the advantages of both proactive and reactive routing protocols and uses a zone-based approach to reduce control overhead. ZRP can be used to enable efficient communication in IoT networks with a large number of devices.

#### Learning Tricks:

- Mnemonic: "RPMCZ" (pronounced as "R-P-M-C-Z") can be helpful in remembering the names of the five routing protocols discussed in this section.
- To remember the difference between CoAP and MQTT, think of CoAP as a protocol for accessing and manipulating resources (like a web API) and MQTT as a protocol for publishing and subscribing to messages (like a messaging system).
- To remember the difference between RPL and ZRP, think of RPL as a protocol that uses a DAG to represent the network topology and ZRP as a protocol that uses zones to reduce control overhead.