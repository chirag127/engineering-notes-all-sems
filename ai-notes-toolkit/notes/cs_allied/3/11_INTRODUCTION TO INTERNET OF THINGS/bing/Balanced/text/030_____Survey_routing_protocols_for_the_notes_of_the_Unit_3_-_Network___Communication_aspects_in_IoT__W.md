### Survey routing protocols for IoT

- Routing protocols are essential for data communication and network management in IoT applications.
- Routing protocols for IoT must consider the characteristics and requirements of IoT devices, such as low power, limited memory, heterogeneous network, mobility, scalability, security, etc.
- Routing protocols for IoT can be classified into different categories based on different criteria, such as network topology, routing strategy, network layer, etc.
- Some of the common categories of routing protocols for IoT are:

  - Flat routing protocols: These protocols do not use any hierarchy or clustering in the network and treat all nodes equally. Examples of flat routing protocols are Flooding, Gossiping, SPIN, Directed Diffusion, etc.
  - Hierarchical routing protocols: These protocols use a hierarchical structure or clustering in the network and assign different roles and responsibilities to different nodes. Examples of hierarchical routing protocols are LEACH, PEGASIS, HEED, TEEN, etc.
  - Geographic routing protocols: These protocols use the location information of the nodes to make routing decisions and forward packets to the nodes that are closer to the destination. Examples of geographic routing protocols are GPSR, GEAR, GAF, etc.
  - Data-centric routing protocols: These protocols use the data attributes or queries to route the packets and reduce the redundant or irrelevant data transmission. Examples of data-centric routing protocols are Directed Diffusion, COUGAR, ACQUIRE, etc.
  - Multipath routing protocols: These protocols use multiple paths to route the packets and increase the reliability and fault-tolerance of the network. Examples of multipath routing protocols are AOMDV, SMR, BRA, etc.
  - QoS-aware routing protocols: These protocols consider the quality of service requirements of the applications and route the packets according to the network conditions and constraints. Examples of QoS-aware routing protocols are SAR, SPEED, MMSPEED, etc.
  - Security-aware routing protocols: These protocols consider the security issues and challenges of the IoT network and route the packets according to the security policies and mechanisms. Examples of security-aware routing protocols are SEAD, ARAN, SIA, etc.

- Some of the standard protocols and platforms for IoT are:

  - RPL: Routing Protocol for Low-Power and Lossy Networks. It is an IPv6-based protocol that uses a Destination Oriented Directed Acyclic Graph (DODAG) to route the packets in IoT networks. It supports both point-to-point and point-to-multipoint communication and provides various features such as loop avoidance, multipath support, load balancing, etc.
  - CoAP: Constrained Application Protocol. It is an application layer protocol that enables RESTful web services for IoT devices. It uses UDP as the transport layer protocol and provides various features such as caching, discovery, observation, etc.
  - MQTT: Message Queuing Telemetry Transport. It is a publish/subscribe messaging protocol that enables lightweight and reliable communication for IoT devices. It uses TCP as the transport layer protocol and provides various features such as quality of service, retain messages, last will and testament, etc.
  - 6LoWPAN: IPv6 over Low-Power Wireless Personal Area Networks. It is an adaptation layer protocol that enables the transmission of IPv6 packets over IEEE 802.15.4 networks. It provides various features such as header compression, fragmentation, reassembly, etc.
  - ZigBee: It is a wireless technology that enables low-power and low-data-rate communication for IoT devices. It uses IEEE 802.15.4 as the physical and MAC layer protocol and provides various features such as mesh networking, security, self-organization, etc.