### TCP over Wireless

TCP (Transmission Control Protocol) is a widely used protocol for reliable and ordered delivery of data over the internet. However, when it comes to wireless networks, there are several MAC (Media Access Control) issues that can affect the performance of TCP. In this section, we will discuss these issues and how they can be addressed.

#### MAC Issues in Wireless Networks

- Hidden Terminal Problem: In wireless networks, nodes communicate using radio waves. When a node transmits a packet, it can be received by other nearby nodes, which can cause interference. The hidden terminal problem occurs when two nodes cannot hear each other but can hear a third node. In this case, if both nodes transmit at the same time, their packets will collide at the third node, causing a loss of data.
- Exposed Terminal Problem: In contrast to the hidden terminal problem, the exposed terminal problem occurs when a node refrains from transmitting data because it detects another transmission in progress, even though the transmission would not interfere with the ongoing transmission.
- Channel Error: Wireless channels are subject to errors due to interference, fading, and noise. These errors can cause packet loss and delay, which can affect TCP performance.

#### IEEE 802.11

IEEE 802.11 is a set of standards for wireless LAN (Local Area Network) communication. It defines the physical and MAC layer protocols for wireless networks. The following are the MAC layer protocols defined by IEEE 802.11:

- Distributed Coordinated Function (DCF): DCF is the default MAC protocol in IEEE 802.11. It uses the Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) protocol to avoid collisions.
- Point Coordination Function (PCF): PCF is an optional MAC protocol in IEEE 802.11. It uses a central coordinator to schedule transmissions, which can reduce collisions.

#### Bluetooth

Bluetooth is a wireless technology that allows devices to communicate over short distances. It uses frequency hopping spread spectrum (FHSS) to avoid interference from other wireless devices. The following are some features of Bluetooth:

- Ad-hoc networking: Devices can form ad-hoc networks without the need for a central access point.
- Low power consumption: Bluetooth devices have low power consumption, which makes them suitable for battery-operated devices.
- Limited range: Bluetooth has a limited range of about 10 meters, which makes it suitable for personal area networks.

#### TCP Performance over Wireless

TCP was designed for wired networks and assumes that packet loss is due to congestion. However, in wireless networks, packet loss can also occur due to channel errors. This can cause TCP to misinterpret packet loss and reduce its congestion window unnecessarily. Several modifications to TCP have been proposed to address this issue, including:

- Explicit Congestion Notification (ECN): ECN allows routers to notify the sender of congestion without dropping packets.
- Selective Acknowledgment (SACK): SACK allows the receiver to acknowledge individual packets, which can reduce retransmission delays.
- Forward Error Correction (FEC): FEC allows the receiver to recover lost packets by using redundant information.

In conclusion, TCP over wireless networks can be affected by MAC issues such as the hidden terminal problem, exposed terminal problem, and channel errors. IEEE 802.11 and Bluetooth are two wireless technologies that use different MAC protocols. To improve TCP performance over wireless, modifications such as ECN, SACK, and FEC have been proposed.