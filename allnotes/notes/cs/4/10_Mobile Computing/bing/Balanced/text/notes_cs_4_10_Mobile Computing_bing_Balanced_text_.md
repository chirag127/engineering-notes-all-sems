

## Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks.
- Mobile computing enables users to communicate, access information, and perform tasks anytime and anywhere, without being constrained by physical location or wired connections.
- Mobile computing involves three main components: mobile devices, wireless networks, and mobile applications.
- Mobile devices are handheld or wearable computers that have wireless communication capabilities, such as smartphones, tablets, laptops, smartwatches, etc.
- Wireless networks are the infrastructure that provides connectivity and services to mobile devices, such as cellular networks, Wi-Fi networks, Bluetooth networks, etc.
- Mobile applications are the software programs that run on mobile devices and provide various functionalities, such as web browsing, email, social media, gaming, etc.

- Wireless telephony is the transmission of voice and data over wireless networks, using radio waves or electromagnetic signals.
- Wireless telephony enables users to make and receive phone calls, send and receive text messages, and access the internet, without being connected to a fixed line or a physical terminal.
- Wireless telephony is based on the cellular concept, which divides a geographical area into smaller regions called cells, each served by a base station that communicates with mobile devices within its range.
- The cellular concept allows multiple users to share the same frequency band, by assigning different channels to different cells, and reusing the same channels in non-adjacent cells.
- The cellular concept also enables handover, which is the process of transferring an ongoing call from one base station to another, as the mobile device moves from one cell to another.

- GSM (Global System for Mobile communication) is a standard developed by the European Telecommunications Standards Institute (ETSI) to describe the protocols for second-generation (2G) digital cellular networks used by mobile devices such as mobile phones and tablets.
- GSM is an open and digital cellular technology that uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate channels to multiple users.
- GSM uses four different frequency bands: 850 MHz, 900 MHz, 1800 MHz, and 1900 MHz, depending on the region and the operator.
- GSM provides voice and data services, such as voice calls, text messages, multimedia messages, and internet access, using circuit-switched and packet-switched technologies.
- GSM has a hierarchical network architecture, consisting of three main components: mobile stations, base station subsystems, and network and switching subsystems.
- Mobile stations are the devices that communicate with the GSM network, such as mobile phones and tablets. They have a unique identifier called International Mobile Equipment Identity (IMEI) and a subscriber identity module (SIM) card that stores the user's information and authentication data.
- Base station subsystems are the components that provide radio coverage and connectivity to the mobile stations, such as base transceiver stations (BTS) and base station controllers (BSC). They have a unique identifier called Cell Global Identity (CGI) and manage the radio resources, channels, and handovers within their area.
- Network and switching subsystems are the components that provide the core functionality and services of the GSM network, such as mobile switching centers (MSC), home location registers (HLR), visitor location registers (VLR), authentication centers (AUC), and equipment identity registers (EIR). They handle the call routing, switching, registration, authentication, and billing of the mobile stations.



### Air-interface for mobile computing

- The air interface is the communication link between the two stations in mobile or wireless communication.
- The air interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection.
- The air interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network.
- Different air interface technologies are used for different cellular standards, such as TDMA and CDMA for GSM, OFDMA for LTE, and NR for 5G .
- The air interface is also called the UM interface in GSM, as it is analogous to the U interface of ISDN.
- The air interface waveform of LTE and NR is based on orthogonal frequency division multiplexing (OFDM), which is highly spectrally efficient and allows high data rate transmission with low receiver complexity even in a dispersive radio channel.



### Channel structure for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- A channel in cellular system is a communication path between a base station and a mobile terminal.
- There are two types of channels: physical and logical.
- A physical channel is a specific frequency or a pair of frequencies (one for uplink and one for downlink) that are allocated to a cell.
- A logical channel is a function or a service that is provided by a physical channel.
- For example, a voice call may use a traffic channel (TCH) as a logical channel, which is carried by a physical channel with a certain frequency.
- There are different types of logical channels for different purposes, such as control, signaling, broadcast, etc.
- The channel structure of a cellular system defines how the physical and logical channels are organized and used in the system.
- The channel structure may vary depending on the cellular standard, such as GSM, CDMA, LTE, etc.
- The channel structure affects the performance, capacity, and quality of service of the cellular system.
- The channel structure also determines the channel allocation and reuse strategies, which are methods to efficiently use the limited spectrum resources in a cellular system.
- Channel allocation and reuse aim to maximize the number of users that can be served in a given area, while minimizing the interference and noise that may degrade the communication quality.
- Channel allocation and reuse can be done in different ways, such as fixed, dynamic, hybrid, etc.
- In fixed channel allocation, each cell is assigned a fixed number of channels that are not shared with other cells.
- In dynamic channel allocation, the channels are assigned to the cells on demand, based on the traffic load and interference conditions.
- In hybrid channel allocation, a combination of fixed and dynamic methods is used.
- The channel structure of GSM, which is a widely used cellular standard, is based on the following principles:
  - GSM uses frequency division duplexing (FDD) to separate the uplink and downlink channels.
  - GSM uses time division multiple access (TDMA) to divide each physical channel into eight time slots, each carrying a logical channel.
  - GSM uses frequency hopping to reduce the interference and fading effects by changing the frequency of the physical channel in each time slot.
  - GSM defines several types of logical channels, such as broadcast control channel (BCCH), common control channel (CCCH), dedicated control channel (DCCH), traffic channel (TCH), etc.
  - GSM uses a hierarchical cell structure, where each cell can be divided into smaller cells with different channel sets, to increase the capacity and coverage of the system.



### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile users in a wireless cellular network.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is the process of informing the network about the current location of the mobile user, usually initiated by the mobile user when it moves across a predefined boundary (such as a cell or a registration area).
- Location lookup is the process of finding the current location of the mobile user, usually initiated by the network when it needs to deliver a call or a message to the mobile user.
- Paging is the process of notifying the mobile user about an incoming call or a message, usually initiated by the network after locating the mobile user.
- Location management involves two types of databases: Home Location Register (HLR) and Visitor Location Register (VLR).
- HLR is a centralized database that stores the permanent information of all the mobile users in the network, such as their service profile, authentication data, and current location (in terms of the VLR that serves them).
- VLR is a local database that stores the temporary information of the mobile users that are currently visiting its service area, such as their identity, location (in terms of the cell or the base station that serves them), and service status.
- HLR and VLR communicate with each other to update and lookup the location of the mobile users, using standardized protocols such as MAP (Mobile Application Part) or IS-41.
- Location management can be classified into two categories: flat and hierarchical.
- Flat location management uses a single level of database (HLR) to store and retrieve the location of the mobile users, without any intermediate level of database (VLR). This simplifies the network architecture, but increases the signaling overhead and the database size.
- Hierarchical location management uses multiple levels of databases (HLR and VLR) to store and retrieve the location of the mobile users, with each level covering a different geographical area. This reduces the signaling overhead and the database size, but increases the network complexity and the latency.
- Handoff is the process of transferring the ongoing communication of a mobile user from one base station to another, without interrupting the service quality or the user perception.
- Handoff can be classified into two types: horizontal and vertical.
- Horizontal handoff occurs when the mobile user moves from one base station to another within the same network or the same technology (such as GSM or CDMA).
- Vertical handoff occurs when the mobile user moves from one network to another or from one technology to another (such as GSM to Wi-Fi or CDMA to LTE).
- Handoff involves three main steps: handoff initiation, handoff decision, and handoff execution.
- Handoff initiation is the process of detecting the need for a handoff, usually based on the signal strength, the signal quality, or the user preference.
- Handoff decision is the process of selecting the best target base station for the handoff, usually based on the network load, the available resources, or the user profile.
- Handoff execution is the process of switching the communication channel from the old base station to the new base station, usually using a predefined signaling protocol (such as GSM BSSMAP or CDMA IS-95).
- Handoff can be further classified into two types: hard and soft.
- Hard handoff occurs when the mobile user breaks the connection with the old base station before establishing the connection with the new base station. This causes a temporary interruption in the service, but reduces the interference and the resource consumption.
- Soft handoff occurs when the mobile user maintains the connection with both the old and the new base stations simultaneously. This avoids any interruption in the service, but increases the interference and the resource consumption.



### Channel allocation in cellular systems

- Channel allocation means to assign the available channels (frequencies, time slots, codes, etc.) to the cells in a cellular system .
- Channel allocation is a key issue in cellular systems, as it affects the capacity, quality, and interference of wireless communications.
- Channel allocation strategies can be classified into three categories:
  - Fixed channel allocation (FCA): Each cell is assigned a fixed number of channels, regardless of the traffic demand. The channels are reused in different cells according to a reuse pattern. FCA is simple and robust, but it may cause wastage of channels or blocking of calls.
  - Dynamic channel allocation (DCA): The channels are not permanently assigned to any cell, but are allocated on demand according to the traffic load and interference conditions. DCA can adapt to traffic variations and improve the spectrum efficiency, but it requires more complex coordination and signaling.
  - Hybrid channel allocation (HCA): A combination of FCA and DCA, where some channels are fixed and some are dynamic. HCA can balance the trade-off between simplicity and adaptability, but it may introduce more interference and handoff failures.
- Channel allocation algorithms can be based on different criteria, such as:
  - Future blocking probability in neighboring cells: The probability that a channel request in a neighboring cell will be rejected due to the lack of available channels.
  - Reuse distance: The minimum distance between two cells that use the same channel, which determines the level of co-channel interference.
  - Usage frequency of the candidate channel: The number of times that a channel has been used in a given period, which reflects the channel quality and availability.
  - Average blocking probability of the overall system: The average probability that a channel request in any cell will be rejected due to the lack of available channels.
  - Instantaneous channel occupancy distribution: The distribution of the number of occupied channels in each cell, which indicates the traffic load and congestion.



### CDMA for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- CDMA stands for Code Division Multiple Access and is a spread spectrum multiple access technique  .
- Spread spectrum technique spreads bandwidth of data in a uniform manner for the same transmitted power.
- CDMA is a digital cellular technology used for mobile communication .
- CDMA is the base on which access methods such as cdmaOne, CDMA2000, and WCDMA are built .
- CDMA allows numerous signals to occupy a single transmission channel, optimizing the use of available bandwidth .
- CDMA uses a special coding scheme, where each transmitter is assigned a code, to allow multiple users to be multiplexed over the same physical channel  .
- CDMA is a form of direct-sequence spread spectrum (DSSS) modulation, where the data signal is multiplied by a pseudorandom noise (PN) code sequence that has a much higher bit rate than the data signal  .
- CDMA has several advantages over other multiple access techniques, such as:
  - Higher spectral efficiency, as more users can share the same bandwidth without interference  .
  - Better security, as the data signal is scrambled by the PN code and can only be decoded by the intended receiver  .
  - Improved voice quality, as the background noise and cross-talk are reduced by the spread spectrum technique  .
  - Greater flexibility, as the users can dynamically adjust their transmission power and code length according to the channel conditions  .
- CDMA has some disadvantages, such as:
  - Higher complexity, as the transmitter and receiver need to synchronize their PN codes and perform complex signal processing  .
  - Near-far problem, where a strong signal from a nearby transmitter can interfere with a weak signal from a faraway transmitter, if they use the same code  .
  - Cell breathing, where the coverage area of a cell varies depending on the number and location of active users  .
- CDMA is one of the multiple access techniques used in mobile computing, along with FDMA (Frequency Division Multiple Access) and TDMA (Time Division Multiple Access).
- FDMA divides the available bandwidth into frequency bands, and assigns each user a different band.
- TDMA divides the available bandwidth into time slots, and assigns each user a different slot.
- CDMA, FDMA, and TDMA are used to enable wireless telephony, which is the transmission and reception of voice signals over a wireless network.
- Wireless telephony is based on the cellular concept, where the service area is divided into small regions called cells, and each cell is served by a base station.
- GSM (Global System for Mobile Communications) is a standard for wireless telephony that uses a combination of FDMA and TDMA to provide voice and data services.
- GSM is the most widely used wireless telephony standard in the world, with over 5 billion subscribers as of 2020.
- GSM operates in the 900 MHz and 1800 MHz frequency bands in Europe and Asia, and in the 850 MHz and 1900 MHz frequency bands in North America and South America.
- GSM uses a 200 kHz channel bandwidth, and divides it into eight time slots, each with a duration of 0.577 ms.
- GSM uses a 25 MHz frequency band, and divides it into 124 channels, each with a 200 kHz bandwidth.
- GSM supports a maximum data rate of 9.6 kbps per time slot, and a maximum voice quality of 13 kbps per time slot.
- GSM uses a variety of techniques to improve the performance and reliability of wireless telephony, such as:
  - Frequency hopping, where the



### GPRS for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- GPRS stands for General Packet Radio Service .
- It is a packet oriented wireless data communication service for mobile communications on 2G and 3G cellular communication systems .
- It is non-voice, high speed packet switching technology intended for GSM networks .
- It enables moderately high-speed data transfers using packet-based technologies .
- It offers more data transmission options for GSM-based devices, as GSM networks at the time could only use Short Message Service (SMS), for example, to transmit a small amount of data .
- It supports data functions across cellular internet connections.
- It establishes a connected mobile environment for IoT applications.
- It has advantages such as:
  - Higher data rates than circuit-switched services .
  - More efficient use of network resources and bandwidth .
  - Always-on connectivity and faster access to data services .
  - Billing based on data volume rather than connection time .
- It has disadvantages such as:
  - Limited coverage and availability in some areas .
  - Variable and unpredictable performance depending on network congestion and signal quality .
  - Security and privacy risks due to data transmission over public networks .
- It has applications such as:
  - Web browsing and email on mobile devices  .
  - Multimedia messaging service (MMS) and instant messaging (IM) on mobile devices  .
  - Location-based services and navigation on mobile devices  .
  - Wireless application protocol (WAP) and internet protocol (IP) access on mobile devices  .
  - Remote monitoring and control of IoT devices.
  - Mobile commerce and banking on mobile devices  .



## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- Wireless networking is the communication of data between devices without using cables or wires.
- Wireless LAN (WLAN) is a type of wireless network that connects devices in a local area, such as a home, office, or campus.
- WLANs use high-frequency radio waves to transmit and receive data over the air.
- WLANs have several advantages over wired LANs, such as mobility, scalability, ease of installation, and lower cost.
- WLANs also have some challenges, such as security, interference, and limited range.

### MAC issues

- MAC (Medium Access Control) is the sublayer of the data link layer that controls how devices access the shared wireless medium.
- MAC issues are the problems that arise due to the characteristics of the wireless medium and the multiple access techniques used by the devices.
- Some of the MAC issues are:

  - Half-duplex operation: Wireless devices can either send or receive data at a given time, but not both simultaneously. This limits the throughput and efficiency of the wireless network.
  - Time-varying channel: The wireless channel is affected by factors such as distance, obstacles, noise, and interference, which can change over time. This causes variations in the signal strength, quality, and availability of the wireless channel.
  - Burst channel errors: The wireless channel is prone to errors due to noise, interference, and fading. These errors can occur in bursts, meaning that several consecutive bits or packets can be corrupted or lost. This reduces the reliability and performance of the wireless network.

### IEEE 802.11

- IEEE 802.11 is the standard that defines the architecture and specifications of WLANs.
- IEEE 802.11 specifies the MAC and PHY (Physical) layers of the WLAN protocol stack.
- IEEE 802.11 has several amendments that define different versions of the standard, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax. These versions differ in terms of frequency band, modulation scheme, data rate, channel width, and range.
- IEEE 802.11 also defines several features and functions to enhance the WLAN performance, such as security, quality of service, power management, roaming, and mesh networking.

### Blue Tooth

- Blue Tooth is a wireless technology that enables short-range communication between devices, such as phones, headsets, keyboards, mice, printers, and speakers.
- Blue Tooth uses low-power radio waves in the 2.4 GHz ISM (Industrial, Scientific, and Medical) band to create personal area networks (PANs) or piconets.
- Blue Tooth devices can communicate with each other using a master-slave architecture, where one device acts as the master and controls the communication with up to seven slaves. Multiple piconets can form a scatternet, where devices can belong to more than one piconet and relay data between them.
- Blue Tooth has several versions that define different profiles and protocols for different applications and services, such as audio, video, data, and voice.

### Wireless

- Wireless is a broad term that refers to any type of communication that does not use wires or cables.
- Wireless can be classified into different categories based on the range, coverage, and topology of the network, such as:

  - Wireless PAN (WPAN): A wireless network that connects devices within a personal or small area, such as a room or a car. Examples are Blue Tooth, ZigBee, and infrared.
  - Wireless LAN (WLAN): A wireless network that connects devices within a local or medium area, such as a home, office, or campus. Examples are IEEE 802.11, Wi-Fi, and WiMAX.
  - Wireless MAN (WMAN): A wireless network that connects devices within a metropolitan or large area, such as a city or a region. Examples are cellular networks, satellite networks, and microwave networks.
  - Wireless WAN (WWAN): A wireless network that connects devices across a wide or global area, such as a country or the world. Examples are cellular networks, satellite networks, and microwave networks.



### Multiple Access Protocols

- Multiple access protocols are used to coordinate the access of multiple nodes or users to a shared network channel, such as a wireless LAN or a satellite network.
- Multiple access protocols can be classified into three categories: random access, controlled access, and channelization.
- Random access protocols allow nodes to transmit data whenever they have data to send, without any coordination with other nodes. However, this may result in collisions, which degrade the network performance and waste the channel bandwidth.
- Controlled access protocols require nodes to obtain permission before transmitting data, either from a central controller or from other nodes. This reduces the probability of collisions, but introduces some delay and overhead in the channel access.
- Channelization protocols divide the channel into smaller sub-channels, either in time, frequency, or code domain, and assign them to different nodes. This prevents collisions, but requires synchronization and coordination among nodes.

- Some common multiple access protocols that may be used in wireless networks are:

  - Carrier-sense multiple access with collision avoidance (CSMA/CA), used in IEEE 802.11 / WiFi, potentially using a distributed coordination function. This protocol allows nodes to sense the channel before transmitting data, and to back off if the channel is busy. It also uses an acknowledgment mechanism to confirm the successful reception of data, and a random backoff algorithm to resolve collisions.
  - ALOHA and slotted ALOHA, used in ALOHAnet. These protocols allow nodes to transmit data at any time, without sensing the channel. Slotted ALOHA divides the time into discrete slots, and requires nodes to transmit data only at the beginning of a slot, which improves the channel utilization.
  - Reservation ALOHA (R-ALOHA) and Mobile Slotted Aloha (MS-ALOHA). These protocols are extensions of ALOHA and slotted ALOHA, which use a reservation mechanism to allocate slots to nodes that have data to send. This reduces the collision probability and increases the channel efficiency.
  - Code-division multiple access (CDMA), used in cellular networks and satellite networks. This protocol assigns a unique code to each node, and allows nodes to transmit data simultaneously on the same channel, using different codes. The receiver can recover the data from a specific node by using the corresponding code. This increases the channel capacity and provides resistance to interference and multipath fading.
  - Orthogonal frequency-division multiple access (OFDMA) and orthogonal frequency-division multiplexing (OFDM), used in 4G and 5G cellular networks and WiMAX. These protocols divide the channel into multiple orthogonal sub-carriers, and assign them to different nodes or data streams. This improves the spectral efficiency and mitigates the effects of frequency-selective fading and inter-symbol interference.



### TCP over wireless

- TCP (Transmission Control Protocol) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to factors such as fading, shadowing, interference, mobility, and handoffs, which are not related to congestion.
- TCP cannot distinguish between congestion losses and wireless losses, and may unnecessarily reduce the sending rate, leading to poor performance and underutilization of the wireless bandwidth.
- Therefore, TCP needs to be adapted or enhanced to cope with the characteristics of wireless networks and improve its efficiency and resource utilization.
- Some of the challenges and solutions for TCP over wireless networks are:

  - **Wireless link errors:** Wireless links are prone to high bit error rates and bursty losses due to noise, interference, and fading. TCP may misinterpret these losses as congestion and invoke congestion control mechanisms, resulting in low throughput and unfairness. Some possible solutions are:
    - **Link layer retransmissions:** The link layer can detect and correct errors by using techniques such as checksums, acknowledgments, and retransmissions. This can hide the wireless losses from TCP and improve its performance. However, link layer retransmissions may increase the delay and jitter, and may also cause duplicate acknowledgments and spurious timeouts at the TCP layer.
    - **Selective acknowledgments:** TCP can use selective acknowledgments (SACK) to inform the sender about the non-contiguous segments that have been received. This can reduce the number of retransmissions and improve the throughput. However, SACK may not work well in the presence of high error rates and long feedback delays.
    - **Explicit loss notification:** The link layer or the network layer can provide explicit feedback to the TCP sender about the wireless losses, using mechanisms such as Explicit Congestion Notification (ECN) or Explicit Bad State Notification (EBSN). This can help TCP to distinguish between congestion losses and wireless losses, and avoid unnecessary congestion control actions. However, explicit loss notification may require modifications to the network infrastructure and the TCP protocol.

  - **Handoffs:** Handoffs occur when a mobile host moves from one base station to another during an ongoing TCP connection. Handoffs can cause packet losses, delays, and route changes, which can affect the TCP performance. Some possible solutions are:
    - **Fast retransmit and fast recovery:** TCP can use fast retransmit and fast recovery algorithms to quickly recover from packet losses during handoffs. Fast retransmit triggers a retransmission based on duplicate acknowledgments, and fast recovery maintains the congestion window size until the retransmitted segment is acknowledged. This can reduce the recovery time and improve the throughput. However, fast retransmit and fast recovery may not work well in the presence of high error rates and long feedback delays.
    - **Make-before-break handoffs:** The mobile host can establish a new connection with the new base station before breaking the old connection with the old base station. This can reduce the packet losses and delays during handoffs. However, make-before-break handoffs may require additional resources and coordination between the base stations and the mobile host.
    - **Mobile IP:** Mobile IP is a protocol that allows a mobile host to maintain its IP address while moving across different networks. Mobile IP uses a home agent and a foreign agent to route the packets to the mobile host. This can preserve the TCP connection and avoid route changes during handoffs. However, Mobile IP may introduce additional overhead and latency, and may also cause suboptimal routing and security issues.

  - **End-to-end semantics:** TCP provides end-to-end semantics, which means that a packet is acknowledged only after it is received by the final destination. This ensures the reliability and integrity of the data. However, in wireless networks, end-to-end semantics may not be desirable or feasible, due to the high error rates, delays, and mobility of the wireless links. Some possible solutions are:
    - **Split-connection:** The TCP connection can be split into two sub-connections: one between the sender and the base station, and another between the base station and the receiver. The base station can act as a proxy and buffer the packets, and acknowledge them to the sender before forwarding them to the receiver. This can improve the TCP performance by isolating the wireless losses from the sender and reducing the end-to-end delay. However, split-connection may violate the end-to-end semantics and introduce security and reliability issues.
    - **Snoop protocol:** The snoop protocol is



### Wireless applications

Wireless applications are the software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, etc. Wireless applications enable users to access information, services, and entertainment without being constrained by wires or cables. Some of the benefits of wireless applications are:

- Mobility: Users can access wireless applications from anywhere within the coverage area of the wireless network, and move freely without losing connectivity.
- Convenience: Users do not need to plug in or unplug wires or cables to use wireless applications, which reduces the hassle and clutter of wires.
- Cost-effectiveness: Wireless applications can reduce the cost of installation, maintenance, and operation of wired networks, and also save energy and resources.
- Flexibility: Wireless applications can support a variety of devices, platforms, and standards, and can be easily updated or modified to meet changing user needs and preferences.

Some of the challenges of wireless applications are:

- Security: Wireless applications are vulnerable to unauthorized access, interception, modification, or disruption of data transmitted over wireless networks, which can compromise the privacy and integrity of users and applications.
- Reliability: Wireless applications depend on the availability and quality of wireless signals, which can be affected by factors such as interference, noise, distance, obstacles, weather, etc., which can cause delays, errors, or failures in wireless communication.
- Compatibility: Wireless applications need to be compatible with different wireless technologies, protocols, and standards, which can vary across regions, devices, and networks, and can pose interoperability and compatibility issues for users and applications.
- Performance: Wireless applications need to cope with the limited bandwidth, power, memory, and processing capabilities of wireless devices and networks, which can affect the speed, quality, and functionality of wireless applications.

Some of the examples of wireless applications are:

- Wireless Internet: Wireless applications that enable users to access the internet and web-based services, such as browsing, emailing, social networking, online shopping, etc., using wireless devices and networks, such as Wi-Fi, cellular, or satellite.
- Wireless Multimedia: Wireless applications that enable users to access, stream, download, or share multimedia content, such as audio, video, images, etc., using wireless devices and networks, such as Bluetooth, Wi-Fi, cellular, or satellite.
- Wireless Gaming: Wireless applications that enable users to play games, either individually or with other players, using wireless devices and networks, such as Bluetooth, Wi-Fi, cellular, or satellite.
- Wireless Location-Based Services: Wireless applications that enable users to access information or services based on their geographic location, such as navigation, maps, weather, traffic, local search, etc., using wireless devices and networks, such as GPS, Wi-Fi, cellular, or satellite.
- Wireless Health: Wireless applications that enable users to monitor, manage, or improve their health and wellness, such as fitness trackers, wearable sensors, telemedicine, etc., using wireless devices and networks, such as Bluetooth, Wi-Fi, cellular, or satellite.



### Data Broadcasting

- Data broadcasting is a group communication, where a sender sends data to receivers simultaneously .
- This is an all-to-all communication model where each sending device transmits data to all other devices in the network domain.
- Data broadcasting can be used for information dissemination in wireless networks, such as traffic information, weather updates, news, etc.
- Data broadcasting can also be used for network management, such as routing updates, address resolution, etc.
- Data broadcasting can be performed using different techniques, such as flooding, gossiping, multicasting, etc.
- Data broadcasting can be challenged by factors such as limited bandwidth, high error rates, dynamic topology, etc.
- Data broadcasting can be improved by using methods such as network coding, cooperation, smart antennas, etc.

### Wireless Networking

- Wireless networking refers to a computer network that makes use of radio frequency (RF) connections between nodes in the network .
- Wireless networking is a popular solution for homes, businesses, and telecommunications networks, as it offers mobility, flexibility, scalability, and cost-effectiveness.
- Wireless networking can be classified into different types, such as wireless personal area network (WPAN), wireless local area network (WLAN), wireless metropolitan area network (WMAN), wireless wide area network (WWAN), etc.
- Wireless networking can also be categorized based on the network architecture, such as infrastructure-based, ad hoc, mesh, etc.
- Wireless networking can be implemented using various standards, protocols, and technologies, such as IEEE 802.11, Bluetooth, Wi-Fi, WiMAX, cellular, etc .
- Wireless networking can be affected by issues such as security, interference, congestion, power consumption, etc .
- Wireless networking can be enhanced by using techniques such as encryption, authentication, channel allocation, power management, etc .

### Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth

- Wireless LAN (WLAN) is a type of wireless network that covers a small geographic area, such as a home, office, or campus .
- WLAN uses RF signals to connect devices, such as laptops, smartphones, tablets, etc, to a wireless access point (AP), which provides access to the Internet or other networks .
- WLAN operates in the unlicensed frequency bands, such as 2.4 GHz and 5 GHz, which are shared by other devices and sources of interference .
- WLAN faces medium access control (MAC) issues, such as hidden terminal problem, exposed terminal problem, collision avoidance, etc, which affect the network performance and reliability .
- WLAN adopts various MAC protocols, such as carrier sense multiple access with collision avoidance (CSMA/CA), distributed coordination function (DCF), point coordination function (PCF), etc, to coordinate the access to the shared medium .
- WLAN follows the IEEE 802.11 standard, which defines the physical layer (PHY) and MAC layer specifications for WLAN .
- IEEE 802.11 has several amendments, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax, etc, which provide different data rates, modulation schemes, channel widths, etc .
- IEEE 802.11 also supports various features, such as quality of service (QoS), security, roaming, power saving, etc, to improve the WLAN performance and functionality .
- Bluetooth is another type of wireless network that operates in the 2.4 GHz band and provides short-range, low-power, and low-cost wireless connectivity between devices, such as headphones, keyboards, mice, etc .
- Bluetooth uses a frequency hopping spread spectrum (FHSS) technique to avoid interference and increase security .
- Bluetooth follows a master-slave architecture, where a master device can communicate with up to seven slave devices in a piconet, and multiple piconets can form a scatternet .



### Mobile IP

- Mobile IP (MIP) is a protocol that allows mobile devices to move from one network to another while maintaining the same permanent IP address.
- Mobile IP is based on IP and can support any media that can support IP, such as wired and wireless networks.
- Mobile IP is designed to support seamless and continuous Internet connectivity, especially for roaming between overlapping wireless systems.
- Mobile IP consists of three main components: a home agent, a foreign agent, and a mobile node.
- A home agent is a router on the home network of the mobile node that maintains a binding table of the current location of the mobile node.
- A foreign agent is a router on the visited network of the mobile node that provides routing and other services to the mobile node.
- A mobile node is a device that can change its point of attachment to the Internet, such as a laptop or a smartphone.
- A mobile node has two IP addresses: a home address and a care-of address.
- A home address is a permanent IP address assigned to the mobile node on its home network.
- A care-of address is a temporary IP address assigned to the mobile node on the visited network.
- A mobile node registers its care-of address with its home agent, which updates the binding table and forwards any packets destined for the mobile node to the care-of address.
- A mobile node can use its home address to communicate with any other node on the Internet, regardless of its current location.
- A mobile node can also use its care-of address to communicate with other nodes on the visited network, which can reduce the overhead and latency of routing through the home agent.
- Mobile IP can be implemented for both IPv4 and IPv6, with some differences and extensions.
- Mobile IP for IPv4 is described in IETF RFC 5944, and extensions are defined in IETF RFC 4721.
- Mobile IP for IPv6 is described in IETF RFC 6275, and extensions are defined in IETF RFC 5555.
- Mobile IP can be used to find the local IP address of a mobile device on a network, such as an iPhone or an Android phone.
- To find the local IP address of an iPhone, one can go to Settings > Wi-Fi, tap the network name, and look for the IP Address field under the IPv4 Address header.
- To find the local IP address of an Android phone, one can go to Settings > Network & Internet > Wi-Fi, tap the network name, and look for the IP Address field under the Advanced section.



### WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer is of most interest to content developers because it contains among other things, device specifications, scripting languages, and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems. The application layer also includes the Wireless Application Environment (WAE), which provides a framework for developing and delivering applications and services over wireless networks.
  - Session Layer: This layer provides session management and transaction support for WAP applications. It consists of two protocols: the Wireless Session Protocol (WSP) and the Wireless Transaction Protocol (WTP). WSP is a binary-encoded version of HTTP that offers fast connection suspension and reconnection, and supports both connection-oriented and connectionless services. WTP is a lightweight transaction-oriented protocol that provides reliable request/response and unreliable datagram services.
  - Security Layer: This layer provides data integrity and privacy for WAP applications. It consists of the Wireless Transport Layer Security (WTLS) protocol, which is based on the Transport Layer Security (TLS) protocol used in the web. WTLS provides encryption, authentication, and data compression for WAP communications.
  - Transport Layer: This layer provides data transfer services for WAP applications. It consists of the Wireless Datagram Protocol (WDP), which is an adaptation layer that allows WAP to operate over various wireless network technologies, such as GSM, CDMA, and CDPD. WDP provides a common interface for the upper layers of the WAP protocol stack and hides the details of the underlying network from them.
  - Bearers: These are the physical wireless network technologies that carry the WAP traffic. They include GSM, CDMA, CDPD, SMS, GPRS, UMTS, and Bluetooth. Each bearer has its own characteristics, such as bandwidth, latency, and reliability, and may require different adaptations of the WAP protocols.
- The WAP architecture comprises several components, each serving a specific function. These components include:
  - WAP Gateway: This is a server that acts as an intermediary between the wireless network and the internet. It performs protocol conversion, data compression, and security functions. It also caches frequently accessed content and provides access control and billing services.
  - WAP Proxy: This is a client-side component that resides on the wireless device. It communicates with the WAP gateway and the WAP application server using the WAP protocols. It also interprets and displays the WML content on the device's screen.
  - WAP Application Server: This is a server that hosts the WAP applications and content. It generates dynamic WML pages based on the requests from the WAP proxy and the data from the web server or the database server. It also provides application logic and business rules for the WAP applications.
  - Web Server: This is a server that hosts the web content and resources for the WAP applications. It communicates with the WAP application server using the HTTP protocol. It may also provide access to other web services, such as email, news, and search engines.
  - Database Server: This is a server that stores and manages the data for the WAP applications. It communicates with the WAP application server using the SQL protocol or other data access methods. It may also provide data analysis and reporting services for the WAP applications.



### Protocol Stack for Wireless Networking

- A protocol stack is an implementation of a set of communication protocols that work together to provide network functionality.
- A protocol stack consists of different layers, each of which performs a specific function and interacts with the adjacent layers through well-defined interfaces.
- A protocol stack for wireless networking is designed to enable data transmission and reception over wireless channels, such as radio waves or infrared signals.
- A protocol stack for wireless networking may differ from a protocol stack for wired networking in some aspects, such as:
  - The need to discover and connect to other wireless devices dynamically.
  - The need to cope with variable and unreliable channel conditions, such as noise, interference, fading, and mobility.
  - The need to optimize the use of limited resources, such as bandwidth, power, and memory.
- A protocol stack for wireless networking may include the following layers :
  - Physical layer: This layer is responsible for encoding and decoding the data into signals that can be transmitted and received over the wireless medium. It also handles modulation, demodulation, synchronization, and error detection and correction.
  - Data link layer: This layer is responsible for framing and delimiting the data into packets that can be sent and received over the wireless medium. It also handles medium access control, flow control, and error control.
  - Network layer: This layer is responsible for routing and forwarding the packets across different wireless nodes or networks. It also handles addressing, congestion control, and network management.
  - Transport layer: This layer is responsible for providing end-to-end reliable and ordered delivery of data between wireless applications. It also handles segmentation, reassembly, and connection management.
  - Application layer: This layer is responsible for providing the specific functionality and services that the wireless applications require. It also handles user interface, data representation, and security.
- A protocol stack for wireless networking may use different protocols at each layer, depending on the type and characteristics of the wireless network. Some examples of wireless networking protocols are:
  - IEEE 802.11: This is a family of protocols that define the standards for wireless local area networks (WLANs). It includes variants such as 802.11a, 802.11b, 802.11g, 802.11n, and 802.11ac, which differ in terms of frequency, bandwidth, and data rate.
  - Bluetooth: This is a protocol that defines the standards for wireless personal area networks (WPANs). It enables short-range wireless communication between devices such as smartphones, laptops, headphones, and speakers.
  - Wireless in the subject of Mobile Computing: This is a broad term that refers to the use of wireless networks and devices to enable mobile computing, which is the ability to access and process data and applications from anywhere and anytime. It includes aspects such as wireless sensor networks, mobile ad hoc networks, mobile cloud computing, and mobile edge computing.



### Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, and processing power.
- WAE consists of several components, such as:
  - Wireless Markup Language (WML), which is a markup language similar to HTML, but optimized for small screens and user input methods.
  - Wireless Markup Language Script (WMLScript), which is a scripting language similar to JavaScript, but with a smaller footprint and less complexity.
  - Wireless Telephony Application Interface (WTAI), which is an extension that allows WAP applications to access phone-specific features, such as dialing, messaging, and call control.
  - Wireless Datagram Protocol (WDP), which is a transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS.
  - Wireless Session Protocol (WSP), which is a session layer protocol that provides reliable and secure communication between WAP clients and servers, and supports features such as caching, cookies, and content negotiation.
  - Wireless Transaction Protocol (WTP), which is a transaction layer protocol that provides efficient and reliable data exchange between WAP clients and servers, and supports features such as segmentation, reassembly, and acknowledgment.
  - Wireless Application Protocol Binary XML (WBXML), which is a binary representation of XML documents, used to reduce the size and increase the speed of data transmission.
- WAE provides a vendor-neutral and platform-independent application architecture that supports browsing, scripting, and extensions that allow cellular network operators to offer network services within WAP.



### Applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves or infrared signals. Wireless networking has many applications, such as:

  - Providing internet access to mobile devices, such as laptops, smartphones, tablets, etc.
  - Connecting devices within a local area network (LAN), such as printers, scanners, cameras, etc.
  - Enabling wireless personal area networks (WPANs), such as Bluetooth, that allow devices to exchange data over short distances.
  - Supporting wireless sensor networks (WSNs), such as ZigBee, that consist of small, low-power devices that monitor physical or environmental conditions.
  - Facilitating wireless ad hoc networks, such as Wi-Fi Direct, that allow devices to form spontaneous connections without a central coordinator.

- Wireless LAN (WLAN) is a type of wireless networking that connects devices within a limited area, such as a home, office, campus, etc. WLANs use the IEEE 802.11 standard, which defines the medium access control (MAC) and physical (PHY) layers of the wireless communication protocol. Some of the features and issues of WLANs are:

  - WLANs use the Ethernet protocol and CSMA/CA (carrier sense multiple access with collision avoidance) for path sharing. CSMA/CA is a technique that avoids collisions by sensing the channel before transmitting and backing off if the channel is busy.
  - WLANs operate in the unlicensed frequency bands, such as 2.4 GHz and 5 GHz, which are shared by other devices and sources of interference. WLANs use techniques such as frequency hopping, direct sequence spread spectrum, and orthogonal frequency division multiplexing to cope with interference and multipath fading.
  - WLANs support different modes of operation, such as infrastructure mode and ad hoc mode. In infrastructure mode, WLANs use a base station, called an access point (AP), that connects the wireless devices to a wired network. In ad hoc mode, WLANs use peer-to-peer (P2P) communication, without an AP, using Wi-Fi Direct technology.
  - WLANs have different versions, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that offer different data rates, ranges, and features. The latest version, 802.11ax, also known as Wi-Fi 6, can achieve up to 10 Gbps of data rate and support up to 1024 devices per AP.

- Bluetooth is a wireless technology that enables short-range communication between devices, such as headphones, keyboards, mice, speakers, etc. Bluetooth uses the IEEE 802.15.1 standard, which covers the MAC and PHY layers of the wireless protocol. Some of the features and issues of Bluetooth are:

  - Bluetooth operates in the 2.4 GHz frequency band, which is divided into 79 channels, each 1 MHz wide. Bluetooth uses frequency hopping spread spectrum (FHSS) to hop from one channel to another, avoiding interference and increasing security.
  - Bluetooth supports different versions, such as Bluetooth 1.0, Bluetooth 2.0, Bluetooth 3.0, Bluetooth 4.0, Bluetooth 5.0, and Bluetooth 6.0, that offer different data rates, ranges, and features. The latest version, Bluetooth 6.0, can achieve up to 48 Mbps of data rate and up to 400 meters of range.
  - Bluetooth supports different profiles, such as Advanced Audio Distribution Profile (A2DP), Hands-Free Profile (HFP), Human Interface Device Profile (HID), etc., that define the specific capabilities and functions of the devices. For example, A2DP enables high-quality audio streaming, HFP enables hands-free calling, and HID enables wireless input devices.



## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

- Data management issues in mobile computing refer to the challenges and problems that arise when managing data in a mobile environment, where users can access data from and to mobile devices, such as smartphones, tablets, laptops, etc.
- Some of the data management issues in mobile computing are   :
  - Mobile database design: How to design a database that can support the frequent disconnections and reconnections of mobile devices, the limited resources of mobile devices, the heterogeneity of mobile devices and networks, and the global name resolution problem.
  - Security: How to protect the data on mobile devices from unauthorized access, theft, loss, or damage, and how to ensure the privacy and integrity of the data during transmission and synchronization.
  - Data distribution and replication: How to distribute and replicate the data among mobile devices and fixed servers, and how to maintain the consistency and availability of the data in the presence of network failures, mobility, and disconnections.
  - Data caching and hoarding: How to cache and hoard the data on mobile devices to improve the performance and availability of data access, and how to manage the cache and hoard consistency and coherence with the original data sources.
  - Data synchronization and reconciliation: How to synchronize and reconcile the data between mobile devices and fixed servers, and how to handle the conflicts and inconsistencies that may arise due to concurrent updates, disconnections, or mobility.
  - Data broadcasting and dissemination: How to broadcast and disseminate the data from fixed servers to mobile devices, and how to support the selective tuning and filtering of the data by the mobile devices according to their interests and preferences.
  - Query processing and optimization: How to process and optimize the queries issued by mobile devices, and how to take into account the characteristics and constraints of mobile devices, networks, and data sources.
  - Transaction management and recovery: How to support the transactional properties of atomicity, consistency, isolation, and durability in mobile computing, and how to recover from the failures and errors that may occur in mobile computing.
- Data replication for mobile computers is a technique that involves creating and maintaining multiple copies of the same data on different mobile devices or fixed servers, in order to improve the data availability, reliability, and performance in mobile computing   .
- Some of the benefits of data replication for mobile computers are:
  - It reduces the network traffic and communication cost by allowing the mobile devices to access the data locally or from nearby replicas, rather than from distant servers.
  - It improves the data access performance and response time by avoiding the network latency and congestion, and by exploiting the parallelism and load balancing among the replicas.
  - It enhances the data availability and fault tolerance by enabling the mobile devices to access the data even when they are disconnected from the network or when the network or the servers are down.
  - It increases the scalability and adaptability of the system by allowing the addition and removal of mobile devices and replicas without affecting the data access.
- Some of the challenges of data replication for mobile computers are:
  - It requires more storage space and memory on the mobile devices and the servers to store the replicas, which may be limited or scarce resources in mobile computing.
  - It introduces the problem of replica consistency and coherence, which means that the replicas should reflect the same state and value of the data, and that any update made to one replica should be propagated and reflected on the other replicas.
  - It involves the trade-off between the data freshness and the data availability, which means that the more frequent the synchronization and reconciliation of the replicas, the more fresh and consistent the data, but the less available and accessible the data.
  - It depends on the network connectivity and bandwidth, which may be variable and unreliable in mobile computing, and which may affect the synchronization and reconciliation of the replicas.
- Adaptive clustering for mobile is a technique that involves grouping the mobile devices into clusters based on their proximity, similarity, or common interests, and assigning a cluster head for each cluster, which acts as a representative and a coordinator for the cluster members   .
- Some of the benefits of adaptive clustering for mobile are:
  - It reduces the network overhead and energy consumption by allowing the cluster head to perform the data aggregation, compression, filtering, and dissemination for the cluster members, rather than having each mobile device communicate with the servers or the other mobile devices individually.



### Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables. Wireless networks can enable mobile computing, which is the ability to access and process data from anywhere and anytime using portable devices.

Some of the topics related to wireless networks and mobile computing are:

- Data management issues: These are the challenges and solutions for managing data in wireless networks and mobile environments, such as data consistency, availability, caching, synchronization, replication, dissemination, and query processing. 
- Data replication for mobile computers: This is the process of creating and maintaining multiple copies of data on different mobile devices or servers, to improve data availability, reliability, and performance. Data replication can be classified into two types: eager replication and lazy replication. Eager replication updates all the replicas as soon as a change occurs, while lazy replication updates the replicas periodically or on demand. 
- Adaptive clustering for mobile wireless networks: This is a technique to organize mobile nodes into groups or clusters, based on their location, mobility, and communication patterns. Adaptive clustering can improve network scalability, resource utilization, energy efficiency, routing, and throughput. Adaptive clustering can be based on different criteria, such as node degree, node ID, node location, node mobility, node battery power, or node traffic load.  
- File system: This is the component of the operating system that manages the storage and retrieval of data on the devices. File systems can be designed to support wireless networks and mobile computing, by providing features such as data compression, encryption, caching, replication, synchronization, and fault tolerance. Some examples of file systems for mobile computing are Coda, Ficus, Odyssey, and Rover. 
- Disconnected operations: These are the situations where mobile devices lose their connection to the network or the server, due to factors such as low signal strength, high interference, or battery depletion. Disconnected operations can affect the data availability, consistency, and security of the mobile devices. To cope with disconnected operations, mobile devices can use techniques such as hoarding, reconciliation, and encryption. Hoarding is the process of prefetching and caching data that may be needed during disconnection. Reconciliation is the process of resolving conflicts and inconsistencies that may arise when the connection is restored. Encryption is the process of protecting the data from unauthorized access or modification. 
- Mobile agents computing: This is a paradigm of distributed computing, where software agents can migrate from one host to another in the network, carrying their code, data, and state. Mobile agents can perform tasks on behalf of the mobile devices, such as data collection, processing, filtering, and delivery. Mobile agents can reduce the network traffic, latency, and bandwidth consumption, as well as enhance the adaptability, scalability, and fault tolerance of the system. 
- Security and fault tolerance: These are the aspects of ensuring the confidentiality, integrity, and availability of the data and the system in wireless networks and mobile computing. Security and fault tolerance can be achieved by using techniques such as authentication, authorization, encryption, digital signatures, checksums, backups, replication, recovery, and checkpointing. 
- Transaction processing in a mobile computing environment: This is the process of executing a sequence of operations on the data, such as read, write, commit, or abort, in a reliable and consistent manner. Transaction processing in a mobile computing environment faces challenges such as network partitioning, disconnection, mobility, concurrency, and limited resources. Transaction processing can be supported by using protocols such as two-phase commit, three-phase commit, optimistic concurrency control, or timestamp ordering. 

: Mobile Computing (PDF Notes) - Gate Knowledge
: Adaptive clustering for mobile wireless networks | IEEE Journals ...
: Mobile Computing: Data Management Issues - Academia.edu
: Clustering In Mobile Wireless Ad Hoc Networks | SpringerLink
: Wireless Networking and Mobile Data Management | SpringerLink



### File system for mobile computing

- A file system is a software component that manages the storage and retrieval of data on a persistent device, such as a hard disk, flash memory, or optical disc.
- A file system for mobile computing is a file system that supports the mobility of both users and devices, and adapts to the challenges of wireless and mobile environments, such as network disconnection, low bandwidth, high latency, and limited battery power.
- Some of the design issues for a file system for mobile computing are:
  - How to provide location transparency, i.e., the ability to access files regardless of their physical location or the location of the user or device.
  - How to support user mobility, i.e., the ability to access files from different devices and networks, and to migrate files across devices and networks.
  - How to ensure data consistency and availability, i.e., the ability to access the latest version of a file and to handle concurrent updates and conflicts, especially in the presence of network disconnection or partition.
  - How to optimize network and device resources, i.e., the ability to reduce network traffic and storage overhead, and to conserve battery power and bandwidth.
  - How to provide security and privacy, i.e., the ability to authenticate users and devices, to encrypt and decrypt data, and to control access to files and directories.
- One of the design options for a file system for mobile computing is to use a distributed file system, such as the Andrew File System (AFS) or the Coda File System, which are based on the client-server model, where a central server stores the files and a client caches the files locally for faster access and offline operation.
- A distributed file system for mobile computing should provide the following features:
  - Caching: The client should cache the files locally to improve performance and availability, and to reduce network traffic and power consumption. The caching should be persistent, i.e., the cached files should survive across reboots and crashes, and should be synchronized with the server periodically or on demand.
  - Replication: The server should replicate the files across multiple servers to improve availability and fault tolerance, and to balance the load. The replication should be consistent, i.e., the replicas should have the same version of a file, and should be updated atomically and reliably.
  - Disconnected operation: The client should be able to operate in the absence of network connectivity, i.e., to read and write files from the local cache, and to reconcile the changes with the server when the network is restored. The reconciliation should handle conflicts, i.e., the situation where the same file has been modified by different clients or servers while disconnected.
  - Adaptive clustering: The client should be able to form clusters with other nearby clients to share files and resources, and to reduce the dependency on the server. The clustering should be adaptive, i.e., the clusters should be formed and dissolved dynamically based on the network conditions and the user preferences.
- An example of a file system for mobile computing that implements these features is the Coda File System, which is an extension of the AFS. Coda provides the following advantages:
  - High performance through client-side persistent caching
  - High availability through server replication
  - Disconnected operation for mobile computing
  - Network bandwidth adaptation
  - Security model for authentication, encryption and access control
  - Continued operation during partial network failures in server network
  - Good scalability



### Disconnected operations

- Disconnected operations are a mode of operation in mobile computing that allows users to execute applications when the network is unavailable or unreliable .
- Disconnected operations can be voluntary or involuntary, depending on the user's choice or the network conditions .
- Disconnected operations require mechanisms to handle data consistency, synchronization, and recovery when the network is restored  .
- Disconnected operations can benefit from mobile computation, which is the ability to migrate code and data across different hosts in the network .
- Disconnected operations can improve the availability, performance, and scalability of mobile applications  .



## Unit 4 - Mobile Agents computing, security and fault tolerance, transaction processing in mobile computing

- Mobile agents are software entities that can autonomously migrate from one host to another in a network, carrying their code and state with them.
- Mobile agents can be used for various applications, such as distributed information retrieval, electronic commerce, network management, and load balancing.
- Mobile agents face several challenges, such as security, fault tolerance, and transaction processing, which need to be addressed for their successful deployment.

### Security
- Security is a major concern for mobile agents, as they may encounter malicious hosts or other agents that can tamper with their code, data, or execution.
- Some of the security threats for mobile agents are:
  - Code tampering: modifying the agent's code to alter its functionality or behavior.
  - Data tampering: modifying the agent's data to corrupt its state or results.
  - Eavesdropping: intercepting the agent's communication or accessing its private data.
  - Repudiation: denying the agent's actions or transactions.
  - Masquerading: impersonating the agent or its owner.
  - Denial of service: preventing the agent from completing its task or returning to its owner.
- Some of the security techniques for mobile agents are:
  - Encryption: encrypting the agent's code, data, or communication to prevent unauthorized access or modification.
  - Authentication: verifying the identity and integrity of the agent or its owner using digital signatures, certificates, or passwords.
  - Authorization: granting or denying access rights to the agent or its resources based on predefined policies or rules.
  - Auditing: logging the agent's actions or transactions for accountability or verification purposes.
  - Sandbox: isolating the agent's execution environment from the host system to limit its access or impact.
  - Obfuscation: hiding or obscuring the agent's code or data to make it difficult to analyze or modify.

### Fault tolerance
- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures or errors.
- In mobile agent computing, any component of the network - node, link, or agent - may fail at any time, thus preventing the agent from continuing its execution or returning its results.
- Some of the fault tolerance techniques for mobile agents are:
  - Replication: creating multiple copies of the agent and executing them on different hosts to increase the probability of success or reduce the response time.
  - Checkpointing: saving the agent's state periodically or at strategic points to enable its recovery or restart in case of failure.
  - Recovery: restoring the agent's state from a checkpoint or a replica and resuming its execution from the point of failure.
  - Migration: moving the agent from a faulty or overloaded host to another host to avoid or escape from failure.
  - Rejuvenation: refreshing or renewing the agent's code or data to prevent or correct errors or degradation.

### Transaction processing
- Transaction processing is the execution of a series of operations that form a logical unit of work, such as a database query, a payment, or a reservation.
- Transactions have four properties: atomicity, consistency, isolation, and durability (ACID), which ensure the correctness and reliability of the operations and their results.
- In mobile agent computing, transaction processing is challenging, as the agent may visit multiple hosts, interact with multiple resources, and encounter failures or concurrency issues during its execution.
- Some of the transaction processing techniques for mobile agents are:
  - Two-phase commit: coordinating the commitment or abort of a transaction among multiple participants using a prepare and a commit phase.
  - Nested transactions: structuring a transaction as a hierarchy of subtransactions, each with its own ACID properties, to allow partial commitment or abort.
  - Sagas: decomposing a transaction into a sequence of compensatable actions, each with a corresponding undo action, to allow partial rollback or recovery.
  - Optimistic concurrency control: allowing concurrent execution of transactions without locking, and detecting and resolving conflicts at commit time.
  - Mobile transaction models: defining the semantics and protocols for mobile transactions, such as atomic, consistent, isolated, and mobile (ACIM), or atomic, consistent, isolated, and resilient (ACIR).



### Environment for Mobile Agents Computing

- A mobile agent is a piece of software that can move from one host to another in a network, carrying its state and data, and executing autonomously.
- A mobile agent environment is the infrastructure that supports the creation, migration, execution, and communication of mobile agents.
- A mobile agent environment consists of the following components:
  - A mobile agent platform, which is the software layer that provides the basic services and facilities for mobile agents, such as agent creation, migration, execution, communication, security, and management.
  - A mobile agent language, which is the programming language or framework that enables the development of mobile agents, such as Java, Python, or Aglets.
  - A mobile agent system, which is the application or middleware that uses mobile agents to achieve a specific goal, such as distributed information retrieval, network management, or e-commerce.
- A mobile agent environment can be classified according to different criteria, such as the mobility model, the communication model, the security model, or the application domain .
  - The mobility model defines how and when mobile agents move from one host to another, such as strong mobility (the agent can move at any point of its execution) or weak mobility (the agent can only move when it is idle or suspended).
  - The communication model defines how mobile agents interact with each other and with other entities, such as message passing, remote method invocation, or tuple spaces.
  - The security model defines how mobile agents protect themselves and their hosts from malicious attacks, such as encryption, authentication, access control, or sandboxing.
  - The application domain defines the specific problem or scenario that mobile agents are used to solve or support, such as mobile data computing, e-commerce, networking, manufacturing, or scientific computing .



## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over wireless links.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved by using GPS, signal strength, angle of arrival, or other techniques.
- MAC (Medium Access Control) issues refer to the challenges of coordinating the access of multiple nodes to the shared wireless medium, avoiding collisions, and ensuring fairness and efficiency. MAC protocols for ad hoc networks can be classified into contention-based and reservation-based protocols, depending on whether they use random or deterministic access schemes.
- Routing protocols are algorithms that enable the nodes in an ad hoc network to discover and maintain routes to other nodes. Routing protocols can be categorized into proactive, reactive, and hybrid protocols, depending on whether they maintain routes constantly, on-demand, or selectively.
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks that maintains complete and consistent routing information at each node. GSR uses link state packets to exchange topology information periodically, and uses a shortest path algorithm to compute routes. GSR suffers from high overhead and scalability issues.



### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing protocol for ad hoc mobile networks based on the Bellman–Ford algorithm.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- The sequence number is used to distinguish stale route information from the new and thus prevent the formation of routing loops.
- Each node maintains a routing table that contains the following information for each destination: the next hop, the number of hops, the sequence number, and the installation time.
- The sequence number is originated and incremented by the destination node whenever it updates its route information.
- Each node periodically broadcasts its routing table to its neighbors, and also sends triggered updates when it detects any significant change in the topology.
- The nodes update their routing tables based on the received information, using the following rules:
  - If the received sequence number is greater than the stored one, the node updates the route with the new information.
  - If the received sequence number is equal to the stored one, the node compares the number of hops and chooses the route with the smaller hop count.
  - If the received sequence number is smaller than the stored one, the node discards the received information.
- DSDV provides only one route for a source/destination pair, and thus does not support multipath routing.
- DSDV reduces the control overhead and latency of the classical Bellman-Ford algorithm, but still suffers from frequent updates and wasted bandwidth.



### Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing, which means the source node specifies the complete sequence of intermediate nodes to reach the destination node .
- It consists of two main phases: route discovery and route maintenance.
- Route discovery is initiated by the source node when it has data to send to the destination node and does not have a valid route.
- The source node broadcasts a route request packet that contains the source and destination addresses, a unique identification number, and a list of nodes that have forwarded the packet.
- Each intermediate node that receives the route request packet checks if it is the destination node or if it has a route to the destination node in its cache.
- If yes, it sends a route reply packet back to the source node along the reverse path of the route request packet.
- If no, it appends its own address to the list of nodes and forwards the route request packet to its neighbors.
- The source node collects multiple route reply packets and selects the best route based on some criteria, such as the shortest hop count or the lowest delay.
- Route maintenance is performed by the source node and the intermediate nodes to detect and repair any link failures along the route.
- The source node monitors the acknowledgments from the next hop node to ensure the successful delivery of the data packets.
- If the source node does not receive an acknowledgment within a certain time, it assumes that the link to the next hop node is broken and initiates a new route discovery.
- The intermediate nodes also monitor the link status to their next hop nodes and send a route error packet to the source node if they detect a link failure.
- The source node then removes the broken link from its cache and tries to find an alternative route to the destination node.
- DSR has some advantages, such as:
  - It reduces the overhead of periodic routing updates and table maintenance .
  - It allows multiple routes to the same destination and enables route caching and route reuse .
  - It adapts quickly to the topology changes and supports asymmetric and unidirectional links .
- DSR also has some disadvantages, such as:
  - It may incur high overhead and latency for long routes due to the source routing mechanism .
  - It may suffer from stale routes and route loops due to the lack of feedback from the destination node .
  - It may not scale well for large networks with high mobility and traffic load .



### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks  .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing  .
- AODV offers quick adaptation to dynamic link conditions, low processing and memory overhead, low network utilization, and determines unicast routes to destinations within the ad hoc network .
- AODV uses two types of messages: route request (RREQ) and route reply (RREP)  .
- AODV uses sequence numbers to ensure loop-free and up-to-date routes  .
- AODV uses route error (RERR) messages to notify the source of a broken link  .
- AODV uses hello messages to maintain local connectivity and detect link failures  .
- AODV is the routing protocol used in Zigbee – a low power, low data rate wireless ad hoc network.
- AODV has various implementations such as MAD-HOC, Kernel-AODV, AODV-UU, AODV-UCSB and AODV-UIUC.
- AODV won the SIGMOBILE Test of Time Award in 2018.



### Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated on-demand routing protocol that was developed by Vincent Park and Scott Corson in 1997 .
- TORA is based on the concept of link reversal, which is a distributed algorithm that dynamically maintains a directed acyclic graph (DAG) of routes from the source to the destination .
- TORA consists of three main phases: route creation, route maintenance, and route erasure .
- Route creation: The source node initiates the route discovery process by broadcasting a query packet containing its own height, which is a tuple of four values: (τ, oid, r, δ). The height represents the logical distance from the destination and is used to construct the DAG. The τ value is a timestamp, the oid value is the originator id, the r value is a reflection flag, and the δ value is a propagation mode flag . The query packet is propagated through the network until it reaches the destination or an intermediate node that has a route to the destination. The node that receives the query packet updates its own height to be greater than that of the sender and sends a reply packet containing its new height back to the sender. The reply packet is used to establish a downward link in the DAG. The route creation phase ends when the source node receives a reply packet .
- Route maintenance: The route maintenance phase is triggered when a link failure occurs in the DAG. The node that detects the link failure sets its height to NULL and broadcasts an update packet containing its new height to its neighbors. The update packet causes the nodes that receive it to adjust their heights accordingly and propagate the update packet further if necessary. The update packet also reverses the direction of the affected links, creating new downward links in the DAG. The route maintenance phase ends when the network reaches a consistent state .
- Route erasure: The route erasure phase is initiated when a source node or an intermediate node no longer needs a route to the destination. The node broadcasts a clear packet containing the destination id to erase all the routes to that destination. The clear packet is flooded through the network and causes the nodes that receive it to reset their heights to NULL and delete any routing information related to that destination .
- TORA is an efficient, highly adaptive, and scalable routing protocol that can handle frequent topology changes and network partitions  . However, TORA also has some limitations, such as the possibility of generating temporary routing loops, the overhead of maintaining multiple routes, and the dependence on synchronized clocks .



### QoS in Ad Hoc Networks

- Quality of service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc. 
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or central coordination. 
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes and applications.  
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.  
- QoS in ad hoc networks can be classified into two categories: hard QoS and soft QoS. Hard QoS guarantees the QoS requirements of the applications with strict bounds, while soft QoS provides the QoS requirements with probabilistic bounds or best-effort service.  
- QoS in ad hoc networks can be supported by various mechanisms, such as QoS-aware routing protocols, QoS-aware MAC protocols, QoS-aware cross-layer design, QoS-aware resource management, QoS-aware admission control, QoS-aware scheduling, QoS-aware traffic shaping, etc.   
- QoS in ad hoc networks can be evaluated by various metrics, such as throughput, delay, jitter, packet loss, packet delivery ratio, end-to-end delay, energy consumption, etc.   
- QoS in ad hoc networks can be improved by various techniques, such as adaptive QoS, QoS negotiation, QoS feedback, QoS monitoring, QoS adaptation, QoS optimization, QoS prediction, QoS learning, etc.



### Applications of Ad Hoc Networks

Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of mobile nodes that communicate with each other directly or through intermediate nodes. Ad hoc networks have many potential applications in various domains, such as:

- **Military battlefield**: Ad hoc networks can provide secure and reliable communication among soldiers, vehicles, and command centers in hostile environments. They can also support situational awareness, target tracking, and data fusion.
- **Vehicular ad hoc networks (VANETs)**: Ad hoc networks can enable vehicles to exchange information about traffic conditions, road safety, navigation, and entertainment. They can also support intelligent transportation systems, such as collision avoidance, platooning, and cooperative driving .
- **Smartphone ad hoc networks (SPANs)**: Ad hoc networks can allow smartphones to form peer-to-peer (P2P) networks without depending on cellular or Wi-Fi networks. They can enable users to share data, resources, and services, such as file transfer, chat, gaming, and social networking .
- **Wireless sensor networks (WSNs)**: Ad hoc networks can connect a large number of sensor nodes that collect and process data from the physical environment. They can support various applications, such as environmental monitoring, disaster management, health care, and smart homes.
- **Industrial and commercial applications**: Ad hoc networks can facilitate cooperative mobile data exchange among workers, customers, and devices in different scenarios, such as manufacturing, mining, retail, and tourism.

