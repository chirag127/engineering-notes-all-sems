# Wireless Medium Access Issues in IoT

- Wireless medium access issues refer to the challenges and problems that arise when multiple IoT devices share the same wireless channel for data transmission and reception.
- Wireless medium access issues can affect the performance, reliability, and energy efficiency of IoT networks, especially in scenarios with high density, mobility, and interference of IoT devices.
- Some of the common wireless medium access issues in IoT are:

  - **Hidden terminal problem**: This occurs when two IoT devices that are out of each other's transmission range try to communicate with a common receiver at the same time, causing collisions and packet loss at the receiver.
  - **Exposed terminal problem**: This occurs when an IoT device that is within the transmission range of another device refrains from sending data to avoid interfering with the ongoing transmission of the other device, even though the intended receiver is not affected by the interference.
  - **Interference problem**: This occurs when IoT devices operating in the same or adjacent frequency bands cause mutual interference and degradation of signal quality, resulting in reduced throughput and increased energy consumption.
  - **Synchronization problem**: This occurs when IoT devices have different clock rates and time references, making it difficult to coordinate their transmissions and receptions, especially in duty-cycled networks where devices switch between active and sleep modes to save energy.
  - **Scalability problem**: This occurs when the number of IoT devices in a network increases beyond the capacity of the wireless channel, leading to increased contention, collisions, and delays.

- To address these wireless medium access issues, various medium access control (MAC) protocols have been proposed and developed for IoT networks. MAC protocols are responsible for coordinating and regulating the access of IoT devices to the shared wireless channel, as well as providing mechanisms for collision avoidance, interference mitigation, synchronization, and energy conservation.
- Some of the common types of MAC protocols for IoT networks are:

  - **Contention-based MAC protocols**: These protocols allow IoT devices to access the wireless channel in a random and distributed manner, without requiring a central controller or prior reservation. Examples of contention-based MAC protocols are Carrier Sense Multiple Access (CSMA), Aloha, and Slotted Aloha.
  - **Contention-free MAC protocols**: These protocols allocate the wireless channel to IoT devices in a deterministic and centralized manner, using a controller or a reservation scheme. Examples of contention-free MAC protocols are Time Division Multiple Access (TDMA), Frequency Division Multiple Access (FDMA), and Code Division Multiple Access (CDMA).
  - **Hybrid MAC protocols**: These protocols combine the features of contention-based and contention-free MAC protocols, aiming to achieve a balance between flexibility and efficiency. Examples of hybrid MAC protocols are Reservation Aloha, Dynamic TDMA, and Polling.
  - **Cognitive MAC protocols**: These protocols enable IoT devices to sense and adapt to the wireless channel conditions, such as spectrum availability, interference level, and traffic demand. Examples of cognitive MAC protocols are Cognitive Radio MAC, WLAN Aware Cognitive MAC, and Opportunistic Spectrum Access MAC.

- The choice of MAC protocol for IoT networks depends on various factors, such as network topology, traffic pattern, application requirements, and hardware constraints. There is no single MAC protocol that can suit all IoT scenarios, and therefore, a comparative survey and analysis of different MAC protocols is necessary to evaluate their strengths and weaknesses, and to select the most appropriate one for a given IoT application.