# Unit 3 - Network & Communication aspects in IoT

## Wireless Medium access issues

- Wireless medium access issues refer to the challenges of sharing the wireless channel among multiple IoT devices that may have different communication requirements and constraints.
- Some of the issues are:
  - Interference: The wireless channel is prone to interference from other devices, environmental factors, and multipath fading, which can degrade the signal quality and cause packet loss.
  - Bandwidth: The wireless channel has limited bandwidth, which may not be sufficient to support the data rate and latency requirements of some IoT applications.
  - Energy: The wireless transmission and reception consume a significant amount of energy, which can deplete the battery of IoT devices quickly.
  - Scalability: The wireless channel may not be able to accommodate the increasing number of IoT devices and their traffic demands, leading to congestion and collisions.
  - Security: The wireless channel is vulnerable to eavesdropping, jamming, spoofing, and other malicious attacks, which can compromise the confidentiality, integrity, and availability of IoT data and services.

## MAC protocol survey

- MAC protocol stands for medium access control protocol, which is a set of rules that govern how IoT devices access and share the wireless channel.
- The main objective of MAC protocol is to coordinate the transmission and reception of packets among IoT devices, while minimizing interference, collisions, energy consumption, and latency.
- There are different types of MAC protocols for IoT, such as:
  - Contention-based: These protocols allow IoT devices to compete for the channel access, using mechanisms such as random backoff, carrier sensing, and acknowledgments. Examples are CSMA/CA, ALOHA, and Slotted ALOHA.
  - Reservation-based: These protocols allocate the channel access to IoT devices in advance, using mechanisms such as time division multiple access (TDMA), frequency division multiple access (FDMA), and code division multiple access (CDMA). Examples are LEACH, SMAC, and TRAMA.
  - Hybrid: These protocols combine the features of contention-based and reservation-based protocols, using mechanisms such as polling, token passing, and adaptive TDMA. Examples are ZMAC, BMA, and RICER.

## Survey routing protocols

- Routing protocol is a set of rules that determine how IoT devices forward packets to their destinations, using the available paths in the network.
- The main objective of routing protocol is to find the optimal routes for IoT packets, while maximizing network performance, reliability, and lifetime.
- There are different types of routing protocols for IoT, such as:
  - Proactive: These protocols maintain the routing information for all destinations in the network, using periodic updates and exchanges. Examples are DSDV, OLSR, and RIP.
  - Reactive: These protocols discover the routing information on demand, using route request and reply messages. Examples are AODV, DSR, and RPL.
  - Hybrid: These protocols combine the features of proactive and reactive protocols, using hierarchical or zone-based structures. Examples are ZRP, CBRP, and EIGRP.

## Sensor deployment & Node discovery

- Sensor deployment is the process of placing and configuring the IoT devices in the network, according to the application requirements and environmental conditions.
- The main objective of sensor deployment is to ensure the coverage, connectivity, and functionality of the IoT network, while minimizing the cost and complexity.
- There are different methods of sensor deployment, such as:
  - Deterministic: These methods follow a predefined pattern or plan for sensor placement, such as grid, hexagonal, or triangular. Examples are Grid Deployment, Hexagonal Deployment, and Triangular Deployment.
  - Random: These methods rely on random or probabilistic sensor placement, such as uniform, Gaussian, or Poisson. Examples are Uniform Deployment, Gaussian Deployment, and Poisson Deployment.
  - Adaptive: These methods adjust the sensor placement dynamically, based on the feedback or learning from the network. Examples are Mobile Deployment, Self-Deployment, and Reinforcement Learning Deployment.

- Node discovery is the process of identifying and locating the IoT devices in the network, using their unique identifiers and attributes.
- The main objective of node discovery is to enable the communication and cooperation among IoT devices, while reducing the overhead and latency.
- There are different techniques of node