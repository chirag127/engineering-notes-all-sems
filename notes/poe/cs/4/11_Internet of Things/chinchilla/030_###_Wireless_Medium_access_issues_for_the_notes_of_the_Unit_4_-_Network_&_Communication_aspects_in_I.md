### Wireless Medium Access Issues for the Notes of Unit 4 - Network & Communication Aspects in IoT in the Subject of Internet of Things

In IoT networks, wireless medium access plays a crucial role in determining the overall performance of the network. Due to the limited bandwidth and high interference in wireless channels, it is important to implement efficient medium access control (MAC) protocols. In this section, we will discuss some of the major wireless medium access issues in IoT networks.

#### 1. Hidden Terminal Problem
The hidden terminal problem occurs when two nodes are out of range of each other but are within range of a third node. In this case, the two nodes cannot directly communicate with each other, but they may transmit at the same time, causing interference at the third node. To solve this problem, protocols such as carrier sense multiple access with collision avoidance (CSMA/CA) are used, which requires nodes to sense the channel before transmitting.

#### 2. Exposed Terminal Problem
The exposed terminal problem occurs when a node refrains from transmitting due to interference from a node that is not within range of the intended receiver. This can cause unnecessary delays and reduce network efficiency. To solve this problem, protocols such as request to send/clear to send (RTS/CTS) are used, which allow nodes to request permission from the receiver to transmit.

#### 3. Channel Congestion
In densely populated IoT networks, multiple nodes may attempt to access the channel simultaneously, causing congestion and collisions. This can result in significant delays and reduced throughput. To mitigate this problem, protocols such as time division multiple access (TDMA) and frequency division multiple access (FDMA) are used, which divide the channel into time or frequency slots, respectively.

#### 4. Quality of Service (QoS)
IoT networks often require different levels of QoS for different applications. For example, real-time applications such as video streaming require low latency and high bandwidth, while non-real-time applications such as sensor data transmission may tolerate higher latency and lower bandwidth. To support different QoS requirements, protocols such as the IEEE 802.11e standard have been developed, which provide different levels of service through prioritization and traffic scheduling.

#### 5. Energy Efficiency
In IoT networks, many devices are battery-powered and have limited energy resources. Therefore, it is important to design MAC protocols that minimize energy consumption while maintaining network performance. Protocols such as the IEEE 802.11ah standard have been developed for low-power IoT devices, which use a combination of TDMA and power-saving mechanisms to reduce energy consumption.

Mnemonics and Learning Tricks:
- For the Hidden Terminal Problem, remember "CSMA/CA: Check Before You Transmit" to remind you to sense the channel before transmitting to avoid interference.
- For the Exposed Terminal Problem, remember "RTS/CTS: Request To Send, Clear To Send" to remind you that nodes should request permission from the receiver before transmitting to avoid unnecessary delays.
- For Channel Congestion, remember "TDMA: Time Division, FDMA: Frequency Division" to recall the different protocols that divide the channel to reduce congestion.
- For QoS, remember "802.11e: Eight Quality Services" to remind you of the IEEE standard that provides different levels of service through prioritization and traffic scheduling.
- For Energy Efficiency, remember "802.11ah: Always on, Always Hungry" to remind you that low-power IoT devices need to conserve energy while maintaining network performance.