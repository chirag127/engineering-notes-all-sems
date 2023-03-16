# Protocol Stack for Wireless Networking

- A protocol stack is an implementation of a computer networking protocol suite or protocol family that defines the rules and formats for data communication between devices.
- A protocol stack consists of different layers, each of which performs a specific function and interacts with the adjacent layers through well-defined interfaces.
- A protocol stack for wireless networking is designed to handle the challenges and requirements of wireless communication, such as mobility, security, scalability, reliability, and energy efficiency.
- A protocol stack for wireless networking may differ from a protocol stack for wired networking in some aspects, such as the physical layer, the medium access control (MAC) layer, and the network layer.
- The physical layer is responsible for transmitting and receiving bits over the wireless medium, such as radio waves, infrared, or optical signals. The physical layer may use different modulation, coding, and multiplexing techniques to achieve higher data rates, lower error rates, and better spectrum utilization.
- The MAC layer is responsible for coordinating the access to the shared wireless medium among multiple devices, such as stations, access points, or routers. The MAC layer may use different protocols, such as carrier sense multiple access with collision avoidance (CSMA/CA), time division multiple access (TDMA), or frequency division multiple access (FDMA), to avoid or resolve collisions, improve throughput, and reduce latency.
- The network layer is responsible for routing packets from the source to the destination across multiple hops or networks, such as the internet, cellular networks, or ad hoc networks. The network layer may use different protocols, such as internet protocol (IP), mobile IP, ad hoc on-demand distance vector (AODV), or dynamic source routing (DSR), to handle mobility, address allocation, route discovery, and route maintenance.

## Wireless LAN Overview

- A wireless LAN (WLAN) is a type of wireless network that connects devices within a limited area, such as a home, office, or campus, using radio waves or infrared signals.
- A WLAN typically consists of one or more access points (APs) that provide wireless connectivity to a wired network, such as the internet, and one or more stations (STAs) that communicate with the APs or with each other.
- A WLAN may operate in two modes: infrastructure mode or ad hoc mode.
- In infrastructure mode, the STAs communicate with the APs, which act as bridges between the wireless and wired networks. The APs also coordinate the access to the wireless medium among the STAs using a MAC protocol, such as CSMA/CA.
- In ad hoc mode, the STAs communicate directly with each other without the need for an AP. The STAs form a self-organizing and self-configuring network, called an ad hoc network, and use a MAC protocol, such as TDMA, or a network protocol, such as AODV, to coordinate the access to the wireless medium and to route packets among themselves.

## MAC Issues

- The MAC layer of a WLAN faces several issues that are specific to wireless communication, such as hidden terminal problem, exposed terminal problem, fading, interference, and security.
- The hidden terminal problem occurs when two STAs that are out of the range of each other try to transmit to a common AP or STA at the same time, causing a collision at the receiver. This problem can be solved by using a handshake mechanism, such as request to send/clear to send (RTS/CTS), that allows the sender and the receiver to reserve the wireless medium before transmitting data.
- The exposed terminal problem occurs when a STA that is in the range of another STA but not in the range of its intended receiver refrains from transmitting because it senses the wireless medium to be busy, even though its transmission would not cause a collision at the receiver. This problem can be solved by using a busy tone mechanism, such as multiple access with collision avoidance (MACA), that allows the sender to notify its neighbors that it is transmitting data and that they can transmit as well.
- Fading is the variation of the signal strength over time and space due to the effects of reflection, refraction, diffraction, scattering, and absorption of the wireless signals by the environment. Fading can cause errors, delays, and losses in the wireless communication. Fading can be mitigated by using techniques such as diversity, adaptive