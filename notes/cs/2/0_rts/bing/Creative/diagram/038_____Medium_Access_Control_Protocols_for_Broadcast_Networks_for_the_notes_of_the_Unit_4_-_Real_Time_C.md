### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols are mechanisms that allow several users or transmitters to access a common medium or channel, such as a wireless network or a shared bus .
- MAC protocols play an important role in the development of both wired and wireless networks, as they determine how the network resources are allocated and utilized .
- MAC protocols can be classified into two main categories: random access and scheduled access .
  - Random access protocols allow users to transmit whenever they have data to send, without any coordination or reservation. However, they may cause collisions or interference among concurrent transmissions, which reduces the network performance and reliability .
  - Scheduled access protocols require users to follow some rules or agreements to access the medium, such as time division, frequency division, code division, or spatial division. They can avoid collisions and improve the network efficiency, but they may incur some overhead or delay for synchronization or reservation .
- MAC protocols can also be designed for different network scenarios, such as unicast, multicast, or broadcast .
  - Unicast protocols are used for point-to-point communication between a sender and a receiver, such as TCP/IP or Ethernet .
  - Multicast protocols are used for group communication among a sender and multiple receivers, such as IP multicast or wireless sensor networks .
  - Broadcast protocols are used for one-to-many communication from a sender to all other nodes in the network, such as radio or TV broadcasting or emergency warning systems .
- Broadcast MAC protocols face some unique challenges, such as how to ensure the reliability and timeliness of the broadcast messages, how to cope with the dynamic and heterogeneous network conditions, and how to minimize the energy consumption and bandwidth usage .
- Some examples of broadcast MAC protocols are:
  - ABROAD, an adaptive MAC protocol that adjusts the transmission rate and power according to the channel quality and network density, and uses a feedback mechanism to detect and recover from packet losses .
  - B-MAC, a low-power MAC protocol that uses preamble sampling and clear channel assessment to reduce the idle listening and collision overhead, and supports broadcast and unicast transmissions .
  - RAP, a real-time MAC protocol that assigns priorities to broadcast messages based on their deadlines and importance, and uses a reservation scheme to guarantee the delivery of high-priority messages .

: Medium access control - an overview | ScienceDirect Topics
: Medium access control (Chapter 3) - Fundamentals of Mobile Data Networks
: Medium Access Control - Medium access control | Coursera
: An adaptive medium access control (MAC) protocol for reliable broadcast in wireless networks
: B-MAC: Versatile Low Power Media Access for Wireless Sensor Networks
: RAP: A Real-Time Communication Architecture for Large-Scale Wireless Sensor Networks