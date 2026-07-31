# Wireless Medium Access Issues for the Notes of the Unit 4 - Network & Communication Aspects in IoT in the Subject of Internet of Things

- Wireless medium access is the process of coordinating the transmission and reception of data among multiple devices that share a common wireless channel.
- Wireless medium access is challenging in IoT because of the following issues :
  - **Interference**: IoT devices may operate in the same frequency band as other wireless technologies, such as WiFi, Bluetooth, ZigBee, etc. This may cause interference and degrade the performance of IoT devices.
  - **Energy efficiency**: IoT devices are often battery-powered and have limited energy resources. Therefore, they need to minimize their energy consumption while maintaining reliable communication.
  - **Scalability**: IoT devices may be deployed in large numbers and have diverse requirements and capabilities. Therefore, they need to adapt to the dynamic network conditions and support heterogeneous traffic types and quality of service.
  - **Mobility**: IoT devices may be mobile or attached to mobile platforms, such as drones, vehicles, robots, etc. Therefore, they need to cope with the changes in the wireless channel and the network topology.
  - **Security**: IoT devices may be vulnerable to malicious attacks, such as jamming, eavesdropping, spoofing, etc. Therefore, they need to protect their data and identity from unauthorized access and manipulation.

- Wireless medium access control (MAC) is the sublayer of the data link layer that is responsible for addressing these issues and providing efficient and reliable communication among IoT devices.
- Wireless MAC protocols can be classified into two main categories :
  - **Contention-based protocols**: These protocols allow IoT devices to compete for the wireless channel and access it probabilistically. They are simple, flexible, and scalable, but they may suffer from collisions, delays, and low throughput.
  - **Contention-free protocols**: These protocols assign the wireless channel to IoT devices deterministically, either by a central controller or by a distributed algorithm. They are efficient, reliable, and secure, but they may require synchronization, overhead, and complexity.

- Some examples of contention-based protocols are :
  - **Carrier sense multiple access (CSMA)**: This protocol requires IoT devices to sense the wireless channel before transmitting and defer their transmission if the channel is busy. It reduces collisions, but it may cause hidden and exposed terminal problems.
  - **Carrier sense multiple access with collision avoidance (CSMA/CA)**: This protocol enhances CSMA by using a handshake mechanism, such as request-to-send (RTS) and clear-to-send (CTS) frames, to reserve the wireless channel before transmitting. It solves the hidden and exposed terminal problems, but it may introduce overhead and delays.
  - **Carrier sense multiple access with collision detection (CSMA/CD)**: This protocol enhances CSMA by allowing IoT devices to detect collisions during transmission and abort their transmission if a collision occurs. It reduces the duration of collisions, but it may not be feasible in wireless environments due to the signal attenuation and propagation delay.
  - **Aloha**: This protocol allows IoT devices to transmit at any time without sensing the wireless channel. It is simple and robust, but it may cause frequent collisions and low throughput.

- Some examples of contention-free protocols are :
  - **Time division multiple access (TDMA)**: This protocol divides the wireless channel into time slots and assigns each slot to a specific IoT device. It avoids collisions, but it may require synchronization and waste bandwidth if the traffic is bursty or variable.
  - **Frequency division multiple access (FDMA)**: This protocol divides the wireless channel into frequency bands and assigns each band to a specific IoT device. It avoids collisions, but it may require frequency planning and waste bandwidth if the traffic is low or sporadic.
  - **Code division multiple access (CDMA)**: This protocol assigns a unique code to each IoT device and allows them to transmit simultaneously using the same frequency band. It avoids collisions, but it may require complex encoding and decoding and suffer from interference if the codes are not orthogonal.
  - **Orthogonal frequency division multiple access (OFDMA)**: This protocol combines FDMA and CDMA and assigns a subset of orthogonal subcarriers to each IoT device. It avoids collisions, but it may require complex modulation and demodulation and suffer from inter-carrier interference if the channel is not flat.

- Some examples of hybrid protocols that combine contention-based and contention-free protocols are :
  - **