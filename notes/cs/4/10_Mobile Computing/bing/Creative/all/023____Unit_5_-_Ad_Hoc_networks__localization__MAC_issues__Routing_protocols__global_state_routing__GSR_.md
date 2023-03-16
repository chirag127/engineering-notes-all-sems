# Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

## Ad Hoc Networks
- An ad hoc network is a temporary type of wireless local area network (LAN) that is spontaneously formed when devices connect and communicate with each other directly  .
- An ad hoc network does not require any central access point or router, but relies on the cooperation and coordination of the participating nodes  .
- An ad hoc network can be used for various purposes, such as emergency communication, military operations, sensor networks, peer-to-peer file sharing, etc  .
- An ad hoc network has some advantages, such as flexibility, scalability, mobility, and low cost  .
- An ad hoc network also has some challenges, such as limited resources, dynamic topology, security, and routing  .

## Localization
- Localization is the process of determining the physical position of a node or device in an ad hoc network.
- Localization is important for many applications and services that rely on location information, such as navigation, tracking, geocasting, etc.
- Localization can be achieved by using various techniques, such as global positioning system (GPS), radio frequency identification (RFID), ultrasound, infrared, etc.
- Localization can be classified into two categories: range-based and range-free.
- Range-based localization methods use the distance or angle measurements between nodes to estimate their positions, such as trilateration, triangulation, multilateration, etc.
- Range-free localization methods do not use distance or angle measurements, but rely on other information, such as connectivity, hop count, centroid, etc.

## MAC Issues
- MAC stands for medium access control, which is a sublayer of the data link layer that coordinates the access of multiple nodes to a shared wireless medium.
- MAC issues refer to the challenges and problems that arise in the design and implementation of MAC protocols for ad hoc networks.
- Some of the MAC issues are:

  - Hidden terminal problem: when two nodes that are out of the range of each other transmit to a common receiver at the same time, causing a collision.
  - Exposed terminal problem: when a node that is in the range of a sender and a receiver cannot transmit to another node, because it thinks that the channel is busy, causing a waste of bandwidth.
  - Fairness problem: when some nodes get more access to the channel than others, causing a degradation of performance and quality of service.
  - Energy efficiency problem: when nodes consume more power than necessary to transmit or receive data, causing a reduction of battery life and network lifetime.

- Some of the MAC protocols that are proposed for ad hoc networks are:

  - IEEE 802.11: the standard for wireless LANs, which uses a distributed coordination function (DCF) based on carrier sense multiple access with collision avoidance (CSMA/CA) and an optional point coordination function (PCF) based on polling.
  - IEEE 802.15.4: the standard for low-rate wireless personal area networks (LR-WPANs), which uses a slotted or unslotted CSMA/CA and an optional time division multiple access (TDMA) with a superframe structure.
  - IEEE 802.16: the standard for wireless metropolitan area networks (WMANs), which uses a centralized or distributed scheduling based on TDMA or orthogonal frequency division multiple access (OFDMA).
  - Bluetooth: a technology for short-range wireless communication, which uses a frequency hopping spread spectrum (FHSS) and a master-slave architecture.

## Routing Protocols
- Routing is the process of finding and maintaining paths between nodes in an ad hoc network.
- Routing protocols are the algorithms and rules that govern the routing process.
- Routing protocols can be classified into three categories: proactive, reactive, and hybrid.
- Proactive routing protocols maintain routes to all destinations at all times, regardless of the traffic demand, such as destination-sequenced distance vector (DSDV), optimized link state routing (OLSR), etc.
- Reactive routing protocols discover routes on