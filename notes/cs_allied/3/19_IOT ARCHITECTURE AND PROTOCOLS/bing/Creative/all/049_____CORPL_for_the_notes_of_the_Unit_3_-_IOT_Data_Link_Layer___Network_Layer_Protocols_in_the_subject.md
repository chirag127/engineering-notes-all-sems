# CORPL for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- CORPL stands for **C**ontrol **O**bjective **R**outing **P**rotocol for **L**ow power and Lossy Networks.
- It is a network layer protocol that is designed for IoT applications that require reliable and energy-efficient data delivery in constrained environments.
- It is based on the concept of **control objectives**, which are high-level goals that the network should achieve, such as minimizing delay, maximizing throughput, or balancing load.
- CORPL uses a distributed algorithm to compute optimal routes based on the control objectives and the network state, such as link quality, traffic load, and residual energy.
- CORPL is compatible with the IPv6 Routing Protocol for Low-Power and Lossy Networks (RPL), which is the standard routing protocol for IoT networks.
- CORPL can interoperate with RPL nodes and use RPL messages to exchange routing information.
- CORPL has the following advantages over RPL:
  - It can support multiple and dynamic control objectives, while RPL can only support one static objective.
  - It can adapt to network changes faster and more accurately, while RPL may suffer from routing loops, inconsistencies, and suboptimal paths.
  - It can achieve better performance in terms of packet delivery ratio, end-to-end delay, and energy consumption, while RPL may incur more overhead and waste more resources.
- CORPL has the following limitations and challenges:
  - It requires more computation and memory than RPL, which may be an issue for resource-constrained devices.
  - It may not be compatible with some existing RPL features, such as storing mode, non-storing mode, and multicast.
  - It may need to deal with security and privacy issues, such as authentication, authorization, and confidentiality of routing information.