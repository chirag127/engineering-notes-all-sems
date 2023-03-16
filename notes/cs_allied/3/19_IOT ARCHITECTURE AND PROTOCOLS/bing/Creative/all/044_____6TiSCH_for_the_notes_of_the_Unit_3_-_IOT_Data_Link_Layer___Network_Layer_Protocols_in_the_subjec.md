# 6TiSCH

- 6TiSCH stands for IPv6 over the Time Slotted Channel Hopping (TSCH) mode of IEEE 802.15.4e.
- It is a protocol stack that combines the industrial performance of TSCH with the seamless integration of IPv6 for the Industrial Internet of Things (IIoT).
- It enables reliable and delay-bounded communication in multi-hop and scalable networks of low-power and lossy devices.
- It consists of several components, such as:
  - The IEEE 802.15.4e TSCH link layer protocol, which provides time synchronization, channel hopping, and medium access control.
  - The 6TiSCH Operation Sublayer (6top), which provides an interface between the link layer and the network layer, and allows the nodes to dynamically allocate and manage the TSCH schedule.
  - The 6top Protocol (6P), which defines the messages and procedures for the nodes to negotiate the TSCH schedule with their neighbors.
  - The 6LoWPAN adaptation layer, which enables the compression and fragmentation of IPv6 packets over the IEEE 802.15.4 frame format.
  - The IP-in-IP encapsulation, which allows the nodes to tunnel IPv6 packets over the 6LoWPAN network.
  - The Routing Protocol for Low-Power and Lossy Networks (RPL), which provides routing and topology management for the 6TiSCH network.
- 6TiSCH is a working group at the Internet Engineering Task Force (IETF), which is standardizing the architecture and protocols for 6TiSCH networks.
- 6TiSCH is a key technology for the convergence of Operational Technology (OT) and Information Technology (IT), as it offers both industrial performance and seamless integration into the Internet.