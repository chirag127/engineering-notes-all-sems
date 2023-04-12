

# Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks.
- Mobile computing enables users to communicate, access information, and perform tasks anytime and anywhere, without being constrained by physical location or wired connections.
- Mobile computing involves various components, such as mobile devices, wireless networks, mobile applications, and mobile middleware.
- Mobile computing faces various issues and challenges, such as limited battery life, security and privacy, network heterogeneity, mobility management, data synchronization, and quality of service.
- Wireless telephony is the transmission and reception of voice signals over wireless networks, such as cellular networks, satellite networks, and radio networks.
- Wireless telephony enables users to make and receive phone calls without being tethered to a landline or a fixed location.
- Wireless telephony has evolved from the first generation (1G) analog networks to the fifth generation (5G) digital networks, offering improved voice quality, data services, and network capacity.
- Cellular concept is the basic principle of wireless telephony, which divides a large geographical area into smaller regions called cells, each served by a base station.
- Cellular concept allows multiple users to share the same frequency band by using different channels within each cell, and by reusing the same channels in different cells that are sufficiently apart to avoid interference.
- Cellular concept enables wireless telephony to achieve high spectral efficiency, coverage, and capacity, by using techniques such as frequency reuse, cell splitting, and handover.
- GSM (Global System for Mobile communication) is a standard developed by the European Telecommunications Standards Institute (ETSI) to describe the protocols for second-generation (2G) digital cellular networks used by mobile devices such as mobile phones and tablets.
- GSM uses a variation of time division multiple access (TDMA) and frequency division multiple access (FDMA) to multiplex multiple users on the same frequency band .
- GSM operates on four different frequency bands: 850 MHz, 900 MHz, 1800 MHz, and 1900 MHz, depending on the region and the operator .
- GSM provides various services, such as voice calls, text messages, data transmission, roaming, and encryption .
- GSM consists of three main components: the mobile station (MS), the base station subsystem (BSS), and the network and switching subsystem (NSS) .
- The mobile station (MS) is the user's device, such as a mobile phone or a tablet, that communicates with the base station over the air interface.
- The base station subsystem (BSS) consists of the base transceiver station (BTS) and the base station controller (BSC), which manage the radio resources and the communication between the mobile station and the network.
- The network and switching subsystem (NSS) consists of the mobile switching center (MSC), the home location register (HLR), the visitor location register (VLR), the authentication center (AUC), and the equipment identity register (EIR), which perform the functions of call routing, subscriber management, authentication, and security.



# Air-interface for Mobile Computing

- The air interface is the communication link between the two stations in mobile or wireless communication.
- The air interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection.
- The air interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network.
- The air interface is also called a "radio interface" or the "UM interface" as it is analogous to U interface of ISDN .
- The air interface is the wireless counterpart of the physical layer 1 in the OSI model.
- The air interface is the technology used for the radio transmission between mobile devices and the base station in a cellular network.
- The air interface of different cellular systems may use different modulation techniques, such as TDMA and CDMA for GSM and CDMA networks respectively, and OFDMA for LTE networks .
- The air interface waveform of LTE and NR, like many other modern digital communication standards, is based on orthogonal frequency division multiplexing (OFDM).
- OFDM is highly spectrally efficient and allows high data rate transmission with low receiver complexity even in a dispersive radio channel.
- The air interface is one of the key components of mobile computing, as it enables the wireless communication between mobile devices and the network infrastructure.



# Channel Structure for Mobile Computing

- Mobile computing is the use of wireless devices and networks to access, process, and transmit data and services.
- Wireless telephony is the technology of providing voice and data communication over wireless channels, such as cellular networks, satellite networks, and radio networks.
- Cellular concept is the idea of dividing a large geographic area into smaller cells, each with its own base station and frequency allocation, to increase the capacity and coverage of wireless networks.
- GSM (Global System for Mobile Communications) is a standard for digital cellular networks that uses time division multiple access (TDMA) to divide each frequency channel into eight time slots, each carrying a burst of data or voice.
- Channel structure is the way of organizing the physical and logical channels in a wireless network to carry different types of information and signals.

## Physical Channels

- Physical channels are the basic units of transmission in a wireless network, defined by the frequency and the time slot used by a transmitter and a receiver.
- In GSM, each frequency channel has a bandwidth of 200 kHz and is divided into eight time slots, each lasting 0.577 ms. Each time slot can carry one burst of data or voice, which is 156.25 bits long.
- A physical channel can be either full-rate or half-rate, depending on the number of time slots used by a user. A full-rate channel uses one time slot per frame (4.615 ms), while a half-rate channel uses one time slot every two frames (9.23 ms).
- A physical channel can also be either uplink or downlink, depending on the direction of transmission. An uplink channel is used by a mobile station to transmit to a base station, while a downlink channel is used by a base station to transmit to a mobile station.

## Logical Channels

- Logical channels are the types of information and signals carried by the physical channels, such as traffic, control, and broadcast.
- In GSM, there are three types of logical channels: traffic channels (TCHs), control channels (CCHs), and the cell broadcast channel (CBCH) .
- Traffic channels are used to carry user data and voice between a mobile station and a base station. They can be either full-rate or half-rate, depending on the data rate and the codec used.
- Control channels are used to carry signaling and management information between a mobile station and a base station, such as synchronization, authentication, paging, location update, handover, and power control. They can be either common or dedicated, depending on the scope and the purpose of the information.
- The cell broadcast channel is used to transmit short messages to all mobile stations in a cell, such as emergency alerts, weather reports, or advertisements. It is a downlink-only channel that uses one time slot per frame.

## Channel Allocation

- Channel allocation is the process of assigning physical and logical channels to users and base stations in a wireless network, to optimize the performance and the quality of service.
- Channel allocation strategies can be classified into fixed, dynamic, hybrid, and borrowing, depending on the criteria and the flexibility of the allocation .
- Fixed channel allocation assigns a fixed number of channels to each cell, regardless of the traffic demand. It is simple and efficient, but it may cause channel wastage or congestion in some cells.
- Dynamic channel allocation assigns channels to cells on demand, based on the traffic load and the interference level. It is adaptive and flexible, but it may cause channel fragmentation or overhead in some cases.
- Hybrid channel allocation combines fixed and dynamic allocation, by reserving some channels for each cell and sharing the rest among neighboring cells. It is a compromise between simplicity and adaptability, but it may require complex coordination and signaling.
- Borrowing channel allocation allows a cell to borrow channels from neighboring cells when its own channels are not enough. It is a form of dynamic allocation, but it may cause interference or conflict with the original owners of the channels.



# Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile users in a wireless cellular network.
- Location management consists of two main functions: location update and location lookup.
- Location update is the process of informing the network about the current location of a mobile user when it moves from one location area to another.
- Location lookup is the process of finding the current location of a mobile user when a call or a message is destined to it.
- Location management aims to minimize the signaling overhead and the delay involved in locating mobile users.
- Location management schemes can be classified into two types: centralized and distributed.
- Centralized schemes use a single database to store the location information of all mobile users, such as the home location register (HLR) in GSM networks.
- Distributed schemes use multiple databases to store the location information of mobile users, such as the visitor location registers (VLRs) in GSM networks.
- HLR-VLR is a hierarchical distributed scheme that divides the service area into location areas (LAs), each with a VLR.
- HLR is a database that contains the subscription information and some location information of all mobile users in the network.
- VLR is a database that contains the information of the mobile users that are currently visiting its LA.
- When a mobile user moves from one LA to another, it performs a location update to the new VLR, which then contacts the HLR to obtain the user's information.
- When a call or a message is destined to a mobile user, the network queries the HLR to find the VLR that serves the user's current LA, and then queries the VLR to find the user's current cell.
- Handoff is the process of transferring an ongoing call or a data session from one cell or channel to another without interrupting the service.
- Handoff is necessary when a mobile user moves out of the coverage area of the current cell or when the current cell or channel becomes congested or interfered.
- Handoff can be classified into two types: hard handoff and soft handoff.
- Hard handoff is the process of breaking the connection with the current cell or channel before establishing a new connection with the target cell or channel.
- Soft handoff is the process of establishing a new connection with the target cell or channel before breaking the connection with the current cell or channel.
- Handoff can also be classified into two types: horizontal handoff and vertical handoff.
- Horizontal handoff is the process of transferring a call or a data session from one cell or channel to another within the same network or technology.
- Vertical handoff is the process of transferring a call or a data session from one network or technology to another, such as from cellular to Wi-Fi.
- Handoff aims to maintain the quality of service and the continuity of service for mobile users.
- Handoff involves three main phases: handoff initiation, handoff decision, and handoff execution.
- Handoff initiation is the phase of detecting the need for a handoff based on some criteria, such as signal strength, signal quality, or user preference.
- Handoff decision is the phase of selecting the target cell or channel for the handoff based on some criteria, such as availability, capacity, or cost.
- Handoff execution is the phase of switching the connection from the current cell or channel to the target cell or channel without interrupting the service.



# Channel Allocation in Cellular Systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- When a user wants to make a call request, then by using channel allocation strategies, their requests are fulfilled.
- Channel allocation strategies are designed in such a way that there is efficient use of frequencies, time slots and bandwidth .
- The channel is allocated following an algorithm which accounts the following criteria:
  - Future blocking probability in neighboring cells and reuse distance
  - Usage frequency of the candidate channel
  - Average blocking probability of the overall system
  - Instantaneous channel occupancy distribution
- There are three types of channel allocation schemes:
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels and the channels are not shared among the cells. If all the channels in a cell are occupied, then the call request is blocked or handed over to another cell.
  - Dynamic channel allocation (DCA): The channels are not permanently assigned to the cells, but are allocated on demand according to the traffic conditions. The channels are shared among the cells and the allocation algorithm tries to minimize the interference and maximize the utilization.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed for each cell and some are dynamically allocated. This scheme can balance the trade-off between performance and complexity.



# CDMA for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- CDMA stands for Code Division Multiple Access and is a spread spectrum multiple access technique  .
- Spread spectrum technique spreads bandwidth of data in a uniform manner for the same transmitted power.
- CDMA is a digital cellular technology used for mobile communication .
- CDMA is the base on which access methods such as cdmaOne, CDMA2000, and WCDMA are built .
- CDMA allows numerous signals to occupy a single transmission channel, optimizing the use of available bandwidth .
- CDMA uses codes to differentiate between multiple users sharing the same frequency .
- CDMA has advantages such as increased capacity, improved voice quality, enhanced security, and reduced interference .
- CDMA has disadvantages such as complex receiver design, synchronization issues, and power control problems .
- CDMA is one of the multiple access techniques in mobile computing, along with FDMA (Frequency Division Multiple Access) and TDMA (Time Division Multiple Access).
- FDMA divides the frequency spectrum into distinct channels and assigns one channel to each user.
- TDMA divides the time into slots and assigns one slot to each user in a cyclic manner.
- CDMA, FDMA, and TDMA are used to achieve efficient and fair allocation of resources among multiple users in a wireless network.
- CDMA is compatible with other cellular technologies such as GSM (Global System for Mobile Communications), which is the most widely used standard for mobile telephony .
- GSM is a cellular concept that divides a geographical area into cells, each served by a base station .
- GSM uses a combination of FDMA and TDMA to multiplex users on the same channel .
- GSM provides services such as voice, data, SMS, and roaming .
- GSM has advantages such as international compatibility, low-cost handsets, and high-quality voice .
- GSM has disadvantages such as limited data rates, security vulnerabilities, and spectrum inefficiency .
- CDMA and GSM are examples of wireless telephony, which is the transmission of voice and data over a wireless network .
- Wireless telephony is a part of mobile computing, which is the use of computing devices that can communicate wirelessly and are portable .
- Mobile computing has issues such as mobility, heterogeneity, scalability, security, and energy efficiency .
- Mobile computing has applications such as e-commerce, e-learning, e-health, social networking, and location-based services .
- Mobile computing has challenges such as network availability, bandwidth limitations, device diversity, user interface design, and data synchronization .



# GPRS for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- GPRS stands for **General Packet Radio Service** .
- It is a **packet oriented wireless data communication service** for mobile communications on **2G and 3G cellular networks**  .
- It is **non-voice**, high speed packet switching technology intended for GSM networks .
- It enables **moderately high-speed data transfers** using packet-based technologies .
- It offers more data transmission options for GSM-based devices, as GSM networks at the time could only use Short Message Service (SMS), for example, to transmit a small amount of data.
- It establishes a **connected mobile environment** for IoT applications.
- It supports **multiple users** on a single channel by using **statistical multiplexing**.
- It uses **logical channels** to transmit data packets between mobile stations and the network.
- It has two main classes of logical channels: **Packet Data Channels (PDCHs)** and **Packet Control Channels (PCCHs)**.
- PDCHs are used to carry user data and network control information.
- PCCHs are used to carry signaling information between the mobile station and the network.
- It has two main network elements: **Serving GPRS Support Node (SGSN)** and **Gateway GPRS Support Node (GGSN)**.
- SGSN is responsible for **authentication, encryption, mobility management, and session management** of the mobile stations.
- GGSN is responsible for **interfacing with external packet data networks** and routing data packets to and from the SGSN.
- It has four main modes of operation: **Idle mode, Ready mode, Standby mode, and Transfer mode**.
- Idle mode is when the mobile station is **not attached** to the GPRS network and **cannot send or receive** data packets.
- Ready mode is when the mobile station is **attached** to the GPRS network and has a **temporary logical link** with the SGSN.
- Standby mode is when the mobile station is **attached** to the GPRS network but has a **dormant logical link** with the SGSN.
- Transfer mode is when the mobile station is **sending or receiving** data packets over the PDCHs.
- It has several advantages, such as:
  - **Higher data rates** than circuit-switched services .
  - **Efficient use of radio resources** by sharing channels among multiple users .
  - **Always-on connectivity** without occupying a dedicated channel .
  - **Flexible billing** based on volume or duration of data transfer .
  - **Support for a variety of applications**, such as email, web browsing, multimedia messaging, online gaming, etc. .
- It has some disadvantages, such as:
  - **Limited coverage** in some areas or countries.
  - **Variable data rates** depending on the network congestion and channel quality .
  - **Security risks** due to the possibility of data interception or modification .
  - **Compatibility issues** with some devices or networks .



# Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

## Wireless Networking
- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless networking can provide mobility, convenience, scalability, and cost-effectiveness for users and network administrators.
- Wireless networking can also pose challenges such as security, interference, reliability, and compatibility.

## Wireless LAN Overview
- A wireless LAN (WLAN) is a local area network (LAN) that uses wireless media to connect devices.
- A WLAN typically consists of one or more access points (APs) that provide wireless coverage to a certain area, and one or more wireless stations (STAs) that communicate with the APs.
- A WLAN can operate in two modes: infrastructure mode and ad hoc mode.
  - In infrastructure mode, the STAs associate with an AP and use it as a relay to communicate with other STAs or the wired network.
  - In ad hoc mode, the STAs form a peer-to-peer network without an AP and communicate directly with each other.

## MAC Issues
- The medium access control (MAC) layer is responsible for coordinating the access of multiple STAs to the shared wireless medium.
- The MAC layer faces several issues in wireless networking, such as:
  - Hidden terminal problem: when two STAs are within the range of an AP but not within the range of each other, they may not sense each other's transmissions and cause collisions at the AP.
  - Exposed terminal problem: when a STA is within the range of two APs but not within the range of the intended receiver, it may unnecessarily defer its transmission to avoid interfering with another transmission that does not affect the receiver.
  - Fading and multipath: when the wireless signal is attenuated or distorted by obstacles, reflections, or interference, resulting in reduced signal quality and increased bit error rate.
  - Mobility: when the STAs move within or across the coverage areas of different APs, requiring handoff and reassociation procedures to maintain connectivity.

## IEEE 802.11
- IEEE 802.11 is a family of standards that define the MAC and physical layer (PHY) specifications for WLANs.
- IEEE 802.11 defines several PHY technologies that operate in different frequency bands and offer different data rates, such as:
  - 802.11a: 5 GHz band, up to 54 Mbps
  - 802.11b: 2.4 GHz band, up to 11 Mbps
  - 802.11g: 2.4 GHz band, up to 54 Mbps
  - 802.11n: 2.4 GHz and/or 5 GHz band, up to 600 Mbps
  - 802.11ac: 5 GHz band, up to 6.9 Gbps
  - 802.11ax: 2.4 GHz and/or 5 GHz band, up to 9.6 Gbps
- IEEE 802.11 also defines several MAC features and enhancements, such as:
  - Distributed coordination function (DCF): a basic MAC scheme that uses carrier sense multiple access with collision avoidance (CSMA/CA) and binary exponential backoff to access the medium.
  - Point coordination function (PCF): an optional MAC scheme that uses a centralized controller (point coordinator) to poll the STAs and grant them access to the medium.
  - Quality of service (QoS): a set of MAC mechanisms that provide differentiated services for different traffic classes, such as voice, video, and data.
  - Security: a set of MAC protocols that provide authentication, encryption, and integrity protection for wireless communications, such as wired equivalent privacy (WEP), Wi-Fi protected access (WPA), and WPA2.

## Bluetooth
- Bluetooth is a wireless technology that enables short-range communication between devices, such as phones, headsets, keyboards, mice, printers, etc.
- Bluetooth uses a frequency-hopping spread spectrum (FHSS) technique to hop among 79 channels in the 2.4 GHz band, each with a bandwidth of 1 MHz.
- Bluetooth devices form a piconet, which is a network of up to eight devices, one of which acts as a master and the others as slaves.
- Multiple piconets can be interconnected to form a scatternet, which is a network of multiple masters and slaves.

## Wireless
- Wireless is a broad term that encompasses any communication that does not use wires or cables, such as radio, infrared, microwave, satellite, cellular, etc.



# Multiple Access Protocols

Multiple access protocols are techniques that allow multiple nodes or users to share a common communication channel, such as a wireless network or a satellite network. Multiple access protocols are used to coordinate the access to the channel and avoid collisions or interference among the nodes. There are different types of multiple access protocols, such as:

- **Random access protocols**: These protocols allow any node to transmit at any time without prior coordination. However, there is a possibility of collisions, which means that two or more nodes transmit at the same time and their signals interfere with each other. To deal with collisions, random access protocols use some mechanisms, such as:

  - **ALOHA**: This is the simplest random access protocol, which was used in the ALOHAnet, the first wireless network. In ALOHA, a node transmits a frame whenever it has data to send, without checking the channel status. If the node receives an acknowledgment from the receiver, it means that the transmission was successful. Otherwise, it means that a collision occurred and the node has to retransmit the frame after a random time interval. ALOHA has two variants: pure ALOHA and slotted ALOHA. In pure ALOHA, the node can transmit at any time, while in slotted ALOHA, the node can only transmit at the beginning of a time slot. Slotted ALOHA has a higher throughput than pure ALOHA, because it reduces the probability of collisions.

  - **Carrier-sense multiple access (CSMA)**: This is an improvement over ALOHA, which was used in the Ethernet network. In CSMA, a node senses the channel before transmitting a frame. If the channel is idle, the node transmits the frame. If the channel is busy, the node defers the transmission until the channel becomes idle. CSMA reduces the collisions, but does not eliminate them completely, because of the propagation delay, which is the time it takes for a signal to travel from one node to another. CSMA has three variants: 1-persistent CSMA, non-persistent CSMA, and p-persistent CSMA. In 1-persistent CSMA, the node transmits the frame as soon as the channel is idle, while in non-persistent CSMA, the node waits for a random time interval before sensing the channel again. In p-persistent CSMA, the node transmits the frame with a probability p when the channel is idle, and defers the transmission with a probability 1-p.

  - **CSMA with collision detection (CSMA/CD)**: This is an extension of CSMA, which was used in the wired Ethernet network. In CSMA/CD, a node senses the channel before transmitting a frame, and also monitors the channel during the transmission. If the node detects a collision, it aborts the transmission and sends a jamming signal to inform the other nodes. Then, the node waits for a random time interval before retransmitting the frame. CSMA/CD improves the efficiency of CSMA, because it reduces the wasted time and bandwidth due to collisions.

  - **CSMA with collision avoidance (CSMA/CA)**: This is another extension of CSMA, which was used in the wireless IEEE 802.11 network. In CSMA/CA, a node senses the channel before transmitting a frame, and also performs a handshake with the receiver. The handshake consists of two control frames: request to send (RTS) and clear to send (CTS). The node sends an RTS frame to the receiver, and waits for a CTS frame from the receiver. If the node receives a CTS frame, it means that the channel is reserved for the node and the receiver, and the node can transmit the data frame. If the node does not receive a CTS frame, it means that a collision occurred or the channel is busy, and the node has to defer the transmission. CSMA/CA avoids the collisions, but introduces some overhead due to the control frames.

- **Controlled access protocols**: These protocols require some coordination among the nodes before transmitting a frame. The coordination can be done by a central controller or by the nodes themselves. Controlled access protocols avoid collisions, but may introduce some delay or complexity. Some examples of controlled access protocols are:

  - **Reservation ALOHA (R-ALOHA)**: This is a hybrid protocol that combines random access and controlled access. In R-ALOHA, the channel is divided into two subchannels: a reservation subchannel and a data subchannel. The reservation subchannel uses slotted A



# TCP over wireless

Transmission Control Protocol (TCP) is the most widely used transport layer protocol in the Internet. It provides reliable, in-order and congestion-controlled delivery of data packets. TCP assumes that the underlying network is relatively reliable and that most packet losses are due to congestion. However, in wireless networks, packet losses can occur more frequently due to unreliable wireless links, fading, shadowing, interference, mobility and handoffs. These losses can degrade the performance of TCP, as it may mistakenly invoke congestion control mechanisms and reduce the sending rate. Therefore, TCP needs to be adapted or enhanced to cope with the characteristics of wireless networks.

Some of the challenges and solutions for TCP over wireless networks are:

- **TCP unaware link layer**: In this approach, the link layer protocol tries to recover from wireless losses by using techniques such as error correction, retransmission, interleaving and adaptive modulation. This can reduce the packet loss rate seen by TCP, but it can also increase the delay and jitter, which can affect TCP's timeout and retransmission mechanisms. Moreover, some losses may still occur at the link layer, which can trigger TCP's congestion control. Therefore, this approach alone is not sufficient to improve TCP performance over wireless networks.

- **TCP aware link layer**: In this approach, the link layer protocol informs TCP about the cause of packet losses, such as wireless errors or congestion. This can be done by using explicit notification schemes, such as Explicit Loss Notification (ELN) or Explicit Congestion Notification (ECN), or by using implicit notification schemes, such as Explicit Bad State Notification (EBSN) or Wireless Duplicate Acknowledgements (WDA). Based on this feedback, TCP can adjust its sending rate accordingly, without invoking unnecessary congestion control. This approach can improve TCP performance over wireless networks, but it requires modifications to both the link layer and the TCP layer.

- **Split connection**: In this approach, the TCP connection is split into two sub-connections at the wireless interface, namely, the base station, which in turn uses some other reliable connection to connect to the destination. The base station acts as a proxy for the TCP sender and the TCP receiver, and performs local retransmissions, buffering, rate adaptation and congestion control for the wireless sub-connection. The advantage of this approach is that it isolates the wireless losses from the end-to-end TCP connection, and avoids unnecessary congestion control and timeout at the TCP sender. The disadvantage of this approach is that it breaks the end-to-end semantics of TCP, and introduces additional delay and overhead at the base station.

- **End-to-end enhancement**: In this approach, the TCP sender or the TCP receiver modifies its behavior to cope with wireless losses, without changing the TCP protocol itself. For example, the TCP sender can use selective acknowledgements (SACK) to recover from multiple losses in a window, or use delayed acknowledgements (DACK) to reduce the number of duplicate acknowledgements. The TCP receiver can use fast retransmit and fast recovery (FR/FR) to trigger early retransmissions, or use explicit congestion notification (ECN) to inform the TCP sender about congestion. The advantage of this approach is that it preserves the end-to-end semantics of TCP, and does not require any changes to the intermediate nodes. The disadvantage of this approach is that it may not be able to distinguish between wireless losses and congestion losses, and may still suffer from performance degradation.

- **Cross-layer optimization**: In this approach, the TCP layer interacts with other layers of the protocol stack, such as the physical layer, the link layer, the network layer and the application layer, to obtain information and feedback about the wireless network conditions, such as channel quality, link state, network topology and application requirements. Based on this information, the TCP layer can adapt its parameters and algorithms to optimize its performance over wireless networks. For example, the TCP layer can use adaptive modulation and coding (AMC) at the physical layer, or use adaptive routing and forwarding (ARF) at the network layer, to improve the reliability and efficiency of data transmission. The advantage of this approach is that it can exploit the opportunities and overcome the challenges of wireless networks, and achieve better performance than the traditional layer-based approaches. The disadvantage of this approach is that it requires coordination and cooperation among different layers, and may introduce complexity and overhead to the protocol stack.



# Wireless Applications

Wireless applications are software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, and wireless internet. Wireless applications enable users to access information, services, and entertainment without being constrained by wires or cables. Wireless applications can be classified into different categories based on their functions, such as:

- **Voice applications**: These are applications that allow users to make and receive voice calls over wireless networks, such as cellular phones and voice over IP (VoIP) services. Voice applications can also include features such as voice mail, caller ID, conference calling, and voice recognition.
- **Data applications**: These are applications that allow users to send and receive data over wireless networks, such as text messages, emails, web browsing, file transfer, and cloud computing. Data applications can also include features such as encryption, compression, synchronization, and backup.
- **Multimedia applications**: These are applications that allow users to stream or download multimedia content over wireless networks, such as music, videos, games, and podcasts. Multimedia applications can also include features such as digital rights management, quality of service, and interactive media.
- **Location-based applications**: These are applications that use the location information of the user or the device to provide services or information, such as navigation, weather, traffic, local search, and social networking. Location-based applications can also include features such as geofencing, geotagging, and augmented reality.
- **Sensor applications**: These are applications that use wireless sensors to collect and transmit data from the physical environment, such as temperature, humidity, pressure, motion, and light. Sensor applications can also include features such as data analysis, visualization, and automation.

Wireless applications can be developed using various tools and platforms, such as:

- **Wireless Application Protocol (WAP)**: This is a set of standards that defines how wireless devices can access web content and services. WAP uses a markup language called Wireless Markup Language (WML) and a scripting language called WMLScript to create wireless web pages and applications.
- **Java 2 Platform, Micro Edition (J2ME)**: This is a version of Java that is designed for small and resource-constrained devices, such as mobile phones and PDAs. J2ME provides a set of APIs and libraries that enable developers to create portable and secure wireless applications.
- **Android**: This is an open-source operating system and platform that is based on Linux and Java. Android provides a rich set of APIs and libraries that enable developers to create powerful and innovative wireless applications for smartphones and tablets.
- **iOS**: This is an operating system and platform that is developed by Apple for its devices, such as iPhone and iPad. iOS provides a set of APIs and libraries that enable developers to create elegant and intuitive wireless applications for its devices.
- **Windows Phone**: This is an operating system and platform that is developed by Microsoft for its devices, such as Lumia and Surface. Windows Phone provides a set of APIs and libraries that enable developers to create modern and dynamic wireless applications for its devices.



# Data Broadcasting for Wireless Networking

- Data broadcasting is a group communication, where a sender sends data to receivers simultaneously .
- Data broadcasting can be an efficient way of information dissemination in wireless networks, especially when the client demands are local or correlated.
- Data broadcasting can be performed using different techniques, such as push, pull, or hybrid.
  - Push: The server broadcasts data periodically without waiting for client requests. Clients can tune in to the broadcast channel and receive the data they need. This technique is suitable for popular or time-sensitive data.
  - Pull: The server broadcasts data only in response to client requests. Clients can send their queries to the server and wait for the data to be delivered. This technique is suitable for personalized or rare data.
  - Hybrid: The server broadcasts data using a combination of push and pull techniques. Clients can either receive data from the periodic broadcast or send requests to the server. This technique can balance the trade-off between server load and client latency.
- Data broadcasting can be improved using different methods, such as network coding, cooperation, or smart antennas.
  - Network coding: The server encodes the data using linear combinations of packets before broadcasting. Clients can decode the data using the received packets and their own packets. This method can increase the throughput and reduce the number of transmissions.
  - Cooperation: The clients cooperate with each other by relaying the data they receive to other clients. This method can enhance the coverage and reliability of the broadcast.
  - Smart antennas: The server uses directional antennas to broadcast data to different regions or clients. This method can reduce the interference and increase the capacity of the broadcast.



# Mobile IP

Mobile IP is a communication protocol that allows mobile device users to move from one network to another while maintaining the same permanent IP address. Mobile IP is an extension of the Internet Protocol (IP) and is defined by the Internet Engineering Task Force (IETF) in RFC 2002 and RFC 5944.

## Overview of Mobile IP

Mobile IP enables seamless and continuous Internet connectivity for mobile devices. Mobile IP is useful for roaming between overlapping wireless systems, such as WLAN, WiMAX, and cellular networks. Mobile IP can also support mobility across different types of networks, such as wired and wireless LANs.

Mobile IP works by using two types of IP addresses: a home address and a care-of address. The home address is the permanent IP address of the mobile device, which belongs to its home network. The care-of address is the temporary IP address of the mobile device, which belongs to the current network that the device is visiting. The care-of address changes as the device moves from one network to another.

Mobile IP also uses three types of entities: a home agent, a foreign agent, and a mobile node. The home agent is a router on the home network that maintains a binding between the home address and the care-of address of the mobile device. The foreign agent is a router on the visited network that provides routing services to the mobile device. The mobile node is the mobile device that uses Mobile IP to communicate with other nodes on the Internet.

The basic operation of Mobile IP is as follows:

- When the mobile node is on its home network, it communicates with other nodes using its home address as the source and destination IP address.
- When the mobile node moves to a foreign network, it obtains a care-of address from the foreign agent or by using DHCP. The mobile node then registers its care-of address with its home agent, which creates a binding entry in its binding cache.
- The home agent intercepts any packets destined to the home address of the mobile node and tunnels them to the care-of address of the mobile node. The foreign agent decapsulates the packets and delivers them to the mobile node.
- The mobile node can also send packets to other nodes using its home address as the source IP address. The foreign agent encapsulates the packets and tunnels them to the home agent, which decapsulates the packets and forwards them to the destination node.

## Advantages and Disadvantages of Mobile IP

Some of the advantages of Mobile IP are:

- It supports transparent mobility for mobile devices across different networks and subnets.
- It preserves the existing IP applications and security mechanisms without requiring any modifications.
- It is scalable and compatible with the Internet infrastructure and standards.

Some of the disadvantages of Mobile IP are:

- It introduces additional overhead and latency due to the tunneling and encapsulation processes.
- It may cause suboptimal routing and increased network congestion due to the triangular routing problem.
- It may suffer from security issues such as spoofing, replay, and denial-of-service attacks.

## References

: Mobile IP | What is Mobile IP - javatpoint. https://www.javatpoint.com/what-is-mobile-ip
: Mobile IP - Wikipedia. https://en.wikipedia.org/wiki/Mobile_IP
: Introduction to Mobile IP - Cisco. https://www.cisco.com/c/en/us/td/docs/ios/solutions_docs/mobile_ip/mobil_ip.html
: How to Find Your Phone's IP Address on Android or iPhone - MUO. https://www.makeuseof.com/tag/find-ip-address-mobile-smartphone/



# WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer is of most interest to content developers because it contains among other things, device specifications, scripting languages, and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems. The application layer also includes the Wireless Application Environment (WAE), which provides a framework for developing and delivering applications and services over wireless networks.
  - Session Layer: This layer provides a reliable session service between applications, based on a request-response paradigm. The session layer uses the Wireless Session Protocol (WSP), which is a binary-encoded version of the HTTP protocol, optimized for low-bandwidth and high-latency wireless links.
  - Transaction Layer: This layer provides a lightweight transaction service on top of the session layer, based on a two-phase commit protocol. The transaction layer uses the Wireless Transaction Protocol (WTP), which supports reliable and unreliable datagram service, and user datagram service.
  - Security Layer: This layer provides data integrity and privacy services for the wireless network, based on encryption and authentication mechanisms. The security layer uses the Wireless Transport Layer Security (WTLS), which is derived from the TLS protocol, but adapted for the wireless environment.
  - Transport Layer: This layer provides a common interface for the upper layers to access different wireless bearers, such as GSM, CDMA, TDMA, SMS, etc. The transport layer uses the Wireless Datagram Protocol (WDP), which is a general datagram service that can be mapped to any available wireless data service.
- The WAP architecture also includes several components, each serving a specific function. These components include:
  - WAP Client: This is the wireless device that runs a micro-browser and interacts with the WAP gateway. The WAP client can be a mobile phone, a PDA, a pager, or any other device that supports WAP.
  - WAP Gateway: This is the intermediary between the wireless network and the internet. The WAP gateway performs several functions, such as protocol translation, content encoding and decoding, security services, and caching. The WAP gateway can be a standalone server or a cluster of servers.
  - WAP Server: This is the server that hosts the WAP applications and content. The WAP server can be a web server, an application server, or a database server. The WAP server communicates with the WAP gateway using standard internet protocols, such as HTTP, HTTPS, or TCP/IP.
  - WAP Application: This is the software that provides the functionality and user interface for the wireless device. The WAP application can be written in WML, WMLScript, or any other language supported by the WAE. The WAP application can also use WAP Push, which is a service that allows the WAP server to initiate a session with the WAP client and send notifications or updates.



# Protocol Stack for Wireless Networking

A protocol stack is a set of software components that implement different communication protocols for a network. A protocol is a set of rules and procedures that define how data is exchanged between devices. A protocol stack allows different types of devices and networks to communicate with each other by providing a common interface and a standard format for data transmission.

A protocol stack typically consists of several layers, each of which performs a specific function in the communication process. The layers are arranged in a hierarchical order, from the lowest to the highest level of abstraction. The lower layers deal with the physical and data link aspects of the network, such as how to transmit and receive bits, frames, and packets. The higher layers deal with the network, transport, and application aspects of the network, such as how to route, segment, and deliver data, and how to provide services and functionalities to the users and applications.

A protocol stack for wireless networking is a protocol stack that is designed to support wireless communication over a wireless medium, such as radio waves, infrared, or optical signals. Wireless networking poses some unique challenges and requirements for the protocol stack, such as:

- Wireless networks are prone to interference, noise, and fading, which can cause errors, delays, and losses in data transmission.
- Wireless networks have limited bandwidth and power resources, which require efficient and adaptive use of the wireless medium and the devices' energy.
- Wireless networks are dynamic and heterogeneous, which require flexible and scalable network architectures and protocols that can cope with changes in topology, mobility, and diversity of devices and networks.
- Wireless networks have diverse applications and services, which require different levels of quality of service, security, and reliability.

Some examples of protocol stacks for wireless networking are:

- IEEE 802.11: This is a family of standards that define the physical and data link layers for wireless local area networks (WLANs). IEEE 802.11 supports various wireless technologies, such as Wi-Fi, WiMAX, and WiGig, and various modes of operation, such as infrastructure, ad hoc, and mesh. IEEE 802.11 provides features such as authentication, encryption, channel access, and power management for wireless communication.
- Bluetooth: This is a standard that defines the physical and data link layers for wireless personal area networks (WPANs). Bluetooth supports short-range wireless communication between devices, such as smartphones, laptops, headphones, and keyboards. Bluetooth provides features such as discovery, pairing, bonding, and profiles for wireless communication.
- Wireless in Mobile Computing: This is a broad term that refers to the use of wireless networks and devices for mobile computing applications, such as mobile web browsing, email, social media, and location-based services. Wireless in mobile computing involves various protocol stacks, such as cellular networks (e.g., GSM, CDMA, LTE, 5G), satellite networks (e.g., GPS, Iridium, Globalstar), and mobile ad hoc networks (e.g., MANET, VANET, DTN). Wireless in mobile computing provides features such as mobility management, handover, roaming, and security for wireless communication.



# Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, processing power, and user interface.
- WAE consists of the following components :
  - Wireless Markup Language (WML): A markup language similar to HTML, but optimized for small screens and low bandwidth. WML defines the structure and content of web pages for wireless devices.
  - Wireless Markup Language Script (WMLScript): A scripting language similar to JavaScript, but with a smaller footprint and less functionality. WMLScript enables dynamic and interactive web pages for wireless devices.
  - Wireless Telephony Application Interface (WTAI): A set of extensions to WML and WMLScript that allow wireless devices to access telephony services, such as making and receiving calls, sending and receiving messages, and accessing phonebook entries.
  - Wireless Datagram Protocol (WDP): A transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS. WDP enables WAE applications to be independent of the underlying network.
  - Wireless Session Protocol (WSP): A session layer protocol that provides reliable and secure communication between wireless devices and web servers. WSP supports features such as connection-oriented and connectionless modes, caching, and content encoding.
  - Wireless Transaction Protocol (WTP): A transaction layer protocol that provides efficient and reliable data exchange between wireless devices and web servers. WTP supports features such as segmentation and reassembly, acknowledgements, and retransmissions.
  - Wireless Application Protocol Binary XML (WBXML): A binary representation of XML documents that reduces the size and complexity of data transmission. WBXML is used to encode WML, WMLScript, and WTAI documents for wireless devices.

# Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- A wireless LAN (WLAN) is a local area network that uses wireless communication to connect devices within a limited geographic area, such as a home, office, or campus.
- A WLAN typically consists of the following components:
  - Wireless stations: Devices that have wireless network adapters, such as laptops, smartphones, tablets, and printers.
  - Access points: Devices that act as bridges between wireless stations and wired networks, such as routers, switches, and gateways.
  - Distribution system: The wired network that connects access points and provides access to other networks, such as the internet.
- A WLAN operates in one of the following modes:
  - Infrastructure mode: Wireless stations communicate with each other and with the wired network through access points. This mode provides more coverage, security, and scalability than ad hoc mode.
  - Ad hoc mode: Wireless stations communicate with each other directly without using access points. This mode is suitable for temporary or spontaneous networks, such as peer-to-peer file sharing or gaming.
- A WLAN faces several challenges at the medium access control (MAC) layer, which is responsible for coordinating the access of multiple devices to a shared wireless medium, such as radio frequency (RF) spectrum. Some of these challenges are:
  - Hidden terminal problem: A situation where two wireless stations are within the range of an access point, but not within the range of each other. This may cause collisions and interference when both stations transmit at the same time.
  - Exposed terminal problem: A situation where two wireless stations are within the range of each other, but not within the range of the intended receiver. This may cause unnecessary waiting and inefficiency when one station defers its transmission to avoid colliding with the other station's transmission.
  - Fading and multipath propagation: The phenomenon where the wireless signal strength varies due to obstacles, reflections, and interference. This may cause errors and losses in data transmission.
  - Mobility and handoff: The phenomenon where wireless stations move from one access point to another. This may cause interruptions and delays in data transmission.
- IEEE 802.11 is a family of standards that define the physical and MAC layers of WLANs. The most common variants of IEEE 802.11 are:
  - IEEE 802.11a: Operates in the 5 GHz



# Applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves or infrared signals.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs can be classified into two types: infrastructure and ad hoc.
  - Infrastructure WLANs use a base station, such as a wireless access point (AP), to coordinate the communication among the devices. The AP is usually connected to a wired network, such as the Internet, and acts as a gateway for the wireless devices.
  - Ad hoc WLANs do not use a base station, but rely on the devices to communicate directly with each other. This mode is also known as peer-to-peer (P2P) or Wi-Fi Direct.
- The main standard for WLANs is IEEE 802.11, which defines the Medium Access Control (MAC) and Physical Layer (PHY) protocols for wireless communication.
  - The MAC layer is responsible for controlling the access to the shared wireless medium, avoiding collisions, and ensuring reliable data delivery.
  - The PHY layer is responsible for encoding, modulating, transmitting, receiving, and demodulating the wireless signals.
  - IEEE 802.11 has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of frequency, bandwidth, data rate, modulation, and range.
- The main MAC issues in WLANs are:
  - Hidden terminal problem: when two devices are in the range of the AP, but not in the range of each other, they may not sense each other's transmission and cause a collision at the AP.
  - Exposed terminal problem: when two devices are in the range of each other, but not in the range of the AP, they may unnecessarily defer their transmission, even if they do not interfere with the AP.
  - Near-far problem: when a device close to the AP transmits at a high power, it may drown out the signal of a device far from the AP, causing unfairness and inefficiency.
- The main MAC technique used in IEEE 802.11 is Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA), which is based on the following principles:
  - Before transmitting, a device senses the channel to check if it is idle or busy. If it is busy, the device waits for a random backoff time before trying again.
  - Before transmitting data, a device sends a short Request to Send (RTS) frame to the AP, and waits for a Clear to Send (CTS) frame from the AP. This is called the RTS/CTS handshake, and it helps to avoid the hidden terminal problem and reserve the channel for the data transmission.
  - After transmitting data, a device waits for an acknowledgment (ACK) frame from the AP, which confirms the successful reception of the data. If the ACK is not received within a timeout, the device assumes a collision or an error, and retransmits the data after a random backoff time.
- Bluetooth is another wireless technology that enables short-range communication among devices, such as phones, laptops, headphones, keyboards, and mice.
  - Bluetooth uses a frequency-hopping spread spectrum (FHSS) technique, which means that it changes the frequency of the signal rapidly and randomly, to avoid interference and improve security.
  - Bluetooth devices form a network called a piconet, which consists of one master device and up to seven active slave devices. The master device controls the frequency hopping and the synchronization of the piconet.
  - Multiple piconets can be interconnected to form a scatternet, which allows more devices to communicate with each other.
  - Bluetooth has several versions, such as Bluetooth 1.0, Bluetooth 2.0, Bluetooth 3.0, Bluetooth 4.0, Bluetooth 5.0, and Bluetooth 6.0, which differ in terms of data rate, range, power consumption, and features.
- Wireless multiple access protocols are the rules that govern how multiple devices share the wireless medium and avoid collisions and interference.
  - The main types of wireless multiple access protocols are:
    - Frequency division multiple access (FDMA): each device is assigned a different frequency band to transmit and receive data, and the



# Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

- Data management issues
  - Data management is the process of collecting, storing, processing, and distributing data in a mobile computing environment.
  - Data management issues arise due to the characteristics of mobile computing, such as mobility, heterogeneity, disconnection, limited resources, and security.
  - Some of the data management issues are:
    - Data availability: How to ensure that data is accessible to mobile users even when they are disconnected from the network or move across different networks.
    - Data consistency: How to maintain the integrity and correctness of data when it is replicated or cached on multiple devices or servers.
    - Data synchronization: How to coordinate the updates and changes of data among different replicas or caches.
    - Data dissemination: How to efficiently and effectively distribute data to mobile users according to their interests, preferences, and contexts.
    - Data security: How to protect data from unauthorized access, modification, or disclosure when it is transmitted or stored on mobile devices or servers.

- Data replication for mobile computers
  - Data replication is a technique to improve data availability and performance by creating and maintaining multiple copies of data on different devices or servers.
  - Data replication for mobile computers is a special case of data replication that considers the challenges and requirements of mobile computing, such as frequent disconnection, limited bandwidth, and variable network quality.
  - Data replication for mobile computers can be classified into two types: client-initiated and server-initiated.
    - Client-initiated replication: The mobile client decides when and what data to replicate from the server, based on its needs and resources. The client is responsible for managing and synchronizing the replicas with the server.
    - Server-initiated replication: The server decides when and what data to replicate to the mobile client, based on its policies and knowledge. The server is responsible for managing and synchronizing the replicas with the client.
  - Data replication for mobile computers can also be classified into two modes: eager and lazy.
    - Eager replication: The replicas are updated as soon as possible after a change occurs on the original data. Eager replication ensures strong consistency, but requires high communication cost and availability.
    - Lazy replication: The replicas are updated periodically or on demand after a change occurs on the original data. Lazy replication reduces communication cost and tolerates disconnection, but may cause weak consistency and conflicts.

- Adaptive clustering for mobile
  - Adaptive clustering is a technique to organize mobile nodes into groups or clusters based on their proximity, similarity, or functionality.
  - Adaptive clustering for mobile aims to achieve efficient and scalable data management, communication, and coordination among mobile nodes, especially in ad hoc or peer-to-peer networks.
  - Adaptive clustering for mobile can be classified into two types: centralized and distributed.
    - Centralized clustering: A single node or a set of nodes act as the cluster head or leader, and control the formation and maintenance of the cluster. The cluster head is responsible for managing the cluster members, routing the messages, and providing services to the cluster.
    - Distributed clustering: All nodes participate in the formation and maintenance of the cluster, and share the responsibilities of the cluster head. The cluster is self-organized and self-healing, and adapts to the changes in the network topology and conditions.
  - Adaptive clustering for mobile can also be classified into two modes: static and dynamic.
    - Static clustering: The clusters are formed once and remain unchanged until the network is reconfigured or terminated. Static clustering simplifies the cluster management, but may not reflect the current network state or user needs.
    - Dynamic clustering: The clusters are formed and reformed dynamically according to the network state or user needs. Dynamic clustering adapts to the network changes, but may incur high overhead and instability.



# Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables. Wireless networks can enable mobile computing, which is the ability to access and process data from anywhere and anytime using portable devices.

## Data Management Issues

Data management issues in wireless networks include:

- Data availability: How to ensure that data is accessible to mobile users even when they are disconnected from the network or move across different network domains.
- Data consistency: How to maintain the integrity and correctness of data when it is replicated or cached on multiple devices or servers.
- Data security: How to protect data from unauthorized access, modification, or disclosure when it is transmitted over wireless channels or stored on mobile devices.
- Data adaptation: How to adjust data to suit the varying capabilities and preferences of mobile devices and users, such as screen size, bandwidth, battery power, etc.

## Data Replication for Mobile Computers

Data replication is the process of creating and maintaining multiple copies of data on different devices or servers. Data replication can improve data availability, performance, and fault tolerance for mobile computers, but it also introduces challenges such as:

- Replica placement: How to decide where and how many replicas of data should be created and stored, considering factors such as network topology, user mobility, access patterns, etc.
- Replica update: How to propagate changes made to data on one device or server to other replicas, ensuring data consistency and minimizing communication costs.
- Replica selection: How to choose the best replica of data to access or update, considering factors such as data freshness, network latency, user preferences, etc.

## Adaptive Clustering for Mobile Wireless Networks

Adaptive clustering is a technique to organize mobile nodes into groups or clusters based on their proximity, connectivity, or other criteria. Adaptive clustering can provide several benefits for mobile wireless networks, such as:

- Spatial reuse of bandwidth: By dividing the network into non-overlapping clusters, each cluster can use a different frequency or code to communicate, reducing interference and increasing network capacity.
- Controlled access to resources: By assigning a cluster head or leader to each cluster, the cluster head can coordinate the allocation or reservation of bandwidth, power, or other resources among the cluster members, improving network efficiency and fairness.
- Robustness to topology changes: By dynamically adjusting the cluster structure according to the node mobility, failure, or insertion/removal, the network can maintain its connectivity and functionality, enhancing network reliability and scalability.



# File system for mobile computing

A file system is a software component that manages the storage and retrieval of data on a persistent device. A file system for mobile computing is a file system that supports the mobility and wireless connectivity of users and devices in a distributed environment. Some of the challenges and requirements for designing a file system for mobile computing are:

- Location transparency: The file system should provide a uniform namespace and access interface for files regardless of their physical location or network topology.
- User mobility: The file system should allow users to access their files from different devices and locations, and to move or migrate their files across devices and networks.
- Compatibility: The file system should be compatible with existing operating system interfaces and applications, and interoperate with other file systems and protocols.
- Performance: The file system should provide high performance and low latency for file operations, especially in wireless and mobile scenarios.
- Availability: The file system should ensure the availability and consistency of files in the presence of network failures, disconnections, partitions, and mobility events.
- Security: The file system should provide security mechanisms for authentication, encryption, and access control of files and users.
- Adaptability: The file system should adapt to the changing network conditions and resource constraints of mobile and wireless environments, such as bandwidth, latency, power, and storage.

One of the file systems that addresses these challenges and requirements is Coda, a distributed file system that supports disconnected operation for mobile computing. Coda is based on the Andrew File System (AFS), but extends it with several features, such as:

- Client-side persistent caching: Coda caches files on the client device and allows the client to access and modify them even when disconnected from the network or the server. The cached files are synchronized with the server when the connection is re-established.
- Server replication: Coda replicates files on multiple servers to increase availability and fault tolerance. The replication is done at the granularity of volumes, which are logical collections of files. Coda uses a weak consistency model for replication, which allows concurrent updates on different replicas, but may result in conflicts that need to be resolved by the user or the application.
- Security model: Coda uses a security model based on Kerberos for authentication, encryption, and access control. Coda uses tokens to authenticate users and grant them access to files and volumes. Coda also supports encryption of file data and metadata to protect them from eavesdropping and tampering.
- Network bandwidth adaptation: Coda adapts to the network bandwidth and latency by using different modes of operation, such as write-back caching, write-disconnected operation, and hoarding. Write-back caching allows the client to defer the propagation of updates to the server until the network conditions are favorable. Write-disconnected operation allows the client to perform updates on cached files without contacting the server, and to reconcile them later. Hoarding allows the client to prefetch and cache files that are likely to be accessed in the future, based on the user's preferences and usage patterns.



# Disconnected operations

- Disconnected operation is a mode of operation in mobile computing that allows users to execute applications when the network is unavailable or unreliable .
- Disconnected operation can be voluntary or involuntary, depending on the user's choice or the network conditions .
- Disconnected operation requires mechanisms to handle data consistency, synchronization, and recovery when the network is restored  .
- Disconnected operation can be supported by various techniques, such as:
  - Server replication: replicating data and services on multiple servers to increase availability and fault tolerance .
  - Client caching: storing data and services on the client device to reduce network traffic and latency .
  - Mobile computation: transferring code and data between the client and the server to execute applications locally or remotely .
  - Adaptive clustering: grouping mobile devices based on their location, connectivity, and resources to share data and services.
- Disconnected operation can improve the performance, reliability, and usability of mobile computing applications, but also introduces challenges such as:
  - Data consistency: maintaining the correctness and coherence of data across multiple replicas and caches .
  - Synchronization: reconciling the changes made by different clients and servers during disconnection .
  - Recovery: restoring the normal operation of the system after a failure or a disconnection .
  - Security: protecting the data and services from unauthorized access, modification, or disclosure .
  - Resource management: allocating and managing the limited resources of mobile devices, such as battery, memory, and bandwidth .



## Unit 4 - Mobile Agents Computing, Security and Fault Tolerance, Transaction Processing in Mobile Computing

### Mobile Agents Computing

- A mobile agent is a composition of computer software and data that is able to migrate (move) from one computer to another autonomously and continue its execution on the destination computer .
- A mobile agent is a specific form of mobile code, within the field of code mobility. However, in contrast to the remote evaluation and code on demand programming paradigms, mobile agents are active in that they can choose to migrate between computers at any time during their execution.
- The mobile agents are autonomous with intelligence, social ability, learning, and the most important feature is their mobility. They are independent in nature, self-driven and do not require a corresponding node for communication. They can work efficiently even after the user gets disconnected from the network.
- Some of the advantages of mobile agents are:
  - They can reduce the network traffic by moving the computation to the data source instead of transferring the data over the network.
  - They can overcome the network latency by executing asynchronously and autonomously.
  - They can adapt to the dynamic network conditions and reconfigure themselves accordingly.
  - They can provide fault tolerance by resuming their execution from the last checkpoint or migrating to another host in case of failure.
  - They can enhance the security and privacy by encrypting their code and data and verifying their integrity and authenticity.
- Some of the challenges of mobile agents are:
  - They need a common platform or a middleware to support their mobility and interoperability across heterogeneous hosts and networks.
  - They need a secure and reliable mechanism to protect themselves and the hosts from malicious attacks and unauthorized access.
  - They need a coordination and communication protocol to interact with other agents and resources in a distributed environment.
  - They need a standard and efficient way to represent, store and exchange their code and data.
  - They need a performance evaluation and optimization technique to measure and improve their efficiency and effectiveness.



# Environment for Mobile Agents Computing

- Mobile agents are autonomous software entities that can migrate from one host to another in a network, carrying their code and state.
- Mobile agents can benefit from the dynamic and heterogeneous nature of mobile computing environments, where devices may have different capabilities, resources, and connectivity.
- Mobile agents can perform tasks such as information retrieval, data processing, service brokering, contract negotiation, parallel computing, and simulation in mobile computing environments .
- Mobile agents can also overcome some of the limitations of traditional client-server models, such as network latency, bandwidth consumption, and server overload.
- Mobile agents require a suitable execution environment that can support their mobility, security, communication, and coordination.
- Some of the features of a mobile agent environment are:
  - A migration mechanism that allows the agent to transfer its code and state to another host, either by copying or moving.
  - A communication mechanism that allows the agent to exchange messages with other agents or hosts, either synchronously or asynchronously.
  - A security mechanism that protects the agent from malicious hosts and protects the host from malicious agents, using techniques such as encryption, authentication, access control, and sandboxing.
  - A coordination mechanism that allows the agent to cooperate with other agents or hosts, using techniques such as naming, directory services, negotiation, and collaboration.
  - A management mechanism that allows the agent to monitor and control its own behavior and resources, using techniques such as introspection, adaptation, and self-organization.



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



# Destination sequenced distance vector routing (DSDV)

- Destination sequenced distance vector routing (DSDV) is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- It adds a new attribute, sequence number, to each route table entry of the conventional Routing Information Protocol (RIP).
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- A limitation of DSDV is that it provides only one route for a source/destination pair.
- DSDV is also based on distance vector routing and thus uses bidirectional links.
- A node holds a routing table containing all the possible destinations within the network and the number of hops to each destination.
- A node periodically broadcasts its routing table to its neighbors.
- A node updates its routing table if it receives a new sequence number or a lower metric for an existing route.
- DSDV uses two types of packets for routing updates: full dump and incremental.
- A full dump packet contains all the routing table entries and is sent infrequently.
- An incremental packet contains only the updated entries and is sent more frequently.
- DSDV reduces the control overhead by using triggered updates and settling time.
- A triggered update is sent when a node detects a significant change in the network topology.
- A settling time is the time period during which a node waits for possible updates before broadcasting a new route.
- DSDV is suitable for small and moderately sized networks with low mobility.
- DSDV is not scalable for large networks with high mobility due to frequent updates and large routing tables.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on Dynamic Source Routing (DSR) for the Unit 5 of Mobile Computing.

# Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing instead of relying on the routing table at each intermediate node .
- Source routing means that the source node specifies the complete sequence of nodes to the destination in the packet header .
- DSR consists of two main mechanisms: route discovery and route maintenance .
- Route discovery is the process of finding a route from the source to the destination when there is no cached route available .
- Route discovery involves broadcasting a route request (RREQ) packet by the source node, which is forwarded by the intermediate nodes until it reaches the destination or a node with a cached route to the destination .
- The destination or the intermediate node then sends a route reply (RREP) packet back to the source node along the reverse path of the RREQ packet .
- The source node then caches the route in its route cache and uses it to send data packets .
- Route maintenance is the process of detecting and repairing link failures along the route .
- Route maintenance involves sending route error (RERR) packets by the node that detects a link failure, which are propagated back to the source node .
- The source node then removes the broken route from its route cache and initiates a new route discovery if needed .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages include:
  - No periodic routing updates, which reduces the control overhead and bandwidth consumption .
  - No need to maintain routing tables at each node, which saves memory and processing power .
  - Loop-free routes, since the source node specifies the entire route in the packet header .
  - Support for multiple routes to the same destination, which increases the reliability and load balancing .
- Disadvantages include:
  - Large packet header size, which increases the transmission delay and consumes more bandwidth .
  - Route cache inconsistency, which may lead to stale or invalid routes due to network topology changes .
  - Vulnerability to malicious nodes, which may alter or drop the packets or the route information .




# Ad Hoc On-Demand Distance Vector Routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, where each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses three types of control messages: route request (RREQ), route reply (RREP) and route error (RERR)  .
- AODV operates in two phases: route discovery and route maintenance  .
- Route discovery is initiated when a source node needs to send a packet to a destination node and does not have a valid route to it  .
- The source node broadcasts a RREQ message to its neighbors, which contains the source and destination addresses, a sequence number and a hop count  .
- Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node and forwards the RREQ message to its neighbors, increasing the hop count by one  .
- If an intermediate node has a fresh route to the destination node (i.e., a route with a sequence number equal or higher than the one in the RREQ message), it sends a RREP message back to the source node along the reverse route  .
- If the destination node receives the RREQ message, it generates a RREP message with its own sequence number and the hop count set to zero  .
- The source node selects the route with the highest destination sequence number and the lowest hop count as the best route and starts sending data packets along it  .
- Route maintenance is performed when a link break occurs in an active route  .
- The node that detects the link break sends a RERR message to its upstream neighbors, informing them about the unreachable destinations  .
- The upstream nodes update their routing tables and propagate the RERR message to their upstream neighbors until the source node is reached  .
- The source node can either drop the packets destined to the unreachable destination or initiate a new route discovery  .
- AODV has some advantages, such as low overhead, loop-freeness, scalability and adaptability to dynamic network conditions .
- AODV also has some disadvantages, such as high latency, vulnerability to routing attacks, and dependence on reliable broadcast .



# Temporary Ordered Routing Algorithm (TORA)

- TORA is a source-initiated on-demand routing protocol for wireless ad hoc networks .
- TORA is based on the link reversal algorithm, which dynamically changes the direction of links to maintain routes in the network  .
- TORA has three main phases: route creation, route maintenance, and route erasure .
- Route creation: The source node broadcasts a query packet with a destination address and a unique reference level. The reference level is used to assign a height to each node in the network. The height is a tuple of four values: (τ, oid, r, δ), where τ is the reference level, oid is the originator id, r is a reflection bit, and δ is a propagation ordering parameter. The height is used to create a directed acyclic graph (DAG) rooted at the destination. The nodes that receive the query packet compare their heights with the reference level. If their height is undefined or higher than the reference level, they update their height to be lower than the reference level and append their own id to the packet. Then they broadcast the packet to their neighbors. This process continues until the packet reaches the destination or a node that has a route to the destination. The destination or the intermediate node replies with an update packet that contains its height and the destination address. The update packet propagates back to the source along the reverse path of the query packet, updating the height of each node along the way. When the source receives the update packet, it has a route to the destination .
- Route maintenance: When a link failure occurs, the nodes adjacent to the link update their heights to be higher than their neighbors and set the reflection bit to 1. This creates a temporary loop in the DAG. Then they broadcast a clear packet to their neighbors to invalidate the routes that use the failed link. The clear packet contains the destination address and the reference level of the failed link. The nodes that receive the clear packet compare their heights with the reference level. If their height is lower than or equal to the reference level, they ignore the packet. If their height is higher than the reference level, they update their height to be lower than the reference level and forward the packet to their neighbors. This process continues until the loop is eliminated and a new DAG is formed .
- Route erasure: When a source node no longer needs a route to a destination, it broadcasts a clear packet with the destination address and a reference level of (0, 0, 0, 0). This packet erases all the routes to the destination in the network. The nodes that receive the clear packet set their heights to be undefined and forward the packet to their neighbors .
- TORA is efficient, adaptive, loop-free, and scalable, but it has some drawbacks, such as high overhead, multiple routes, and dependence on synchronized clocks  .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on QoS in Ad Hoc Networks for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

# QoS in Ad Hoc Networks

- QoS stands for Quality of Service, which refers to the ability of a network to provide satisfactory performance and reliability for different types of applications and users .
- QoS is an essential component of ad hoc networks, which are self-organizing networks of mobile nodes that communicate over wireless channels without any fixed infrastructure or centralized control  .
- QoS requirements arise at the application layer in the form of restrictions on values of certain QoS metrics, such as bandwidth, delay, jitter, packet loss, throughput, reliability, etc .
- QoS support in ad hoc networks is challenging due to the following factors  :
  - Dynamic topology: The mobility of nodes causes frequent changes in the network topology, which affects the availability and quality of links and routes.
  - Limited resources: The wireless channels have limited bandwidth and are prone to interference, noise, and fading. The nodes have limited battery power, memory, and processing capabilities.
  - Distributed operation: The nodes have to cooperate and coordinate with each other to perform routing, medium access control, and other network functions, without any centralized authority or global information.
  - Heterogeneity: The nodes and applications may have different QoS requirements, capabilities, and preferences, which need to be accommodated by the network.
- QoS support in ad hoc networks can be achieved at different layers of the network stack, such as the physical layer, the MAC layer, the network layer, the transport layer, and the application layer  .
- QoS support at the physical layer involves techniques such as adaptive modulation, coding, power control, and antenna diversity, to improve the signal quality and reliability of the wireless links .
- QoS support at the MAC layer involves techniques such as channel access schemes, scheduling algorithms, admission control, and resource reservation, to allocate the channel resources among the competing nodes and to reduce the collisions, contention, and interference  .
- QoS support at the network layer involves techniques such as routing protocols, route discovery, route maintenance, route selection, and load balancing, to find and maintain feasible and optimal paths for the data packets that satisfy the QoS requirements  .
- QoS support at the transport layer involves techniques such as congestion control, flow control, error control, and reliability mechanisms, to regulate the data transmission and to ensure the end-to-end QoS guarantees  .
- QoS support at the application layer involves techniques such as adaptive applications, QoS-aware middleware, and QoS negotiation, to adjust the application behavior and parameters according to the network conditions and user preferences  .
- QoS support in ad hoc networks is an active and challenging research area, which requires cross-layer design and optimization, as well as cooperation and coordination among the nodes and the network layers  .



# Applications of Ad Hoc Networks

Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of nodes that communicate with each other directly or through intermediate nodes. Ad hoc networks have many potential applications in various domains, such as:

- **Military battlefield**: Ad hoc networks can provide secure and robust communication among soldiers, vehicles, and command centers in a dynamic and hostile environment.
- **Vehicular ad hoc networks (VANETs)**: Ad hoc networks can enable vehicles to exchange information about traffic conditions, road safety, navigation, entertainment, and other services . Intelligent VANETs can use artificial intelligence and ad hoc technologies to coordinate actions during accidents or emergencies.
- **Smartphone ad hoc networks (SPANs)**: Ad hoc networks can allow smartphones to form peer-to-peer networks without relying on cellular or Wi-Fi networks. SPANs can enable users to share data, resources, and services in a decentralized and cooperative manner .
- **Wireless sensor networks (WSNs)**: Ad hoc networks can connect a large number of sensor nodes that collect and process data from the physical environment. WSNs can be used for various applications, such as environmental monitoring, disaster management, health care, smart homes, and industrial automation.
- **Industrial and commercial applications**: Ad hoc networks can support cooperative mobile data exchange among workers, customers, and devices in various scenarios, such as conferences, exhibitions, warehouses, factories, and offices.

