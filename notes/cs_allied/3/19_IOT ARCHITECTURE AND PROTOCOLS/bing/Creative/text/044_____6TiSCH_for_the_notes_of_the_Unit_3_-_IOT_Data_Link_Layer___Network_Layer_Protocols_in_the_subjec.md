### 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e, which is a standard for low-power wireless communication in industrial and IoT applications .
- 6TiSCH combines the benefits of TSCH, which provides reliable and deterministic communication with channel hopping and time synchronization, and IPv6, which enables seamless integration with the Internet and end-to-end addressing .
- 6TiSCH defines a network architecture and a protocol suite that includes the following components:
  - The 6TiSCH Operation Sublayer (6top), which is a logical link layer that manages the TSCH schedule and the allocation of timeslots and channels to the nodes.
  - The 6top Protocol (6P), which is a signaling protocol that allows the nodes to negotiate and update their TSCH schedule with their neighbors.
  - The 6LoWPAN adaptation layer, which enables the compression and fragmentation of IPv6 packets over the IEEE 802.15.4 frame format.
  - The IP-in-IP encapsulation, which allows the nodes to tunnel IPv6 packets over the 6LoWPAN network to reach the border router or the backbone network.
  - The Routing Protocol for Low-Power and Lossy Networks (RPL), which is a distance-vector routing protocol that establishes a Directed Acyclic Graph (DAG) topology among the nodes and provides routing metrics and policies.
- 6TiSCH is intended to provide a scalable, secure, and interoperable solution for the Industrial Internet of Things (IIoT), where the nodes need to communicate with high reliability, low latency, and low energy consumption .