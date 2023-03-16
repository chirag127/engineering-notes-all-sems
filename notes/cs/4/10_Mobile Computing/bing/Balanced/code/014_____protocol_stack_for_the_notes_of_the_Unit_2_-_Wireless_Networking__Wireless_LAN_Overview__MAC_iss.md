### Protocol Stack

A protocol stack is a set of software components that implement different communication protocols for a network. A protocol is a set of rules and procedures that define how data is exchanged between devices. A protocol stack allows different types of devices and networks to communicate with each other by providing a common interface and a standard format for data transmission.

A protocol stack typically consists of several layers, each of which performs a specific function in the communication process. The layers are arranged in a hierarchical order, from the lowest to the highest level of abstraction. The lower layers deal with the physical and data link aspects of the network, such as how to transmit and receive bits, frames, and packets. The higher layers deal with the network, transport, and application aspects of the network, such as how to route, segment, and deliver data, and how to provide services and functionalities for the end users.

A protocol stack can be implemented in hardware, software, or a combination of both. Some examples of protocol stacks are the TCP/IP stack, the OSI stack, and the Bluetooth stack.

### Wireless Networking

Wireless networking is a type of networking that uses radio waves or other wireless signals to connect devices without wires or cables. Wireless networking enables mobility, flexibility, and scalability for network users and applications. Wireless networking can be used for various purposes, such as personal, local, metropolitan, or global area networks, wireless sensor networks, wireless ad hoc networks, wireless mesh networks, and wireless personal area networks.

Wireless networking faces some challenges and limitations, such as interference, security, reliability, power consumption, and bandwidth. Wireless networking also requires different protocols and standards to address the specific characteristics and requirements of wireless communication.

### Wireless LAN Overview

A wireless LAN (WLAN) is a type of wireless network that connects devices within a limited area, such as a home, office, campus, or hotspot. A WLAN typically uses the IEEE 802.11 standard, which defines the physical and data link layers of the protocol stack for wireless LANs. The IEEE 802.11 standard has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of frequency, modulation, data rate, range, and compatibility.

A WLAN consists of two main components: a wireless access point (AP) and a wireless station (STA). An AP is a device that acts as a central hub for the WLAN, providing wireless connectivity and network services to the STAs. A STA is a device that connects to the AP wirelessly, such as a laptop, smartphone, tablet, or printer. A STA can also act as an AP, creating a peer-to-peer or ad hoc network with other STAs.

A WLAN operates in two modes: infrastructure mode and ad hoc mode. In infrastructure mode, the STAs communicate with the AP, which is connected to a wired network or the Internet. In ad hoc mode, the STAs communicate directly with each other, without the need for an AP or a wired network.

### MAC Issues

The medium access control (MAC) layer is the sublayer of the data link layer that controls how devices access and share the wireless medium. The MAC layer is responsible for coordinating the transmission and reception of frames, avoiding and resolving collisions, managing the channel access, and ensuring the reliability and efficiency of the wireless communication.

The MAC layer faces some issues and challenges in wireless networks, such as:

- Hidden terminal problem: This occurs when two STAs that are out of range of each other try to transmit to the same AP at the same time, causing a collision at the AP. The STAs are unaware of each other's transmission, hence they are hidden terminals.
- Exposed terminal problem: This occurs when a STA that is in range of two APs refrains from transmitting to one AP because it hears another STA transmitting to the other AP, even though the two transmissions do not interfere with each other. The STA is unnecessarily exposed to the other STA's transmission, hence it is an exposed terminal.
- Near-far problem: This occurs when a STA that is close to the AP transmits at a high power, drowning out the transmission of another STA that is far from the AP. The near STA dominates the channel access, while the far STA suffers from low signal-to-noise ratio.
- Fading problem: This occurs when the wireless signal experiences variations in amplitude, phase, or frequency due to the effects of the environment, such as reflection, refraction, diffraction, scattering, or absorption. Fading causes distortion, attenuation,