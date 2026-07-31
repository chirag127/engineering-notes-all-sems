

## Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks.
- Mobile computing enables users to communicate, access information, and perform tasks anytime and anywhere, without being constrained by physical location or wired connections.
- Mobile computing involves three main components: mobile devices, wireless networks, and mobile applications.
- Mobile devices are handheld or wearable computers that can perform various functions, such as voice calls, text messaging, web browsing, gaming, photography, etc.
- Wireless networks are the infrastructure that connects mobile devices to each other and to the internet, using radio waves or other electromagnetic signals.
- Mobile applications are the software programs that run on mobile devices and provide specific services or functionalities to the users.
- Some of the issues or challenges in mobile computing are:
  - Limited battery life and processing power of mobile devices
  - Security and privacy of data and communication over wireless networks
  - Quality and reliability of wireless connectivity and coverage
  - Compatibility and interoperability of different mobile devices, networks, and applications
  - User interface design and usability of mobile applications
  - Scalability and management of mobile systems and services
- Wireless telephony is the technology that enables voice communication over wireless networks, using mobile phones or other devices.
- Wireless telephony can be classified into different generations, based on the technology and standards used.
- The first generation (1G) of wireless telephony used analog signals and circuit-switched networks to provide voice-only services.
- The second generation (2G) of wireless telephony used digital signals and packet-switched networks to provide voice and data services.
- The cellular concept is the basic principle of wireless telephony, which divides a geographical area into smaller regions called cells, each served by a base station that communicates with the mobile devices within its range.
- The cellular concept allows multiple users to share the same frequency band, by assigning different channels to different cells, and reusing the same channels in non-adjacent cells.
- The cellular concept also enables handover, which is the process of transferring an ongoing call from one base station to another, as the mobile device moves across different cells.
- GSM (Global System for Mobile Communication) is a standard developed by the European Telecommunications Standards Institute (ETSI) to describe the protocols for 2G digital cellular networks used by mobile devices such as mobile phones and tablets.
- GSM uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to divide the frequency band into multiple channels, and each channel into multiple time slots, that can be allocated to different users.
- GSM operates on four different frequency bands: 850 MHz, 900 MHz, 1800 MHz, and 1900 MHz.
- GSM provides various services, such as voice calls, text messaging, data transmission, roaming, encryption, etc.
- GSM consists of three main subsystems: the mobile station (MS), the base station subsystem (BSS), and the network and switching subsystem (NSS).
- The mobile station (MS) is the user's device that communicates with the base station over the air interface.
- The base station subsystem (BSS) consists of the base transceiver station (BTS) and the base station controller (BSC). The BTS is the radio equipment that transmits and receives signals from the MS. The BSC is the controller that manages the BTS and the handover process.
- The network and switching subsystem (NSS) consists of the mobile switching center (MSC), the home location register (HLR), the visitor location register (VLR), the authentication center (AUC), and the equipment identity register (EIR). The MSC is the switch that connects the BSS to the public switched telephone network (PSTN) or other networks. The HLR is the database that stores the permanent information of the subscribers, such as their phone number, service profile, location, etc. The VLR is the database that stores the temporary information of the subscribers who are visiting a certain area. The AUC is the entity that verifies the identity and security of the subscribers. The EIR is the entity that checks the validity and status of the MS equipment.



### Air-interface

- The air-interface is the communication link between the two stations in mobile or wireless communication  .
- The air-interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection  .
- The air-interface defines the frequency, channel bandwidth and modulation scheme of the radio transmission .
- The air-interface is also called the access mode or the radio interface  .
- The air-interface is the wireless counterpart of the physical layer 1 in the OSI model .
- The air-interface is the interface between the mobile station and the base transceiver station in a cellular network .
- The air-interface is also called the UM interface as it is analogous to U interface of ISDN.
- The air-interface of GSM runs on a range of frequencies including 900, 1800 and 1900 MHz.
- The air-interface of GSM uses frequency division duplex (FDD) that divides the channel into several sub-bands.
- The air-interface of GSM is based on time division multiple access (TDMA) that allows multiple users to share the same frequency channel by dividing the signal into different time slots.
- The air-interface of GSM is divided into three logical channels: traffic channels, control channels and broadcast channels.
- The air-interface of GSM is the central interface of every mobile system and typically the only one to which a customer is exposed.
- The physical characteristics of the air-interface are particularly important for the quality and success of a new mobile standard.



### Channel structure

- A channel is a medium or a path that allows the transmission of signals between a transmitter and a receiver.
- In cellular systems, each cell phone communicates with its base station over two channels, one downstream and one upstream.
- Downstream channel: carries signals from the base station to the cell phone.
- Upstream channel: carries signals from the cell phone to the base station.
- Sometimes, the system uses time division duplexing (TDD), which shares one channel for up and down.
- Channel structure refers to how the channels are allocated and organized in a cellular system.
- Channel structure depends on the frequency reuse pattern, the multiple access technique, and the modulation scheme used in the system.
- Frequency reuse pattern: determines how the available frequency spectrum is divided into smaller units and assigned to different cells in a way that minimizes interference and maximizes capacity.
- Multiple access technique: determines how the channels within each cell are shared among multiple users or devices.
- Modulation scheme: determines how the information is encoded and modulated onto the carrier signal.
- Some examples of channel structure are:
  - Frequency division multiple access (FDMA): divides the frequency spectrum into narrow bands and assigns each band to one user or device per cell. Each user or device occupies a fixed frequency channel for the duration of the communication.
  - Time division multiple access (TDMA): divides the time axis into slots and assigns each slot to one user or device per cell. Each user or device occupies a fixed time slot on a fixed frequency channel for a short duration of the communication.
  - Code division multiple access (CDMA): assigns a unique code to each user or device and allows them to share the same frequency channel simultaneously. Each user or device occupies the entire frequency spectrum for the duration of the communication, but the signals are separated by the codes.
  - Orthogonal frequency division multiple access (OFDMA): divides the frequency spectrum into subcarriers and assigns each subcarrier to one user or device per cell. Each user or device occupies a variable number of subcarriers depending on the data rate and channel conditions.



### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile users in a wireless cellular network.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is the process of notifying the network about the current location of a mobile user, usually initiated by the mobile user when it moves across a predefined boundary (such as a cell or a registration area).
- Location lookup is the process of finding the current location of a mobile user, usually initiated by the network when it needs to deliver a call or a message to the mobile user.
- Paging is the process of broadcasting a message to a set of cells where the mobile user is expected to be, usually initiated by the network after performing a location lookup, to alert the mobile user about an incoming call or message.
- Location management involves two types of databases: Home Location Register (HLR) and Visitor Location Register (VLR).
- HLR is a centralized database that stores the permanent information of all mobile users in the network, such as their phone numbers, service profiles, and current location areas.
- VLR is a local database that stores the temporary information of mobile users who are currently visiting a specific service area, such as their phone numbers, service profiles, and current cells.
- HLR and VLR communicate with each other to update and query the location information of mobile users.
- HLR-VLR scheme is a hierarchical location management scheme that divides the service coverage area into registration areas (RAs), each with a VLR. Each RA covers a group of base stations (cells).
- In HLR-VLR scheme, a mobile user performs a location update when it moves from one RA to another, and informs both the HLR and the VLR about its new location.
- In HLR-VLR scheme, a location lookup is performed by querying the HLR to find the current RA of the mobile user, and then querying the VLR of that RA to find the current cell of the mobile user.
- In HLR-VLR scheme, a paging is performed by broadcasting a message to the current cell of the mobile user, as obtained from the location lookup.
- Handoff is the process of transferring an ongoing call or data session from one base station to another, without interrupting the communication, when a mobile user moves across the cell boundaries.
- Handoff can be classified into two types: hard handoff and soft handoff.
- Hard handoff is the process of breaking the connection with the old base station before establishing a connection with the new base station. Hard handoff causes a brief interruption in the communication.
- Soft handoff is the process of establishing a connection with the new base station before breaking the connection with the old base station. Soft handoff allows a smooth transition in the communication.



### Channel allocation in cellular systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- Channels are the basic units of communication resources that can carry signals between a base station and a mobile terminal.
- Channels can be divided into frequency channels, time slots, codes, or spatial beams, depending on the modulation and multiple access techniques used.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots, bandwidth, and power, while minimizing interference and maximizing quality of service .
- Channel allocation strategies can be classified into three categories :
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels, regardless of the traffic load. The channels are reused in different cells according to a frequency reuse pattern. FCA is simple and robust, but may result in inefficient utilization of channels and high blocking probability.
  - Dynamic channel allocation (DCA): Channels are not permanently assigned to cells, but are allocated on demand according to the traffic load and the interference situation. DCA can adapt to traffic variations and reduce blocking probability, but requires more complex coordination and signaling among cells.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed and some are dynamic. HCA can balance the trade-off between simplicity and adaptability, but requires a careful design of the fixed and dynamic channel sets.



### CDMA

CDMA stands for Code Division Multiple Access and is a digital cellular technology used for mobile communication. CDMA is based on the spread spectrum technique, which spreads the bandwidth of data in a uniform manner for the same transmitted power. CDMA allows multiple users to share the same frequency channel by assigning each user a unique code that separates their signals from others.

#### Introduction, issues in mobile computing, overview of wireless telephony: cellular concept

- Mobile computing is the ability to use computing devices and applications without being constrained by physical location or network connection. Mobile computing involves mobile communication, mobile hardware, and mobile software.
- Some of the issues in mobile computing are:
  - Mobility: The users and devices can move across different networks and locations, which poses challenges for addressing, routing, security, and quality of service.
  - Resource constraints: The mobile devices have limited battery power, memory, processing, and bandwidth, which affects the performance and functionality of applications.
  - Heterogeneity: The mobile devices and networks can vary in terms of hardware, software, protocols, and standards, which requires interoperability and adaptation.
  - Security: The mobile devices and networks are vulnerable to attacks, eavesdropping, and data theft, which requires encryption, authentication, and access control.
  - User interface: The mobile devices have small screens, keyboards, and input methods, which affects the usability and accessibility of applications.
- Wireless telephony is the transmission of voice and data over wireless networks using radio waves. Wireless telephony includes cellular networks, cordless phones, satellite phones, and voice over IP (VoIP).
- Cellular concept is the idea of dividing a large geographic area into smaller cells, each served by a base station that communicates with mobile devices. Cellular concept enables frequency reuse, which increases the capacity and coverage of wireless networks. Cellular concept also allows handoff, which is the process of transferring an ongoing call from one base station to another as the mobile device moves across cells.

#### GSM

- GSM stands for Global System for Mobile Communications and is a standard for 2G cellular networks. GSM uses TDMA (Time Division Multiple Access) to divide each frequency channel into eight time slots, each assigned to a different user. GSM also uses FDMA (Frequency Division Multiple Access) to divide the frequency spectrum into 124 channels, each with a bandwidth of 200 kHz.
- GSM has four main components:
  - Mobile Station (MS): The mobile device that communicates with the network, such as a phone or a tablet.
  - Base Station Subsystem (BSS): The network infrastructure that connects the mobile stations to the core network, consisting of base transceiver stations (BTS) and base station controllers (BSC).
  - Network and Switching Subsystem (NSS): The core network that performs call processing, switching, and routing, consisting of mobile switching centers (MSC), home location registers (HLR), visitor location registers (VLR), and authentication centers (AuC).
  - Operation and Support Subsystem (OSS): The network management system that monitors, controls, and maintains the network, consisting of operation and maintenance centers (OMC), network management centers (NMC), and billing centers (BC).



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of GPRS for the subject of Mobile Computing.

### GPRS

- GPRS stands for General Packet Radio Service .
- It is a packet oriented wireless data communication service for mobile communications on 2G and 3G cellular communication systems .
- It is non-voice, high speed packet switching technology intended for GSM networks .
- It enables moderately high-speed data transfers using packet-based technologies .
- It offers more data transmission options for GSM-based devices, as GSM networks at the time could only use Short Message Service (SMS), for example, to transmit a small amount of data .
- It supports data functions across cellular internet connections.

### Issues in Mobile Computing

- Mobile computing involves the use of portable devices that can access and process data over wireless networks.
- Some of the issues in mobile computing are:

  - Mobility: The ability to move freely and seamlessly across different locations and networks.
  - Connectivity: The availability and quality of wireless connections and protocols.
  - Power consumption: The limited battery life and energy efficiency of mobile devices.
  - Security: The protection of data and privacy in mobile environments.
  - Scalability: The ability to handle large numbers of mobile users and devices.
  - Heterogeneity: The diversity of mobile devices, platforms, and applications.
  - User interface: The design and usability of mobile applications and services.

### Overview of Wireless Telephony

- Wireless telephony is the transmission of voice and data over wireless networks using radio waves.
- It is also known as cellular telephony or mobile telephony.
- It enables users to make and receive phone calls from anywhere within the coverage area of the wireless network.
- It also supports other services such as SMS, MMS, email, internet access, and multimedia.

### Cellular Concept

- The cellular concept is the basic principle of wireless telephony.
- It divides a large geographical area into smaller regions called cells.
- Each cell has a base station that communicates with the mobile devices within the cell.
- The base stations are connected to a central switching system that coordinates the calls and data transfers between the cells.
- The cellular concept allows the reuse of radio frequencies among different cells, thus increasing the capacity and efficiency of the wireless network.

### GSM

- GSM stands for Global System for Mobile Communications.
- It is a standard for digital cellular telephony that operates on 2G and 3G networks.
- It is the most widely used wireless telephony system in the world, with over 5 billion subscribers.
- It supports voice and data services such as SMS, MMS, GPRS, EDGE, and HSPA.
- It uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate radio channels to mobile devices.
- It uses a SIM card to identify and authenticate the mobile device and the user.



## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs use radio waves or infrared signals to transmit and receive data over the air.
- WLANs have several advantages over wired LANs, such as mobility, scalability, ease of installation, and lower cost.
- WLANs also have some challenges, such as security, interference, range, and power consumption.

### MAC issues

- MAC (Medium Access Control) is the sublayer of the data link layer that controls how devices access the shared wireless medium.
- MAC issues are the problems or challenges that arise in the MAC sublayer of WLANs, such as collision, hidden terminal, exposed terminal, and fairness.
- Collision is the situation when two or more devices transmit data at the same time, causing interference and data loss.
- Hidden terminal is the situation when two devices that are out of range of each other transmit data to a common receiver, causing collision and data loss.
- Exposed terminal is the situation when a device that is in range of two other devices refrains from transmitting data to one of them, because it hears the transmission of the other one, causing inefficiency and wasted bandwidth.
- Fairness is the issue of ensuring that all devices have equal or proportional access to the wireless medium, without being starved or dominated by others.

### IEEE 802.11

- IEEE 802.11 is the family of standards that define the specifications for WLANs, such as the MAC and PHY (Physical) layers, the frame formats, the security protocols, and the quality of service mechanisms.
- IEEE 802.11 was first published in 1997 and has been revised and amended several times to incorporate new features and technologies, such as higher data rates, wider frequency bands, multiple-input multiple-output (MIMO) antennas, and mesh networking.
- IEEE 802.11 has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that operate in different frequency bands (2.4 GHz, 5 GHz, or 6 GHz) and offer different data rates (from 1 Mbps to 9.6 Gbps).
- IEEE 802.11 also defines several modes of operation, such as infrastructure mode, ad hoc mode, and mesh mode, that determine how devices are organized and connected in a WLAN.

### Bluetooth

- Bluetooth is a wireless technology that enables short-range communication between devices, such as smartphones, laptops, headphones, speakers, keyboards, and mice.
- Bluetooth uses low-power radio waves in the 2.4 GHz band to create personal area networks (PANs) that can support up to eight devices.
- Bluetooth has several versions, such as Bluetooth 1.0, Bluetooth 2.0, Bluetooth 3.0, Bluetooth 4.0, Bluetooth 5.0, and Bluetooth 5.1, that offer different features and capabilities, such as higher data rates, lower power consumption, longer range, and improved security.
- Bluetooth also defines several profiles, such as A2DP, HFP, HID, and SPP, that specify the protocols and functions for different types of applications and services, such as audio streaming, hands-free calling, human interface devices, and serial port emulation.

### Wireless

- Wireless is a broad term that refers to any type of communication that does not use wires or cables, such as radio, infrared, microwave, satellite, cellular, and optical.
- Wireless can be classified into different categories based on the coverage area, such as WLAN, PAN, MAN (Metropolitan Area Network), WAN (Wide Area Network), and GAN (Global Area Network).
- Wireless can also be classified into different generations based on the technology and standards, such as 1G, 2G, 3G, 4G, and 5G for cellular networks, and Wi-Fi, WiMAX, and LTE for wireless broadband networks.
- Wireless has many applications and benefits, such as mobility, convenience, accessibility, and cost-effectiveness, but also some drawbacks, such as security, reliability, interference, and regulation.



### Multiple Access Protocols

- Multiple access protocols are used to coordinate the access of multiple nodes or users to a shared network channel, such as a wireless LAN or a satellite network.
- Multiple access protocols can be classified into three categories: random access, controlled access, and channelization.
- Random access protocols allow nodes to transmit data whenever they have data to send, without any coordination with other nodes. However, this may result in collisions, which degrade the network performance and require retransmission of data.
- Controlled access protocols require nodes to obtain permission from a central controller or from other nodes before transmitting data. This reduces the probability of collisions, but also introduces some delay and overhead.
- Channelization protocols divide the network channel into smaller subchannels, and assign each subchannel to a node or a group of nodes. This avoids collisions, but also reduces the channel utilization and may cause interference among subchannels.

- Some common multiple access protocols that are used in wireless networking are:

  - Carrier-sense multiple access with collision avoidance (CSMA/CA): This protocol is used in IEEE 802.11 / WiFi networks, and it uses a distributed coordination function to avoid collisions. Nodes sense the channel before transmitting data, and if the channel is busy, they defer their transmission until the channel is idle. Nodes also use a random backoff mechanism to reduce the chances of simultaneous transmissions after a busy period. Additionally, nodes use an optional handshake mechanism, where the sender sends a request to send (RTS) frame and waits for a clear to send (CTS) frame from the receiver, before sending the actual data frame. This helps to avoid the hidden node problem, where two nodes that are out of range of each other may interfere with a third node that is in range of both of them.
  - ALOHA and slotted ALOHA: These protocols are used in ALOHAnet, which is one of the first wireless networks. ALOHA allows nodes to transmit data at any time, without sensing the channel or waiting for an acknowledgment. This results in a high collision rate, which reduces the network throughput. Slotted ALOHA divides the time into equal slots, and nodes can only transmit data at the beginning of each slot. This reduces the collision rate by half, but still wastes a lot of channel capacity.
  - Code-division multiple access (CDMA): This protocol is used in cellular networks, such as 2G, 3G, and 4G. CDMA assigns a unique code to each node or user, and allows them to transmit data simultaneously on the same channel. The receiver can recover the data from a specific sender by using the corresponding code to filter out the interference from other senders. CDMA can support a large number of users on the same channel, but it requires complex encoding and decoding techniques, and it is susceptible to noise and multipath fading.
  - Orthogonal frequency-division multiple access (OFDMA): This protocol is used in 4G and 5G cellular networks, and it is an extension of orthogonal frequency-division multiplexing (OFDM). OFDM divides the channel into multiple orthogonal subcarriers, and modulates the data on each subcarrier using different modulation schemes, such as QPSK, 16-QAM, or 64-QAM. OFDMA further divides each subcarrier into multiple subchannels, and assigns each subchannel to a different user or node. This allows multiple users to share the same subcarrier, and also enables adaptive modulation and coding, where the modulation scheme and the code rate can be adjusted according to the channel conditions of each user. OFDMA can achieve high spectral efficiency and robustness against frequency-selective fading, but it requires sophisticated synchronization and equalization techniques, and it introduces a high peak-to-average power ratio (PAPR), which may cause distortion and interference.



### TCP over wireless

- Transmission Control Protocol (TCP) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and low throughput.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, variable bandwidth, and frequent handoffs.
- Several mechanisms have been proposed to improve the performance of TCP over wireless networks, such as:
  - Split-connection: The TCP connection is split into two sub-connections at the base station, one over the wired network and one over the wireless network. The base station acts as a proxy and handles the wireless losses locally, while hiding them from the end hosts. This approach maintains TCP end-to-end semantics, but requires modifications at the base station and may introduce security and scalability issues.
  - Link layer protocols: The link layer provides error recovery and retransmission mechanisms to recover from wireless losses, while suppressing the duplicate acknowledgments (ACKs) or negative acknowledgments (NACKs) from reaching the TCP sender. This approach avoids unnecessary congestion control actions by TCP, but may introduce additional delays and overhead at the link layer and may interfere with TCP's end-to-end reliability.
  - TCP-aware routing: The routing protocol selects the best path for TCP packets based on the link quality and the congestion status of the network. This approach reduces the packet losses and delays for TCP, but requires cooperation and coordination among the routers and may increase the routing complexity and overhead.
  - TCP feedback: The TCP sender receives feedback from the intermediate nodes or the receiver about the cause and location of packet losses, such as congestion or wireless errors. This approach enables TCP to adjust its sending rate and retransmission strategy accordingly, but requires modifications at the TCP sender and the intermediate nodes and may introduce additional feedback messages and overhead.



### Wireless applications

Wireless applications are the software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, etc. Wireless applications enable users to access information and services without being constrained by wires or cables. Some of the benefits of wireless applications are:

- Mobility: Users can access wireless applications from anywhere within the coverage area of the wireless network, and move freely without losing connectivity.
- Convenience: Users do not need to plug in or unplug wires or cables to use wireless applications, which reduces the hassle and complexity of using devices.
- Cost-effectiveness: Wireless applications can reduce the cost of installation and maintenance of wired networks, and also save energy and resources by eliminating the need for wires or cables.
- Reliability: Wireless applications can be more reliable than wired applications, as they are less prone to errors or failures caused by physical damage or interference of wires or cables.

Some of the examples of wireless applications are:

- Wireless Internet: Users can access the internet from their wireless devices, such as smartphones, tablets, laptops, etc., using wireless protocols, such as Wi-Fi, cellular, or satellite. Wireless internet enables users to browse the web, send and receive emails, stream videos, download files, etc., without requiring a wired connection.
- Wireless Voice: Users can make and receive voice calls from their wireless devices, such as cellular phones, using wireless technologies, such as GSM, CDMA, or VoIP. Wireless voice enables users to communicate with other users, regardless of their location or distance.
- Wireless Messaging: Users can send and receive text messages, multimedia messages, or instant messages from their wireless devices, such as cellular phones, using wireless technologies, such as SMS, MMS, or IM. Wireless messaging enables users to exchange information, such as text, images, audio, or video, with other users, in a fast and convenient way.
- Wireless Data: Users can transfer data, such as files, documents, or photos, from their wireless devices, such as smartphones, tablets, laptops, etc., to other devices, such as printers, scanners, or computers, using wireless technologies, such as Bluetooth, NFC, or Wi-Fi Direct. Wireless data enables users to share data, without requiring a physical connection or a common network.
- Wireless Location: Users can determine their location, or the location of other users or objects, from their wireless devices, such as smartphones, tablets, laptops, etc., using wireless technologies, such as GPS, Wi-Fi, or cellular. Wireless location enables users to navigate, track, or find their way, using maps, directions, or geolocation services.



### Data Broadcasting

- Data broadcasting is a group communication, where a sender sends data to receivers simultaneously .
- This is an all-to-all communication model where each sending device transmits data to all other devices in the network domain.
- Data broadcasting can be used for information dissemination in wireless networks, such as traffic information, weather updates, news, etc.
- Data broadcasting can improve the network performance by reducing the number of transmissions and saving bandwidth and energy.
- Data broadcasting can also pose some challenges, such as security issues, interference, synchronization, and scalability.

### Wireless Networking

- Wireless networking refers to a computer network that makes use of radio frequency (RF) connections between nodes in the network .
- Wireless networking is a popular solution for homes, businesses, and telecommunications networks, as it offers mobility, flexibility, and convenience.
- Wireless networking can be classified into different types, such as wireless personal area network (WPAN), wireless local area network (WLAN), wireless metropolitan area network (WMAN), and wireless wide area network (WWAN).
- Wireless networking can also face some challenges, such as security risks, signal interference, range limitations, and compatibility issues .

### Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth

- Wireless LAN (WLAN) is a type of wireless network that connects devices within a limited area, such as a home, office, or campus.
- WLAN uses a medium access control (MAC) protocol to coordinate the access of multiple devices to the shared wireless medium.
- MAC issues in WLAN include hidden terminal problem, exposed terminal problem, collision avoidance, power management, and quality of service.
- IEEE 802.11 is a family of standards that define the physical and MAC layers of WLAN.
- IEEE 802.11 specifies different variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that differ in terms of frequency, bandwidth, modulation, and data rate.
- Blue Tooth is a type of WPAN that enables short-range wireless communication between devices, such as phones, laptops, headphones, speakers, etc.
- Blue Tooth uses a frequency-hopping spread spectrum (FHSS) technique to avoid interference and enhance security.
- Blue Tooth also defines different profiles, such as headset profile, hands-free profile, advanced audio distribution profile, etc, that specify the capabilities and functionalities of different devices.



### Mobile IP

- Mobile IP (MIP) is a protocol that allows mobile devices to move from one network to another while maintaining the same permanent IP address.
- Mobile IP is based on IP and can support any media that can support IP, such as wired and wireless networks.
- Mobile IP is designed to support seamless and continuous Internet connectivity, especially for roaming between overlapping wireless systems.
- Mobile IP consists of three main components: a home agent, a foreign agent, and a mobile node.
  - A home agent is a router on the home network of the mobile node that maintains a binding table of the current location of the mobile node and forwards packets to it.
  - A foreign agent is a router on the visited network of the mobile node that provides services such as registration and packet delivery to the mobile node.
  - A mobile node is a device that can change its point of attachment to the Internet, such as a laptop or a smartphone.
- Mobile IP works as follows:
  - When a mobile node moves to a new network, it obtains a care-of address (CoA) from the foreign agent or by using DHCP.
  - The mobile node registers its CoA with its home agent through the foreign agent or directly.
  - The home agent updates its binding table with the new CoA of the mobile node and sends an acknowledgement to the mobile node.
  - When a correspondent node (CN) wants to communicate with the mobile node, it sends packets to the home address of the mobile node.
  - The home agent intercepts the packets and tunnels them to the CoA of the mobile node using IP encapsulation.
  - The foreign agent decapsulates the packets and delivers them to the mobile node.
  - The mobile node can also send packets to the CN using reverse tunneling, where the packets are encapsulated by the foreign agent and decapsulated by the home agent. This is optional and depends on the network configuration.
- Mobile IP has some advantages and disadvantages:
  - Advantages:
    - It preserves the existing IP address and routing infrastructure.
    - It supports transparent mobility and session continuity for the mobile node and the CN.
    - It is compatible with existing applications and protocols.
  - Disadvantages:
    - It introduces additional overhead and latency due to encapsulation and tunneling.
    - It may cause suboptimal routing and increased network congestion due to triangular routing.
    - It may suffer from security and scalability issues due to the reliance on the home agent.



### WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: Wireless Application Environment (WAE). This layer is of most interest to content developers because it contains among other things, device specifications, content formats, scripting languages, and protocols for content delivery and user interaction. The main components of this layer are:
    - Wireless Markup Language (WML): An XML-based markup language that defines the content and layout of web pages for wireless devices. WML is optimized for small screens, low bandwidth, and limited input capabilities.
    - Wireless Markup Language Script (WMLScript): A scripting language that allows dynamic content generation and client-side logic on wireless devices. WMLScript is similar to JavaScript, but with some differences and limitations.
    - Wireless Telephony Application (WTA): A set of extensions to WML and WMLScript that enable telephony services, such as call control, messaging, phone book, and voice mail, on wireless devices.
    - Wireless Datagram Protocol (WDP): A protocol that provides a common interface for data transport across different wireless networks, such as GSM, CDMA, and TDMA. WDP acts as an adaptation layer that maps WAP requests and responses to the specific features of the underlying network.
  - Session Layer: Wireless Session Protocol (WSP). This layer provides session management and service invocation for WAP applications. WSP supports two modes of operation: connection-oriented and connectionless. In connection-oriented mode, WSP establishes a reliable session between the client and the server, and provides features such as segmentation, reassembly, retransmission, and transaction management. In connectionless mode, WSP provides a simple datagram service that does not require a session establishment or maintenance.
  - Transaction Layer: Wireless Transaction Protocol (WTP). This layer provides a lightweight transaction-oriented service on top of WDP. WTP supports three classes of transactions: unreliable one-way, reliable one-way, and reliable two-way. WTP also provides features such as user datagram segmentation, reassembly, and retransmission, as well as optional acknowledgment and confirmation mechanisms.
  - Security Layer: Wireless Transport Layer Security (WTLS). This layer provides data integrity, privacy, and authentication for WAP communications. WTLS is based on the Transport Layer Security (TLS) protocol, but with some modifications and optimizations for wireless environments. WTLS supports various cryptographic algorithms, such as RSA, Diffie-Hellman, and Elliptic Curve, and various cipher suites, such as RC4, DES, and AES.
  - Transport Layer: Wireless Transport Protocol (WTP). This layer provides a reliable transport service on top of WDP. WTP supports features such as congestion control, flow control, and error recovery. WTP also provides optional features such as delayed acknowledgments, selective acknowledgments, and fast retransmit.

- The WAP architecture also includes some additional components, such as:
  - WAP Gateway: A server that acts as an intermediary between the wireless network and the internet. The WAP gateway performs functions such as protocol translation, content encoding and decoding, content adaptation, and caching.
  - WAP Proxy: A server that acts as a proxy for the wireless device. The WAP proxy performs functions such as content filtering, access control, and caching.
  - WAP Push: A mechanism that allows the server to initiate a WAP session and push content to the wireless device. The WAP push uses a protocol called Wireless Push Access Protocol (WPAP), which is based on WSP and WTP.
  - WAP Browser: A software application that runs on the wireless device and allows the user to access WAP content and services. The WAP browser interprets WML, WMLScript, and WTA, and communicates with the WAP gateway and the WAP server using WDP, WSP, WTP, and WTLS.

- The following diagram illustrates the WAP architecture and the protocol stack:

```
+-----------------+    +-----------------+    +-----------------+
|  WAP Server     |    |  WAP Gateway    |    |  WAP Device

```




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



### Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, and processing power.
- WAE consists of the following components :
  - Wireless Markup Language (WML): a markup language similar to HTML, but optimized for small screens and user input methods.
  - Wireless Markup Language Script (WMLScript): a scripting language similar to JavaScript, but with a smaller footprint and fewer features.
  - Wireless Telephony Application Interface (WTAI): a set of extensions that allow WAP applications to access phone-specific functions, such as dialing, messaging, and call control.
  - Wireless Datagram Protocol (WDP): a transport layer protocol that provides a common interface for WAP applications to use different wireless network technologies, such as GSM, CDMA, and GPRS.
  - Wireless Session Protocol (WSP): a session layer protocol that provides reliable and secure communication between WAP clients and servers, as well as features such as caching, cookies, and content negotiation.
  - Wireless Transaction Protocol (WTP): a transaction layer protocol that provides efficient and reliable request-response services for WAP applications, such as browsing and e-commerce.
  - Wireless Application Protocol Binary XML (WBXML): a binary representation of XML documents that reduces the size and complexity of WML and WMLScript files.
- Another example of an application environment for wireless networking is the Java 2 Platform, Micro Edition (J2ME), which is a subset of the Java platform designed for resource-constrained devices, such as mobile phones and PDAs.
- J2ME consists of the following components:
  - Connected Limited Device Configuration (CLDC): a set of core Java APIs and a virtual machine that provide the basic functionality and compatibility for J2ME applications.
  - Mobile Information Device Profile (MIDP): a set of Java APIs and a user interface framework that provide the common features and services for J2ME applications, such as networking, graphics, media, and security.
  - Optional Packages: a set of additional Java APIs that provide specific functionality and support for J2ME applications, such as Bluetooth, web services, and location-based services.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing:

- Wireless LAN (WLAN) is a network that connects devices wirelessly using radio waves. WLAN can be used for various purposes, such as internet access, file sharing, printing, gaming, and streaming. WLAN can be classified into two types: infrastructure and ad hoc. Infrastructure WLAN uses a base station, such as a router or an access point, to coordinate the communication among the devices. Ad hoc WLAN does not use a base station, but rather allows the devices to communicate directly with each other. 
- IEEE 802.11 is a set of standards that defines the technologies for WLANs. IEEE 802.11 specifies the Medium Access Control (MAC) and Physical Layer (PHY) protocols for wireless communication. The MAC layer is responsible for controlling the access to the shared wireless medium and avoiding collisions. The PHY layer is responsible for encoding, modulating, and transmitting the data over the wireless channel. IEEE 802.11 has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that differ in terms of data rates, frequency bands, modulation schemes, and channel widths.  
- Bluetooth is a wireless technology that enables short-range communication between devices, such as phones, laptops, headphones, speakers, keyboards, and mice. Bluetooth uses radio frequency (RF) waves to transmit data and voice signals. Bluetooth operates in the 2.4 GHz frequency band and can support up to eight devices in a network, called a piconet. Bluetooth also supports the creation of larger networks, called scatternets, by interconnecting multiple piconets. Bluetooth defines the entire protocol stack, from the physical layer to the application layer. Bluetooth has several versions, such as Bluetooth 1.0, Bluetooth 2.0, Bluetooth 3.0, Bluetooth 4.0, Bluetooth 5.0, and Bluetooth 6.0, that differ in terms of data rates, power consumption, security, and features. 
- Wireless multiple access protocols are the rules that govern how multiple devices can share the wireless medium without interfering with each other. Wireless multiple access protocols can be classified into two categories: contention-based and reservation-based. Contention-based protocols, such as Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA), allow the devices to contend for the channel and back off in case of a collision. Reservation-based protocols, such as Time Division Multiple Access (TDMA), Frequency Division Multiple Access (FDMA), and Code Division Multiple Access (CDMA), assign the channel to the devices based on time, frequency, or code, respectively. 
- TCP over wireless is the adaptation of the Transmission Control Protocol (TCP) to the wireless environment. TCP is a reliable and connection-oriented protocol that ensures the correct and in-order delivery of data packets over the internet. However, TCP faces some challenges in the wireless environment, such as high bit error rates, variable delays, bandwidth fluctuations, and mobility. TCP over wireless aims to overcome these challenges by using various techniques, such as selective acknowledgments, fast retransmissions, congestion control, and handoff management. 
- Wireless applications are the software programs that run on wireless devices and use wireless networks to provide various services, such as web browsing, email, messaging, social media, e-commerce, gaming, and streaming. Wireless applications can be classified into two types: native and web-based. Native applications are installed on the device and can access the device's hardware and software features. Web-based applications are accessed through a web browser and can run on any device that supports the browser. Wireless applications use various protocols and standards to communicate with the wireless networks, such as Mobile IP, Wireless Application Protocol (WAP), and Hypertext Transfer Protocol (HTTP).  




## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

- Data management issues in mobile computing refer to the challenges and problems that arise when managing data in a mobile environment, where users can access data from and to mobile devices, such as smartphones, tablets, laptops, etc.
- Some of the data management issues in mobile computing are:

  - Mobile database design: This involves designing a database that can support the needs and requirements of mobile users, such as frequent disconnections, limited bandwidth, variable network quality, location awareness, etc. Mobile database design also has to deal with the global name resolution problem, which is the difficulty of identifying and locating data items in a distributed system.
  - Security: This involves protecting the data that is stored and transmitted in a mobile environment, which is more vulnerable to attacks, theft, loss, or damage than data in a fixed location. Security measures include encryption, authentication, authorization, access control, backup, etc.
  - Data distribution and replication: This involves deciding how to distribute and replicate data among mobile devices and fixed servers, to improve data availability, reliability, and performance. Data distribution and replication also have to consider the trade-offs between data consistency and data currency, which are the degree to which the data reflects the latest updates and the degree to which the data is synchronized across different copies, respectively.
  - Data caching: This involves storing frequently accessed or recently updated data in the local memory of mobile devices, to reduce the network traffic and the response time. Data caching also has to deal with the cache coherence problem, which is the difficulty of maintaining the consistency and validity of cached data when the original data is modified or invalidated.
  - Data synchronization: This involves updating and reconciling the data that is stored and modified in different locations, such as mobile devices and fixed servers, to ensure data consistency and currency. Data synchronization also has to deal with the conflict resolution problem, which is the difficulty of resolving the discrepancies and contradictions that may arise when different users or devices update the same data item concurrently or independently.
  - Data broadcasting: This involves transmitting data from a fixed server to multiple mobile devices simultaneously, to disseminate information efficiently and effectively. Data broadcasting also has to deal with the data indexing problem, which is the difficulty of organizing and accessing the data that is broadcasted in a sequential and periodic manner.

- Data replication for mobile computers is a technique that involves creating and maintaining multiple copies of data in different locations, such as mobile devices and fixed servers, to improve data availability, reliability, and performance in a mobile environment.
- Some of the benefits of data replication for mobile computers are:

  - It reduces the network traffic and the response time, by allowing mobile users to access local copies of data instead of remote copies of data.
  - It increases the data availability and reliability, by allowing mobile users to access data even when they are disconnected from the network or when the network is unreliable.
  - It enhances the data performance, by allowing mobile users to access data that is closer to their current location or context.

- Some of the challenges of data replication for mobile computers are:

  - It increases the storage space and the memory consumption, by requiring multiple copies of data to be stored and maintained in different locations.
  - It introduces the data consistency and currency issues, by requiring multiple copies of data to be synchronized and updated when the data is modified or invalidated.
  - It complicates the data management and the query processing, by requiring the data replication policies and the data access methods to be designed and implemented.

- Adaptive clustering for mobile is a technique that involves grouping mobile devices into clusters based on their proximity, connectivity, or similarity, to facilitate data management and communication in a mobile environment.
- Some of the benefits of adaptive clustering for mobile are:

  - It reduces the network traffic and the energy consumption, by allowing mobile devices to communicate with each other within clusters instead of with distant servers or devices.
  - It increases the data availability and reliability, by allowing mobile devices to share and backup data within clusters instead of relying on fixed servers or devices.
  - It enhances the data performance and quality, by allowing mobile devices to access data that is relevant to their current location or context.

- Some of the challenges of adaptive clustering for mobile are:

  - It increases the computation and communication overhead, by requiring mobile devices to form and maintain clusters dynamically and periodically.
  - It introduces the cluster formation and maintenance issues, by requiring the cluster criteria and the cluster protocols to be defined and executed.
  - It complicates the data management and the query processing, by requiring the data distribution and replication strategies and the data access methods to



### Wireless Networks

- Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables or wires.
- Wireless networks can be classified into different types based on the coverage area, such as wireless personal area network (WPAN), wireless local area network (WLAN), wireless metropolitan area network (WMAN), and wireless wide area network (WWAN).
- Wireless networks can also be classified based on the network topology, such as infrastructure-based networks, where devices communicate through a fixed base station or access point, and ad hoc networks, where devices communicate directly with each other without a central coordinator.

### Data Management Issues

- Data management issues are the challenges and problems that arise when managing data in wireless networks, especially in mobile computing environments.
- Some of the data management issues are:

  - Data availability: How to ensure that data is accessible and consistent to mobile users, even when they are disconnected from the network or move across different network domains.
  - Data replication: How to distribute copies of data across multiple locations to improve data availability, performance, and fault tolerance, while minimizing communication and storage costs.
  - Data synchronization: How to maintain the consistency and coherence of replicated data, by detecting and resolving conflicts and updates among different copies.
  - Data caching: How to store frequently accessed or recently used data in the local memory of mobile devices, to reduce network traffic and improve response time.
  - Data adaptation: How to adjust the quality and quantity of data delivered to mobile devices, based on their capabilities, preferences, and network conditions.
  - Data security: How to protect the confidentiality, integrity, and authenticity of data transmitted and stored in wireless networks, from unauthorized access, modification, or disclosure.

### Data Replication for Mobile Computers

- Data replication for mobile computers is a technique that creates and maintains multiple copies of data in different locations, such as mobile devices, base stations, or servers, to improve data availability, performance, and fault tolerance in wireless networks.
- Data replication for mobile computers can be classified into different types based on the replication strategy, such as:

  - Static replication: The number and location of replicas are fixed and predetermined, and do not change with the network dynamics or user behavior.
  - Dynamic replication: The number and location of replicas are determined and adjusted at runtime, based on the network dynamics or user behavior, such as data access patterns, network conditions, or user mobility.
  - Hybrid replication: A combination of static and dynamic replication, where some replicas are fixed and some are variable, or where different replication strategies are applied to different data items or regions.

- Data replication for mobile computers can also be classified into different types based on the replication granularity, such as:

  - Full replication: The entire data set is replicated at each location, and all replicas are identical and complete.
  - Partial replication: Only a subset of the data set is replicated at each location, and different locations may have different subsets of data.
  - Fragmented replication: The data set is divided into smaller units or fragments, and each location may have different fragments of data.

### Adaptive Clustering for Mobile Wireless Networks

- Adaptive clustering for mobile wireless networks is a technique that organizes mobile nodes into groups or clusters, where each cluster has a leader or a clusterhead that coordinates the communication and resource management within the cluster and with other clusters.
- Adaptive clustering for mobile wireless networks can provide several benefits, such as:

  - Spatial reuse of bandwidth: By dividing the network into smaller regions, the same frequency or code can be reused by different clusters, increasing the network capacity and reducing interference.
  - Controlled access to resources: By assigning different roles and priorities to clusterheads and cluster members, the network can allocate and reserve bandwidth, power, or other resources in a fair and efficient manner.
  - Robustness to topology changes: By dynamically adjusting the cluster size, shape, and membership, the network can cope with the mobility, failure, or insertion/removal of nodes, maintaining network connectivity and stability.

- Adaptive clustering for mobile wireless networks can be classified into different types based on the cluster formation criteria, such as:

  - Connectivity-based clustering: The clusters are formed based on the connectivity or reachability of nodes, such as the number of neighbors, the hop distance, or the link quality.
  - Identifier-based clustering: The clusters are formed based on the identifiers or attributes of nodes, such as the node ID, the location, or the battery level.
  - Hybrid clustering: A combination of connectivity-based and identifier-based clustering, where both the connectivity and the attributes of nodes are considered in cluster formation.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the file system for mobile computing:

### File system for mobile computing

- A file system is a software component that manages the storage and retrieval of data on a persistent device, such as a hard disk, flash memory, or optical disc.
- A file system for mobile computing is a file system that supports the mobility of both users and devices, and adapts to the challenges of wireless and mobile environments, such as network disconnection, low bandwidth, high latency, and limited battery power.
- Some of the design issues for a file system for mobile computing are:

  - Location transparency: the ability to access files regardless of their physical location or the location of the user or device.
  - User mobility: the ability to maintain user preferences, settings, and access rights across different devices and networks.
  - Compatibility: the ability to interoperate with existing operating system interfaces and applications, and to support different file formats and protocols.
  - Caching: the ability to store copies of frequently accessed or modified files locally on the device, to reduce network traffic and improve performance.
  - Replication: the ability to create and maintain multiple copies of files on different servers, to enhance availability, reliability, and fault tolerance.
  - Consistency: the ability to ensure that all replicas of a file are synchronized and reflect the latest changes, and to resolve any conflicts that may arise due to concurrent updates or network partitions.
  - Security: the ability to protect the confidentiality, integrity, and authenticity of files and their access, and to prevent unauthorized or malicious actions.

- One example of a file system for mobile computing is Coda, which was developed at Carnegie Mellon University in the 1990s. Coda has the following features:

  - Disconnected operation: the ability to work offline when the network is unavailable or unreliable, and to synchronize the changes with the servers when the network is restored.
  - High performance: the ability to use client-side persistent caching to store large amounts of data locally, and to use bandwidth adaptation techniques to optimize the network usage.
  - Server replication: the ability to use multiple servers to store replicas of files, and to use a voting protocol to select the best server for each operation.
  - Security: the ability to use authentication, encryption, and access control mechanisms to secure the files and their access, and to use a secure RPC protocol to communicate with the servers.

- Coda uses a hierarchical namespace to organize the files, and supports the standard POSIX file system interface. Coda also supports file locking, file versioning, and file attributes. Coda uses a client-server architecture, where the clients are the mobile devices and the servers are the fixed hosts. Coda uses a weak consistency model, where the clients can modify the cached files locally, and the servers can reconcile the changes later. Coda uses a conflict resolution mechanism, where the clients can detect and resolve any conflicts that may occur due to concurrent updates or network partitions. Coda also uses a hoarding mechanism, where the clients can predict and prefetch the files that they may need in the future, based on their access patterns and preferences.



### Disconnected operations

- Disconnected operations are a mode of operation in mobile computing that allows users to execute applications when the network is unavailable or unreliable .
- Disconnected operations can be voluntary (when the user decides to work off-line) or involuntary (when the network fails or is inaccessible)  .
- Disconnected operations require mechanisms to handle data consistency, synchronization, and recovery when the network is restored   .
- Disconnected operations can be supported by different techniques, such as:
  - Server replication: replicating data from servers to clients or vice versa, to provide local access and availability  .
  - Mobile computation: moving code or processes from servers to clients or vice versa, to reduce network traffic and latency  .
  - Caching and hoarding: storing frequently or recently accessed data or files on the client, and prefetching data or files that are likely to be needed in the future  .
  - Reintegration: reconciling the changes made by the client and the server during disconnection, and resolving any conflicts or inconsistencies  .
- Disconnected operations pose several challenges and trade-offs, such as:
  - Limited resources: mobile devices have constraints on battery life, memory, storage, and processing power, which affect the performance and functionality of disconnected operations  .
  - User interface: mobile devices have small screens and keyboards, which limit the data entry and display capabilities of disconnected operations  .
  - Security and privacy: disconnected operations may expose sensitive data or code to unauthorized access or modification, or compromise the integrity and authenticity of the data or code  .
  - Quality of service: disconnected operations may degrade the quality of service of the applications, such as responsiveness, accuracy, reliability, and availability  .



## Unit 4 - Mobile Agents Computing, Security and Fault Tolerance, Transaction Processing in Mobile Computing

### Mobile Agents Computing

- A mobile agent is a composition of computer software and data that is able to migrate (move) from one computer to another autonomously and continue its execution on the destination computer .
- A mobile agent is a specific form of mobile code, within the field of code mobility. However, in contrast to the remote evaluation and code on demand programming paradigms, mobile agents are active in that they can choose to migrate between computers at any time during their execution.
- The mobile agents are autonomous with intelligence, social ability, learning, and the most important feature is their mobility. They are independent in nature, self-driven and do not require a corresponding node for communication. They can work efficiently even after the user gets disconnected from the network.
- Some of the advantages of mobile agents are:
  - They can reduce the network traffic by moving the computation to the data source instead of transferring the data over the network.
  - They can overcome the network latency by executing asynchronously and autonomously.
  - They can adapt to the dynamic network conditions and reconfigure themselves accordingly.
  - They can provide fault tolerance by replicating themselves or resuming from a checkpoint.
  - They can enhance the security and privacy by encrypting the data and code during migration.
- Some of the challenges of mobile agents are:
  - They need a compatible execution environment on each host computer, which may require a standard platform or a common language.
  - They need to ensure the integrity and authenticity of the code and data during migration, which may require digital signatures or certificates.
  - They need to protect themselves from malicious hosts or other agents, which may require encryption or sandboxing techniques.
  - They need to coordinate with other agents or resources, which may require communication protocols or coordination mechanisms.

### Security and Fault Tolerance

- Security and fault tolerance are two important aspects of mobile computing, as the mobile devices and networks are prone to various threats and failures.
- Security refers to the protection of the data and code from unauthorized access, modification, or disclosure. Security can be achieved by using various techniques, such as:
  - Authentication: verifying the identity of the users or agents before granting access to the resources or services.
  - Authorization: specifying the permissions or privileges of the users or agents to access or modify the resources or services.
  - Encryption: transforming the data or code into an unreadable form to prevent eavesdropping or tampering.
  - Integrity: ensuring that the data or code has not been altered or corrupted during transmission or storage.
  - Non-repudiation: preventing the users or agents from denying their actions or transactions.
- Fault tolerance refers to the ability of the system to continue functioning correctly in the presence of faults or errors. Fault tolerance can be achieved by using various techniques, such as:
  - Replication: creating multiple copies of the data or code to increase the availability and reliability of the system.
  - Checkpointing: saving the state of the system periodically to enable recovery or rollback in case of failures.
  - Recovery: restoring the system to a consistent and correct state after a failure or error.
  - Reconfiguration: changing the structure or behavior of the system to adapt to the changing conditions or requirements.

### Transaction Processing in Mobile Computing

- A transaction is a logical unit of work that consists of a sequence of operations that must be executed atomically, consistently, isolated, and durably (ACID properties).
- Transaction processing in mobile computing is challenging due to the characteristics of the mobile environment, such as:
  - Mobility: the mobile devices and agents can move across different locations and networks, which may affect the connectivity and availability of the resources or services.
  - Heterogeneity: the mobile devices and agents can have different capabilities and preferences, which may affect the performance and quality of the transactions.
  - Disconnection: the mobile devices and agents can experience voluntary or involuntary disconnection from the network, which may affect the completion and consistency of the transactions.
  - Limited resources: the mobile devices and agents can have limited battery, memory, or bandwidth, which may affect the efficiency and scalability of the transactions.
- Some of the solutions for transaction processing in mobile computing are:
  - Mobile transaction model: a model that defines the structure and behavior of the transactions in the mobile environment, such as the phases, states, operations, and rules of the transactions.
  - Mobile transaction management: a mechanism that coordinates and controls the execution of the transactions in the mobile environment,



# Environment for Mobile Agents

- A mobile agent is a software entity that can migrate from one node to another in a network, carrying its code, data, and execution state .
- A mobile agent environment is the software infrastructure that supports the creation, execution, migration, and communication of mobile agents .
- A mobile agent environment consists of the following components :
  - **Agent platform**: The computational environment in which an agent operates. It provides the basic services and resources for agent creation, execution, migration, and communication. It also ensures the security and integrity of the agents and the host system. The agent platform where an agent originates is called the home platform, and the platform where an agent migrates to is called the foreign platform.
  - **Agent server**: The software component that manages the agent platform and provides the interface for agent interaction. It is responsible for accepting incoming agents, dispatching outgoing agents, and controlling the local agent execution. It also handles the agent registration, authentication, and authorization .
  - **Agent transport service**: The software component that implements the agent migration mechanism. It is responsible for transferring the agent code, data, and execution state between agent platforms. It also handles the agent serialization, deserialization, and encapsulation .
  - **Agent communication service**: The software component that implements the agent communication mechanism. It is responsible for enabling the exchange of messages and data between agents, users, and systems. It also handles the agent naming, addressing, and routing .
  - **Agent development tools**: The software tools that support the design, implementation, testing, and debugging of mobile agents. They may include agent programming languages, libraries, frameworks, compilers, interpreters, editors, debuggers, and profilers .
  - **Agent applications**: The software applications that use mobile agents to perform various tasks and functions. They may include agent-based information retrieval, e-commerce, network management, distributed computing, and mobile computing .



## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over wireless links.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved by using GPS, signal strength, angle of arrival, or other techniques.
- MAC (Medium Access Control) issues refer to the challenges of coordinating the access of multiple nodes to the shared wireless medium, avoiding collisions, and maximizing throughput. Some of the MAC protocols for ad hoc networks are CSMA/CA, MACA, MACAW, FAMA, and IEEE 802.11.
- Routing protocols are the algorithms that enable the nodes in an ad hoc network to discover and maintain routes to each other. Routing protocols can be classified into proactive, reactive, and hybrid protocols, depending on whether they maintain routes constantly, on-demand, or both.
- Global state routing (GSR) is an example of a proactive routing protocol for ad hoc networks. It is based on the link-state algorithm, where each node periodically broadcasts its link state information to all other nodes. GSR uses a hierarchical structure to reduce the overhead of flooding the network with link state packets.



### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- It adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- Using the sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- DSDV provides only one route for a source/destination pair.
- DSDV requires each node to periodically broadcast routing updates.
- DSDV uses bidirectional links.
- DSDV has two types of routing updates: full dump and incremental.
  - Full dump: a node sends its entire routing table to its neighbors.
  - Incremental: a node sends only the updated entries to its neighbors.
- DSDV has two types of packets: advertisement and request.
  - Advertisement: a node broadcasts its routing table or the updated entries to its neighbors.
  - Request: a node sends a query to its neighbors for a specific destination.
- DSDV has two types of routes: settled and unstable.
  - Settled: a route that has not changed for a certain period of time.
  - Unstable: a route that has changed recently or frequently.
- DSDV has two types of sequence numbers: even and odd.
  - Even: a sequence number assigned by the destination node to its own route.
  - Odd: a sequence number assigned by an intermediate node to a route learned from another node.
- DSDV uses the following rules to update the routing table:
  - If a route has a higher sequence number, it is preferred over a route with a lower sequence number.
  - If two routes have the same sequence number, the one with a lower hop count is preferred.
  - If a route has an odd sequence number, it is marked as unstable and used only if no other route is available.
  - If a route has an even sequence number, it is marked as settled and used as the default route.
- DSDV has the following advantages:
  - It is simple and easy to implement.
  - It guarantees loop-free routes.
  - It supports both unicast and multicast routing.
- DSDV has the following disadvantages:
  - It consumes a lot of bandwidth and battery power due to frequent routing updates.
  - It does not scale well to large networks due to the overhead of maintaining routing tables.
  - It does not handle mobility and topology changes well due to the delay in propagating updates.



# Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing instead of relying on the routing table at each intermediate node .
- Source routing means that the source node specifies the complete sequence of nodes to the destination in the packet header .
- DSR consists of two main mechanisms: route discovery and route maintenance .
- Route discovery is the process of finding a route from the source to the destination when there is no cached route available .
- Route discovery involves sending a route request packet that is flooded through the network until it reaches the destination or a node with a cached route .
- The route request packet contains the source and destination addresses, a unique identification number, and a list of nodes that have forwarded the packet .
- The destination or the intermediate node with a cached route sends a route reply packet back to the source along the reverse path of the route request packet .
- The route reply packet contains the source and destination addresses, the identification number, and the list of nodes that form the route .
- The source node caches the route and uses it to send data packets to the destination .
- Route maintenance is the process of detecting and repairing link failures in the route .
- Route maintenance involves sending route error packets when a node detects a link failure in the route .
- The route error packet contains the source and destination addresses, the identification number, and the list of nodes that are unreachable due to the link failure .
- The node that receives the route error packet removes the failed link from its cache and propagates the route error packet to the source node .
- The source node initiates a new route discovery if it still needs to communicate with the destination .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages:
  - It reduces the control overhead by eliminating periodic table updates and using caching .
  - It supports multiple routes to the same destination and allows load balancing and route selection .
  - It adapts quickly to topology changes and node mobility .
- Disadvantages:
  - It consumes more bandwidth and memory due to the source routing header .
  - It may suffer from stale routes and route loops due to caching .
  - It may not scale well to large networks due to flooding .



### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, which means that each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses three types of control messages to discover and maintain routes: route request (RREQ), route reply (RREP) and route error (RERR) .
- AODV is a reactive protocol, which means that it only initiates a route discovery process when a node needs to send data to a destination and does not have a valid route to it .
- AODV avoids routing loops by using sequence numbers to indicate the freshness of a route .
- AODV is the routing protocol used in Zigbee – a low power, low data rate wireless ad hoc network.
- AODV has various implementations such as MAD-HOC, Kernel-AODV, AODV-UU, AODV-UCSB and AODV-UIUC.
- AODV has some advantages such as low network overhead, quick adaptation to network changes, scalability and support for multicast .
- AODV has some disadvantages such as high latency for route discovery, vulnerability to malicious attacks, frequent route breaks and excessive flooding in large networks .



### Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated on-demand routing protocol that was proposed by Park and Corson in 1997 .
- TORA is based on the concept of link reversal, which is a technique to dynamically change the direction of links in a network to avoid routing loops and maintain connectivity .
- TORA consists of three main phases: route creation, route maintenance, and route erasure .
- In route creation, the source node broadcasts a query packet to its neighbors, which contains the destination address and a height value. The height value is used to assign a logical direction to each link in the network. The query packet is propagated until it reaches the destination or a node that has a route to the destination. The node that receives the query packet replies with an update packet, which contains the new height value for the link. The update packet is sent back to the source along the reverse path of the query packet, creating a directed acyclic graph (DAG) from the source to the destination .
- In route maintenance, if a link failure occurs, the nodes that are affected by the failure adjust their height values to reflect the change in the network topology. The node with the broken link increases its height value to a value higher than any of its neighbors, and broadcasts an update packet to inform them of the change. The neighbors that receive the update packet compare their height values with the new value, and if they are lower, they reverse the direction of the link and forward the update packet. This process continues until a new DAG is formed or the network is partitioned .
- In route erasure, if a node detects that the network is partitioned or the route is no longer needed, it broadcasts a clear packet to erase the route. The clear packet contains the destination address and a flag to indicate the reason for the erasure. The nodes that receive the clear packet delete the route information and forward the packet to their neighbors. The clear packet is propagated until it reaches the nodes that are not affected by the erasure .
- TORA is designed to be highly adaptive, efficient, loop-free, and scalable in dynamic and large-scale ad hoc networks. It can handle multiple concurrent routes to the same destination, and can quickly recover from link failures and network partitions .
- TORA has some limitations, such as the overhead of route creation and maintenance, the possibility of temporary routing loops, and the dependence on synchronized clocks for the height values .



### QoS in Ad Hoc Networks

- Quality of service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc.  
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or centralized control.  
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes.    
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.    
- QoS in ad hoc networks can be supported by using various techniques, such as QoS-aware routing protocols, QoS-aware MAC protocols, QoS-aware scheduling algorithms, QoS-aware admission control, QoS-aware resource allocation, QoS-aware cross-layer optimization, etc.    
- QoS in ad hoc networks can be evaluated by using various metrics, such as throughput, delay, jitter, packet delivery ratio, energy consumption, etc.    
- QoS in ad hoc networks can be improved by using various methods, such as adaptive QoS, cooperative QoS, multipath QoS, multicast QoS, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some applications of ad hoc networks for the notes of Unit 5:

- **Military battlefield**: Ad hoc networks can be used to maintain an information network between the soldiers, vehicles, and military headquarters without relying on fixed infrastructure or centralized control.
- **Vehicular ad hoc network (VANET)**: Ad hoc networks can be used for communication between vehicles, such as sharing traffic information, road conditions, or safety alerts. Intelligent VANETs use artificial intelligence and ad hoc technologies to communicate what should happen during accidents .
- **Smartphone ad hoc network (SPAN)**: Ad hoc networks can be created on smartphones via existing technologies like Wi-Fi and Bluetooth, without depending on cellular carrier networks or wireless access points. SPANs can enable peer-to-peer communication, file sharing, or social networking among smartphone users .
- **Industrial and commercial applications**: Ad hoc networks can be used for cooperative mobile data exchange among workers, customers, or devices in various scenarios, such as emergency response, disaster relief, health care, education, entertainment, or smart cities.

