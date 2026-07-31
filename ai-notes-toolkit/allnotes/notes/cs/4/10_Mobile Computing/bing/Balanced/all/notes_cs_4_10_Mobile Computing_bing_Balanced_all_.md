

## Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks.
- Mobile computing enables users to communicate, access information, and perform tasks anytime and anywhere, without being constrained by physical location or wired connections.
- Mobile computing involves various challenges and issues, such as:
  - Mobility: the ability to move within or across networks while maintaining connectivity and service quality.
  - Limited resources: the constraints on battery power, memory, processing speed, and bandwidth of mobile devices.
  - Heterogeneity: the diversity of mobile devices, networks, applications, and protocols that need to interoperate.
  - Security: the protection of data and privacy from unauthorized access, modification, or disclosure.
  - Scalability: the ability to support a large number of mobile users and devices without degrading performance or reliability.
- Wireless telephony is the provision of voice and data services over wireless networks, such as cellular networks, Wi-Fi, and satellite networks.
- Wireless telephony enables users to make and receive calls, send and receive messages, and access the internet using wireless devices, such as mobile phones, smartphones, and tablets.
- Wireless telephony involves various technologies and standards, such as:
  - Cellular concept: the division of a geographic area into smaller regions called cells, each served by a base station that communicates with mobile devices using radio frequencies.
  - GSM: the Global System for Mobile Communications, a standard developed by the European Telecommunications Standards Institute (ETSI) to describe the protocols for second-generation digital cellular networks used by mobile devices such as mobile phones and tablets.
  - GSM uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate radio channels to multiple users.
  - GSM uses four different frequency bands of 850 MHz, 900 MHz, 1800 MHz and 1900 MHz, depending on the region and the operator.
  - GSM manages communication between mobile stations, base stations, and switching systems, and provides various services, such as voice calls, text messages, data transmission, roaming, and encryption  .



# Air-Interface for Mobile Computing

- The air interface is the communication link between the two stations in mobile or wireless communication.
- The air interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection  .
- The air interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network .
- The air interface is also called a "radio interface" or an "access mode" .
- Different cellular standards use different air interfaces, such as TDMA and CDMA for GSM, OFDMA for LTE, and NR for 5G  .
- The air interface is a key factor for the performance, capacity, and quality of service of a cellular network .



# Channel Structure

- Channel structure is the way of organizing the communication channels in a mobile network.
- A channel is a logical or physical path for transmitting data between a mobile device and a base station.
- Channel structure affects the performance, efficiency, and reliability of the mobile network.

## Physical and Logical Channels

- Physical channels are defined by the frequency and time slot used for transmission.
- Logical channels are defined by the type and purpose of the data carried by the physical channel.
- There are two types of logical channels: traffic channels and control channels.
- Traffic channels (TCHs) are used to carry voice or data between the mobile device and the base station.
- Control channels (CCHs) are used to carry signaling and management information between the mobile device and the base station.
- Control channels can be further classified into broadcast channels, common control channels, and dedicated control channels.

## Channel Structure in GSM

- GSM is a widely used standard for cellular communication that uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate channels.
- GSM divides the frequency spectrum into 124 carrier frequencies, each with a bandwidth of 200 kHz.
- Each carrier frequency is divided into eight time slots, each with a duration of 0.577 ms.
- Each time slot can carry one physical channel, which can be assigned to one logical channel.
- GSM uses different logical channels for different purposes, such as:

  - Broadcast Control Channel (BCCH): used to broadcast system information and cell parameters to all mobile devices in the cell.
  - Frequency Correction Channel (FCCH): used to synchronize the frequency of the mobile devices with the base station.
  - Synchronization Channel (SCH): used to synchronize the time slot of the mobile devices with the base station.
  - Paging Channel (PCH): used to alert the mobile devices of incoming calls or messages.
  - Random Access Channel (RACH): used by the mobile devices to request access to the network or to respond to paging messages.
  - Access Grant Channel (AGCH): used by the base station to assign a traffic channel or a dedicated control channel to a mobile device.
  - Standalone Dedicated Control Channel (SDCCH): used to exchange authentication, encryption, and location update information between the mobile device and the base station.
  - Slow Associated Control Channel (SACCH): used to carry measurement reports and power control commands between the mobile device and the base station.
  - Fast Associated Control Channel (FACCH): used to carry urgent signaling information, such as handover commands, by stealing a traffic channel time slot.
  - Cell Broadcast Channel (CBCH): used to broadcast short messages to all mobile devices in the cell.



# Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is a fundamental problem in personal communication services network (PCSN) that allows the network to locate and track the mobile users and deliver calls to them  .
- Location management consists of three main tasks: location update, location lookup, and paging  .
- Location update is the process of informing the network about the current location of the mobile user, which is recorded in the home location register (HLR) and the visitor location register (VLR) databases  .
- HLR is a centralized database that stores the permanent information of all the subscribers in the network, such as their phone numbers, service profiles, and current locations .
- VLR is a local database that stores the temporary information of the subscribers who are currently visiting a certain registration area (RA) in the network, such as their authentication data, temporary phone numbers, and location areas (LAs) .
- RA is a logical area that covers a group of base stations (cells) and is served by a VLR .
- LA is a logical area that covers a group of cells and is served by a mobile switching center (MSC) .
- Location lookup is the process of finding the current location of the mobile user when a call arrives for them, which involves querying the HLR and the VLR databases  .
- Paging is the process of sending a broadcast message to the mobile user in their current LA to alert them about the incoming call and establish a connection  .
- Handoff is the process of transferring the ongoing call from one cell to another as the mobile user moves across the network, which involves updating the routing information and allocating the radio resources  .
- Handoff can be classified into two types: hard handoff and soft handoff  .
- Hard handoff is the process of breaking the connection with the old cell before establishing a connection with the new cell, which results in a brief interruption of the call  .
- Soft handoff is the process of maintaining the connection with both the old and the new cells until the call is transferred to the new cell, which results in a seamless transition of the call  .
- Location management and handoff management are interrelated, as the location update and lookup affect the handoff performance and vice versa  .
- Location management and handoff management face several challenges and trade-offs, such as minimizing the signaling overhead, reducing the latency, balancing the load, preserving the quality of service, and ensuring the security and privacy of the users    .
- Location management and handoff management can be improved by using various techniques, such as hierarchical, distributed, or hybrid architectures, location caching, location prediction, mobility modeling, adaptive algorithms, and cooperative strategies    .



# Channel Allocation in Cellular Systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- When a user wants to make a call request, the channel allocation strategies assign a channel to the user based on some criteria.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots and bandwidth .
- Channel allocation strategies can be classified into three types:
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels that are not shared with other cells. The channels are allocated based on the traffic demand of each cell. FCA has low overhead but high blocking probability.
  - Dynamic channel allocation (DCA): Each cell can use any channel that is not used by any neighboring cell. The channels are allocated based on the current traffic demand and interference conditions of each cell. DCA has high overhead but low blocking probability.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed and some are dynamic. HCA can balance the trade-off between overhead and blocking probability.
- The channel allocation algorithms consider the following criteria:
  - Future blocking probability in neighboring cells: The probability that a channel request in a neighboring cell will be rejected due to interference from the current cell.
  - Reuse distance: The minimum distance between two cells that use the same channel to avoid interference.
  - Usage frequency of the candidate channel: The number of times the channel has been used in the past.
  - Average blocking probability of the overall system: The probability that a channel request in any cell will be rejected due to lack of available channels.
  - Instantaneous channel occupancy distribution: The number of channels that are currently occupied in each cell.



# CDMA for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- CDMA stands for Code Division Multiple Access and is a spread spectrum multiple access technique  .
- Spread spectrum technique spreads bandwidth of data in a uniform manner for the same transmitted power.
- CDMA is a digital cellular technology used for mobile communication .
- CDMA is the base on which access methods such as cdmaOne, CDMA2000, and WCDMA are built .
- CDMA allows numerous signals to occupy a single transmission channel, optimizing the use of available bandwidth .
- CDMA uses a special coding scheme, where each transmitter is assigned a code, to allow multiple users to be multiplexed over the same physical channel  .
- CDMA is a form of direct-sequence spread spectrum (DSSS) modulation, where a data signal is multiplied by a pseudorandom noise (PN) code sequence that has a much higher data rate than the original signal  .
- CDMA has several advantages over other multiple access techniques, such as:
  - Higher spectral efficiency, as more users can share the same bandwidth without interference  .
  - Better security, as the code sequence makes the signal difficult to intercept or jam  .
  - Improved voice quality, as the signal can be recovered from noise and fading by using error correction and diversity techniques  .
  - Greater flexibility, as the code sequence can be dynamically changed to accommodate different services and user demands  .
- CDMA has some disadvantages, such as:
  - Higher complexity, as the code sequence generation and synchronization require more processing power and memory  .
  - Near-far problem, where a strong signal from a nearby transmitter can interfere with a weak signal from a distant transmitter, unless power control is implemented  .
  - Cell breathing, where the coverage area of a cell varies depending on the number of active users and their locations  .
- CDMA is one of the multiple access techniques used in mobile computing, along with FDMA (Frequency Division Multiple Access) and TDMA (Time Division Multiple Access).
- FDMA divides the available bandwidth into frequency bands, and assigns each user a different band.
- TDMA divides the available bandwidth into time slots, and assigns each user a different slot.
- CDMA, FDMA, and TDMA are used to achieve frequency reuse, which is the concept of using the same radio frequency in different cells to increase the capacity of a cellular network.
- GSM (Global System for Mobile Communications) is a standard for 2G digital cellular networks that uses a combination of FDMA and TDMA to achieve multiple access.
- GSM divides the available bandwidth into 200 kHz carrier frequencies, and each carrier frequency is divided into eight time slots.
- GSM uses a cellular concept, where a large geographic area is divided into smaller areas called cells, each served by a base station.
- GSM uses a hierarchical structure of cells, where smaller cells are nested within larger cells, to provide better coverage and capacity.
- GSM uses handover techniques, where a mobile station switches from one base station to another as it moves across cells, to maintain seamless connectivity.
- GSM provides various services, such as voice, data, SMS, and roaming, to its users.



# GPRS for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- GPRS stands for **General Packet Radio Service** .
- It is a **packet oriented** wireless data communication service for mobile communications on **2G and 3G** cellular communication systems  .
- It is **non-voice**, high speed packet switching technology intended for GSM networks .
- It enables **moderately high-speed data transfers** using packet-based technologies .
- It offers more data transmission options for GSM-based devices, as GSM networks at the time could only use Short Message Service (SMS), for example, to transmit a small amount of data .
- It establishes a **connected mobile environment** for IoT applications.
- It supports **multiple users** on a single channel by using **statistical multiplexing** .
- It uses **logical channels** to transmit data packets between mobile stations and the network .
- It has two main classes of logical channels: **Packet Data Channels (PDCHs)** and **Packet Control Channels (PCCHs)** .
- PDCHs are used to carry user data and some signaling messages .
- PCCHs are used to carry control and signaling messages for GPRS .
- It has two main modes of operation: **GPRS attach/detach** and **PDP context activation/deactivation** .
- GPRS attach/detach is the process of registering or deregistering a mobile station with the GPRS network .
- PDP context activation/deactivation is the process of establishing or releasing a logical connection between a mobile station and a packet data network (such as the internet) .
- It has four main entities in its network architecture: **Base Station Subsystem (BSS)**, **Serving GPRS Support Node (SGSN)**, **Gateway GPRS Support Node (GGSN)**, and **Packet Data Protocol (PDP)** .
- BSS consists of **Base Transceiver Stations (BTSs)** and **Base Station Controllers (BSCs)** that provide radio access and control functions for GPRS .
- SGSN is a network node that handles **mobility management**, **session management**, **authentication**, and **charging** functions for GPRS .
- GGSN is a network node that acts as an **interface** between the GPRS network and external packet data networks .
- PDP is a protocol that defines the **format** and **addressing** of data packets exchanged between a mobile station and a packet data network .
- It has several advantages, such as:
  - **Increased data rates** compared to circuit-switched services .
  - **Efficient use of radio resources** by using packet switching and statistical multiplexing .
  - **Always-on connectivity** for mobile users without occupying a dedicated channel .
  - **Support for a variety of applications** such as email, web browsing, multimedia, and IoT  .
- It also has some disadvantages, such as:
  - **Limited coverage** in some areas due to the availability of GPRS-enabled base stations .
  - **Variable data rates** depending on the network congestion and radio conditions .
  - **Security risks** due to the possibility of data interception and modification .
  - **High power consumption** for mobile devices due to the frequent transmission and reception of data packets .



## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves or infrared signals.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs use the IEEE 802.11 standard, which defines the medium access control (MAC) and physical layer (PHY) specifications for wireless communication.
- MAC is the sublayer of the data link layer that controls how devices access the shared wireless medium and avoid collisions.
- PHY is the sublayer of the data link layer that defines the modulation, coding, and transmission of wireless signals.
- IEEE 802.11 has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that differ in terms of frequency, bandwidth, data rate, and range.
- IEEE 802.11 uses the Ethernet protocol and CSMA/CA (carrier sense multiple access with collision avoidance) for MAC.
- CSMA/CA is a technique that allows devices to sense the wireless medium before transmitting and to back off if the medium is busy.
- CSMA/CA also uses a mechanism called RTS/CTS (request to send/clear to send) to reserve the medium for a data transmission and to avoid the hidden node problem.
- The hidden node problem occurs when two devices that are out of range of each other try to communicate with a common device, causing collisions and interference.
- IEEE 802.11 also uses a mechanism called fragmentation to divide large data frames into smaller fragments and to reduce the probability of errors and retransmissions.
- IEEE 802.11 also uses a mechanism called acknowledgement (ACK) to confirm the successful reception of a data frame or a fragment.
- IEEE 802.11 also uses a mechanism called power management to conserve the battery life of wireless devices by switching them to a low-power mode when they are idle or not associated with an access point (AP).
- An AP is a device that acts as a bridge between the wireless and wired networks and provides wireless connectivity to the devices associated with it.
- A WLAN can operate in two modes: infrastructure mode and ad hoc mode.
- In infrastructure mode, the wireless devices communicate through one or more APs that are connected to a wired network.
- In ad hoc mode, the wireless devices communicate directly with each other without any AP or wired network.
- Bluetooth is another wireless technology that enables short-range communication between devices, such as phones, headsets, keyboards, mice, printers, etc.
- Bluetooth uses the IEEE 802.15.1 standard, which defines the MAC and PHY specifications for wireless personal area networks (WPANs).
- WPANs are wireless networks that connect devices within a personal area, such as a room or a car.
- Bluetooth uses a technique called frequency hopping spread spectrum (FHSS) to hop among 79 channels in the 2.4 GHz band and to avoid interference from other wireless devices.
- Bluetooth also uses a technique called adaptive frequency hopping (AFH) to detect and avoid the channels that are occupied by other wireless devices, such as Wi-Fi or microwave ovens.
- Bluetooth also uses a technique called inquiry and paging to discover and connect with other Bluetooth devices within range.
- Bluetooth also uses a technique called pairing to establish a secure and encrypted link between two Bluetooth devices.
- Bluetooth also uses a technique called service discovery protocol (SDP) to exchange information about the services and capabilities of the Bluetooth devices.
- Bluetooth also uses a technique called logical link control and adaptation protocol (L2CAP) to multiplex multiple logical channels over a single physical link and to adapt the data packets to the characteristics of the wireless medium.
- Bluetooth also uses a technique called radio frequency communication (RFCOMM) to emulate a serial port and to provide a reliable and bidirectional data stream between the Bluetooth devices.
- Bluetooth also uses a technique called object exchange (OBEX) to exchange objects, such as files, contacts, calendars, etc., between the Bluetooth devices.
- Bluetooth also uses a technique called advanced audio distribution profile (A2DP) to stream high-quality audio between the Bluetooth devices, such as a phone and a headset.
- Bluetooth also uses a technique called audio/video remote control profile (AVRCP) to control the playback of audio and video between the Bluetooth devices, such as a phone and a speaker.
- Wireless is a



# Multiple Access Protocols

- Multiple access protocols are used to coordinate the access of multiple nodes or users to a shared network channel, such as a wireless LAN or a satellite network.
- Multiple access protocols can be classified into three categories: random access, controlled access, and channelization.
- Random access protocols allow nodes to transmit data whenever they have data to send, without any coordination with other nodes. However, this may result in collisions, which degrade the network performance and waste the channel bandwidth.
- Controlled access protocols require nodes to obtain permission from a central controller or from other nodes before transmitting data. This reduces the probability of collisions, but introduces some delay and overhead in the network.
- Channelization protocols divide the channel into smaller subchannels, and assign each subchannel to a node or a group of nodes. This avoids collisions, but may not utilize the channel efficiently if some subchannels are idle or underutilized.

## Random Access Protocols

- Some common random access protocols that may be used in wireless networks are:

  - ALOHA: It is a simple protocol that allows nodes to transmit data whenever they have data to send, without any sensing or reservation. It is prone to collisions, especially when the network load is high. There are two variants of ALOHA: pure ALOHA and slotted ALOHA. Pure ALOHA does not have any synchronization among nodes, while slotted ALOHA divides the time into equal slots and requires nodes to transmit only at the beginning of a slot. Slotted ALOHA has a higher throughput than pure ALOHA, but still suffers from collisions .
  - CSMA: It stands for Carrier Sense Multiple Access. It is a protocol that requires nodes to sense the channel before transmitting data. If the channel is busy, the node defers its transmission until the channel becomes idle. This reduces the chance of collisions, but does not eliminate them completely. There are different variants of CSMA, such as 1-persistent CSMA, non-persistent CSMA, and p-persistent CSMA, which differ in how nodes choose their backoff time after sensing a busy channel .
  - CSMA/CA: It stands for Carrier Sense Multiple Access with Collision Avoidance. It is a protocol that enhances CSMA by using a handshake mechanism to reserve the channel before transmitting data. The sender node first sends a Request to Send (RTS) frame to the receiver node, and waits for a Clear to Send (CTS) frame from the receiver. If the sender receives the CTS, it proceeds to transmit the data frame, otherwise it backs off and retries later. This protocol avoids collisions by preventing other nodes from transmitting during the RTS-CTS-data exchange. It is used in IEEE 802.11 / WiFi networks, potentially using a distributed coordination function .

## Controlled Access Protocols

- Some common controlled access protocols that may be used in wireless networks are:

  - Reservation ALOHA (R-ALOHA): It is a protocol that combines ALOHA and reservation techniques. It divides the time into frames, and each frame consists of two subframes: a reservation subframe and a data subframe. Nodes use the reservation subframe to send reservation requests to a central controller, which then allocates the data subframe slots to the nodes based on their requests. This protocol reduces collisions and improves the throughput of ALOHA, but introduces some delay and overhead in the network.
  - Mobile Slotted Aloha (MS-ALOHA): It is a protocol that adapts slotted ALOHA to the dynamic nature of mobile networks. It allows nodes to change their slots according to their mobility and traffic patterns. Nodes use a reservation slot to inform the central controller about their slot preferences, and the controller assigns the slots to the nodes based on their requests and the availability of the slots. This protocol improves the performance and flexibility of slotted ALOHA, but requires some synchronization and coordination among nodes and the controller.
  - Polling: It is a protocol that uses a central controller to poll each node in a predefined order and grant them the channel access. The controller maintains a list of active nodes and cycles through them, asking each node if it has data to send. If the node has data, it transmits the data to the controller or to the destination node, otherwise it waits for the next poll. This protocol avoids collisions and ensures fair access to the channel, but introduces some delay and overhead in the network.

## Channelization



# TCP over wireless

- TCP (Transmission Control Protocol) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and low throughput.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, variable bandwidth, and frequent handoffs.

## TCP over wireless challenges

- Wireless networks have different characteristics and challenges than wired networks, which affect the performance of TCP. Some of these challenges are:

  - **High delays**: Wireless networks may have higher propagation delays due to the long distances between the sender and the receiver, especially in satellite networks. TCP relies on timers and acknowledgments to estimate the round-trip time (RTT) and detect losses, which may be inaccurate or delayed in wireless networks. This may lead to spurious timeouts, unnecessary retransmissions, and slow recovery.

  - **High error rates**: Wireless links are prone to errors due to various factors, such as noise, interference, fading, and shadowing. TCP treats all losses as congestion losses and invokes congestion control mechanisms, such as slow start and congestion avoidance, to reduce the congestion window and the sending rate. This may result in underutilization of the available bandwidth and low throughput.

  - **Variable bandwidth**: Wireless networks may have variable bandwidth due to factors such as channel conditions, interference, and mobility. TCP uses the congestion window to control the sending rate, which is based on the assumption of a fixed bandwidth. TCP may not be able to adapt quickly to the changing bandwidth and may cause either congestion or underutilization.

  - **Frequent handoffs**: Wireless networks may involve frequent handoffs due to mobility of the nodes. Handoffs may cause temporary disconnections, packet losses, or route changes, which may affect the TCP performance. TCP may interpret these events as congestion and reduce the sending rate, or may experience long timeouts and slow recovery.

## TCP over wireless solutions

- Several solutions have been proposed to improve the performance of TCP over wireless networks. These solutions can be classified into four categories:

  - **End-to-end solutions**: These solutions modify the TCP sender or receiver to cope with wireless losses without involving the intermediate nodes. For example, TCP selective acknowledgment (SACK) allows the receiver to report multiple non-contiguous segments that have been received, which can help the sender to avoid unnecessary retransmissions. TCP Vegas is another example that uses the RTT variation to detect congestion instead of packet losses.

  - **Link-layer solutions**: These solutions enhance the link layer protocols to provide local reliability and error recovery over the wireless links, without modifying the TCP layer. For example, automatic repeat request (ARQ) is a technique that uses acknowledgments and retransmissions at the link layer to ensure reliable delivery of packets. Forward error correction (FEC) is another technique that adds redundant bits to the packets to correct errors at the receiver without retransmissions.

  - **Split-connection solutions**: These solutions split the TCP connection into two sub-connections: one over the wired network and one over the wireless network. The intermediate node, such as the base station, acts as a proxy that terminates the TCP connection from the sender and initiates a new TCP connection to the receiver. The proxy can use different TCP variants or parameters for each sub-connection and can perform local error recovery over the wireless link.

  - **Cross-layer solutions**: These solutions exploit the interactions and information exchange between different layers of the network stack to optimize the TCP performance over wireless networks. For example, TCP feedback (TCP-F) is a technique that uses the feedback from the network layer to inform the TCP sender about the wireless link conditions and the cause of packet losses. TCP adaptive pacing (TCP-AP) is another technique that uses the feedback from the physical layer to adjust the TCP sending rate according to the wireless channel quality.



# Wireless Applications

Wireless applications are software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, and wireless internet. Wireless applications enable users to access information, services, and entertainment without being constrained by wires or cables. Wireless applications can be classified into different categories based on their functions, such as:

- **Voice applications**: These are applications that enable users to make and receive voice calls over wireless networks, such as cellular phones, voice over IP (VoIP), and voice over WLAN (VoWLAN). Voice applications can also include features such as voice mail, caller ID, conference calling, and voice recognition.
- **Data applications**: These are applications that enable users to send and receive data over wireless networks, such as email, instant messaging, web browsing, file transfer, and cloud computing. Data applications can also include features such as encryption, compression, synchronization, and backup.
- **Multimedia applications**: These are applications that enable users to access and share multimedia content over wireless networks, such as audio, video, images, and games. Multimedia applications can also include features such as streaming, downloading, editing, and sharing.
- **Location-based applications**: These are applications that use the location information of the user or the device to provide services or information, such as navigation, tracking, geofencing, and geotagging. Location-based applications can also include features such as maps, directions, points of interest, and location-aware advertising.
- **Sensor-based applications**: These are applications that use the data collected by sensors embedded in the device or the environment to provide services or information, such as health monitoring, fitness tracking, environmental sensing, and smart home automation. Sensor-based applications can also include features such as data analysis, visualization, and feedback.

Wireless applications can be developed using various platforms, tools, and languages, such as:

- **Wireless Application Protocol (WAP)**: This is a set of standards that defines how wireless devices can access information and services over wireless networks. WAP uses a markup language called Wireless Markup Language (WML) to create web pages that can be displayed on wireless devices. WAP also uses a protocol called Wireless Session Protocol (WSP) to establish and maintain sessions between wireless devices and servers.
- **Java Platform, Micro Edition (Java ME)**: This is a platform that provides a set of APIs and tools for developing applications that run on small and resource-constrained devices, such as mobile phones, PDAs, and embedded systems. Java ME supports various configurations and profiles that define the features and functionalities of different types of devices. Java ME also supports a technology called Java Wireless Messaging API (JWMA) that enables applications to send and receive SMS and MMS messages.
- **Android**: This is an open-source operating system and platform that is based on Linux and Java. Android provides a set of APIs and tools for developing applications that run on devices that use the Android operating system, such as smartphones, tablets, and smart TVs. Android also supports a technology called Android Application Framework (AAF) that enables applications to access various features and services of the device, such as sensors, cameras, GPS, and Bluetooth.
- **iOS**: This is an operating system and platform that is developed by Apple. iOS provides a set of APIs and tools for developing applications that run on devices that use the iOS operating system, such as iPhones, iPads, and iPods. iOS also supports a technology called Cocoa Touch that enables applications to access various features and services of the device, such as touch screen, accelerometer, gyroscope, and Face ID.



# Data Broadcasting for Wireless Networking

- Data broadcasting is a group communication, where a sender sends data to receivers simultaneously .
- Data broadcasting can be used for efficient information dissemination in wireless networks, where clients have local and dynamic data demands.
- Data broadcasting can be implemented using different techniques, such as push, pull, or hybrid.
- Push-based broadcasting is where the server periodically transmits data items to the clients, without any explicit requests from them.
- Pull-based broadcasting is where the clients send requests to the server for specific data items, and the server responds by transmitting them.
- Hybrid broadcasting is a combination of push and pull, where the server transmits some data items periodically, and some on demand.
- Data broadcasting can benefit from network coding or cooperation, which are techniques to improve the throughput and reliability of wireless transmissions.
- Network coding is where the server combines multiple data items into a single coded packet, which can be decoded by multiple clients.
- Cooperation is where the clients help each other by relaying data items that they have received to other clients who need them.
- Data broadcasting can also leverage smart antennas, which are antennas that can adjust their radiation patterns to focus on specific directions or clients.
- Smart antennas can improve the performance of wireless push systems by reducing interference and increasing coverage.
- Data broadcasting can be applied to various wireless networks, such as wireless LANs, Bluetooth, or cellular networks .
- Wireless LANs are local area networks that use radio frequency (RF) connections between nodes in the network .
- IEEE 802.11 is a set of standards that define the physical and medium access control (MAC) layers of wireless LANs .
- MAC issues in wireless LANs include how to share the wireless medium among multiple nodes, how to avoid or resolve collisions, how to handle hidden and exposed terminals, and how to save energy .
- Bluetooth is a short-range wireless technology that enables wireless communication between devices, such as phones, laptops, headsets, or printers .
- Bluetooth uses a frequency-hopping spread spectrum (FHSS) technique, where the devices change their frequency of transmission in a pseudo-random manner to avoid interference .
- Bluetooth devices form ad hoc networks called piconets, where one device acts as a master and up to seven devices act as slaves .
- Multiple piconets can be interconnected to form a scatternet, where some devices act as bridges between different piconets .
- Wireless is a term that refers to any communication that does not use wires or cables, such as radio, cellular, satellite, or infrared .
- Wireless networks can be classified into different types, such as wireless personal area networks (WPANs), wireless local area networks (WLANs), wireless metropolitan area networks (WMANs), or wireless wide area networks (WWANs) .
- WPANs are networks that cover a small area, such as a room or a car, and use technologies such as Bluetooth or ZigBee .
- WLANs are networks that cover a larger area, such as a building or a campus, and use technologies such as IEEE 802.11 or Wi-Fi .
- WMANs are networks that cover a city or a region, and use technologies such as IEEE 802.16 or WiMAX .
- WWANs are networks that cover a country or a continent, and use technologies such as cellular or satellite .



# Mobile IP

Mobile IP is a communication protocol that allows the users to move from one network to another with the same IP address. It ensures that the communication will continue without the user's sessions or connections being dropped. It was designed to support seamless and continuous Internet connectivity. It is used in many wired and wireless environments where users have to carry their mobile devices across multiple LAN subnets. Mobile IP is scalable for the Internet because it is based on IP—any media that can support IP can support Mobile IP.

Some of the applications of Mobile IP are:

- Roaming between overlapping wireless systems, e.g., IP over DVB, WLAN, WiMAX and BWA.
- Mobile data communication in cellular systems such as 3G and in wireless LAN such as 802.11, and extending into satellite communication.
- Supporting mobile devices that need to access the Internet or other IP-based networks while moving across different networks or link layers.

Some of the key concepts and components of Mobile IP are:

- Home network: The network where the mobile device has a permanent IP address and is registered.
- Foreign network: The network where the mobile device is currently located and has a temporary IP address.
- Home agent: A router on the home network that maintains a binding table of the mobile device's permanent and temporary IP addresses and forwards packets to the foreign network.
- Foreign agent: A router on the foreign network that provides a temporary IP address to the mobile device and forwards packets to the mobile device from the home agent.
- Care-of address: The temporary IP address assigned to the mobile device on the foreign network.
- Tunneling: The process of encapsulating and decapsulating packets between the home agent and the foreign agent to deliver them to the mobile device.
- Registration: The process of notifying the home agent of the mobile device's current care-of address and updating the binding table.



# WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer is of most interest to content developers because it contains among other things, device specifications, scripting languages, and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems. The application layer also includes the Wireless Application Environment (WAE), which provides a framework for developing and delivering wireless applications and services.
  - Session Layer: This layer provides a reliable session service between applications, based on a request-response paradigm. The session layer uses the Wireless Session Protocol (WSP), which is a binary-encoded version of the HTTP protocol, optimized for low-bandwidth and high-latency networks.
  - Transaction Layer: This layer provides a lightweight transaction service on top of the session layer, based on a two-phase commit protocol. The transaction layer uses the Wireless Transaction Protocol (WTP), which supports reliable and unreliable request-response and one-way transactions.
  - Security Layer: This layer provides data integrity and privacy services for the wireless network. The security layer uses the Wireless Transport Layer Security (WTLS), which is a wireless-optimized version of the TLS protocol, based on the SSL protocol. WTLS supports encryption, authentication, and data compression.
  - Transport Layer: This layer provides a datagram service and a connection-oriented service for the upper layers. The transport layer uses the Wireless Datagram Protocol (WDP), which is an adaptation layer that allows WAP to be used over various types of wireless networks, such as GSM, CDMA, CDPD, and SMS. WDP also supports port numbers to identify different WAP services.
- The WAP architecture also includes several components, each serving a specific function. These components include:
  - WAP Client: This is the wireless device that runs a micro-browser and interacts with the WAP gateway. The WAP client uses WML to display content and WMLScript to execute scripts on the device. The WAP client also supports cookies, caching, and push services.
  - WAP Gateway: This is the intermediary between the wireless network and the internet. The WAP gateway performs several tasks, such as protocol translation, content encoding and decoding, content filtering and adaptation, and security services. The WAP gateway also supports proxy and caching functions to improve performance and reduce network traffic.
  - WAP Server: This is the web server that hosts the wireless applications and content. The WAP server uses standard web technologies, such as HTML, XML, CGI, and Java, to generate dynamic content for the WAP clients. The WAP server also supports WML and WMLScript to create wireless-specific content and functionality.
- The WAP architecture is illustrated in the following diagram:

WAP architecture diagram



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



# Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, and processing power.
- WAE consists of the following components :
  - Wireless Markup Language (WML): A markup language similar to HTML, but optimized for small screens and low bandwidth. WML defines the content and layout of web pages for wireless devices.
  - Wireless Markup Language Script (WMLScript): A scripting language similar to JavaScript, but with a smaller footprint and fewer features. WMLScript enables dynamic and interactive web pages for wireless devices.
  - Wireless Telephony Application Interface (WTAI): A set of extensions to WML and WMLScript that allow wireless devices to access telephony services, such as making and receiving calls, sending and receiving messages, and accessing phonebook entries.
  - Wireless Datagram Protocol (WDP): A transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS. WDP enables WAP applications to run over any wireless network.
  - Wireless Session Protocol (WSP): A session layer protocol that provides reliable and secure communication between wireless devices and web servers. WSP supports features such as connection-oriented and connectionless modes, session management, and content encoding.
  - Wireless Transaction Protocol (WTP): A transaction layer protocol that provides efficient and reliable data transfer between wireless devices and web servers. WTP supports features such as segmentation and reassembly, error recovery, and acknowledgments.
  - Wireless Application Protocol Binary XML (WBXML): A binary representation of XML documents that reduces the size and complexity of web pages for wireless devices. WBXML enables faster parsing and transmission of web content.

- Another example of an application environment for wireless networking is the Java 2 Platform, Micro Edition (J2ME), which is a subset of the Java platform designed for resource-constrained devices, such as mobile phones, PDAs, and embedded systems.
- J2ME consists of the following components:
  - Connected Limited Device Configuration (CLDC): A set of core Java APIs and a virtual machine that provide the basic functionality and compatibility for J2ME applications. CLDC defines features such as threads, exceptions, input/output, networking, and security.
  - Mobile Information Device Profile (MIDP): A set of Java APIs and a user interface framework that provide the specific functionality and compatibility for mobile devices. MIDP defines features such as graphics, multimedia, user input, persistent storage, and application management.
  - Optional Packages: A set of additional Java APIs that provide optional functionality and compatibility for J2ME applications. Optional packages include features such as Bluetooth, wireless messaging, location, and web services.

- Wireless networking also involves other application environments, such as Bluetooth, IEEE 802.11, and Wireless LAN. These application environments define the protocols, standards, and tools that enable wireless devices to communicate with each other and form wireless networks.
- Bluetooth is a short-range wireless technology that enables wireless devices to exchange data and voice over a personal area network (PAN). Bluetooth defines features such as device discovery, pairing, security, and profiles.
- IEEE 802.11 is a set of standards that define the physical and data link layers of wireless local area networks (WLANs). IEEE 802.11 defines features such as modulation, encryption, authentication, and quality of service.
- Wireless LAN is a generic term that refers to any wireless network that connects devices within a limited geographic area, such as a home, office, or campus. Wireless LANs can use different technologies, such as IEEE 802.11, Bluetooth, or infrared.

: Wireless Application Environment Overview - Oracle
: Wireless Application Environment - BrainKart
: What Is J2ME? - Oracle
: Bluetooth Technology Website
: IEEE 802.11 Wireless LANs - IEEE
: Wireless LAN - Wikipedia



# Applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless networking is the use of wireless communication technologies to connect devices and networks without wires or cables.
- Wireless LAN (WLAN) is a type of wireless networking that allows devices to communicate within a local area network (LAN) using radio waves or infrared signals.
- WLAN can provide mobility, flexibility, scalability, and cost-effectiveness for network users and administrators.
- WLAN can be classified into two types: infrastructure and ad hoc.
  - Infrastructure WLAN uses a central device called an access point (AP) to connect wireless devices to a wired LAN or the internet.
  - Ad hoc WLAN does not use an AP, but rather allows wireless devices to communicate directly with each other in a peer-to-peer (P2P) fashion.
- WLAN can also be categorized based on the standards and protocols they use, such as IEEE 802.11, Bluetooth, Wi-Fi Direct, etc.
- IEEE 802.11 is the most widely used standard for WLAN, which defines the medium access control (MAC) and physical (PHY) layers for wireless communication.
  - MAC layer is responsible for coordinating the access of multiple wireless devices to the shared wireless medium, using techniques such as carrier sense multiple access with collision avoidance (CSMA/CA), request to send/clear to send (RTS/CTS), and fragmentation and reassembly.
  - PHY layer is responsible for encoding, modulating, transmitting, receiving, and demodulating the wireless signals, using different frequency bands, modulation schemes, and data rates, such as 2.4 GHz, 5 GHz, OFDM, QPSK, 11 Mbps, 54 Mbps, etc.
- IEEE 802.11 has several amendments and extensions, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which provide different features and enhancements for WLAN, such as higher data rates, wider channels, multiple-input multiple-output (MIMO) antennas, beamforming, etc.
- Bluetooth is another standard for WLAN, which is designed for short-range, low-power, and low-cost wireless communication between devices, such as smartphones, laptops, headphones, keyboards, mice, etc.
  - Bluetooth uses a frequency-hopping spread spectrum (FHSS) technique to avoid interference and increase security, by changing the frequency of the wireless signal every 625 microseconds.
  - Bluetooth also uses a master-slave architecture, where one device acts as the master and controls the communication with up to seven other devices, forming a piconet.
  - Bluetooth can also form a scatternet, where multiple piconets are interconnected by shared devices.
  - Bluetooth has several versions and profiles, such as Bluetooth 1.0, Bluetooth 2.0, Bluetooth 3.0, Bluetooth 4.0, Bluetooth 5.0, etc., which provide different features and enhancements for WLAN, such as higher data rates, lower power consumption, longer range, etc.
- Wireless multiple access protocols are the rules and algorithms that govern how multiple wireless devices share the wireless medium and avoid collisions and interference.
  - Wireless multiple access protocols can be classified into two types: random access and controlled access.
    - Random access protocols allow wireless devices to transmit whenever they have data to send, without coordination with other devices, such as ALOHA, slotted ALOHA, CSMA, CSMA/CA, etc.
    - Controlled access protocols require wireless devices to obtain permission or reservation before transmitting, with coordination with other devices, such as polling, token passing, reservation ALOHA, etc.
- TCP over wireless is the use of the transmission control protocol (TCP) for reliable and ordered data delivery over wireless networks, which are prone to errors, losses, delays, and variations.
  - TCP over wireless faces several challenges and issues, such as TCP misinterpreting wireless losses as congestion losses, TCP triggering unnecessary retransmissions and timeouts, TCP reducing the congestion window and throughput, TCP experiencing spurious retransmissions and duplicate acknowledgments, etc.
  - TCP over wireless can be improved and enhanced by using different techniques and solutions, such as link layer retransmission, split TCP, TCP snooping, selective acknowledgment, fast retransmit and recovery, etc.
- Wireless applications are the software and services that use wireless networks and technologies to provide various functions and features for users and organizations, such as web browsing,



## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to a fixed network via wireless links .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and resolving global names.
  - Security: The data on mobile devices is more vulnerable to theft, loss, or damage than the data on fixed locations. Therefore, encryption, authentication, and backup mechanisms are needed.
  - Data distribution and replication: The uneven and dynamic network topology, the limited bandwidth and battery power, and the high mobility of mobile devices require efficient and adaptive strategies for data replication and synchronization.
  - Query processing and optimization: The query processing and optimization techniques for mobile databases need to consider the network heterogeneity, the location and context awareness, the data availability and consistency, and the user preferences and profiles.
  - Transaction management: The transaction management protocols for mobile databases need to cope with the issues of concurrency control, recovery, and commit in the presence of disconnections, failures, and mobility.
  - Data broadcasting and caching: Data broadcasting and caching are techniques to improve the data availability and reduce the communication cost for mobile devices. Data broadcasting involves disseminating data to a large number of mobile devices via a wireless channel, while data caching involves storing frequently accessed data on the mobile devices or intermediate servers.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data on different locations.
- Data replication for mobile computers aims to improve the data availability, reduce the communication cost, and enhance the system performance and scalability .
- Data replication for mobile computers faces several challenges, such as :
  - How to select the data items to be replicated and where to place them?
  - How to maintain the consistency and freshness of the replicated data in the presence of updates, disconnections, and mobility?
  - How to handle the conflicts and reconcile the divergent replicas when they reconnect?
  - How to adapt the replication strategy to the changing network conditions and user requirements?
- Data replication for mobile computers can be classified into two categories: server-initiated and client-initiated .
  - Server-initiated replication: The server decides which data items to replicate and where to place them, based on the global information about the system state and the user profiles. The server also initiates the data synchronization and conflict resolution processes. This approach is suitable for scenarios where the server has a high degree of control and the network is relatively stable .
  - Client-initiated replication: The client decides which data items to replicate and where to place them, based on the local information about the data access patterns and the network conditions. The client also initiates the data synchronization and conflict resolution processes. This approach is suitable for scenarios where the client has a high degree of autonomy and the network is highly dynamic .

### Adaptive clustering for mobile

- Adaptive clustering is a technique to organize the mobile devices into groups or clusters, based on some criteria such as location, connectivity, or similarity .
- Adaptive clustering for mobile aims to improve the data management and communication efficiency, reduce the network overhead and energy consumption, and enhance the system scalability and fault tolerance .
- Adaptive clustering for mobile faces several challenges, such as :
  - How to form and maintain the clusters in the presence of mobility, disconnections, and failures?
  - How to select the cluster heads or coordinators and balance the load among them?
  - How to handle the inter-cluster and intra-cluster communication and data exchange?
  - How to adapt the clustering strategy to the changing network conditions and user requirements?
- Adaptive clustering for mobile can be classified into two categories: centralized and distributed .
  - Centralized clustering: A central server or a designated cluster head is responsible for forming and maintaining the clusters, based on the global information about



# Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables. Wireless networks can enable mobile computing, which is the ability to access and process data from anywhere and anytime using portable devices.

## Data Management Issues

Data management issues in wireless networks include:

- Data availability: How to ensure that data is accessible to mobile users even when they are disconnected from the network or when the network is unreliable.
- Data consistency: How to maintain the correctness and integrity of data when it is replicated or cached on multiple devices or locations.
- Data security: How to protect data from unauthorized access, modification, or disclosure when it is transmitted over wireless channels or stored on mobile devices.
- Data adaptation: How to adjust data to the varying capabilities and preferences of mobile devices and users, such as screen size, bandwidth, battery power, and location.

## Data Replication for Mobile Computers

Data replication is the process of creating and maintaining multiple copies of data on different devices or locations. Data replication can improve data availability, performance, and fault tolerance for mobile computers, but it also introduces challenges for data consistency and synchronization.

Some data replication methods for mobile computers are:

- Static replication: Data is replicated in advance based on predefined criteria, such as popularity, frequency, or location. Static replication is simple and efficient, but it may not adapt well to dynamic changes in data or user behavior.
- Dynamic replication: Data is replicated on demand based on the current needs and requests of mobile users. Dynamic replication is more flexible and adaptive, but it may incur more overhead and complexity for data allocation and coordination.
- Hybrid replication: Data is replicated using a combination of static and dynamic methods, such as replicating some data statically and some data dynamically, or using static replication with dynamic updates.

## Adaptive Clustering for Mobile Wireless Networks

Adaptive clustering is a technique for organizing nodes in a mobile wireless network into groups or clusters, where each cluster has a leader or a clusterhead that coordinates the communication and resource management within the cluster. Adaptive clustering can improve the scalability, efficiency, and robustness of mobile wireless networks, but it also requires a mechanism for cluster formation and maintenance.

Some adaptive clustering algorithms for mobile wireless networks are:

- Lowest-ID algorithm: Nodes are assigned unique IDs, and the node with the lowest ID in a neighborhood becomes the clusterhead. This algorithm is simple and deterministic, but it may result in unbalanced clusters or frequent cluster changes due to node mobility.
- Highest-Degree algorithm: Nodes are assigned degrees based on the number of neighbors they have, and the node with the highest degree in a neighborhood becomes the clusterhead. This algorithm is more balanced and stable than the Lowest-ID algorithm, but it may require more communication overhead to update the degrees of nodes.
- Weighted Clustering algorithm: Nodes are assigned weights based on multiple factors, such as degree, mobility, battery power, and distance, and the node with the lowest weight in a neighborhood becomes the clusterhead. This algorithm is more flexible and adaptive than the previous algorithms, but it may require more computation overhead to calculate the weights of nodes.



# File system for mobile computing

A file system is a software component that manages the storage and retrieval of data on a persistent device. A file system for mobile computing is a file system that supports the mobility of both users and devices in a distributed network environment. Some of the challenges and design issues for a file system for mobile computing are:

- Data management issues: How to handle the heterogeneity of devices, data formats, and access methods in a mobile network? How to ensure the consistency, availability, and security of data across different locations and devices? How to cope with the limited and variable bandwidth, latency, and reliability of wireless communication?
- Data replication for mobile computers: How to replicate data among multiple servers and clients to improve performance, fault tolerance, and availability? How to synchronize the replicas when the network connectivity is intermittent or unreliable? How to resolve conflicts and maintain consistency among replicas? How to balance the trade-off between replication and storage overhead?
- Adaptive clustering for mobile wireless networks: How to organize the mobile devices into logical groups or clusters based on their physical proximity, network connectivity, or application interests? How to dynamically adjust the cluster membership and structure according to the mobility and network conditions? How to efficiently route data and messages within and across clusters? How to manage the resources and load among cluster members?

One example of a file system for mobile computing is Coda, which is a distributed file system that supports disconnected operation for mobile clients. Coda has the following features :

- High performance through client-side persistent caching: Coda caches files on the local disk of the client, which reduces the network traffic and improves the response time. Coda also supports write-back caching, which allows the client to defer the propagation of updates to the server until the network is available.
- Server replication: Coda replicates files among multiple servers, which enhances the availability and fault tolerance of the file system. Coda also supports dynamic server selection, which allows the client to choose the best server based on the network conditions and the server load.
- Security model for authentication, encryption and access control: Coda uses Kerberos for authentication, which verifies the identity of the users and servers. Coda also uses encryption to protect the data and messages from eavesdropping and tampering. Coda also supports access control lists (ACLs) for each file and directory, which specify the permissions of different users and groups.
- Continued operation during partial network failures: Coda can handle network partitions, which occur when some servers or clients are isolated from the rest of the network due to network failures or mobility. Coda allows the clients to continue to access and modify the cached files in their local disk, and the servers to continue to serve the requests from the connected clients. Coda also supports reconciliation, which is the process of merging the updates from different partitions when the network connectivity is restored.
- Network bandwidth adaptation: Coda can adapt to the changes in the network bandwidth, which vary depending on the wireless signal strength, the network congestion, and the user mobility. Coda uses different modes of operation, such as hoarding, weakly connected, and fully connected, to optimize the network usage and performance. Coda also supports bandwidth estimation, which measures the available bandwidth and adjusts the data transfer rate accordingly.



# Disconnected operations

- Disconnected operations are a mode of operation in mobile computing that allows users to execute applications when the network is unavailable or unreliable .
- Disconnected operations can be voluntary or involuntary, depending on the user's choice or the network conditions .
- Disconnected operations require mechanisms to handle data consistency, synchronization, and recovery when the network is reconnected  .
- Disconnected operations can benefit from data replication, which is the process of maintaining multiple copies of data on different servers or devices .
- Data replication can improve data availability, performance, and fault tolerance in mobile computing, but also introduces challenges such as replica management, conflict resolution, and bandwidth consumption .
- Adaptive clustering is a technique to organize mobile devices into groups based on their proximity, connectivity, and mobility patterns.
- Adaptive clustering can facilitate data replication and synchronization among mobile devices, as well as reduce the communication overhead and energy consumption.
- Adaptive clustering can also support collaborative applications, load balancing, and distributed processing in mobile computing.



## Unit 4 - Mobile Agents computing, security and fault tolerance, transaction processing in mobile computing

- Mobile agents are software components that can autonomously migrate from one computer to another in a network and resume their execution on the destination computer   .
- Mobile agents have advantages such as reducing network traffic, overcoming network latency, adapting to dynamic environments, and enhancing fault tolerance  .
- Mobile agents also face challenges such as security threats, malicious hosts, communication failures, and resource constraints  .
- Security and fault tolerance are two important aspects of mobile agent systems that ensure the reliability and integrity of mobile agents and their tasks     .
- Security mechanisms for mobile agents include encryption, authentication, digital signatures, access control, firewalls, and intrusion detection   .
- Fault tolerance mechanisms for mobile agents include replication, checkpointing, recovery, migration, and transactional models   .
- Transaction processing in mobile computing is the execution of transactions that involve mobile hosts, such as laptops, smartphones, or tablets, that access shared data in a database    .
- Transaction processing in mobile computing faces challenges such as network disconnection, data inconsistency, concurrency control, and commit protocols    .
- Transaction models for mobile computing include flat transactions, nested transactions, open-nested transactions, reporting transactions, and semantic transactions    .
- Transaction models for mobile computing aim to provide atomicity, consistency, isolation, and durability (ACID) properties, as well as flexibility, adaptability, and scalability    .



# Environment for Mobile Agents Computing

- A mobile agent is a piece of software that can move from one host to another in a network, carrying its state and data, and executing autonomously.
- A mobile agent environment is the infrastructure that supports the creation, migration, execution, and communication of mobile agents.
- A mobile agent environment consists of the following components:
  - A mobile agent platform: a software layer that provides the basic services and resources for mobile agents, such as agent creation, migration, execution, security, and communication.
  - A mobile agent language: a programming language or a framework that enables the development of mobile agents, such as Java, Python, or Aglets.
  - A mobile agent system: a collection of mobile agent platforms that cooperate to support the mobility and interoperability of mobile agents across different hosts and networks.
- A mobile agent environment can be classified according to the following criteria:
  - The mobility model: the way mobile agents move from one host to another, such as strong mobility (the agent preserves its entire state and execution point) or weak mobility (the agent preserves only its data and restarts its execution).
  - The communication model: the way mobile agents communicate with each other and with other entities, such as message passing, remote procedure call, or tuple spaces.
  - The security model: the way mobile agents protect themselves and their hosts from malicious attacks, such as encryption, authentication, access control, or sandboxing.
- A mobile agent environment can provide several benefits for mobile computing applications, such as :
  - Reducing network traffic and latency by moving computation closer to data sources or destinations.
  - Enhancing scalability and fault tolerance by distributing tasks among multiple hosts and agents.
  - Supporting dynamic and adaptive behavior by allowing agents to react to changing network conditions and user preferences.
  - Enabling interoperability and integration by allowing agents to interact with heterogeneous systems and platforms.



# Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over wireless links.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved by using GPS, signal strength, angle of arrival, or other techniques.
- MAC (Medium Access Control) issues refer to the challenges of coordinating the access of multiple nodes to the shared wireless medium, avoiding collisions, and maximizing throughput. Some of the MAC protocols for ad hoc networks are CSMA/CA, MACA, MACAW, FAMA, and IEEE 802.11.
- Routing protocols are algorithms that enable the nodes in an ad hoc network to discover and maintain routes to each other. Routing protocols can be classified into proactive, reactive, or hybrid, depending on whether they maintain routes constantly, on-demand, or both.
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks that uses link state information to compute the shortest paths between nodes. Each node periodically broadcasts its link state to all other nodes, and maintains a complete topology map of the network. GSR suffers from high overhead and scalability issues.



# Destination sequenced distance vector routing (DSDV)

- Destination sequenced distance vector routing (DSDV) is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- It adds a new attribute, sequence number, to each route table entry of the conventional Routing Information Protocol (RIP).
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- A limitation of DSDV is that it provides only one route for a source/destination pair.
- DSDV is also based on distance vector routing and thus uses bidirectional links.
- DSDV requires each node to periodically broadcast routing updates.
- This is a table driven algorithm based on modifications made to the Bellman-Ford routing mechanism.
- DSDV can be classified into two categories: full dump and incremental.
- Full dump broadcasts the entire routing table to the neighbors, while incremental broadcasts only the entries that have changed since the last update.
- DSDV uses two types of packets for routing updates: update packets and request packets.
- Update packets contain the routing information, such as destination address, next hop, number of hops, and sequence number.
- Request packets are used to request routing information from the neighbors when a node does not have a route to a destination.
- DSDV maintains two tables: a routing table and a neighbor table.
- The routing table stores the routing information for each destination, such as next hop, number of hops, sequence number, and a flag to indicate the status of the route.
- The neighbor table stores the information about the neighbors, such as their addresses, sequence numbers, and the status of the link.
- DSDV uses two rules to update the routing table:
  - If a new route has a higher sequence number than the existing one, it replaces the existing one.
  - If a new route has the same sequence number as the existing one, but a lower metric (number of hops), it replaces the existing one.
- DSDV also uses a settling time to reduce the fluctuations in the routing table.
- The settling time is the time interval between receiving a routing update and broadcasting it to the neighbors.
- If a node receives a better route for a destination within the settling time, it cancels the previous update and broadcasts the new one.
- DSDV has some advantages and disadvantages:
  - Advantages:
    - It avoids routing loops by using sequence numbers.
    - It provides consistent and up-to-date routing information.
    - It is simple and easy to implement.
  - Disadvantages:
    - It generates a lot of overhead due to periodic updates.
    - It wastes bandwidth and battery power by broadcasting unnecessary updates.
    - It does not support multipath routing.
    - It does not adapt well to dynamic network topology.



# Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing instead of relying on the routing table at each intermediate node .
- Source routing means that the source node specifies the complete sequence of nodes to the destination in the packet header .
- DSR consists of two main mechanisms: route discovery and route maintenance .
- Route discovery is the process of finding a route from the source to the destination when there is no cached route available .
- Route discovery involves sending a route request packet that is flooded through the network until it reaches the destination or a node with a cached route to the destination .
- The route request packet contains the source and destination addresses, a unique identification number, and a list of nodes that have forwarded the packet .
- The destination or the intermediate node with a cached route sends a route reply packet back to the source along the reverse path of the route request .
- The route reply packet contains the source and destination addresses, the identification number, and the list of nodes that form the route .
- The source node caches the route for future use and sends the data packets along the route .
- Route maintenance is the process of detecting and repairing link failures along the route .
- Route maintenance involves sending route error packets when a node detects a link failure or receives a packet with an unknown destination .
- The route error packet contains the source and destination addresses, the identification number, and the list of nodes that are unreachable .
- The node that receives the route error packet removes the failed link from its cache and propagates the route error packet to the source or any upstream node that uses the failed link .
- The source node or the upstream node initiates a new route discovery if it still needs to communicate with the destination .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages:
  - It reduces the control overhead by eliminating periodic updates and using caching .
  - It supports multiple routes to the same destination and allows load balancing and route selection .
  - It adapts quickly to topology changes and node mobility .
- Disadvantages:
  - It may cause high latency and overhead during route discovery .
  - It may consume more bandwidth and energy due to source routing and flooding .
  - It may suffer from stale routes and routing loops due to caching .



# Ad Hoc On-Demand Distance Vector Routing (AODV)

- AODV is a **reactive** routing protocol for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations **on demand** and supports both **unicast** and **multicast** routing .
- AODV uses **routing tables** with one entry for each destination and **sequence numbers** to validate routing information and prevent routing loops .
- AODV uses three types of control messages: **Route Request (RREQ)**, **Route Reply (RREP)** and **Route Error (RERR)**  .
- AODV operates as follows   :
  - When a source node wants to send a packet to a destination node, it first checks its routing table for a valid route. If no route is found, it broadcasts a RREQ message to its neighbors.
  - The RREQ message contains the source and destination addresses, the source and destination sequence numbers, a broadcast ID and a hop count. The broadcast ID and the source address uniquely identify a RREQ message.
  - Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node and forwards the RREQ message to its neighbors, unless it has a valid route to the destination node with a higher or equal sequence number than the one in the RREQ message. In that case, it unicasts a RREP message back to the source node along the reverse route.
  - The RREP message contains the source and destination addresses, the destination sequence number, a hop count and a lifetime. The destination sequence number indicates the freshness of the route and the lifetime indicates how long the route is valid.
  - When the source node receives the RREP message, it updates its routing table with a forward route to the destination node and starts sending data packets along the route.
  - If a link break occurs in the route, the upstream node that detects the link break sends a RERR message to the source node, indicating the unreachable destinations. The RERR message contains the source and destination addresses, the destination sequence number and a list of unreachable destinations.
  - When the source node receives the RERR message, it invalidates the route to the destination node and initiates a new route discovery process if needed.



# Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated on-demand routing protocol that was proposed by Park and Corson in 1997 .
- TORA is designed for wireless mobile ad hoc networks that are highly dynamic and have frequent topology changes .
- TORA is based on the concept of link reversal, which is a technique to re-establish routes after link failures without global network information .
- TORA consists of three main phases: route creation, route maintenance, and route erasure  .
  - Route creation: When a source node wants to send data to a destination node, it broadcasts a query packet containing the destination ID. The query packet propagates through the network until it reaches the destination or a node that has a route to the destination. The nodes that receive the query packet assign themselves a height metric based on their distance from the destination. The height metric is used to create a directed acyclic graph (DAG) rooted at the destination. The nodes that have a lower height than their neighbors are downstream nodes, and the nodes that have a higher height than their neighbors are upstream nodes. The upstream nodes send update packets to their downstream nodes to inform them of their height and establish routes. The source node receives an update packet from one of its downstream nodes and selects it as the next hop to the destination.
  - Route maintenance: When a link failure occurs, the nodes that are affected by the link failure adjust their height metrics to reflect the new topology. The nodes that lose all their downstream neighbors increase their height to a value higher than their highest neighbor and broadcast a clear packet to invalidate the routes that use the failed link. The clear packet triggers a new route creation phase to re-establish the routes.
  - Route erasure: When a source node no longer needs a route to a destination node, it broadcasts a clear packet containing the destination ID. The clear packet propagates through the network and erases all the routes to the destination. The nodes that receive the clear packet reset their height metrics to null.
- TORA has some advantages and disadvantages as a routing protocol for ad hoc networks  .
  - Advantages:
    - TORA is highly adaptive and scalable to large and dense networks.
    - TORA minimizes the control overhead by using local information and avoiding global network updates.
    - TORA avoids routing loops by using the height metric and the DAG structure.
    - TORA supports multiple routes to the same destination, which increases the reliability and load balancing of the network.
  - Disadvantages:
    - TORA may create long and suboptimal routes due to the link reversal technique and the propagation delay of the control packets.
    - TORA may generate a large number of control packets in the presence of frequent link failures, which consumes bandwidth and energy.
    - TORA does not consider the quality of service (QoS) parameters such as delay, bandwidth, and reliability in the route selection process.
    - TORA does not provide security mechanisms to prevent malicious attacks on the routing protocol.



# QoS in Ad Hoc Networks

- Quality of service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc. 
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or centralized control. 
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes and applications.  
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.  
- QoS in ad hoc networks can be classified into two categories: hard QoS and soft QoS. Hard QoS guarantees the QoS requirements of the applications with strict bounds, while soft QoS provides the best-effort QoS with statistical guarantees.  
- QoS in ad hoc networks can be supported by various mechanisms, such as QoS-aware routing, QoS-aware MAC, QoS-aware scheduling, QoS-aware admission control, QoS-aware resource allocation, QoS-aware cross-layer optimization, etc.   
- QoS in ad hoc networks can be evaluated by various metrics, such as throughput, delay, jitter, packet loss, packet delivery ratio, energy consumption, etc.   
- QoS in ad hoc networks can be improved by various techniques, such as adaptive QoS, cooperative QoS, distributed QoS, multipath QoS, etc.   
- QoS in ad hoc networks is an active research area that aims to provide better QoS for various applications and scenarios, such as multimedia, real-time, emergency, vehicular, etc.



# Applications of Ad Hoc Networks

Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of nodes that communicate with each other directly or through intermediate nodes. Ad hoc networks have many potential applications in various domains, such as:

- **Military battlefield**: Ad hoc networks can provide secure and robust communication among soldiers, vehicles, and command centers in hostile environments. They can also support situational awareness, target tracking, and data fusion.
- **Vehicular ad hoc networks (VANETs)**: Ad hoc networks can enable vehicles to exchange information about traffic conditions, road safety, navigation, and entertainment. They can also support intelligent transportation systems, such as collision avoidance, platooning, and cooperative driving .
- **Smartphone ad hoc networks (SPANs)**: Ad hoc networks can allow smartphones to form peer-to-peer networks without relying on cellular or Wi-Fi networks. They can enable users to share data, resources, and services, such as file transfer, chat, gaming, and social networking .
- **Wireless sensor networks (WSNs)**: Ad hoc networks can connect a large number of sensor nodes that collect and process data from the physical environment. They can support various applications, such as environmental monitoring, health care, smart homes, and industrial automation.
- **Disaster relief and emergency response**: Ad hoc networks can provide communication and coordination among rescue workers, victims, and authorities in scenarios where the existing infrastructure is damaged or unavailable. They can also support disaster management, such as search and rescue, damage assessment, and resource allocation.
- **Industrial and commercial applications**: Ad hoc networks can facilitate cooperative mobile data exchange among workers, customers, and devices in various settings, such as factories, warehouses, offices, and retail stores. They can also support business operations, such as inventory management, asset tracking, and customer service.

