# CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow-Power and Lossy Networks.
- It is a network layer protocol that is designed for IoT applications that require reliable and energy-efficient data delivery.
- It is based on the RPL protocol, which is the standard routing protocol for low-power and lossy networks (LLNs) defined by the IETF .
- CORPL differs from RPL in the following aspects:
  - It uses a **control objective function (COF)** to select the best routes based on multiple metrics, such as hop count, link quality, energy consumption, and delay.
  - It employs a **dynamic parent set (DPS)** mechanism to maintain multiple backup parents for each node, which increases the network resilience and load balancing.
  - It adopts a **cross-layer feedback (CLF)** scheme to monitor the link quality and energy status of each node, which enables the COF to adapt to the network dynamics and optimize the routing performance.
- CORPL has been shown to outperform RPL in terms of packet delivery ratio, end-to-end delay, energy consumption, and network lifetime in various simulation scenarios.