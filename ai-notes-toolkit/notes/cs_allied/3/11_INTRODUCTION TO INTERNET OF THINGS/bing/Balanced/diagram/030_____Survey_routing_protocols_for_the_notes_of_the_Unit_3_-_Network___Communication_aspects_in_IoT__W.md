### Survey routing protocols for IoT

- Routing protocols are responsible for finding and maintaining routes between nodes in a network, such as sensors, actuators, gateways, and servers in IoT.
- Routing protocols for IoT must consider the characteristics and requirements of IoT devices, such as low power, low bandwidth, high mobility, and heterogeneity.
- Routing protocols for IoT can be classified into three categories: flat, hierarchical, and geographic.
  - Flat routing protocols treat all nodes equally and use flooding or gossiping techniques to disseminate information. Examples are AODV, DSR, and OLSR.
  - Hierarchical routing protocols divide the network into clusters and assign different roles to nodes based on their energy or functionality. Examples are LEACH, PEGASIS, and HEED.
  - Geographic routing protocols use the location information of nodes to make routing decisions. Examples are GPSR, GEAR, and GAF.
- Routing protocols for IoT must also address the challenges and issues of IoT, such as scalability, security, mobility, and interoperability.
  - Scalability refers to the ability of a routing protocol to handle a large number of nodes and data in IoT.
  - Security refers to the protection of data and nodes from malicious attacks and unauthorized access in IoT.
  - Mobility refers to the movement of nodes and their impact on routing performance and stability in IoT.
  - Interoperability refers to the compatibility and cooperation of different protocols and standards in IoT.
- Some of the existing and emerging routing protocols for IoT are:
  - RPL: Routing Protocol for Low-Power and Lossy Networks, standardized by IETF, designed for static IoT devices, uses a Directed Acyclic Graph (DAG) structure to route packets, supports IPv6 addressing and header compression.
  - CoAP: Constrained Application Protocol, standardized by IETF, designed for resource-constrained IoT devices, uses a RESTful architecture to enable web services, supports UDP and DTLS transport protocols.
  - MQTT: Message Queuing Telemetry Transport, an open-source protocol, designed for publish-subscribe messaging in IoT, uses a broker to facilitate communication between publishers and subscribers, supports TCP and SSL/TLS transport protocols.
  - 6LoWPAN: IPv6 over Low-Power Wireless Personal Area Networks, standardized by IETF, designed to enable IPv6 connectivity for low-power wireless devices, uses header compression and fragmentation to reduce packet size and overhead.
  - ZigBee: a wireless technology based on IEEE 802.15.4 standard, designed for low-cost, low-power, and low-data-rate IoT applications, uses a star, tree, or mesh topology to form a network, supports AES encryption and key management for security.