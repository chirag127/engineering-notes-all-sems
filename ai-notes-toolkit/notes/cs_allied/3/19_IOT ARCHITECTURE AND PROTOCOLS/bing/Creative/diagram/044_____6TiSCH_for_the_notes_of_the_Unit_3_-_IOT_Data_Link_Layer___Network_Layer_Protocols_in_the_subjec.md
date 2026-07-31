### 6TiSCH

- 6TiSCH stands for IPv6 over the TSCH mode of IEEE 802.15.4e, which is a standard for low-power wireless communication in industrial Internet of Things (IIoT) networks  .
- TSCH stands for Time Slotted Channel Hopping, which is a link layer protocol that allows nodes to synchronize their clocks and hop across different frequency channels to avoid interference and improve reliability .
- 6TiSCH enables the integration of TSCH networks with IPv6, which is the latest version of the Internet Protocol that provides a large address space and end-to-end connectivity  .
- 6TiSCH defines a network architecture and a protocol suite that includes the following components :
  - 6TiSCH Operation Sublayer (6top): a sublayer between the MAC and the network layer that manages the allocation and deallocation of timeslots and channels for data transmission and reception.
  - 6top Protocol (6P): a protocol that runs on top of 6top and allows nodes to negotiate and update their schedules with their neighbors.
  - 6LoWPAN: a protocol that adapts IPv6 packets to the constraints of low-power and lossy networks, such as fragmentation, compression, and header encapsulation.
  - IP-in-IP encapsulation: a technique that allows nodes to tunnel IPv6 packets over another IPv6 network, such as a backbone router network that connects different 6TiSCH subnets.
  - RPL: a routing protocol for low-power and lossy networks that organizes nodes into a Destination Oriented Directed Acyclic Graph (DODAG) based on an objective function and a set of metrics and constraints.
- 6TiSCH aims to provide the following benefits for IIoT applications  :
  - High reliability and low latency: by using TSCH, nodes can avoid collisions and interference and meet the quality of service requirements of industrial applications.
  - Scalability and flexibility: by using IPv6, nodes can have a unique and global identifier and join or leave the network dynamically without affecting the network performance.
  - Interoperability and convergence: by using standard protocols, nodes can communicate with other devices and systems using the same or different technologies, such as Wi-Fi, Ethernet, or cellular networks.