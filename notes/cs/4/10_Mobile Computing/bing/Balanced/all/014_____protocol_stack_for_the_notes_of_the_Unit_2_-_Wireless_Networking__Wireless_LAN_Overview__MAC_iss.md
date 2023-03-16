# Protocol Stack for Wireless Networking

- A protocol stack is an implementation of a set of communication protocols that work together to provide network functionality.
- A protocol stack consists of different layers, each of which performs a specific function and interacts with the adjacent layers through well-defined interfaces.
- A protocol stack for wireless networking aims to hide the complexity of the wireless interface and present a software interface that resembles that of a wired connection.
- However, some differences between a wired and a wireless interface cannot be hidden, such as the steps required to find and connect to other devices, the variability of the channel quality, and the limited power and bandwidth resources.
- Therefore, a protocol stack for wireless networking needs to address some additional challenges and requirements, such as mobility management, power conservation, security, scalability, and interoperability.
- A protocol stack for wireless networking can be divided into four main layers: physical layer, data link layer, network layer, and application layer.
- The physical layer is responsible for transmitting and receiving raw bits over the wireless medium, using modulation, coding, and multiplexing techniques.
- The data link layer is responsible for providing reliable and efficient data transfer between two nodes, using framing, error control, flow control, and medium access control (MAC) techniques.
- The network layer is responsible for providing end-to-end connectivity and routing between nodes, using addressing, forwarding, and routing protocols.
- The application layer is responsible for providing specific services and functionalities to the users and applications, using various protocols and standards.

## Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth

- A wireless LAN (WLAN) is a type of wireless network that connects devices within a limited area, such as a home, office, or campus, using radio waves.
- A WLAN typically consists of one or more access points (APs) that provide wireless connectivity to a wired network, and one or more wireless stations (STAs) that communicate with the APs or with each other.
- A WLAN operates in a shared and unlicensed spectrum, which means that multiple devices can access the same channel, but also that they can interfere with each other and with other sources of noise.
- Therefore, a WLAN needs a MAC protocol that can coordinate the access to the channel and avoid or resolve collisions among the devices.
- A MAC protocol can be classified into two main categories: contention-based and contention-free.
- A contention-based MAC protocol allows any device to access the channel whenever it has data to send, but it also requires a mechanism to detect and recover from collisions, such as carrier sense multiple access with collision avoidance (CSMA/CA) or request to send/clear to send (RTS/CTS) handshake.
- A contention-free MAC protocol assigns the channel to a device for a certain period of time, either by a central controller or by a distributed algorithm, such as time division multiple access (TDMA) or frequency division multiple access (FDMA) .
- IEEE 802.11 is the most widely used standard for WLANs, which defines the physical and data link layers of the protocol stack.
- IEEE 802.11 supports multiple physical layer variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of frequency band, modulation scheme, data rate, and range.
- IEEE 802.11 also defines a MAC protocol that is based on CSMA/CA with optional RTS/CTS handshake, and supports two modes of operation: infrastructure mode and ad hoc mode.
- In infrastructure mode, the STAs communicate with the APs, which act as bridges to the wired network, and the APs coordinate the channel access using a point coordination function (PCF) or a hybrid coordination function (HCF) .
- In ad hoc mode, the STAs communicate directly with each other, without the need for APs, and form a self-organized network, which can use a distributed coordination function (DCF) or an enhanced distributed channel access (EDCA) for channel access.
- Blue Tooth is another standard for wireless networking, which is designed for short-range and low-power communication among devices, such as phones, headsets, keyboards, mice, printers, and sensors