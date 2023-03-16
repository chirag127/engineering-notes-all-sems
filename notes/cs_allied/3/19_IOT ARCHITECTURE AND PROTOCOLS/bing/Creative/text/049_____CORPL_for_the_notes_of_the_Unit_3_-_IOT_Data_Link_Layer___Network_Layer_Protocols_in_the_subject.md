### CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow-Power and Lossy Networks.
- It is a network layer protocol that is designed for IoT applications that require reliable and energy-efficient data delivery.
- It is based on the RPL protocol, which is the standard routing protocol for low-power and lossy networks (LLNs) defined by the IETF .
- CORPL differs from RPL in the following aspects:
  - It uses a **control objective function (COF)** to select the best parent node for each device, instead of using a single objective function (OF) for the whole network.
  - It supports **multiple COFs** for different types of traffic, such as periodic, event-driven, or query-based, and allows devices to switch between them dynamically.
  - It introduces a **routing table compression (RTC)** mechanism to reduce the overhead of storing and updating routing information.
  - It employs a **cross-layer design** that integrates the network layer and the MAC layer to optimize the performance of the protocol.
- CORPL has been shown to achieve better performance than RPL in terms of packet delivery ratio, end-to-end delay, energy consumption, and network lifetime.