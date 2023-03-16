# 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol stack that combines the industrial performance of TSCH with the Internet integration of IPv6.
- It is intended to provide reliable and delay bounded communication in multi-hop and scalable Industrial Internet of Things (IIoT) networks.
- It is a working group at the IETF that is standardizing the 6TiSCH architecture and protocol suite.

## TSCH
- TSCH is a link layer protocol that allows the nodes to change their physical channel after each transmission to eliminate the effects of interference and multipath fading.
- TSCH uses a Time Division Multiple Access (TDMA) schedule that defines when and on which channel a node can transmit or receive.
- TSCH can achieve high reliability, low power consumption, and deterministic latency by avoiding collisions and minimizing idle listening.

## 6TiSCH Architecture
- The 6TiSCH architecture consists of the following components:
  - The IEEE 802.15.4 PHY and MAC layers that provide the physical and link layer services.
  - The 6TiSCH Operation Sublayer (6top) that manages the TSCH schedule and provides an interface between the MAC and the network layer.
  - The 6top Protocol (6P) that enables the nodes to negotiate the TSCH schedule with their neighbors.
  - The 6LoWPAN adaptation layer that compresses the IPv6 headers and fragments the packets to fit the MAC frame size.
  - The IPv6 layer that provides the network layer services and assigns a global address to each node.
  - The IP-in-IP encapsulation that allows the nodes to tunnel the IPv6 packets over the TSCH network.
  - The Routing Protocol for Low-Power and Lossy Networks (RPL) that builds a routing topology and selects the best paths for the IPv6 packets.

## 6TiSCH Benefits
- Some of the benefits of 6TiSCH are :
  - It enables the seamless integration of the IIoT devices with the Internet and the cloud services.
  - It supports a large number of devices with a single IPv6 subnet and a global address space.
  - It provides high reliability, low power consumption, and deterministic latency for the IIoT applications.
  - It allows the dynamic adaptation of the TSCH schedule to the network conditions and the application requirements.
  - It leverages the existing standards and protocols for the IIoT communication.