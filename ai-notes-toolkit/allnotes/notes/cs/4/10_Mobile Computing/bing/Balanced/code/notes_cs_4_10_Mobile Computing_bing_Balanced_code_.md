

## Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks.
- Mobile computing enables users to communicate, access information, and perform tasks anytime and anywhere, without being constrained by physical location or wired connections.
- Mobile computing involves various challenges and issues, such as:
  - Mobility: the ability to move freely and seamlessly across different networks and environments.
  - Connectivity: the quality and availability of wireless connections and services.
  - Power consumption: the limited battery life and energy efficiency of mobile devices.
  - Security: the protection of data and privacy in wireless and open networks.
  - User interface: the design and usability of mobile applications and devices.
  - Scalability: the ability to handle a large number of mobile users and devices.
  - Interoperability: the compatibility and integration of different mobile platforms and standards.
- Wireless telephony is the transmission and reception of voice and data over radio waves, without the use of wires or cables.
- Wireless telephony enables users to make and receive phone calls, send and receive text messages, access the internet, and use other mobile services.
- Wireless telephony is based on the cellular concept, which divides a geographical area into smaller regions called cells, each served by a base station that communicates with mobile stations (such as mobile phones) within its range.
- The cellular concept allows for frequency reuse, which means that the same radio frequencies can be used by different cells that are sufficiently far apart, without causing interference.
- The cellular concept also enables handover, which means that a mobile station can switch from one base station to another as it moves across cells, without interrupting the communication.
- GSM (Global System for Mobile communication) is a standard developed by the European Telecommunications Standards Institute (ETSI) to describe the protocols for second-generation (2G) digital cellular networks used by mobile devices such as mobile phones and tablets.
- GSM uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate radio channels to multiple users simultaneously.
- GSM operates on four different frequency bands: 850 MHz, 900 MHz, 1800 MHz, and 1900 MHz.
- GSM provides various services, such as:
  - Voice calls: the transmission and reception of speech over GSM networks.
  - Short message service (SMS): the exchange of text messages of up to 160 characters between GSM users.
  - Multimedia message service (MMS): the exchange of multimedia messages, such as images, audio, and video, between GSM users.
  - General packet radio service (GPRS): the delivery of data packets over GSM networks, enabling internet access and other data services.
  - Enhanced data rates for GSM evolution (EDGE): an enhancement of GPRS that increases the data transmission speed and capacity of GSM networks.
  - Global roaming: the ability of GSM users to use their mobile devices in other countries and regions that support GSM networks.



# Air-interface for Mobile Computing

- The air interface is the communication link between the two stations in mobile or wireless communication.
- The air interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection.
- The air interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network.
- Different cellular standards use different air interfaces, such as TDMA and CDMA for GSM, OFDMA for LTE, etc .
- The air interface is also called the UM interface in GSM, as it is analogous to U interface of ISDN.
- The air interface is one of the key components for 5G and beyond, as it needs to support diverse services and requirements, such as high data rate, low latency, massive connectivity, etc.
- The air interface waveform of LTE and NR, the 5G standard, is based on orthogonal frequency division multiplexing (OFDM), which is highly spectrally efficient and robust to channel dispersion.




Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Mobile Computing. Here is the content for the topic of channel structure for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

### Channel structure

- A channel is a medium or a path that carries information from one point to another in a communication system.
- In mobile computing, channels are used to transmit and receive data between mobile devices and base stations or between base stations and network controllers.
- Channels can be classified into two types: physical channels and logical channels.
- Physical channels are the actual radio frequencies or time slots that are allocated for communication. Logical channels are the information or data that are carried within the physical channels.
- Different types of logical channels are used for different purposes, such as traffic channels, control channels, and broadcast channels.
- Traffic channels (TCHs) are used to carry voice or data between a mobile device and a base station. Control channels (CCHs) are used to carry signaling and control information, such as call setup, authentication, location update, etc. Broadcast channels (BCCHs) are used to broadcast system information, such as cell identity, frequency allocation, etc.
- In GSM, a cellular network standard, there are several logical channels that are defined for different functions. Some of them are:

  - Broadcast Control Channel (BCCH): It is used to broadcast system information and parameters to all mobile devices in a cell.
  - Frequency Correction Channel (FCCH): It is used to provide frequency synchronization to the mobile devices.
  - Synchronization Channel (SCH): It is used to provide time synchronization and frame alignment to the mobile devices.
  - Random Access Channel (RACH): It is used by the mobile devices to request access to the network or to initiate a call.
  - Paging Channel (PCH): It is used by the network to page a mobile device for an incoming call or a message.
  - Access Grant Channel (AGCH): It is used by the network to assign a traffic channel or a dedicated control channel to a mobile device.
  - Standalone Dedicated Control Channel (SDCCH): It is used to carry signaling and control information between a mobile device and a base station during call setup, authentication, encryption, etc.
  - Slow Associated Control Channel (SACCH): It is used to carry supplementary information, such as power control, timing advance, measurement reports, etc. along with a traffic channel or a dedicated control channel.
  - Fast Associated Control Channel (FACCH): It is used to carry urgent signaling and control information, such as handover commands, call release, etc. by stealing some bits from a traffic channel or a dedicated control channel.
  - Cell Broadcast Channel (CBCH): It is used to broadcast short messages, such as emergency alerts, news, etc. to all mobile devices in a cell.

- The channel structure in GSM is shown in the following diagram:

Channel structure in GSM

- The channel structure in mobile computing is designed to achieve efficient use of the available spectrum, to support multiple users and services, and to provide reliable and secure communication.



### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile users in wireless cellular networks.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is the process of informing the network about the current location of the mobile user, usually initiated by the mobile user when it moves across a predefined boundary called a registration area (RA).
- Location lookup is the process of finding the current location of the mobile user, usually initiated by the network when it needs to deliver a call or a message to the mobile user.
- Paging is the process of notifying the mobile user about an incoming call or a message, usually initiated by the network after locating the mobile user.
- Location management involves two types of databases: the home location register (HLR) and the visitor location register (VLR).
- The HLR is a centralized database that stores the permanent information of all the mobile users in the network, such as their service profile, authentication data, and current location (RA).
- The VLR is a local database that stores the temporary information of the mobile users that are currently visiting a specific RA, such as their temporary identity, authentication data, and current cell.
- The HLR and the VLR communicate with each other to update and retrieve the location information of the mobile users.
- The HLR-VLR scheme is a hierarchical location management scheme that divides the service coverage area into RAs, each with a VLR. Each RA covers a group of base stations (cells).
- The HLR-VLR scheme reduces the location update cost by limiting the updates to the VLRs within the same RA, and reduces the location lookup cost by querying the HLR only once for each RA.
- The HLR-VLR scheme can be further improved by using caching, replication, or mobility prediction techniques to reduce the communication overhead between the HLR and the VLRs.
- Handoff is the process of transferring the ongoing communication of a mobile user from one base station to another, without interrupting the service quality or dropping the call.
- Handoff is necessary to maintain the continuity of service and to balance the load among the base stations.
- Handoff involves four main steps: handoff initiation, handoff decision, handoff execution, and handoff completion.
- Handoff initiation is the process of detecting the need for a handoff, usually based on the signal strength or the quality of service measurements.
- Handoff decision is the process of selecting the target base station for the handoff, usually based on the signal strength, the load, or the user preference.
- Handoff execution is the process of switching the communication channel from the old base station to the new base station, usually with the help of a mobile switching center (MSC) or a base station controller (BSC).
- Handoff completion is the process of updating the location information of the mobile user in the network databases, such as the HLR and the VLR.
- Handoff can be classified into different types based on the direction, the timing, the control, or the technology of the handoff.
- The direction of the handoff can be either horizontal or vertical. Horizontal handoff occurs when the mobile user moves from one base station to another within the same network or the same technology. Vertical handoff occurs when the mobile user moves from one network to another or from one technology to another.
- The timing of the handoff can be either hard or soft. Hard handoff occurs when the mobile user breaks the connection with the old base station before establishing the connection with the new base station. Soft handoff occurs when the mobile user maintains the connection with both the old and the new base stations until the handoff is completed.
- The control of the handoff can be either network-controlled or mobile-controlled. Network-controlled handoff occurs when the network initiates and decides the handoff based on the network measurements. Mobile-controlled handoff occurs when the mobile user initiates and decides the handoff based on the mobile measurements.
- The technology of the handoff can be either circuit-switched or packet-switched. Circuit-switched handoff occurs when the mobile user switches from one circuit to another within the same or different networks. Packet-switched handoff occurs when the mobile user switches from one packet to another within the same or different networks.



### Channel allocation in cellular systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- Channels are the basic units of communication resources that can carry signals between a base station and a mobile terminal.
- Channels can be divided into two types: frequency channels and time channels. Frequency channels use different frequencies to transmit signals, while time channels use different time slots to transmit signals.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots and bandwidth, while minimizing interference and maximizing quality of service .
- Channel allocation strategies can be classified into three categories: fixed channel allocation, dynamic channel allocation and hybrid channel allocation .
- Fixed channel allocation (FCA) assigns a fixed number of channels to each cell, regardless of the traffic demand. FCA is simple and easy to implement, but it may cause channel wastage or blocking in some cells.
- Dynamic channel allocation (DCA) assigns channels to cells on demand, based on the traffic load and interference conditions. DCA is more flexible and adaptive, but it requires more complex coordination and signaling among cells.
- Hybrid channel allocation (HCA) combines FCA and DCA, by dividing the channels into two sets: a fixed set and a dynamic set. The fixed set is allocated to each cell permanently, while the dynamic set is allocated to cells temporarily, based on the traffic and interference situation. HCA can balance the advantages and disadvantages of FCA and DCA.



### CDMA for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- CDMA stands for Code Division Multiple Access and is a spread spectrum multiple access technique  .
- Spread spectrum technique spreads bandwidth of data in a uniform manner for the same transmitted power.
- CDMA is a digital cellular technology used for mobile communication .
- CDMA is the base on which access methods such as cdmaOne, CDMA2000, and WCDMA are built .
- CDMA allows numerous signals to occupy a single transmission channel, optimizing the use of available bandwidth .
- CDMA uses a special coding scheme, where each transmitter is assigned a code, to allow multiple users to be multiplexed over the same physical channel  .
- CDMA is a form of direct-sequence spread spectrum (DSSS) modulation, where the data signal is multiplied by a pseudorandom noise (PN) code sequence that has a much higher data rate than the original signal  .
- CDMA has several advantages over other multiple access techniques, such as:
  - Higher spectral efficiency, as more users can share the same bandwidth without interference  .
  - Better security, as the code sequence makes the signal difficult to intercept or jam  .
  - Improved voice quality, as the signal can be recovered from noise and fading by using error correction and diversity techniques  .
  - Greater flexibility, as the code sequence can be dynamically changed to accommodate different services and user demands  .
- CDMA has some disadvantages, such as:
  - Higher complexity, as the transmitter and receiver need to synchronize the code sequence and perform complex signal processing  .
  - Higher power consumption, as the transmitter needs to spread the signal over a wide bandwidth and the receiver needs to perform correlation and decoding  .
  - Near-far problem, where a strong signal from a nearby user can interfere with a weak signal from a faraway user, unless power control is implemented  .
- CDMA is one of the multiple access techniques used in mobile computing, along with FDMA (Frequency Division Multiple Access) and TDMA (Time Division Multiple Access).
- FDMA divides the available bandwidth into frequency bands, and assigns each user a different band.
- TDMA divides the available bandwidth into time slots, and assigns each user a different slot.
- CDMA, FDMA, and TDMA can be compared based on the following criteria:
  - Bandwidth efficiency: CDMA > TDMA > FDMA
  - Power efficiency: FDMA > TDMA > CDMA
  - Complexity: CDMA > TDMA > FDMA
  - Security: CDMA > TDMA > FDMA
  - Interference: CDMA < TDMA < FDMA
- CDMA is used in wireless telephony, which is the provision of telephone services over wireless networks  .
- Wireless telephony is based on the cellular concept, which divides a geographical area into cells, each served by a base station  .
- The base stations are connected to a mobile switching center (MSC), which coordinates the communication between the users and the public switched telephone network (PSTN)  .
- The cellular concept allows frequency reuse, which increases the capacity of the system by using the same frequency band in different cells  .
- The cellular concept also enables handoff, which is the process of transferring a call from one base station to another as the user moves between cells  .
- GSM (Global System for Mobile Communications) is the most widely used wireless



### GPRS for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- GPRS stands for General Packet Radio Service .
- It is a packet oriented wireless data communication service for mobile communications on 2G and 3G cellular communication systems .
- It is non-voice, high speed packet switching technology intended for GSM networks .
- GSM stands for Global System for Mobile Communications, which is a standard for digital cellular networks.
- GPRS enables moderately high-speed data transfers using packet-based technologies .
- Packet-based technologies allow data to be divided into small units called packets, which are transmitted over a shared channel and reassembled at the destination.
- GPRS offers more data transmission options for GSM-based devices, as GSM networks at the time could only use Short Message Service (SMS), for example, to transmit a small amount of data.
- With GPRS technology, mobile devices could support data functions across cellular internet connections, such as web browsing, email, multimedia messaging, location-based services, and online gaming.
- GPRS also enables mobile devices to connect to the internet using the Internet Protocol (IP), which is the standard protocol for data communication over the internet.
- GPRS uses a logical channel called the Packet Data Channel (PDCH), which is dynamically allocated to a mobile device when it requests a data transfer.
- GPRS also uses a network node called the Gateway GPRS Support Node (GGSN), which acts as an interface between the GPRS network and the internet.
- GPRS has several advantages, such as:
  - It allows efficient use of network resources, as multiple users can share the same channel and only pay for the data they transmit or receive .
  - It provides faster data rates than circuit-switched technologies, which require a dedicated channel for each data connection .
  - It supports a wide range of applications and services, such as internet access, email, multimedia, and location-based services .
  - It is compatible with existing GSM networks and devices, as it only requires software upgrades and minor hardware modifications .
- GPRS also has some disadvantages, such as:
  - It has limited coverage and availability, as not all GSM networks and devices support GPRS technology .
  - It has variable data rates and quality of service, as it depends on factors such as network congestion, signal strength, and device capabilities .
  - It has higher security risks than circuit-switched technologies, as data packets can be intercepted, modified, or lost during transmission .
- GPRS has several applications in mobile computing, such as:
  - It enables mobile devices to access the internet and use web-based services, such as online banking, e-commerce, and social media .
  - It allows mobile devices to send and receive multimedia messages, such as images, audio, and video .
  - It supports location-based services, such as navigation, tracking, and emergency response .
  - It facilitates online gaming, as it provides low latency and high bandwidth for multiplayer games .
  - It enables mobile devices to connect to other networks and devices, such as Bluetooth, Wi-Fi, and VPN .



## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs use radio waves or infrared signals to transmit and receive data over the air.
- WLANs have many advantages over wired LANs, such as mobility, flexibility, scalability, and cost-effectiveness.
- WLANs also have some challenges, such as security, interference, and limited bandwidth.

### MAC issues

- MAC (Medium Access Control) is the sublayer of the data link layer that controls how devices access the shared wireless medium.
- MAC issues are the problems or challenges that arise in the MAC sublayer of WLANs, such as collision, hidden terminal, exposed terminal, and fairness.
- Collision is the situation when two or more devices transmit data at the same time, causing interference and data loss.
- Hidden terminal is the situation when two devices that are out of range of each other transmit data to a common receiver, causing collision and data loss.
- Exposed terminal is the situation when a device that is in range of two other devices refrains from transmitting data to one of them, because it hears the transmission of the other one, causing inefficient use of the medium.
- Fairness is the issue of ensuring that all devices have equal or proportional access to the medium, without starving or dominating the others.

### IEEE 802.11

- IEEE 802.11 is the family of standards that define the specifications for WLANs, such as the MAC and PHY (Physical) layers, the frame formats, the security mechanisms, and the network architectures.
- IEEE 802.11 was first published in 1997, and has been revised and amended several times to incorporate new technologies and features, such as higher data rates, wider frequency bands, multiple-input multiple-output (MIMO) antennas, and quality of service (QoS).
- IEEE 802.11 has many variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, each with different characteristics and capabilities.
- IEEE 802.11 also defines different modes of operation, such as infrastructure mode, ad hoc mode, and mesh mode, each with different network topologies and functionalities.

### Bluetooth

- Bluetooth is a wireless technology that enables short-range communication between devices, such as smartphones, laptops, headphones, speakers, keyboards, and mice.
- Bluetooth uses low-power radio waves in the 2.4 GHz frequency band to establish connections and exchange data.
- Bluetooth has many applications, such as wireless audio, wireless input, wireless printing, wireless file transfer, and wireless personal area network (WPAN).
- Bluetooth has several versions, such as Bluetooth 1.0, Bluetooth 2.0, Bluetooth 3.0, Bluetooth 4.0, Bluetooth 5.0, and Bluetooth 6.0, each with different features and performance.
- Bluetooth also has different profiles, such as Advanced Audio Distribution Profile (A2DP), Hands-Free Profile (HFP), Human Interface Device Profile (HID), and Object Push Profile (OPP), each with different functions and services.

### Wireless

- Wireless is a broad term that refers to any type of communication that does not use wires or cables, such as radio, infrared, microwave, satellite, cellular, and optical.
- Wireless has many advantages, such as mobility, convenience, accessibility, and scalability.
- Wireless also has some disadvantages, such as security, reliability, interference, and regulation.
- Wireless has many applications, such as wireless telephony, wireless internet, wireless sensor networks, wireless power transmission, and wireless charging.



# Multiple Access Protocols

- Multiple access protocols are techniques that allow multiple nodes or users to share a common communication channel or medium.
- They are used to coordinate the access to the channel and avoid collisions or interference among the transmissions.
- They are especially important for wireless networking, where the channel is a shared radio spectrum that can be accessed by anyone within the range.
- There are different types of multiple access protocols, depending on the characteristics of the channel and the network.
- Some of the common multiple access protocols that are used in wireless networking are:

  - **Carrier-sense multiple access with collision avoidance (CSMA/CA)**: This protocol is used in IEEE 802.11 / WiFi networks, where nodes sense the channel before transmitting and back off if the channel is busy. They also use a distributed coordination function (DCF) to exchange control frames before sending data frames, to avoid collisions and increase efficiency.   
  - **ALOHA and slotted ALOHA**: These protocols are used in ALOHAnet, the first wireless packet network. Nodes transmit frames whenever they have data to send, without sensing the channel. Collisions may occur and the nodes have to retransmit the frames after a random time. Slotted ALOHA divides the time into slots and nodes transmit only at the beginning of a slot, which reduces the collision probability.   
  - **Code-division multiple access (CDMA)**: This protocol is used in cellular networks, where nodes use different codes to modulate their signals and transmit simultaneously on the same channel. The receiver can recover the signal of a node by using the same code and canceling out the interference from other nodes. CDMA allows multiple users to share the same channel without collisions, but with some degradation in quality.  
  - **Orthogonal frequency-division multiple access (OFDMA)**: This protocol is used in 4G and 5G cellular networks, where nodes transmit on different subcarriers or frequencies that are orthogonal to each other. The channel is divided into multiple subchannels, each with a different frequency, and nodes are assigned a subset of subchannels to transmit. OFDMA allows multiple users to share the same channel without interference, and also improves the spectral efficiency and robustness against fading.  
  - **Orthogonal frequency-division multiplexing (OFDM)**: This protocol is used in IEEE 802.11a/g/n/ac/ax WiFi networks, where nodes transmit on different subcarriers or frequencies that are orthogonal to each other. The channel is divided into multiple subchannels, each with a different frequency, and nodes transmit on one or more subchannels depending on the data rate and channel conditions. OFDM allows multiple users to share the same channel without interference, and also improves the spectral efficiency and robustness against fading.  

- These are some of the multiple access protocols that are used in wireless networking. They have different advantages and disadvantages, and they are suitable for different scenarios and applications.



### TCP over wireless

- Transmission Control Protocol (TCP) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and low throughput.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, variable bandwidth, and frequent handoffs.
- Several mechanisms have been proposed to improve the performance of TCP over wireless networks, such as:
  - Split-connection: The TCP connection is split into two sub-connections at the base station, one over the wired network and one over the wireless network. The base station acts as a proxy and handles the wireless losses locally, without affecting the end-to-end TCP semantics. This mechanism requires modifications at the base station and the mobile host, but not at the end hosts.
  - Link layer retransmission: The link layer protocol provides local error recovery by retransmitting lost or corrupted packets over the wireless link. This mechanism reduces the number of losses seen by TCP and avoids unnecessary congestion control actions. This mechanism requires modifications at the link layer, but not at the TCP layer or the end hosts.
  - TCP-aware link layer: The link layer protocol is aware of the TCP header and can provide selective retransmission or notification of losses to TCP. This mechanism allows TCP to distinguish between congestion losses and wireless losses and adjust its sending rate accordingly. This mechanism requires modifications at both the link layer and the TCP layer, but not at the end hosts.
  - TCP feedback: The base station or the mobile host provides feedback to the TCP sender about the wireless link conditions, such as the available bandwidth, the error rate, or the congestion status. This mechanism allows TCP to adapt its sending rate and window size to the wireless link characteristics and avoid unnecessary timeouts or retransmissions. This mechanism requires modifications at the TCP layer and the end hosts, but not at the link layer.
  - TCP enhancement: The TCP protocol is modified or extended to incorporate new features or algorithms that can improve its performance over wireless networks. For example, TCP can use selective acknowledgments, fast retransmit, fast recovery, or explicit congestion notification to reduce the impact of losses and recover faster. This mechanism requires modifications at the TCP layer and the end hosts, but not at the link layer or the base station.



### Wireless applications

Wireless applications are software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, and wireless internet. Wireless applications enable users to access information, services, and entertainment without being constrained by wires or cables. Some of the benefits of wireless applications are:

- Mobility: Users can access wireless applications from anywhere within the coverage area of the wireless network, and move freely without losing connectivity.
- Convenience: Users do not need to plug in or unplug devices, or deal with tangled wires or cables.
- Cost-effectiveness: Wireless applications can reduce the cost of installation, maintenance, and operation of wired networks, and also save energy and resources.
- Flexibility: Wireless applications can support a variety of devices, platforms, and protocols, and can adapt to changing user needs and preferences.

Some of the challenges of wireless applications are:

- Security: Wireless applications are vulnerable to eavesdropping, interception, modification, and unauthorized access, as wireless signals can be easily detected and captured by malicious parties.
- Reliability: Wireless applications depend on the quality and availability of the wireless network, which can be affected by interference, noise, congestion, and environmental factors.
- Compatibility: Wireless applications may face compatibility issues with different devices, standards, and protocols, and may require interoperability solutions to ensure seamless communication.
- Performance: Wireless applications may experience lower bandwidth, higher latency, and higher error rates than wired applications, and may require optimization techniques to improve the quality of service.

Some of the examples of wireless applications are:

- Wireless internet: Wireless internet enables users to access the web and other online services using wireless devices, such as smartphones, tablets, laptops, and smart TVs. Wireless internet can be provided by cellular networks, Wi-Fi networks, satellite networks, or other wireless technologies.
- Wireless LANs: Wireless LANs (WLANs) are networks that connect computers or other devices using radio transmissions rather than wired connections. WLANs can provide wireless access to a local network or the internet, and can support various applications, such as file sharing, printing, gaming, and video conferencing. WLANs typically use Wi-Fi technology, which is based on the IEEE 802.11 standard.
- Bluetooth: Bluetooth is a wireless technology that enables short-range communication between devices, such as headphones, speakers, keyboards, mice, printers, and cameras. Bluetooth can support various applications, such as wireless audio, wireless input, wireless printing, and wireless data transfer. Bluetooth is based on the IEEE 802.15.1 standard.
- Wireless in mobile computing: Wireless in mobile computing refers to the use of wireless technologies to support mobile devices and applications, such as smartphones, tablets, laptops, and wearable devices. Wireless in mobile computing can enable various applications, such as mobile web browsing, mobile email, mobile social media, mobile gaming, mobile navigation, mobile health, and mobile payment. Wireless in mobile computing can use various wireless technologies, such as cellular networks, Wi-Fi networks, Bluetooth, NFC, RFID, and GPS.



### Data Broadcasting

Data broadcasting is a group communication technique where a sender sends data to multiple receivers simultaneously. This is an all-to-all communication model where each sending device transmits data to all other devices in the network domain .

Data broadcasting can be used for efficient information dissemination in wireless networks, where the sender can be a base station or a mobile device. Data broadcasting can exploit the locality of client demands, such as in a traffic information system, where nearby clients are likely to request similar data.

Some of the advantages of data broadcasting are:

- It can save bandwidth and energy by reducing the number of transmissions required to deliver data to multiple clients.
- It can improve the scalability and reliability of the network by avoiding congestion and collisions.
- It can support asynchronous and anonymous communication, where clients can receive data without sending requests or revealing their identities.

Some of the challenges of data broadcasting are:

- It can cause interference and noise in the wireless channel, which can degrade the quality of service and the data reception rate.
- It can incur high latency and low freshness of data, as clients have to wait for their desired data to be broadcasted by the sender.
- It can require sophisticated scheduling and indexing mechanisms to optimize the data delivery and the client satisfaction.

Some of the techniques to enhance the performance of data broadcasting are:

- Network coding, which combines multiple data packets into a single coded packet that can be decoded by multiple clients with different demands.
- Cooperation, which allows clients to share their received data with other clients who missed the broadcasted data.
- Smart antennas, which can steer the beam of the broadcasted signal to a specific direction or region, reducing interference and increasing coverage.

### Wireless Networking

Wireless networking is a computer network that makes use of radio frequency (RF) connections between nodes in the network. Wireless networks are a popular solution for homes, businesses, and telecommunications networks, as they offer mobility, flexibility, and scalability .

Wireless networks can be classified into different types based on the range, topology, and architecture of the network, such as:

- Wireless personal area network (WPAN), which connects devices within a few meters, such as Bluetooth, ZigBee, and NFC.
- Wireless local area network (WLAN), which connects devices within a few hundred meters, such as Wi-Fi, WiMAX, and HiperLAN.
- Wireless metropolitan area network (WMAN), which connects devices within a few kilometers, such as cellular networks, satellite networks, and wireless mesh networks.
- Wireless wide area network (WWAN), which connects devices across large geographic areas, such as global positioning system (GPS), radio frequency identification (RFID), and low-power wide-area network (LPWAN).

Some of the advantages of wireless networking are:

- It can provide ubiquitous and seamless connectivity to users, regardless of their location and movement.
- It can reduce the cost and complexity of network installation and maintenance, as it does not require cables and wires.
- It can support dynamic and heterogeneous network configurations, as it can adapt to the changing network conditions and user demands.

Some of the challenges of wireless networking are:

- It can suffer from security and privacy issues, as wireless signals can be intercepted, modified, or spoofed by malicious attackers.
- It can face performance and reliability issues, as wireless signals can be affected by environmental factors, such as noise, interference, fading, and multipath.
- It can consume more power and resources, as wireless devices have to perform complex signal processing and encryption operations.

Some of the techniques to improve the security and efficiency of wireless networking are:

- Encryption, which scrambles the data before transmitting it over the wireless channel, making it unreadable to unauthorized parties.
- Authentication, which verifies the identity and legitimacy of the sender and the receiver of the data, preventing impersonation and spoofing attacks.
- Compression, which reduces the size of the data before transmitting it over the wireless channel, saving bandwidth and energy.

### Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth

Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, an office, or a campus. WLANs use radio waves to transmit and receive data over the air, without requiring cables or wires.

WLANs have to deal with some medium access control (MAC) issues, such as:

- How to share the wireless channel among multiple devices, without causing collisions or interference.
- How to coordinate the transmission and reception of data among multiple devices, without



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
- A mobile node registers its care-of address with its home agent when it moves to a new network.
- A home agent intercepts packets destined for the mobile node's home address and tunnels them to the mobile node's care-of address.
- A foreign agent decapsulates the tunneled packets and delivers them to the mobile node.
- A mobile node can also send packets to other nodes using its home address as the source address.
- A mobile node can use either co-located care-of address or foreign agent care-of address.
- A co-located care-of address is an IP address obtained by the mobile node on the visited network, such as through DHCP.
- A foreign agent care-of address is an IP address of the foreign agent that serves as a proxy for the mobile node.
- Mobile IP can support both IPv4 and IPv6, with some differences in the protocol details.
- Mobile IP for IPv4 is described in IETF RFC 5944, and extensions are defined in IETF RFC 4721.
- Mobile IP for IPv6 is described in IETF RFC 6275, and extensions are defined in IETF RFC 5555.



### WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer is of most interest to content developers because it contains among other things, device specifications, scripting languages, and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems. The application layer also includes the Wireless Application Environment (WAE), which provides a framework for developing and delivering wireless applications and services.
  - Session Layer: This layer provides a reliable session service between applications, based on a request-response paradigm. The session layer uses the Wireless Session Protocol (WSP), which is a binary-encoded version of the HTTP protocol, to enable efficient and fast delivery of data over wireless networks.
  - Transaction Layer: This layer provides a transaction service between applications, based on a two-phase commit protocol. The transaction layer uses the Wireless Transaction Protocol (WTP), which is a lightweight protocol that supports reliable and unreliable transactions, as well as user datagram and connection-oriented services.
  - Security Layer: This layer provides data integrity and privacy services between applications, based on encryption and authentication mechanisms. The security layer uses the Wireless Transport Layer Security (WTLS), which is a variant of the TLS protocol, to enable secure communication over wireless networks.
  - Transport Layer: This layer provides a datagram service between applications, based on the adaptation of internet protocols to the characteristics of wireless networks. The transport layer uses the Wireless Datagram Protocol (WDP), which is a general-purpose protocol that can be mapped to different underlying network protocols, such as IP, SMS, or USSD.
- The WAP architecture also includes several components, each serving a specific function. These components include:
  - WAP Client: This is the wireless device that runs the WAP browser and interacts with the WAP gateway. The WAP client supports the WAP protocol stack and the WAE components, such as WML, WMLScript, and WTAI.
  - WAP Gateway: This is the intermediary between the WAP client and the origin server. The WAP gateway performs protocol conversion, data compression, and security functions. The WAP gateway supports the WAP protocol stack and the WAE components, as well as the HTTP protocol and the HTML language.
  - Origin Server: This is the web server that hosts the wireless applications and services. The origin server supports the HTTP protocol and the HTML language, as well as the WAE components, such as WML, WMLScript, and WTAI.



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



### Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, and processing power.
- WAE consists of the following components :
  - Wireless Markup Language (WML): A markup language similar to HTML, but optimized for small screens and low bandwidth. WML defines the structure and content of web pages for wireless devices.
  - Wireless Markup Language Script (WMLScript): A scripting language similar to JavaScript, but with a smaller footprint and fewer features. WMLScript enables dynamic and interactive web pages for wireless devices.
  - Wireless Telephony Application Interface (WTAI): A set of extensions to WML and WMLScript that allow wireless devices to access telephony services, such as making and receiving calls, sending and receiving messages, and accessing phonebook entries.
  - Wireless Datagram Protocol (WDP): A transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS. WDP enables WAE applications to be independent of the underlying network.
  - Wireless Session Protocol (WSP): A session layer protocol that provides reliable and secure communication between wireless devices and web servers. WSP supports features such as connection-oriented and connectionless modes, caching, and content encoding.
  - Wireless Transaction Protocol (WTP): A transaction layer protocol that provides efficient and reliable data exchange between wireless devices and web servers. WTP supports features such as segmentation and reassembly, acknowledgments, and retransmissions.
  - Wireless Application Protocol Binary XML (WBXML): A binary representation of XML documents that reduces the size and complexity of data transmission. WBXML is used to encode WML, WMLScript, and WTAI documents for wireless devices.

- Another example of an application environment for wireless networking is the Wireless LAN Application Protocol (WLAP), which is a proposed extension of WAP for wireless local area networks (WLANs).
- WLAP aims to provide seamless and secure access to internet-based services for WLAN devices, such as laptops, PDAs, and smartphones.
- WLAP consists of the following components:
  - Wireless LAN Markup Language (WLML): A markup language similar to WML, but with additional features and tags for WLAN devices, such as location, authentication, and encryption.
  - Wireless LAN Script (WLScript): A scripting language similar to WMLScript, but with additional functions and objects for WLAN devices, such as network scanning, roaming, and power management.
  - Wireless LAN Telephony Application Interface (WLTAI): A set of extensions to WLML and WLScript that allow WLAN devices to access telephony services over WLAN networks, such as voice over IP (VoIP), video conferencing, and instant messaging.
  - Wireless LAN Datagram Protocol (WLDP): A transport layer protocol that provides a common interface for different WLAN technologies, such as IEEE 802.11, Bluetooth, and HomeRF. WLDP enables WLAP applications to be independent of the underlying network.
  - Wireless LAN Session Protocol (WLSP): A session layer protocol that provides reliable and secure communication between WLAN devices and web servers. WLSP supports features such as connection-oriented and connectionless modes, caching, and content encoding.
  - Wireless LAN Transaction Protocol (WLTP): A transaction layer protocol that provides efficient and reliable data exchange between WLAN devices and web servers. WLTP supports features such as segmentation and reassembly, acknowledgments, and retransmissions.
  - Wireless LAN Application Protocol Binary XML (WLBXML): A binary representation of XML documents that reduces the size and complexity of data transmission. WLBXML is used to encode WLML, WLScript, and WLTAI documents for WLAN devices.

- The following table summarizes the main differences between WAE and WLAP:

| WAE | WLAP |
| --- | --- |
| Designed for wireless wide area networks (WWANs) | Designed for wireless local area networks (WLANs) |
| Supports low bandwidth, high latency, and high error rate networks | Supports high bandwidth, low latency, and low error rate networks |
| Optimized for small and simple wireless devices | Optimized for large and complex WLAN devices |
| Based



### Applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless networking is the use of wireless communication technologies to connect devices and networks without wires or cables.
- Wireless LAN (WLAN) is a type of wireless networking that connects devices within a local area network (LAN) using radio waves or infrared signals.
- WLAN can be classified into two types: infrastructure and ad hoc.
  - Infrastructure WLAN uses a base station or access point (AP) to coordinate the communication among the wireless devices and the wired network.
  - Ad hoc WLAN does not use a base station or AP, but rather allows the wireless devices to communicate directly with each other in a peer-to-peer (P2P) manner.
- MAC (Medium Access Control) is a sublayer of the data link layer that controls how the wireless devices access the shared wireless medium and avoid collisions.
- IEEE 802.11 is a family of standards that define the MAC and physical (PHY) layer specifications for WLANs. It supports various frequency bands, modulation schemes, data rates, and security mechanisms.
- Blue Tooth is a wireless technology that enables short-range communication between devices such as mobile phones, headsets, keyboards, mice, printers, etc. It uses a low-power radio frequency (RF) in the 2.4 GHz band and supports both voice and data transmission.
- Wireless multiple access protocols are the rules that govern how the wireless devices share the wireless medium and avoid interference. Some of the common protocols are:
  - FDMA (Frequency Division Multiple Access): Each device is assigned a different frequency channel to transmit and receive data.
  - TDMA (Time Division Multiple Access): Each device is assigned a different time slot to transmit and receive data in a round-robin fashion.
  - CDMA (Code Division Multiple Access): Each device is assigned a different code to spread its signal over the entire frequency band and distinguish it from other signals using a correlator.
  - CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance): Each device senses the medium before transmitting and defers its transmission if the medium is busy. It also uses a random backoff mechanism to reduce the probability of collision.
- TCP (Transmission Control Protocol) is a reliable transport layer protocol that ensures the delivery of data packets in order and without errors. However, TCP faces some challenges over wireless networks, such as:
  - High bit error rate: Wireless channels are prone to noise, interference, and fading, which can cause packet loss or corruption.
  - Variable delay: Wireless channels have varying propagation delays and queuing delays, which can affect the estimation of round-trip time (RTT) and congestion window size.
  - Mobility: Wireless devices can move across different networks or subnets, which can cause route changes, handoffs, or disconnections.
- Wireless applications are the software programs that run on wireless devices and use wireless networks to provide various services and functions. Some of the common wireless applications are:
  - Data broadcasting: The transmission of data from a source to multiple receivers over a wireless channel. Examples are news, weather, traffic, stock quotes, etc.
  - Mobile IP: A protocol that enables a mobile device to maintain its IP address and connectivity while moving across different networks. It uses a home agent (HA) and a foreign agent (FA) to route the packets to and from the mobile device.
  - WAP (Wireless Application Protocol): A protocol suite that enables the delivery of web content and services to wireless devices. It uses a WAP gateway to translate between the wireless protocols and the Internet protocols. It also uses a WML (Wireless Markup Language) to format the web pages for the wireless devices.



## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to a fixed network via wireless links .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and resolving global names.
  - Security: The data on mobile devices is more vulnerable to theft, loss, or damage than the data on fixed locations. Therefore, encryption, authentication, and backup mechanisms are needed.
  - Data distribution and replication: The uneven and dynamic network topology, the limited bandwidth and battery power, and the high mobility of mobile devices require efficient and adaptive strategies for data distribution and replication.
  - Data caching and hoarding: The data caching and hoarding techniques aim to improve the data availability and reduce the communication cost by storing frequently accessed or anticipated data on mobile devices.
  - Data dissemination and broadcasting: The data dissemination and broadcasting techniques aim to push relevant data to mobile devices based on their profiles, preferences, or subscriptions.
  - Transaction management: The transaction management techniques aim to ensure the consistency and reliability of data updates in the presence of mobility, disconnection, and concurrency.
  - Query processing and optimization: The query processing and optimization techniques aim to execute queries efficiently and effectively on mobile devices and fixed servers, taking into account the network and device constraints.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data on different locations.
- Data replication can improve the data availability, performance, and fault tolerance for mobile computers, but it also introduces challenges such as :
  - Replica placement: The replica placement problem is to decide where and how many replicas of each data item should be stored, considering the network topology, the access patterns, and the resource limitations .
  - Replica consistency: The replica consistency problem is to ensure that all replicas of the same data item have the same value, or at least an acceptable degree of divergence, despite the updates and disconnections .
  - Replica synchronization: The replica synchronization problem is to propagate the updates among the replicas and resolve any conflicts that may arise due to concurrent or delayed updates .
- Data replication can be classified into two types: eager replication and lazy replication .
  - Eager replication: Eager replication is a replication technique that propagates the updates to all replicas as soon as they occur, ensuring strong consistency among the replicas .
  - Lazy replication: Lazy replication is a replication technique that propagates the updates to the replicas only when they reconnect to the network, allowing temporary inconsistency among the replicas .

### Adaptive clustering for mobile

- Adaptive clustering is a technique that organizes mobile devices into groups called clusters, where each cluster has a leader called a clusterhead that coordinates the communication and data management within and among the clusters .
- Adaptive clustering can improve the scalability, efficiency, and robustness of mobile computing systems, but it also faces challenges such as :
  - Cluster formation: The cluster formation problem is to decide how to partition the mobile devices into clusters, considering the network topology, the device characteristics, and the application requirements .
  - Cluster maintenance: The cluster maintenance problem is to adapt the cluster structure to the changes in the network topology, such as the mobility, disconnection, or failure of mobile devices .
  - Clusterhead selection: The clusterhead selection problem is to decide which mobile device should act as the clusterhead for each cluster, considering the device capabilities, the network conditions, and the load balancing .
- Adaptive clustering can be classified into two types: centralized clustering and distributed clustering .
  - Centralized clustering: Centralized clustering is a clustering technique that relies on a central authority, such as a fixed



### Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables. Wireless networks can enable mobile computing, which is the ability to access and process data from anywhere and anytime using portable devices.

Some of the topics related to wireless networks and mobile computing are:

- Data management issues
- Data replication for mobile computers
- Adaptive clustering for mobile wireless networks

#### Data Management Issues

Data management is the process of storing, organizing, and manipulating data in a way that supports efficient and reliable access and processing. Data management issues are the challenges and problems that arise when dealing with data in wireless networks and mobile computing environments.

Some of the data management issues are:

- Data availability: How to ensure that data is accessible to mobile users even when they are disconnected from the network or when the network is unreliable or congested.
- Data consistency: How to maintain the correctness and integrity of data when it is replicated or cached on multiple devices or locations.
- Data security: How to protect data from unauthorized access, modification, or disclosure when it is transmitted over wireless channels or stored on mobile devices.
- Data adaptation: How to adjust data to suit the needs and preferences of mobile users, such as reducing data size, quality, or complexity to save bandwidth, battery, or storage resources.

#### Data Replication for Mobile Computers

Data replication is the process of creating and maintaining multiple copies of data on different devices or locations. Data replication can improve data availability, performance, and fault tolerance for mobile computers, but it also introduces data consistency issues.

Some of the data replication methods for mobile computers are:

- Static data allocation: Data is replicated and assigned to devices or locations before the system starts. This method is simple and efficient, but it does not adapt to changes in user behavior, network conditions, or data updates.
- Dynamic data allocation: Data is replicated and assigned to devices or locations based on the current system state, such as user requests, network load, or data popularity. This method is more flexible and adaptive, but it also requires more communication and computation overhead.
- Hybrid data allocation: Data is replicated and assigned to devices or locations using a combination of static and dynamic methods, such as using static allocation for frequently accessed or critical data and dynamic allocation for less important or variable data.

#### Adaptive Clustering for Mobile Wireless Networks

Adaptive clustering is a technique to organize nodes in a mobile wireless network into groups or clusters, where each cluster has a leader or a clusterhead that coordinates the communication and resource management within the cluster. Adaptive clustering can improve the scalability, efficiency, and robustness of mobile wireless networks, but it also requires a mechanism to handle cluster formation, maintenance, and reconfiguration.

Some of the features and benefits of adaptive clustering are:

- Spatial reuse of bandwidth: By dividing the network into non-overlapping clusters, the same frequency or code can be used by different clusters without interference, thus increasing the network capacity.
- Controlled resource allocation: By assigning different roles and priorities to clusterheads and cluster members, the network can allocate bandwidth, power, or other resources in a fair and efficient way, such as reserving bandwidth for clusterheads or reducing power consumption for cluster members.
- Robustness to topology changes: By using a self-organizing and distributed algorithm, the network can adapt to changes in node location, motion, failure, or insertion/removal, thus maintaining the network connectivity and functionality.



### File system for mobile computing

A file system is a software component that manages the storage and retrieval of data on a persistent device. A file system for mobile computing is a file system that supports the mobility of both users and devices, and adapts to the challenges of wireless and mobile environments, such as:

- Limited bandwidth
- High latency
- Frequent disconnections
- Variable network quality
- Device heterogeneity
- Security and privacy

Some of the design issues and options for a file system for mobile computing are:

- Data management issues: How to organize, access, update, and synchronize data across multiple devices and locations. Some possible solutions are:

  - Location transparency: A file system that provides a uniform namespace and hides the physical location of data from the users and applications. For example, the Andrew File System (AFS)   uses a global namespace that maps logical names to physical locations.
  - Data replication: A file system that maintains multiple copies of data on different servers or devices to improve availability, performance, and fault tolerance. For example, the Coda File System   uses server replication to provide high availability and disconnected operation for mobile clients.
  - Data synchronization: A file system that ensures the consistency and coherence of data across different replicas. For example, the Coda File System   uses optimistic replication and reconciliation to handle conflicts and updates during reconnection.
  - Data caching: A file system that stores frequently accessed or recently modified data on the local device to reduce network traffic and latency. For example, the Coda File System   uses client-side persistent caching to provide high performance and disconnected operation for mobile clients.

- Adaptive clustering for mobile wireless networks: How to group mobile devices into clusters based on their proximity, connectivity, and similarity, and how to manage the cluster formation, maintenance, and dissolution. Some possible benefits are:

  - Reduced network overhead: Clustering can reduce the number of messages and broadcasts in the network, and improve the scalability and efficiency of the network.
  - Enhanced data availability: Clustering can increase the data accessibility and reliability for mobile devices, especially when they are disconnected from the servers or the Internet. For example, a mobile device can access data from its cluster members or a nearby cluster leader.
  - Improved data consistency: Clustering can facilitate the data synchronization and reconciliation among mobile devices, and reduce the conflicts and inconsistencies caused by concurrent updates or disconnections. For example, a cluster leader can act as a mediator or a coordinator for data updates and conflict resolution.



### Disconnected operations

- Disconnected operation is a mode of operation in mobile computing that allows users to execute applications during temporary failures in networks or when they explicitly decide to work off-line .
- Disconnected operation is a key enabling technology for mobile computing, as it enhances the availability and reliability of mobile applications in the face of network limitations such as short range, inability to operate underground and in steel-framed buildings, or line-of-sight constraints .
- Disconnected operation requires mechanisms to handle the following issues  :
  - Data management: how to ensure data consistency and coherence between the mobile device and the server when the connection is restored.
  - Application adaptation: how to modify the application behavior and interface to cope with the reduced functionality and resources in the disconnected mode.
  - Disconnection detection: how to determine when a disconnection occurs, either voluntarily or involuntarily, and how to notify the user and the application.
  - Reconnection: how to resume the normal operation of the application and the data synchronization when the connection is reestablished.

- Disconnected operation can be implemented using different techniques, such as  :
  - Data replication: copying a subset of the data from the server to the mobile device, and vice versa, to allow local access and modification in the disconnected mode. Data replication can be either eager (performed before the disconnection) or lazy (performed after the reconnection).
  - Mobile computation: transferring a part of the application logic from the server to the mobile device, and vice versa, to allow local execution and interaction in the disconnected mode. Mobile computation can be either proactive (performed before the disconnection) or reactive (performed after the reconnection).
  - Application-specific solutions: designing the application to tolerate or exploit the disconnection, such as by using caching, prefetching, hoarding, or logging techniques.

- Disconnected operation poses several challenges and trade-offs, such as  :
  - Data consistency: how to resolve conflicts and inconsistencies that may arise due to concurrent updates on the replicated data by the mobile device and the server.
  - Data coherence: how to ensure that the mobile device and the server have the same view of the data, and that the data is fresh and valid.
  - Data granularity: how to determine the optimal size and scope of the data to be replicated or transferred, considering the storage and bandwidth constraints of the mobile device and the network.
  - Data selection: how to select the most relevant and useful data to be replicated or transferred, considering the user preferences and the application requirements.
  - Data security: how to protect the data from unauthorized access, modification, or loss, both on the mobile device and during the data transmission.
  - Application performance: how to optimize the application response time, throughput, and quality of service, both in the connected and disconnected modes.
  - Application usability: how to provide a user-friendly and consistent interface for the application, both in the connected and disconnected modes.
  - Application portability: how to ensure that the application can run on different platforms and devices, and can adapt to different network conditions and user contexts.



# Unit 4 - Mobile Agents computing, security and fault tolerance, transaction processing in mobile computing

- Mobile agents are software entities that can autonomously migrate from one computer to another in a network and resume their execution on the destination computer   .
- Mobile agents have several advantages, such as reducing network traffic, overcoming network latency, adapting to dynamic environments, and enhancing fault tolerance  .
- Mobile agents also face several challenges, such as security, interoperability, resource management, and coordination  .
- Security issues in mobile agents include protecting the agent from malicious hosts, protecting the host from malicious agents, and protecting the agent from other agents     .
- Fault tolerance issues in mobile agents include ensuring the reliable execution of the agent, recovering from failures, and maintaining consistency of the agent state   .
- Transaction processing in mobile computing refers to the execution of transactions that involve mobile hosts, such as laptops, smartphones, or tablets, that access shared data in a database    .
- Transaction processing in mobile computing faces several challenges, such as network disconnection, data replication, concurrency control, and commit protocols    .
- Transaction processing in mobile computing requires novel models and techniques, such as open-nesting, semantic properties, compacts, and reporting transactions, to ensure the correctness, efficiency, and adaptability of the transactions    .



### Environment for Mobile Agents

- A mobile agent is a software entity that can migrate from one node to another in a network, carrying its code and state, and executing autonomously .
- A mobile agent environment is the software infrastructure that supports the creation, migration, communication, and execution of mobile agents .
- A mobile agent environment typically consists of the following components :
  - An agent platform: the computational environment in which an agent operates. It provides the basic services and resources for agent creation, migration, communication, and security. The platform where an agent originates is referred to as the home platform, and normally is the most trusted environment for an agent.
  - An agent transport service: the mechanism that enables an agent to move from one platform to another. It is responsible for transferring the agent's code and state, and ensuring the integrity and authenticity of the agent during transit .
  - An agent communication service: the mechanism that enables an agent to communicate with other agents, users, and systems. It is based on a communication language and protocol that define the syntax and semantics of agent messages .
  - An agent security service: the mechanism that protects the agent and the platform from malicious attacks. It includes authentication, authorization, encryption, integrity, confidentiality, and non-repudiation techniques .
- A mobile agent environment can be classified into two types based on the degree of heterogeneity of the platforms :
  - A homogeneous environment: where all the platforms share the same operating system, hardware, and agent system. This type of environment simplifies the agent migration and execution, but limits the portability and interoperability of the agents .
  - A heterogeneous environment: where the platforms may have different operating systems, hardware, and agent systems. This type of environment requires the use of a common agent language or a translation mechanism to enable the agent migration and execution across different platforms. It enhances the portability and interoperability of the agents, but increases the complexity and overhead of the agent system .



## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over a shared wireless channel.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved by using GPS, signal strength, angle of arrival, time of arrival, or other techniques.
- MAC issues refer to the challenges of designing a medium access control (MAC) protocol for ad hoc networks, such as channel access, collision avoidance, fairness, power control, and scalability. MAC protocols can be classified into contention-based, reservation-based, or hybrid schemes.
- Routing protocols are the rules that govern how packets are forwarded from a source node to a destination node in an ad hoc network. Routing protocols can be categorized into proactive, reactive, or hybrid approaches, depending on whether they maintain routing tables, discover routes on demand, or combine both strategies.
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks that uses link state information to compute shortest paths. Each node periodically broadcasts its link state to the entire network, and maintains a complete topology map. GSR reduces the overhead of link state flooding by using a hierarchical structure and a location-aided scheme.



### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing protocol for ad hoc mobile networks based on the Bellman–Ford algorithm.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- The sequence number is used to distinguish stale route information from the new and thus prevent the formation of routing loops.
- Each node maintains a routing table that contains the following information for each destination: the next hop, the number of hops, the sequence number, and the installation time.
- Each node periodically broadcasts its routing table to its neighbors, and updates its own table based on the received information.
- If a node detects a link break, it increments the sequence number of the destination and advertises the metric as infinity.
- DSDV provides only one route for a source/destination pair and does not support multipath routing.
- DSDV reduces the control overhead by using two types of updates: full dump and incremental.
- A full dump update contains all the routing information and is sent less frequently.
- An incremental update contains only the changed information and is sent more frequently.
- DSDV is suitable for small and low-mobility networks, but suffers from frequent updates and large routing tables in large and high-mobility networks.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on dynamic source routing (DSR) for the unit 5 of mobile computing.

### Dynamic source routing (DSR)

- Dynamic source routing (DSR) is a routing protocol for wireless mesh networks. It is similar to AODV in that it forms a route on-demand when a transmitting node requests one. However, it uses source routing instead of relying on the routing table at each intermediate device .
- Source routing means that the sender of a packet determines the complete sequence of nodes through which the packet has to pass. The sender explicitly lists this route in the packet's header, identifying each forwarding hop by the address of the next node to which to transmit the packet on its way to the destination host.
- DSR consists of two main mechanisms: route discovery and route maintenance. Route discovery is the process by which a node S wishing to send a packet to a destination node D obtains a source route to D. Route maintenance is the process of detecting and repairing route errors.
- Route discovery works as follows:
  - S initiates route discovery by broadcasting a route request (RREQ) packet to its neighbors. The RREQ contains the address of S, the address of D, and a unique identification number.
  - Each node receiving the RREQ appends its own address to the route record in the RREQ and forwards the packet to its neighbors, unless it is the destination or it has a route to D in its route cache.
  - If the node has a route to D in its route cache, it returns a route reply (RREP) packet to S, containing the copy of the route record from the RREQ along with the route from its cache.
  - If the node is the destination D, it returns a RREP to S, containing the route record from the RREQ, which is the complete source route from S to D.
  - S can receive multiple RREPs from different nodes and can choose the best route based on some criteria, such as the shortest route or the most reliable route.
  - S caches the routes learned from the RREPs for future use.
- Route maintenance works as follows:
  - When a node encounters a transmission error at its data link layer along a source route, it removes the link from its cache and generates a route error (RERR) packet, which contains the addresses of the two ends of the failed link.
  - The RERR is sent back to the source S, which then removes the failed link from its cache and initiates a new route discovery if necessary.
  - Alternatively, S can use another route from its cache or try to salvage the packet by finding a route to the next hop in the source route.
- DSR has some advantages and disadvantages :
  - Advantages:
    - It eliminates the need for periodic route advertisements and neighbor detection packets, which reduces the network overhead and saves bandwidth.
    - It allows multiple routes to be learned and cached, which increases the route availability and robustness.
    - It supports unidirectional links and asymmetric routes, which are common in wireless networks.
    - It adapts quickly to the topology changes and node mobility, as the routes are maintained only when needed.
  - Disadvantages:
    - It incurs high latency and overhead during route discovery, especially for large networks or high traffic loads.
    - It consumes more bandwidth and energy due to the source routing overhead, which increases with the route length and the number of intermediate nodes.
    - It suffers from the stale route problem, as the cached routes may become invalid due to the topology changes or node failures.
    - It is vulnerable to malicious nodes that can alter, drop, or misroute the packets.



### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- Ad hoc networks are networks that do not have a fixed infrastructure or centralized administration, and consist of nodes that communicate with each other over wireless links .
- AODV establishes routes to destinations on demand, meaning that it only initiates a route discovery process when a node needs to send data to a destination that it does not have a route to  .
- AODV supports both unicast and multicast routing, meaning that it can send data to a single destination or to a group of destinations .
- AODV offers quick adaptation to dynamic link conditions, low processing and memory overhead, and low network utilization  .
- AODV operates as follows   :
  - Each node maintains a routing table that contains information about the next hop and the number of hops to reach each destination.
  - Each node also maintains a sequence number that is incremented whenever the node detects a change in the network topology or initiates a route discovery.
  - When a node needs to send data to a destination that it does not have a route to, it broadcasts a route request (RREQ) message to its neighbors, containing the destination address, the destination sequence number, the source address, the source sequence number, and a hop count.
  - Each node that receives the RREQ message checks its routing table to see if it has a fresh route to the destination, meaning that the destination sequence number in the routing table is equal or greater than the one in the RREQ message. If so, it sends a route reply (RREP) message back to the source, containing the destination address, the destination sequence number, the source address, the hop count, and the lifetime of the route. If not, it rebroadcasts the RREQ message to its neighbors, after incrementing the hop count and updating the source sequence number if necessary.
  - The RREP message is forwarded back to the source along the reverse path of the RREQ message, and each intermediate node updates its routing table with the new route information.
  - The source node can start sending data to the destination once it receives the RREP message, and it also sets a timer for the route lifetime. If the timer expires, the route is considered invalid and a new route discovery is initiated if needed.
  - When a node detects a link break to a next hop, it sends a route error (RERR) message to its upstream neighbors, containing the list of destinations that are unreachable via that link. The upstream neighbors then update their routing tables and propagate the RERR message further if necessary.
  - A node can also send a gratuitous RREP message to its downstream neighbors if it learns a better route to a destination, meaning that the route has a smaller hop count or a larger destination sequence number. The downstream neighbors then update their routing tables and forward the gratuitous RREP message further if necessary.



### Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated on-demand routing protocol that was proposed by Park and Corson in 1997  for wireless mobile ad hoc networks.
- TORA is based on the concept of link reversal, which is a technique to dynamically change the direction of links in a network graph to eliminate routing loops and maintain routes to destinations.
- TORA consists of three main phases: route creation, route maintenance, and route erasure.
- Route creation: When a source node wants to send data to a destination node, it broadcasts a query packet containing the destination ID. The query packet propagates through the network until it reaches the destination or a node that has a route to the destination. The nodes that receive the query packet assign a height value to themselves based on the height of the sender and the direction of the link. The height value is used to create a directed acyclic graph (DAG) rooted at the destination. The nodes that have a downward link to the destination reply with an update packet containing their height value. The update packet travels back to the source along the DAG, establishing routes to the destination.
- Route maintenance: When a link failure occurs, the nodes adjacent to the link increase their height value to a value higher than their neighbors. This causes the links to be reversed and the DAG to be restructured. The nodes that lose all their downstream links broadcast a clear packet to erase invalid routes. The clear packet also triggers a new route creation process if necessary.
- Route erasure: When a source node no longer needs a route to a destination, it broadcasts a clear packet to erase the routes. The clear packet contains the destination ID and a special height value that indicates the erasure. The nodes that receive the clear packet reset their height value and delete the routing entries for the destination.

- TORA is an efficient, adaptive, and scalable routing protocol that can handle network dynamics and mobility. However, it also has some drawbacks, such as:
  - It may generate a large number of control packets during route creation and maintenance, which consumes bandwidth and energy.
  - It may create multiple routes to the same destination, which increases the routing overhead and the probability of routing loops.
  - It does not consider the quality of service (QoS) parameters, such as delay, bandwidth, and reliability, in route selection, which may affect the performance of data transmission.



### QoS in Ad Hoc Networks

- Quality of service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc. 
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or centralized control. 
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes and applications.  
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.  
- QoS in ad hoc networks can be classified into two categories: hard QoS and soft QoS. Hard QoS guarantees the QoS requirements of the applications with strict bounds, while soft QoS provides the best-effort QoS with statistical guarantees.  
- QoS in ad hoc networks can be supported by various mechanisms, such as QoS-aware routing protocols, QoS-aware MAC protocols, QoS-aware scheduling algorithms, QoS-aware admission control, QoS-aware resource reservation, QoS-aware cross-layer optimization, etc.   
- QoS in ad hoc networks can be evaluated by various metrics, such as throughput, delay, jitter, packet loss, packet delivery ratio, energy consumption, etc.   
- QoS in ad hoc networks can be improved by various techniques, such as adaptive QoS, cooperative QoS, multipath QoS, multicast QoS, security QoS, etc.



### Applications for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of mobile nodes that communicate with each other using wireless links. Ad hoc networks have many applications in various domains, such as military, disaster relief, vehicular, sensor, and personal area networks .
- Localization is the process of determining the position of a node in an ad hoc network, based on the information from other nodes or external sources. Localization is essential for many applications that require location-awareness, such as navigation, tracking, routing, and geographic services.
- MAC issues refer to the challenges and design considerations of medium access control protocols for ad hoc networks. MAC protocols are responsible for coordinating the access of multiple nodes to the shared wireless channel, avoiding collisions, and maximizing the channel utilization. MAC issues include how to handle hidden and exposed terminals, how to adapt to dynamic topology and traffic, how to reduce overhead and latency, and how to save energy .
- Routing protocols are the algorithms that enable the nodes in an ad hoc network to discover and maintain routes to other nodes. Routing protocols can be classified into proactive, reactive, and hybrid, depending on whether they maintain routes periodically, on-demand, or both. Routing protocols face many challenges in ad hoc networks, such as scalability, mobility, bandwidth constraints, and security .
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks, based on the link-state algorithm. In GSR, each node maintains a complete view of the network topology and the link states, and periodically exchanges this information with its neighbors. GSR can find the shortest path between any pair of nodes, but it suffers from high overhead and slow convergence .

