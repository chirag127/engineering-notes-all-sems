

# Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks.
- Mobile computing enables users to communicate, access information, and perform tasks anytime and anywhere, without being constrained by physical location or wired connections.
- Mobile computing involves the interaction of mobile devices, wireless networks, and cloud services.
- Some of the issues and challenges in mobile computing are:
  - Limited battery life and processing power of mobile devices.
  - Heterogeneous and dynamic wireless network conditions, such as bandwidth, latency, and coverage.
  - Security and privacy risks due to wireless transmission and data storage on cloud servers.
  - User interface design and usability for small screens and touch inputs.
  - Application development and testing for multiple platforms and devices.
- Wireless telephony is the transmission of voice and data over radio waves, without using wires or cables.
- Wireless telephony enables users to make and receive phone calls, send and receive text messages, and access the internet using mobile phones or other wireless devices.
- Wireless telephony is based on the cellular concept, which divides a geographical area into smaller regions called cells, each served by a base station that communicates with mobile devices within its range.
- The base stations are connected to a central switching system that routes the calls and data between different cells and networks.
- The cellular concept allows for efficient use of the radio spectrum, as different cells can use the same frequency channels without interfering with each other, as long as they are sufficiently separated.
- GSM (Global System for Mobile Communication) is a standard developed by the European Telecommunications Standards Institute (ETSI) to describe the protocols for second-generation digital cellular networks used by mobile devices such as mobile phones and tablets.
- GSM is an open and digital cellular technology that uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to transmit voice and data over radio channels.
- GSM uses four different frequency bands of 850 MHz, 900 MHz, 1800 MHz and 1900 MHz, depending on the region and the operator.
- GSM provides services such as voice calls, text messages, data transmission, roaming, encryption, and authentication.
- GSM is widely used by mobile phone users in Europe and other parts of the world, and is compatible with other standards such as GPRS, EDGE, UMTS, and LTE.



### Air-interface for Mobile Computing

- The air interface is the communication link between the two stations in mobile or wireless communication.
- The air interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection.
- The air interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network.
- Different air interface technologies are used for different cellular standards, such as TDMA and CDMA for GSM, OFDMA for LTE, etc .
- The air interface is also called the UM interface in GSM, as it is analogous to the U interface of ISDN.
- The air interface is one of the key components for achieving the performance and quality of service requirements for mobile computing applications.
- The air interface is also subject to various challenges and issues, such as interference, fading, multipath, mobility, security, etc.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Mobile Computing. Here is the content for the topic of channel structure for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

### Channel Structure

- A channel is a medium or a path that carries information from one point to another in a communication system.
- In mobile computing, channels are used to transmit and receive data between mobile devices and base stations or between base stations and network controllers.
- Channels can be classified into two types: physical channels and logical channels.

#### Physical Channels

- Physical channels are the basic units of transmission in a mobile network.
- They are defined by the frequency, time slot, and code used for modulation and demodulation of the signal.
- Physical channels can be further divided into two types: frequency division multiple access (FDMA) channels and time division multiple access (TDMA) channels.

##### FDMA Channels

- FDMA channels are the channels that use different frequencies to transmit and receive data simultaneously.
- Each channel occupies a certain bandwidth of the spectrum and is separated from other channels by a guard band to avoid interference.
- FDMA channels are used in the first generation (1G) of mobile networks, such as analog cellular systems.

##### TDMA Channels

- TDMA channels are the channels that use the same frequency but different time slots to transmit and receive data sequentially.
- Each channel is divided into a number of time slots, each of which can carry a burst of data from one user or device.
- TDMA channels are used in the second generation (2G) of mobile networks, such as digital cellular systems.

#### Logical Channels

- Logical channels are the channels that carry specific types of information within the physical channels.
- They are defined by the function, format, and protocol of the data transmitted and received.
- Logical channels can be further divided into two types: traffic channels and control channels.

##### Traffic Channels

- Traffic channels are the logical channels that carry user data, such as voice, text, or multimedia.
- They are also called bearer channels or service channels.
- Traffic channels can be either full-rate or half-rate, depending on the data rate and quality required.

##### Control Channels

- Control channels are the logical channels that carry signaling and management information, such as call setup, authentication, location update, or power control.
- They are also called signaling channels or management channels.
- Control channels can be either common or dedicated, depending on the scope and direction of the information.

#### Channel Structure in GSM

- GSM is a 2G mobile network standard that uses TDMA and FDMA to provide voice and data services.
- GSM uses a variety of logical channels within the physical channels to carry traffic and control information.
- The logical channels in GSM can be classified into three types: traffic channels (TCHs), control channels (CCHs), and the cell broadcast channel (CBCH).

##### Traffic Channels (TCHs)

- TCHs are the logical channels that carry user data, such as voice or text, in GSM.
- TCHs can be either full-rate (TCH/F) or half-rate (TCH/H), depending on the data rate and quality required.
- TCHs use one or two time slots in each physical channel, depending on the type of TCH.

##### Control Channels (CCHs)

- CCHs are the logical channels that carry signaling and management information in GSM.
- CCHs can be either common or dedicated, depending on the scope and direction of the information.
- CCHs use one or more time slots in each physical channel, depending on the type of CCH.

###### Common Control Channels (CCCHs)

- CCCHs are the CCHs that carry information that is common to all mobile devices in a cell or a group of cells.
- CCCHs are used for call setup, paging, access request, and access grant.
- CCCHs include the following types:

  - Broadcast Control Channel (BCCH): It carries information about the cell identity, frequency, and configuration.
  - Paging Channel (PCH): It carries information about the mobile devices that are being paged for incoming calls or messages.
  - Random Access Channel (RACH): It carries information about the mobile devices that are requesting access to the network or a specific channel.
  - Access Grant Channel (AGCH): It carries information about the channel assignment and timing advance for the mobile devices that are granted access.

###### Dedicated Control Channels (DCCHs)

- DCCHs



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of location management: HLR-VLR, hierarchical, handoffs for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing.

```markdown
### Location Management
- Location management is the process of tracking and updating the location of mobile users in a wireless cellular network.
- Location management enables the network to deliver calls and messages to the mobile users, and to support mobility and roaming across different service areas.
- Location management consists of two main functions: location update and location lookup.
- Location update is the process of informing the network about the current location of the mobile user, usually when the user moves across a predefined boundary called a registration area (RA).
- Location lookup is the process of finding the current location of the mobile user, usually when the network needs to deliver a call or a message to the user.
- Location management involves the use of databases that store the location information of the mobile users, such as the Home Location Register (HLR) and the Visitor Location Register (VLR).
- The HLR is a centralized database that contains the permanent records of all the mobile users in the network, including their service profiles and their current RAs.
- The VLR is a local database that contains the temporary records of the mobile users who are currently visiting a specific RA, including their service profiles and their current base stations (cells).
- The HLR and the VLR communicate with each other to exchange the location information of the mobile users, and to update the records when the users change their locations.
- The HLR-VLR scheme is a hierarchical location management scheme that reduces the signaling overhead and the database size compared to a flat scheme that uses only one database for the whole network.
- The HLR-VLR scheme also supports roaming across different networks, as the HLR can forward the location information of the mobile user to the VLR of the visited network.

### Handoffs
- Handoff is the process of transferring the ongoing call or data session of a mobile user from one base station to another, without interrupting the service or degrading the quality.
- Handoff is necessary to maintain the continuity of the service and to avoid dropping the call or the session when the mobile user moves out of the coverage area of the current base station.
- Handoff involves the coordination of the mobile user, the current base station, the target base station, and the network controller, which is responsible for managing the radio resources and the handoff decisions.
- Handoff can be classified into different types based on the direction of the handoff initiation, the involvement of the mobile user, the number of channels used, and the type of the network.
- The direction of the handoff initiation can be either network-controlled, mobile-assisted, or mobile-controlled, depending on whether the network, the mobile user, or both initiate the handoff process.
- The involvement of the mobile user can be either hard or soft, depending on whether the mobile user switches from the current channel to the target channel abruptly or smoothly.
- The number of channels used can be either single or multiple, depending on whether the mobile user uses only one channel or more than one channel during the handoff process.
- The type of the network can be either homogeneous or heterogeneous, depending on whether the current and the target base stations belong to the same or different network technologies.
- Handoff can improve the network performance and the user experience by optimizing the radio resource utilization, balancing the traffic load, enhancing the service quality, and supporting the network interoperability.
```



### Channel allocation in cellular systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- Channels are the basic units of communication resources that can carry signals between a base station and a mobile terminal.
- Channels can be divided into two types: frequency channels and time slots.
- Frequency channels are the sub-bands of the radio spectrum that are assigned to a cell.
- Time slots are the intervals of time that are assigned to a user within a frequency channel.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots and bandwidth, while minimizing interference and blocking probability .
- Blocking probability is the probability that a call request is rejected due to lack of available channels.
- Interference is the unwanted signal that degrades the quality of the desired signal.
- Channel allocation strategies can be classified into three categories: fixed, dynamic and hybrid .
- Fixed channel allocation (FCA) assigns a fixed number of channels to each cell, regardless of the traffic load .
- FCA is simple to implement, but it may result in inefficient utilization of channels and high blocking probability in some cells .
- Dynamic channel allocation (DCA) assigns channels to cells on demand, based on the traffic load and the interference level .
- DCA is more flexible and adaptive, but it requires more complex coordination and signaling among cells .
- Hybrid channel allocation (HCA) combines FCA and DCA, by dividing the channels into two sets: fixed and dynamic .
- HCA assigns the fixed channels to each cell permanently, and the dynamic channels to each cell temporarily, based on the traffic load and the interference level .
- HCA is a compromise between FCA and DCA, balancing the simplicity and the efficiency of channel allocation .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on CDMA for the Unit 1 of Mobile Computing.

### CDMA

- CDMA stands for Code Division Multiple Access and is a spread spectrum multiple access technique  .
- Spread spectrum technique spreads the bandwidth of data in a uniform manner for the same transmitted power.
- CDMA allows multiple users to share the same frequency channel by assigning each user a unique code that modulates their signal  .
- CDMA is the base on which access methods such as cdmaOne, CDMA2000, and WCDMA are built .
- CDMA has several advantages over other multiple access techniques, such as:
  - Higher spectral efficiency, as more users can be accommodated in the same bandwidth  .
  - Better security, as the user's signal is encrypted by the code and can only be decoded by the intended receiver  .
  - Lower interference, as the code reduces the effect of noise and other users' signals  .
  - Soft handoff, as the user can communicate with multiple base stations simultaneously during a call transition  .
- CDMA has some disadvantages, such as:
  - Higher complexity, as the code generation and synchronization require more processing power and hardware  .
  - Near-far problem, as the user's signal can be drowned out by a stronger signal from a nearby user if the power control is not adequate  .
  - Cell breathing, as the cell coverage area varies depending on the number of users and their power levels  .




Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of GPRS for the subject of Mobile Computing.

### GPRS

- GPRS stands for General Packet Radio Service .
- It is a packet oriented wireless data communication service for mobile communications on 2G and 3G cellular networks .
- It is non-voice, high speed packet switching technology intended for GSM networks .
- It enables moderately high-speed data transfers using packet-based technologies .
- It offers more data transmission options for GSM-based devices, as GSM networks at the time could only use Short Message Service (SMS), for example, to transmit a small amount of data .
- It supports data functions across cellular internet connections.

### Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM

- Mobile computing is the ability to use computing devices and applications that are not bound by physical location or network connection.
- Mobile computing involves mobile communication, mobile hardware, and mobile software.
- Some of the issues in mobile computing are:
  - Limited battery life and power consumption.
  - Wireless network coverage and quality.
  - Security and privacy of data and communication.
  - Device compatibility and interoperability.
  - User interface design and usability.
- Wireless telephony is the transmission of voice and data over radio waves without using wires.
- Wireless telephony can be divided into two categories: cellular and cordless.
- Cellular telephony is the use of cellular networks that divide a large geographical area into smaller cells, each served by a base station.
- GSM stands for Global System for Mobile Communications.
- GSM is a standard for digital cellular telephony that uses time division multiple access (TDMA) to allocate radio channels to multiple users.
- GSM supports voice, data, and multimedia services.
- GSM operates in the 900 MHz and 1800 MHz bands in Europe and Asia, and in the 850 MHz and 1900 MHz bands in North America and South America.



# Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

## Wireless Networking
- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless networking can provide mobility, flexibility, scalability, and cost-effectiveness for various applications and scenarios.
- Wireless networking can be classified into different types based on the coverage area, such as wireless personal area networks (WPANs), wireless local area networks (WLANs), wireless metropolitan area networks (WMANs), and wireless wide area networks (WWANs).

## Wireless LAN Overview
- A wireless LAN (WLAN) is a type of wireless networking that connects devices within a limited area, such as a home, office, campus, or hotspot.
- A WLAN typically uses radio waves or infrared signals to transmit and receive data over the air.
- A WLAN consists of wireless stations (such as laptops, smartphones, tablets, etc.) and wireless access points (APs) that provide wireless connectivity to a wired network or the Internet.
- A WLAN can operate in two modes: infrastructure mode and ad hoc mode. In infrastructure mode, the wireless stations communicate through the APs, which act as bridges between the wireless and wired networks. In ad hoc mode, the wireless stations communicate directly with each other without using any APs.

## MAC Issues
- The medium access control (MAC) layer is responsible for coordinating the access of multiple wireless stations to the shared wireless medium.
- The MAC layer faces several challenges and issues in wireless networking, such as:
  - Hidden terminal problem: when two wireless stations are within the range of an AP but not within the range of each other, they may not sense each other's transmissions and cause collisions.
  - Exposed terminal problem: when a wireless station is within the range of two APs but not within the range of the intended receiver, it may unnecessarily defer its transmission to avoid collisions with the other AP.
  - Fading and interference: the wireless signals may vary in strength and quality due to obstacles, reflections, multipath, noise, etc., which may affect the reliability and performance of the wireless communication.
  - Mobility and power management: the wireless stations may move across different APs or switch between different power states, which may require the MAC layer to handle the handoff and sleep/wake-up procedures.

## IEEE 802.11
- IEEE 802.11 is the most widely used standard for WLANs, developed by the IEEE 802.11 working group.
- IEEE 802.11 defines the MAC and physical (PHY) layer specifications for WLANs, as well as several amendments and extensions to enhance the functionality and performance of WLANs.
- IEEE 802.11 supports various frequency bands, modulation schemes, data rates, and channel widths, such as:
  - 2.4 GHz band: used by 802.11b, 802.11g, and 802.11n, with data rates up to 11 Mbps, 54 Mbps, and 600 Mbps, respectively, and channel widths of 20 MHz or 40 MHz.
  - 5 GHz band: used by 802.11a, 802.11n, 802.11ac, and 802.11ax, with data rates up to 54 Mbps, 600 Mbps, 6.9 Gbps, and 9.6 Gbps, respectively, and channel widths of 20 MHz, 40 MHz, 80 MHz, 160 MHz, or 320 MHz.
  - 6 GHz band: used by 802.11ax and 802.11be, with data rates up to 9.6 Gbps and 46 Gbps, respectively, and channel widths of 20 MHz, 40 MHz, 80 MHz, 160 MHz, or 320 MHz.
- IEEE 802.11 uses the Ethernet protocol and CSMA/CA (carrier sense multiple access with collision avoidance) as the basic MAC scheme, which requires the wireless stations to sense the medium before transmitting and to wait for an acknowledgment from the receiver after transmitting.
- IEEE 802.11 also supports various MAC enhancements and features, such as:
  - RTS/CTS (request to send/clear to send): a mechanism to solve the hidden terminal problem by exchanging control frames before data frames.
  - NAV (network allocation vector): a mechanism to inform the wireless stations about the duration of the ongoing transmissions and to reserve the medium for future transmissions.
  - DCF (distributed coordination function): a contention-based MAC scheme that uses CSMA/CA and binary



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on multiple access protocols for wireless networking.

### Multiple access protocols for wireless networking

- Multiple access protocols are used to coordinate the access of multiple nodes or users to a shared network channel, such as a wireless LAN or a satellite network.
- Multiple access protocols can be classified into two categories: random access and controlled access.
- Random access protocols allow nodes to transmit data whenever they have data to send, without any coordination with other nodes. However, this may result in collisions, where two or more nodes transmit data at the same time and interfere with each other. Examples of random access protocols are ALOHA, CSMA, CSMA/CA and CSMA/CD.
- Controlled access protocols require nodes to obtain permission or reservation before transmitting data, thus avoiding collisions. However, this may introduce delay and overhead in the network. Examples of controlled access protocols are TDMA, FDMA, CDMA and OFDMA.
- Some common multiple access protocols that are used in wireless networking are:

  - Carrier-sense multiple access with collision avoidance (CSMA/CA), used in IEEE 802.11 / WiFi, which is a random access protocol that uses a distributed coordination function to sense the channel before transmitting and to back off in case of collision.
  - Time division multiple access (TDMA), used in GSM and LTE, which is a controlled access protocol that divides the channel into time slots and assigns each slot to a different node or user.
  - Frequency division multiple access (FDMA), used in AMPS and NMT, which is a controlled access protocol that divides the channel into frequency bands and assigns each band to a different node or user.
  - Code division multiple access (CDMA), used in IS-95 and CDMA2000, which is a controlled access protocol that assigns a unique code to each node or user and allows them to transmit data simultaneously using the same channel, but with different codes.
  - Orthogonal frequency division multiple access (OFDMA), used in WiMAX and LTE, which is a controlled access protocol that combines FDMA and TDMA by dividing the channel into subcarriers and time slots, and assigning each subcarrier and slot to a different node or user.
  - Bluetooth, which is a wireless technology that uses a frequency hopping spread spectrum (FHSS) technique to avoid interference and to allow multiple devices to communicate in a short range network.



# TCP over wireless

- TCP (Transmission Control Protocol) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and underutilization of the wireless bandwidth.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, variable bandwidth, and frequent handoffs.
- Several mechanisms have been proposed to improve the performance of TCP over wireless networks, which can be classified into four categories   :

  - **End-to-end solutions**: These solutions modify the TCP sender or receiver to make them aware of the wireless link conditions and adjust their behavior accordingly. For example, TCP Westwood estimates the available bandwidth based on the rate of acknowledgments and adapts the congestion window accordingly. TCP Snoop caches packets at the base station and retransmits them locally in case of wireless losses, without notifying the TCP sender.
  - **Link layer solutions**: These solutions use link layer protocols to provide reliable data transmission over the wireless link and hide the wireless losses from the TCP layer. For example, Automatic Repeat reQuest (ARQ) protocols use acknowledgments and timeouts to detect and recover from errors. Forward Error Correction (FEC) protocols add redundant bits to the packets to correct errors without retransmission.
  - **Split-connection solutions**: These solutions split the TCP connection into two sub-connections: one between the TCP sender and the base station, and another between the base station and the TCP receiver. The base station acts as a proxy that handles the wireless losses and congestion control for the sub-connection with the TCP receiver. For example, I-TCP uses a TCP connection over the wired network and a non-TCP connection over the wireless network.
  - **Cross-layer solutions**: These solutions exploit the interactions and information exchange between different layers of the network stack to optimize the performance of TCP over wireless networks. For example, TCP-Friendly Rate Control (TFRC) uses feedback from the MAC layer to estimate the wireless link quality and adjust the sending rate accordingly.

: https://en.wikipedia.org/wiki/TCP_Westwood
: https://en.wikipedia.org/wiki/TCP_Snoop
: https://en.wikipedia.org/wiki/Indirect_TCP
: https://en.wikipedia.org/wiki/TCP-friendly_rate_control



### Wireless applications

Wireless applications are software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, and wireless internet. Wireless applications enable users to access information, services, and entertainment without being constrained by wires or cables. Some of the benefits of wireless applications are:

- Mobility: Users can access wireless applications from anywhere within the coverage area of the wireless network, and move freely without losing connectivity.
- Convenience: Users do not need to plug in or unplug devices, or deal with tangled wires or cables.
- Cost-effectiveness: Wireless applications can reduce the cost of installation, maintenance, and operation of wired networks, and also save energy and resources.
- Flexibility: Wireless applications can support a variety of devices, platforms, and protocols, and can adapt to changing user needs and preferences.

Some of the challenges of wireless applications are:

- Security: Wireless applications are vulnerable to eavesdropping, interception, spoofing, and denial-of-service attacks, and need to implement encryption, authentication, and authorization mechanisms to protect data and privacy.
- Reliability: Wireless applications are subject to interference, noise, fading, and congestion, and need to implement error detection, correction, and recovery mechanisms to ensure data integrity and availability.
- Scalability: Wireless applications need to support a large number of users, devices, and services, and need to implement efficient resource allocation, load balancing, and quality of service mechanisms to ensure performance and user satisfaction.
- Compatibility: Wireless applications need to interoperate with different wireless standards, protocols, and technologies, and need to implement cross-layer optimization, adaptation, and coordination mechanisms to ensure functionality and efficiency.

Some of the examples of wireless applications are:

- Cellular phones: Wireless applications on cellular phones provide connectivity for portable and mobile applications, both personal and business, such as voice calls, text messages, emails, web browsing, social media, navigation, music, video, games, and more.
- Wireless LANs: Wireless applications on wireless LANs enable users to access a network without requiring a wired connection, such as wireless routers, access points, laptops, tablets, printers, smart TVs, and more .
- Bluetooth: Wireless applications on Bluetooth enable users to exchange data over short distances, such as wireless headphones, speakers, keyboards, mice, smart watches, fitness trackers, and more.
- Wireless internet: Wireless applications on wireless internet enable users to access the internet over wireless networks, such as Wi-Fi, WiMAX, LTE, 5G, and more .



# Data Broadcasting for Wireless Networking

- Data broadcasting is a group communication, where a sender sends data to receivers simultaneously .
- Data broadcasting can be characterized by locality of client demands, such as traffic information, weather updates, or news headlines.
- Data broadcasting can be efficient and scalable for information dissemination in wireless networks, as it reduces the number of transmissions and avoids contention and collisions.
- Data broadcasting can be implemented using different techniques, such as push-based, pull-based, or hybrid-based.
  - Push-based broadcasting: the sender periodically broadcasts data items according to a predefined schedule, and the receivers tune in to the channel to receive the data they are interested in.
  - Pull-based broadcasting: the receivers send requests for data items to the sender, and the sender broadcasts the requested data items on demand.
  - Hybrid-based broadcasting: the sender combines both push and pull techniques, and broadcasts data items according to a dynamic schedule that adapts to the changing demands of the receivers.
- Data broadcasting can be enhanced by using network coding or cooperation techniques, which can improve the performance and reliability of wireless broadcast channels.
  - Network coding: the sender encodes multiple data items into a single coded packet, and the receivers can decode the data items they are interested in from the coded packet.
  - Cooperation: the receivers cooperate with each other by relaying data items they have received to other receivers who have not received them.
- Data broadcasting can be applied to various wireless networks, such as wireless local area networks (WLANs), wireless personal area networks (WPANs), or wireless metropolitan area networks (WMANs) .
  - WLANs: wireless networks that cover a small geographic area, such as a home, office, or campus, and use radio frequency (RF) technology to connect devices, such as laptops, smartphones, or printers .
  - WPANs: wireless networks that cover a very short range, such as a few meters, and use RF or infrared technology to connect devices, such as headphones, keyboards, or mice .
  - WMANs: wireless networks that cover a large geographic area, such as a city or a region, and use RF or microwave technology to connect devices, such as base stations, access points, or routers .
- Data broadcasting can be standardized by using different protocols, such as IEEE 802.11, Bluetooth, or WiMAX .
  - IEEE 802.11: a set of standards that define the physical and medium access control (MAC) layers of WLANs, and support different data rates, frequencies, and modulations .
  - Bluetooth: a wireless technology that enables WPANs, and supports low-power, short-range, and low-cost communication between devices .
  - WiMAX: a wireless technology that enables WMANs, and supports high-speed, long-range, and broadband communication between devices .



### Mobile IP

- Mobile IP is a protocol that allows mobile devices to maintain their IP address and connectivity across different networks.
- Mobile IP is based on the concept of a home network, where the mobile device has a permanent IP address, and a foreign network, where the mobile device visits temporarily and obtains a temporary IP address.
- Mobile IP uses three main components: a home agent, a foreign agent, and a mobile node.
- A home agent is a router on the home network that keeps track of the mobile node's location and forwards packets to and from the mobile node.
- A foreign agent is a router on the foreign network that provides services to the mobile node, such as assigning a temporary IP address and relaying packets to and from the home agent.
- A mobile node is the device that moves across networks and uses Mobile IP to maintain its IP address and connectivity.
- Mobile IP works as follows:
  - When the mobile node is on its home network, it communicates directly with other nodes using its permanent IP address.
  - When the mobile node moves to a foreign network, it obtains a temporary IP address from the foreign agent and registers its new location with the home agent.
  - The home agent creates a binding between the permanent IP address and the temporary IP address of the mobile node and updates a binding cache.
  - When a node on the Internet wants to communicate with the mobile node, it sends packets to the permanent IP address of the mobile node.
  - The home agent intercepts the packets and encapsulates them with the temporary IP address of the mobile node as the destination address. This process is called tunneling.
  - The home agent sends the encapsulated packets to the foreign agent, which decapsulates them and delivers them to the mobile node.
  - When the mobile node wants to communicate with a node on the Internet, it sends packets to the foreign agent, which encapsulates them with the permanent IP address of the mobile node as the source address and forwards them to the home agent.
  - The home agent decapsulates the packets and sends them to the destination node on the Internet.
  - When the mobile node moves to another foreign network, it repeats the same process of obtaining a new temporary IP address and registering with the home agent.
  - The home agent updates the binding cache and forwards the packets to the new foreign agent.
- Mobile IP has several advantages, such as:
  - It preserves the IP address and connectivity of the mobile node across different networks, which enables seamless mobility and session continuity.
  - It is compatible with existing IP networks and applications, as it does not require any changes to the nodes on the Internet or the mobile node.
  - It supports security and authentication mechanisms, such as IPsec, to protect the communication between the mobile node and the home agent.
- Mobile IP also has some limitations, such as:
  - It introduces additional overhead and latency due to the encapsulation and decapsulation of packets and the registration process.
  - It may cause suboptimal routing and increased network congestion, as the packets have to travel through the home agent and the foreign agent, which may not be the shortest path.
  - It may not work well with some network protocols and applications that rely on the IP address of the mobile node, such as TCP and DNS.



# WAP: Architecture

- Wireless Application Protocol (WAP) is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: Wireless Application Environment (WAE). This layer is of most interest to content developers because it contains among other things, device specifications, content formats, and scripting languages. WAE uses Wireless Markup Language (WML) and WMLScript as the main technologies for creating web applications for mobile devices.
  - Session Layer: Wireless Session Protocol (WSP). This layer provides the upper-level application layer with a consistent interface for two session services: connection-oriented and connectionless. WSP also handles the security aspects of the communication, such as encryption and authentication.
  - Transaction Layer: Wireless Transaction Protocol (WTP). This layer provides a reliable request/response service on top of an unreliable datagram service. WTP supports three classes of transactions: unreliable, reliable, and secure. WTP also handles the retransmission and acknowledgement mechanisms for the data packets.
  - Security Layer: Wireless Transport Layer Security (WTLS). This layer provides data integrity, privacy, and authentication services for the wireless communication. WTLS is based on the Transport Layer Security (TLS) protocol, but it is optimized for the wireless environment. WTLS uses encryption algorithms, such as RSA, DES, and RC4, to protect the data from eavesdropping and tampering.
  - Transport Layer: Wireless Datagram Protocol (WDP). This layer provides a common interface for the upper layers to access different wireless networks, such as GSM, CDMA, and CDPD. WDP adapts the transport layer of the underlying network to a common format, so that the upper layers do not need to know the specific characteristics of each network.
- The WAP architecture also includes a WAP gateway, which is a server that acts as an intermediary between the wireless network and the internet. The WAP gateway performs several functions, such as:
  - Translating between HTTP and WAP protocols
  - Encoding and decoding the data using binary formats to reduce the bandwidth consumption
  - Compressing and decompressing the data to improve the transmission speed
  - Caching the data to reduce the network traffic
  - Filtering the data to adapt to the capabilities and preferences of the wireless devices



### Protocol Stack

A protocol stack is a set of software components that implement different communication protocols for a network. A protocol is a set of rules and procedures that define how data is exchanged between devices. A protocol stack allows different types of devices and networks to communicate with each other by providing a common interface and a standard format for data transmission.

A protocol stack typically consists of several layers, each of which performs a specific function in the communication process. The layers are arranged in a hierarchical order, from the lowest to the highest level. The lower layers deal with the physical and data link aspects of the network, such as how to transmit and receive bits, frames, and packets. The higher layers deal with the network, transport, and application aspects of the network, such as how to route, segment, and deliver data, and how to provide services and functions for the end users.

Some examples of protocol stacks are:

- The TCP/IP protocol stack, which is the most widely used protocol stack for the Internet and other networks. It consists of four main layers: the network access layer, the internet layer, the transport layer, and the application layer.
- The OSI protocol stack, which is a theoretical model that defines seven layers of communication: the physical layer, the data link layer, the network layer, the transport layer, the session layer, the presentation layer, and the application layer.
- The Bluetooth protocol stack, which is a protocol stack for wireless personal area networks (WPANs). It consists of several layers, such as the radio layer, the baseband layer, the link manager layer, the logical link control and adaptation protocol (L2CAP) layer, the service discovery protocol (SDP) layer, and the application layer.

### Wireless Networking

Wireless networking is a type of networking that uses wireless technologies, such as radio waves, infrared, or optical signals, to connect devices and networks without wires or cables. Wireless networking enables mobility, flexibility, and scalability for users and applications. Wireless networking also poses some challenges, such as security, interference, and power consumption.

Some examples of wireless networking technologies are:

- Wireless LAN (WLAN), which is a wireless network that covers a local area, such as a home, an office, or a campus. WLANs use the IEEE 802.11 standard, also known as Wi-Fi, to provide wireless access to the Internet and other networks. WLANs typically operate in the 2.4 GHz or 5 GHz frequency bands, and can support data rates up to 600 Mbps or more.
- Bluetooth, which is a wireless technology that enables short-range communication between devices, such as smartphones, laptops, headphones, and printers. Bluetooth uses the IEEE 802.15.1 standard, and operates in the 2.4 GHz frequency band. Bluetooth can support data rates up to 3 Mbps or more, and can form ad hoc networks called piconets and scatternets.
- Wireless MAN (WMAN), which is a wireless network that covers a metropolitan area, such as a city or a region. WMANs use the IEEE 802.16 standard, also known as WiMAX, to provide wireless broadband access to the Internet and other networks. WMANs typically operate in the 2-66 GHz frequency bands, and can support data rates up to 1 Gbps or more.

### Wireless LAN Overview: MAC Issues, IEEE 802.11, Bluetooth

Wireless LANs (WLANs) are wireless networks that cover a local area, such as a home, an office, or a campus. WLANs use the IEEE 802.11 standard, also known as Wi-Fi, to provide wireless access to the Internet and other networks. WLANs typically operate in the 2.4 GHz or 5 GHz frequency bands, and can support data rates up to 600 Mbps or more.

Some of the main topics related to WLANs are:

- MAC Issues: The medium access control (MAC) layer is the layer that controls how devices access and share the wireless medium. The MAC layer faces some challenges in WLANs, such as hidden and exposed terminals, fading and multipath, and collision avoidance. The MAC layer uses some techniques to overcome these challenges, such as carrier sense multiple access with collision avoidance (CSMA/CA), request to send/clear to send (RTS/CTS), and distributed coordination function (DCF).
- IEEE 802.11: The IEEE 802.11 standard is the standard that defines the physical and MAC layers of WLANs. The IEEE 802.11 standard has several amendments that specify different features and enhancements for WLANs, such as 802.



### Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Protocol (WAP), which was developed by the WAP Forum, a consortium of wireless industry players.
- WAP consists of four main components: Wireless Application Environment (WAE), Wireless Session Protocol (WSP), Wireless Transaction Protocol (WTP), and Wireless Transport Layer Security (WTLS).
- The WAE provides a general-purpose application architecture based on existing web technologies and philosophies, such as HTML, XML, and scripting. The WAE supports browsing, scripting, and extensions that allow cellular network operators to offer network services within WAP.
- The WSP is a session layer protocol that provides reliable and efficient data exchange between wireless devices and web servers. The WSP supports both connection-oriented and connectionless modes, and can handle different types of content, such as text, images, audio, and video.
- The WTP is a transaction layer protocol that provides reliable request-response services over unreliable wireless networks. The WTP supports three classes of transactions: unreliable, reliable, and secure. The WTP also supports features such as segmentation, reassembly, retransmission, and acknowledgment.
- The WTLS is a security layer protocol that provides data encryption, authentication, and integrity protection between wireless devices and web servers. The WTLS is based on the Transport Layer Security (TLS) protocol, but adapted for the wireless environment. The WTLS supports various cryptographic algorithms, such as RSA, DES, and RC4.

### Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- A wireless LAN (WLAN) is a local area network that uses radio waves to connect wireless devices, such as laptops, smartphones, and printers, without the need for cables or wires.
- A WLAN typically consists of one or more access points (APs), which are devices that provide wireless connectivity to a wired network, and one or more stations (STAs), which are devices that communicate with the APs or with each other.
- A WLAN operates in a shared medium, which means that multiple devices can transmit and receive data on the same frequency band. However, this also means that collisions and interference can occur, which can degrade the performance and reliability of the WLAN.
- To avoid collisions and interference, a WLAN needs a medium access control (MAC) protocol, which is a set of rules that determine how devices access the shared medium and resolve conflicts. There are two main types of MAC protocols: contention-based and reservation-based.
- A contention-based MAC protocol allows devices to compete for the medium and transmit data whenever the medium is idle. However, if two or more devices transmit at the same time, a collision occurs and the data is corrupted. To detect and recover from collisions, contention-based MAC protocols use techniques such as carrier sense multiple access with collision avoidance (CSMA/CA), request to send/clear to send (RTS/CTS), and acknowledgments (ACKs).
- A reservation-based MAC protocol allows devices to reserve the medium for a certain period of time and transmit data without contention. However, this requires coordination and synchronization among devices, which can introduce overhead and delay. To reserve and release the medium, reservation-based MAC protocols use techniques such as polling, token passing, and time division multiple access (TDMA).
- IEEE 802.11 is a family of standards that define the physical and MAC layers of WLANs. The IEEE 802.11 standards specify various parameters, such as frequency bands, modulation schemes, data rates, frame formats, and security mechanisms. The IEEE 802.11 standards also define different variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of performance, compatibility, and features.
- Blue Tooth is a wireless technology that enables short-range communication between devices, such as headphones, keyboards, mice, and speakers. Blue Tooth operates in the 2.4 GHz frequency band and uses frequency hopping spread spectrum (FHSS) to avoid interference. Blue Tooth supports various profiles, such as advanced audio distribution profile (A2DP), human interface device profile (HID), and personal area network profile (PAN), which define the capabilities and services of different devices.
- Wireless is a general term that refers to any type of communication that does not require wires



### Applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves or infrared signals.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs can be classified into two types: infrastructure and ad hoc.
  - Infrastructure WLANs use a base station, such as a wireless access point (AP), to coordinate the communication among the devices. The AP is connected to a wired network, such as the Internet, and acts as a bridge between the wireless and wired networks.
  - Ad hoc WLANs do not use a base station, but rely on the devices to communicate directly with each other. This mode is also known as peer-to-peer (P2P) or Wi-Fi Direct. Ad hoc WLANs are easy to set up and can provide basic P2P communication.
- WLANs use the IEEE 802.11 standard, which defines the Medium Access Control (MAC) and Physical Layer (PHY) protocols for wireless communication. The MAC layer is responsible for controlling the access to the shared wireless medium, while the PHY layer is responsible for encoding, modulating, and transmitting the data over the wireless channel.
- IEEE 802.11 has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in terms of data rates, frequency bands, modulation schemes, and channel widths. The most common variants are 802.11b/g/n, which operate in the 2.4 GHz band, and 802.11a/ac/ax, which operate in the 5 GHz band.
- IEEE 802.11 uses the Ethernet protocol and CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance) as the MAC scheme. CSMA/CA is a distributed algorithm that allows the devices to sense the channel before transmitting, and to back off if the channel is busy. CSMA/CA also uses an acknowledgment mechanism to confirm the successful reception of a frame, and a retransmission mechanism to handle the lost or corrupted frames.
- IEEE 802.11 also supports two modes of operation: distributed coordination function (DCF) and point coordination function (PCF). DCF is the basic mode that uses CSMA/CA for contention-based access, while PCF is an optional mode that uses a centralized controller, called the point coordinator (PC), to schedule the access in a polling-based manner. PCF can provide higher priority and guaranteed access for time-sensitive applications, such as voice and video.
- Bluetooth is another wireless technology that enables short-range communication among devices, such as smartphones, laptops, headphones, keyboards, mice, printers, and speakers. Bluetooth uses the 2.4 GHz band and supports data rates up to 3 Mbps.
- Bluetooth is based on the IEEE 802.15.1 standard, which defines the MAC and PHY layers for wireless personal area networks (WPANs). WPANs are wireless networks that cover a small area, typically within 10 meters, and are used for personal or private purposes.
- Bluetooth employs a frequency-hopping spread spectrum (FHSS) technique, which means that the devices change their frequency of operation in a pseudo-random manner, to avoid interference and enhance security. Bluetooth also uses a master-slave architecture, where one device, called the master, controls the communication with up to seven devices, called the slaves, in a network, called a piconet. Multiple piconets can be interconnected to form a larger network, called a scatternet.
- Bluetooth supports two types of links: synchronous connection-oriented (SCO) and asynchronous connectionless (ACL). SCO links are used for voice applications, such as phone calls, and provide a fixed and reserved bandwidth, while ACL links are used for data applications, such as file transfer, and provide a variable and shared bandwidth.
- Wireless multiple access protocols are the protocols that enable multiple devices to share the wireless medium and communicate with each other. Wireless multiple access protocols can be classified into three categories: fixed assignment, random access, and demand assignment.
  - Fixed assignment protocols allocate the wireless resources, such as frequency, time, or code, to the devices in a fixed and predetermined manner. Examples of fixed assignment protocols are frequency division multiple access (FDMA), time division multiple access (



## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to fixed servers or databases through wireless networks .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and transactions, and for resolving global name conflicts.
  - Security: The data stored or transmitted by mobile devices is more vulnerable to unauthorized access, modification, or theft than the data at fixed locations. Therefore, encryption, authentication, and access control mechanisms are needed to protect the mobile data.
  - Data distribution and replication: The uneven and dynamic network connectivity of mobile devices requires efficient strategies for distributing and replicating data among fixed and mobile nodes, to improve data availability and performance.
  - Data caching and hoarding: The limited bandwidth and power of mobile devices motivate the use of data caching and hoarding techniques, which allow mobile devices to store frequently or recently accessed data locally, and to prefetch data that may be needed in the future.
  - Data synchronization and reconciliation: The data cached or hoarded by mobile devices may become stale or inconsistent with the data at the fixed servers or databases, due to updates or disconnections. Therefore, mechanisms are needed to synchronize and reconcile the data when the mobile devices reconnect to the network.
  - Data broadcasting and dissemination: The data broadcasting and dissemination techniques aim to deliver data to multiple mobile devices simultaneously, by using a single broadcast channel or a multicast group. This can reduce the network congestion and the power consumption of mobile devices.
  - Query processing and optimization: The query processing and optimization techniques for mobile databases need to consider the characteristics and constraints of mobile devices and wireless networks, such as limited resources, mobility, disconnection, and location-awareness.
  - Transaction management and recovery: The transaction management and recovery techniques for mobile databases need to ensure the ACID (atomicity, consistency, isolation, and durability) properties of transactions, despite the possibility of failures, disconnections, or conflicts.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data at different locations, to improve data availability, reliability, and performance.
- Data replication for mobile computers involves replicating data among fixed servers or databases and mobile devices, to cope with the challenges of mobile computing, such as limited bandwidth, frequent disconnection, and dynamic network topology.
- Data replication for mobile computers can be classified into two categories:
  - Server-initiated replication: The fixed servers or databases initiate the replication process, by pushing data updates to the mobile devices, or by pulling data updates from the mobile devices. This approach can reduce the communication cost and the data inconsistency, but it requires the servers to know the location and the interest of the mobile devices.
  - Client-initiated replication: The mobile devices initiate the replication process, by requesting data updates from the fixed servers or databases, or by sending data updates to the fixed servers or databases. This approach can increase the data autonomy and the flexibility of the mobile devices, but it may incur more communication cost and data inconsistency.
- Data replication for mobile computers can also be classified into two types:
  - Eager replication: The data updates are propagated to all the replicas as soon as they occur, to ensure that all the replicas are always consistent. This type of replication can provide fast and accurate query responses, but it requires a reliable and stable network connection, and it may cause update conflicts or deadlock.
  - Lazy replication: The data updates are propagated to the replicas only when the network connection is available, to tolerate network disconnection and failure. This type of replication can provide high data availability and low communication cost, but it may cause data inconsistency or staleness, and it requires reconciliation mechanisms.

### Adaptive clustering for mobile

- Adaptive clustering is a technique that dynamically organizes mobile devices into clusters, based on their location, mobility, and communication patterns, to facilitate data management and communication among mobile devices.
- Adaptive clustering for mobile can provide the following benefits:
  - Scalability:



### Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables or wires. Wireless networks can enable mobile computing, which is the ability to access and process data from anywhere and anytime using portable devices.

Some of the topics related to wireless networks and mobile computing are:

- Data management issues
- Data replication for mobile computers
- Adaptive clustering for mobile wireless networks

#### Data Management Issues

Data management is the process of storing, organizing, and manipulating data in a way that meets the needs and requirements of users and applications. Data management issues are the challenges and problems that arise when dealing with data in wireless networks and mobile computing environments.

Some of the data management issues are:

- Data availability: How to ensure that data is accessible and consistent to mobile users, even when they are disconnected from the network or move across different network domains.
- Data dissemination: How to efficiently and effectively distribute data to mobile users, taking into account their interests, preferences, and locations.
- Data caching: How to store data locally on mobile devices or intermediate nodes, such as proxies or base stations, to reduce network traffic and improve performance.
- Data synchronization: How to reconcile the changes made to data by different users or devices, and maintain data consistency and integrity.
- Data security: How to protect data from unauthorized access, modification, or disclosure, especially when data is transmitted over wireless channels or stored on mobile devices.

#### Data Replication for Mobile Computers

Data replication is the technique of creating and maintaining multiple copies of data in different locations, such as servers, mobile devices, or proxies. Data replication can improve data availability, performance, and fault tolerance for mobile computers, but it also introduces challenges such as:

- Replica placement: How to decide where to store the replicas of data, considering factors such as network topology, bandwidth, storage capacity, and access patterns.
- Replica update: How to propagate the changes made to data by different users or devices, and ensure that the replicas are consistent and up-to-date.
- Replica selection: How to choose the best replica to access data, considering factors such as network latency, data freshness, and user preferences.

#### Adaptive Clustering for Mobile Wireless Networks

Adaptive clustering is a technique of organizing nodes in a mobile wireless network into groups or clusters, based on some criteria such as proximity, connectivity, or functionality. Adaptive clustering can provide benefits such as:

- Spatial reuse of bandwidth: By dividing the network into clusters, the same frequency or code can be used by different clusters without interference, increasing the network capacity.
- Controlled access to resources: By assigning a leader or a coordinator to each cluster, the cluster can manage the allocation and reservation of bandwidth or other resources among its members, improving the quality of service.
- Robustness to topology changes: By dynamically adjusting the cluster structure according to the node mobility, failure, or insertion/removal, the network can maintain its connectivity and functionality, enhancing the reliability.



### File system for mobile computing

A file system is a software component that manages the storage and retrieval of data on a persistent device. A file system for mobile computing is a file system that supports the mobility and wireless connectivity of users and devices in a distributed environment.

Some of the challenges and requirements for designing a file system for mobile computing are:

- Location transparency: The file system should provide a uniform namespace for accessing files regardless of their physical location or the network topology.
- User mobility: The file system should allow users to access their files from different devices and locations, and to move or migrate their files across devices and networks.
- Compatibility: The file system should be compatible with existing operating system interfaces and applications, and interoperate with other file systems and protocols.
- Performance: The file system should provide high performance and low latency for file operations, especially in wireless and mobile scenarios.
- Availability: The file system should ensure the availability and consistency of files in the presence of network failures, disconnections, and partitions.
- Replication: The file system should support replication of files across multiple servers for fault tolerance, load balancing, and data locality.
- Security: The file system should provide security mechanisms for authentication, encryption, and access control of files and users.
- Adaptation: The file system should adapt to the changing network conditions and resource constraints of mobile devices and wireless networks.

One example of a file system for mobile computing is Coda, which is a distributed file system that supports disconnected operation, server replication, security, and network bandwidth adaptation. Coda is based on the Andrew File System (AFS) , but extends it with several features for mobile computing, such as:

- Hoarding: A mechanism that allows clients to cache files on their local disks and specify which files they want to keep available when disconnected from the network.
- Reintegration: A mechanism that allows clients to reconcile their cached updates with the server replicas when they reconnect to the network.
- Weakly connected operation: A mode of operation that allows clients to perform file operations with minimal network communication when the network is slow or unreliable.
- Application callbacks: A mechanism that allows applications to register callbacks with the file system to receive notifications of file changes and conflicts.
- Server resolution: A mechanism that allows servers to resolve conflicts among replicas using application-specific policies or user intervention.



# Disconnected operations for mobile computing

- Disconnected operation is a mode of operation in which a mobile device can execute applications without being connected to a network or server .
- Disconnected operation can be voluntary or involuntary, depending on the user's choice or the network availability .
- Disconnected operation can improve the availability, performance, and energy efficiency of mobile devices, but also introduces challenges such as data consistency, synchronization, and security  .
- Disconnected operation can be supported by various techniques, such as:
  - Data replication: copying data from servers to mobile devices and vice versa, to allow access and modification of data while disconnected .
  - Data caching: storing frequently or recently accessed data on mobile devices, to reduce network traffic and latency while disconnected .
  - Data hoarding: prefetching data that is likely to be needed while disconnected, based on user preferences, access patterns, or predictions .
  - Data reconciliation: resolving conflicts and inconsistencies that may arise due to concurrent or divergent updates of replicated data while disconnected .
  - Mobile computation: transferring code or computation from servers to mobile devices or vice versa, to enable execution of applications while disconnected .
- Disconnected operation can be implemented at different levels of granularity, such as file, object, or database level, depending on the type and structure of data and applications .
- Disconnected operation can be evaluated by various metrics, such as availability, performance, energy consumption, data consistency, and user satisfaction .



# Unit 4 - Mobile Agents Computing, Security and Fault Tolerance, Transaction Processing in Mobile Computing

## Mobile Agents Computing

- A mobile agent is a composition of computer software and data that is able to migrate (move) from one computer to another autonomously and continue its execution on the destination computer.
- A mobile agent is a specific form of mobile code, within the field of code mobility. However, in contrast to the remote evaluation and code on demand programming paradigms, mobile agents are active in that they can choose to migrate between computers at any time during their execution.
- Mobile agents are autonomous with intelligence, social ability, learning, and the most important feature is their mobility. They are independent in nature, self-driven and do not require a corresponding node for communication. They can work efficiently even after the user gets disconnected from the network.
- Mobile agents can be used for various applications in mobile computing, such as information retrieval, network management, electronic commerce, distributed computing, and collaborative work .

## Security and Fault Tolerance

- Security and fault tolerance are two major challenges for mobile agents in mobile computing, as they may encounter malicious hosts, network failures, or other unexpected events during their migration and execution.
- Security issues for mobile agents include protecting the agent code and data from unauthorized modification, protecting the agent execution state from tampering, protecting the agent communication from eavesdropping or interception, and protecting the host resources from unauthorized access or consumption by the agent.
- Fault tolerance issues for mobile agents include ensuring the agent availability, reliability, and consistency in the presence of faults, such as agent crash, host crash, network partition, or agent duplication.
- Various techniques have been proposed to address the security and fault tolerance issues for mobile agents, such as encryption, authentication, digital signature, sandboxing, checkpointing, replication, recovery, and consensus.

## Transaction Processing in Mobile Computing

- Transaction processing in mobile computing refers to the execution of transactions that involve mobile hosts, mobile agents, or mobile data in a distributed and mobile environment.
- Transaction processing in mobile computing faces several challenges, such as limited bandwidth, high latency, frequent disconnection, low reliability, and dynamic topology.
- To cope with these challenges, transaction processing in mobile computing requires some special features, such as location transparency, mobility transparency, disconnection transparency, partial replication, adaptive concurrency control, and flexible commit protocols.
- Some examples of transaction models for mobile computing are kangaroo transactions, mobile transactions, nomadic transactions, and adaptive transactions.



### Environment for Mobile Agents Computing

- A mobile agent is a piece of software that can move from one host to another in a network, carrying its state and data, and executing autonomously.
- A mobile agent environment is the infrastructure that supports the creation, migration, execution, and communication of mobile agents.
- A mobile agent environment consists of the following components:
  - A mobile agent platform, which is the software layer that provides the basic services and facilities for mobile agents, such as agent creation, migration, execution, communication, security, and management.
  - A mobile agent language, which is the programming language or framework that enables the development of mobile agents, such as Java, Python, or Aglets.
  - A mobile agent system, which is the application or middleware that uses mobile agents to achieve a specific goal, such as distributed information retrieval, network management, or e-commerce.
- A mobile agent environment can be classified according to different criteria, such as the mobility model, the communication model, the security model, or the application domain.
- Some examples of mobile agent environments are  :
  - Aglets, which is a Java-based mobile agent platform and framework developed by IBM.
  - Grasshopper, which is a mobile agent platform and system that supports interoperability and security for mobile agents.
  - Odyssey, which is a mobile agent system that uses mobile agents to support adaptive resource management in mobile computing environments.
  - Mole, which is a mobile agent system that uses mobile agents to support distributed information retrieval and filtering.
  - MASSIVE, which is a mobile agent system that uses mobile agents to support collaborative virtual environments.



## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over wireless links. Ad hoc networks are suitable for applications that require temporary, dynamic, and self-organizing connectivity, such as disaster relief, military operations, and vehicular networks.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization is important for many applications that need location-aware services, such as routing, data dissemination, and security. Localization can be achieved by using various techniques, such as GPS, signal strength, angle of arrival, time of arrival, and multilateration.
- MAC (Medium Access Control) issues refer to the challenges of coordinating the access of multiple nodes to the shared wireless medium in an ad hoc network. MAC issues include how to avoid or resolve collisions, how to conserve energy, how to handle hidden and exposed terminals, how to adapt to channel variations, and how to support quality of service. MAC protocols can be classified into two categories: contention-based and reservation-based. Contention-based protocols use random access schemes, such as CSMA/CA, to compete for the channel. Reservation-based protocols use control messages, such as RTS/CTS, to reserve the channel for data transmission.
- Routing protocols are algorithms that determine the paths of data packets from source to destination in an ad hoc network. Routing protocols can be classified into two categories: proactive and reactive. Proactive protocols maintain up-to-date routing tables for all nodes in the network, such as DSDV and OLSR. Reactive protocols discover routes on demand, such as DSR and AODV. Routing protocols can also be classified into three categories: flat, hierarchical, and geographic. Flat routing protocols treat all nodes equally and use network-wide flooding or broadcasting to disseminate routing information, such as DSR and AODV. Hierarchical routing protocols divide the network into clusters and use cluster heads to aggregate and forward routing information, such as CGSR and ZRP. Geographic routing protocols use the location information of nodes to guide the routing decisions, such as GPSR and LAR.
- Global state routing (GSR) is a proactive, flat routing protocol for ad hoc networks. It is based on the link-state algorithm, which requires each node to maintain the complete topology of the network. GSR uses periodic hello messages to exchange link-state information with neighbors, and uses a reliable flooding mechanism to propagate link-state updates to all nodes. GSR uses the shortest path algorithm to compute the optimal routes to all destinations. GSR has the advantage of providing loop-free and consistent routes, but has the disadvantage of generating high overhead and consuming large memory and bandwidth.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on destination sequenced distance vector routing (DSDV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- It adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- Using the newly added sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- DSDV is based on the Routing Information Protocol (RIP), which is a distance vector routing protocol that uses hop count as the metric.
- DSDV is also based on distance vector routing and thus uses bidirectional links.
- A limitation of DSDV is that it provides only one route for a source/destination pair.
- DSDV requires each node to periodically broadcast routing updates, which consumes bandwidth and battery power.
- DSDV can be classified into two types: full dump and incremental.
- Full dump is when a node sends its entire routing table to its neighbors, which is done when there are significant changes in the network topology.
- Incremental is when a node sends only the updated entries in its routing table, which is done when there are minor changes in the network topology.
- DSDV uses two types of packets: route advertisement packets and route request packets.
- Route advertisement packets are used to broadcast routing updates to the neighbors.
- Route request packets are used to request a route to a destination when a node does not have a valid route in its routing table.
- DSDV uses two techniques to reduce the routing overhead: triggered updates and settling time.
- Triggered updates are when a node sends a routing update immediately after detecting a change in the network topology, instead of waiting for the periodic update interval.
- Settling time is the time period during which a node waits before propagating a routing update, in order to avoid sending inconsistent or transient updates.
- DSDV has some advantages and disadvantages over other routing protocols for ad hoc networks.
- Advantages:
  - It guarantees loop-free routes.
  - It supports both unicast and multicast routing.
  - It is simple and easy to implement.
- Disadvantages:
  - It suffers from frequent route updates, which consume bandwidth and battery power.
  - It does not support multipath routing, which can improve load balancing and fault tolerance.
  - It does not adapt well to highly dynamic network topologies, where nodes move frequently and rapidly.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on dynamic source routing (DSR) for the unit 5 of mobile computing.

### Dynamic source routing (DSR)

- Dynamic source routing (DSR) is a routing protocol for wireless mesh networks. It is similar to AODV in that it forms a route on-demand when a transmitting node requests one. However, it uses source routing instead of relying on the routing table at each intermediate device .
- Source routing means that the sender of a packet determines the complete sequence of nodes through which the packet has to pass. The sender explicitly lists this route in the packet's header, identifying each forwarding hop by the address of the next node to which to transmit the packet on its way to the destination host.
- DSR consists of two main mechanisms: route discovery and route maintenance. Route discovery is the process by which a node S wishing to send a packet to a destination node D obtains a source route to D. Route maintenance is the process of detecting and repairing route errors.
- Route discovery works as follows:
  - S initiates route discovery by broadcasting a route request (RREQ) packet to its neighbors. The RREQ contains the address of S, the address of D, and a unique identification number.
  - Each node receiving the RREQ appends its own address to the route record in the RREQ and forwards the packet to its neighbors, unless it is the destination or it has a route to D in its route cache.
  - If the node is the destination or has a route to D, it sends a route reply (RREP) packet back to S along the reverse path of the RREQ. The RREP contains the route record accumulated in the RREQ.
  - S receives the RREP and caches the route to D in its route cache. It can then send packets to D using this route.
- Route maintenance works as follows:
  - Each node forwarding a packet to the next hop along the source route is responsible for confirming that the packet has been received by the next hop. This can be done by using link-layer acknowledgments or passive acknowledgments (by overhearing the next hop forwarding the packet).
  - If the node does not receive an acknowledgment, it retransmits the packet until a maximum number of attempts is reached. If the packet is still not acknowledged, the node returns a route error (RERR) packet to the original sender of the packet, indicating the link that failed.
  - The sender of the packet receives the RERR and removes the broken link from its route cache. It can then try to send the packet using another route in its cache or initiate a new route discovery.
- DSR has some advantages and disadvantages :
  - Advantages:
    - It eliminates the need for periodic route advertisements, which reduces the network overhead and saves bandwidth and energy.
    - It allows multiple routes to be learned and cached, which increases the route availability and robustness.
    - It supports unidirectional links and asymmetric routes, which are common in wireless networks.
    - It allows nodes to learn routes opportunistically by snooping on the source routes of the packets they overhear.
  - Disadvantages:
    - It adds the source route to each packet header, which increases the packet size and may cause fragmentation.
    - It may not scale well to large networks, as the route discovery may flood the network and the route caches may become stale or inconsistent.
    - It may suffer from the route cache poisoning problem, where malicious nodes can inject false routes into the caches of other nodes.



### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, where each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses two types of messages: route request (RREQ) and route reply (RREP)  .
- When a source node wants to communicate with a destination node, it broadcasts a RREQ message to its neighbors  .
- The RREQ message contains the source and destination addresses, a sequence number, and a hop count  .
- The sequence number is used to avoid loops and to ensure freshness of routes  .
- The hop count is incremented by one at each intermediate node that forwards the RREQ message  .
- If an intermediate node has a fresh route to the destination, it can send a RREP message back to the source  .
- The RREP message contains the destination address, the sequence number, and the hop count  .
- The source node updates its routing table with the route to the destination and starts sending data packets  .
- If an intermediate node does not have a route to the destination, it rebroadcasts the RREQ message to its neighbors  .
- The RREQ message is propagated until it reaches the destination or a node with a fresh route to the destination  .
- The destination node or the node with a fresh route sends a RREP message back to the source along the reverse path of the RREQ message  .
- Each intermediate node that forwards the RREP message updates its routing table with the route to the destination  .
- AODV also uses route error (RERR) messages to notify the source node of link failures or route breaks  .
- AODV is the routing protocol used in Zigbee – a low power, low data rate wireless ad hoc network.
- AODV has various implementations such as MAD-HOC, Kernel-AODV, AODV-UU, AODV-UCSB and AODV-UIUC.
- AODV has some advantages such as low network overhead, loop-free routes, and quick adaptation to network changes .
- AODV has some disadvantages such as high latency for route discovery, vulnerability to flooding attacks, and lack of scalability for large networks .



### Temporary ordered routing algorithm (TORA) for ad hoc networks

- Temporally Ordered Routing Algorithm (TORA) is a source initiated on-demand routing protocol presented by Park and Corson in 1997 for wireless mobile ad hoc network .
- TORA is an efficient, highly adaptive, and scalable routing protocol based on link reversal algorithm .
- TORA consists of three main functions: route creation, route maintenance, and route erasure .
- Route creation: TORA assigns a height metric to each node in the network, which reflects its logical distance from the destination. The height metric is a tuple of five components: (τ, oid, r, δ, i), where τ is a timestamp, oid is the originator id, r is a reflection bit, δ is a propagation mode bit, and i is the node id. The height metric is used to create a directed acyclic graph (DAG) rooted at the destination, where each node has a height lower than its neighbors. The source node initiates a query (QRY) packet with the destination id, which is broadcast to its neighbors. Each intermediate node that receives the QRY packet and does not have a route to the destination, rebroadcasts the QRY packet. Each intermediate node that has a route to the destination or is the destination itself, replies with an update (UPD) packet containing its height metric. The UPD packet is propagated back to the source along the reverse path of the QRY packet, updating the height metric of each node along the way. The source node selects the lowest height among its neighbors as its next hop to the destination  .
- Route maintenance: TORA detects and repairs link failures locally using the link reversal algorithm. When a node detects a link failure to a downstream neighbor (a neighbor with a lower height), it increases its height to make itself unreachable from the failed link. This may cause some of its upstream neighbors (neighbors with a higher height) to lose their routes to the destination. These nodes then invoke the link reversal algorithm to find new downstream neighbors. The link reversal algorithm works as follows: a node that loses all its downstream neighbors broadcasts a clear (CLR) packet to erase invalid routes, sets its reflection bit to 1, and sets its propagation mode bit to 0. Then, it broadcasts an UPD packet with its new height to its neighbors. If a node receives an UPD packet from a lower neighbor, it sets its propagation mode bit to 1 and updates its height. If a node receives an UPD packet from a higher neighbor and its propagation mode bit is 1, it updates its height. If a node receives an UPD packet from a higher neighbor and its propagation mode bit is 0, it ignores the packet. The link reversal algorithm terminates when a new DAG is formed or no more UPD packets are received  .
- Route erasure: TORA erases invalid routes when they are not needed anymore or when the network partition occurs. A node can erase its routes by setting its height to NULL and broadcasting an UPD packet with the NULL height. This causes its neighbors to erase their routes as well. A node can also erase its routes by broadcasting a flush (FLS) packet, which contains the destination id and the last known height for that destination. The FLS packet is flooded throughout the network, and any node that receives it and has a height equal to or lower than the FLS packet, sets its height to NULL and rebroadcasts the FLS packet. The FLS packet is used to handle network partitions, where the destination becomes unreachable from the source  .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on QoS in Ad Hoc Networks for the Unit 5 of Mobile Computing:

### QoS in Ad Hoc Networks

- Quality of Service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc.  
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or centralized control.  
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes.   
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.  
- QoS in ad hoc networks can be supported by using various techniques, such as QoS-aware routing protocols, QoS-aware MAC protocols, QoS-aware scheduling algorithms, QoS-aware admission control, QoS-aware resource reservation, QoS-aware cross-layer optimization, etc.   
- QoS in ad hoc networks can be evaluated by using various metrics, such as throughput, delay, jitter, packet loss, packet delivery ratio, end-to-end QoS, etc.   
- QoS in ad hoc networks can be improved by using various methods, such as adaptive QoS, QoS negotiation, QoS feedback, QoS monitoring, QoS adaptation, QoS recovery, etc.   




### Applications of Ad Hoc Networks

Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of mobile nodes that communicate with each other directly or through intermediate nodes. Ad hoc networks have many potential applications in various domains, such as:

- **Military battlefield**: Ad hoc networks can provide secure and robust communication among soldiers, vehicles, and command centers in a dynamic and hostile environment.
- **Vehicular ad hoc networks (VANETs)**: Ad hoc networks can enable vehicles to exchange information about traffic conditions, road safety, navigation, entertainment, and other services . Intelligent VANETs can use artificial intelligence and ad hoc technologies to coordinate actions and avoid accidents.
- **Smartphone ad hoc networks (SPANs)**: Ad hoc networks can allow smartphones to form peer-to-peer networks without relying on cellular or Wi-Fi networks. SPANs can support applications such as social networking, file sharing, disaster recovery, and crowd sensing .
- **Wireless sensor networks (WSNs)**: Ad hoc networks can connect a large number of sensor nodes that collect and process data from the physical environment. WSNs can be used for applications such as environmental monitoring, health care, smart homes, and industrial automation.
- **Industrial and commercial applications**: Ad hoc networks can facilitate cooperative mobile data exchange among workers, customers, and devices in various scenarios, such as conferences, exhibitions, warehouses, and factories.

