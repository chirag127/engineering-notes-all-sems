

## Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices that can access and process data over wireless networks. Mobile computing enables users to communicate, work, and access information anytime and anywhere.
- Issues in mobile computing include:
  - Limited battery life and power consumption of mobile devices.
  - Limited bandwidth and network coverage of wireless networks.
  - Security and privacy of data transmitted over wireless networks.
  - Heterogeneity and interoperability of mobile devices and wireless networks.
  - Mobility and location management of mobile devices and users.
  - Adaptability and scalability of mobile applications and services.
- Wireless telephony is the provision of voice and data services over wireless networks. Wireless telephony can be classified into:
  - Cellular networks: A cellular network is a wireless network that divides a geographical area into cells, each served by a base station. Cellular networks use multiple access techniques to allow multiple users to share the same frequency spectrum. Cellular networks can support voice and data services, as well as roaming and handover between cells.
  - Cordless networks: A cordless network is a wireless network that connects a cordless phone to a base station within a short range, typically within a building or a home. Cordless networks use a single frequency channel for each cordless phone and base station pair. Cordless networks can only support voice services, and do not support roaming or handover between base stations.
- Cellular concept: The cellular concept is the principle of dividing a large service area into smaller cells, each served by a base station. The cellular concept enables frequency reuse, which means that the same frequency channels can be used by different cells that are sufficiently far apart to avoid interference. The cellular concept also enables mobility management, which means that the network can track the location and movement of mobile devices and users, and perform handover when they move from one cell to another.
- GSM: GSM stands for Global System for Mobile Communication. GSM is an open and digital cellular technology that is widely used by mobile phone users in Europe and other parts of the world. GSM uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allow multiple users to share the same frequency spectrum. GSM supports voice and data services, as well as roaming and handover between different GSM networks. GSM uses four different frequency bands: 850 MHz, 900 MHz, 1800 MHz and 1900 MHz. GSM has a hierarchical network architecture that consists of the following components:
  - Mobile station (MS): The mobile station is the user device that communicates with the base station. The mobile station consists of two parts: the mobile equipment (ME), which is the physical device, and the subscriber identity module (SIM), which is a smart card that stores the user's identity and authentication information.
  - Base station subsystem (BSS): The base station subsystem is the part of the network that connects the mobile stations to the core network. The base station subsystem consists of two parts: the base transceiver station (BTS), which is the radio equipment that transmits and receives signals from the mobile stations, and the base station controller (BSC), which is the controller that manages the radio resources and the handover of the mobile stations.
  - Network and switching subsystem (NSS): The network and switching subsystem is the core network that provides the voice and data services to the mobile stations. The network and switching subsystem consists of several components, such as the mobile switching center (MSC), which is the switch that connects the base station subsystems and other networks, the home location register (HLR), which is the database that stores the permanent information of the subscribers, the visitor location register (VLR), which is the database that stores the temporary information of the subscribers who are visiting a certain area, and the authentication center (AuC), which is the component that performs the authentication and encryption of the mobile stations.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Mobile Computing. Here are some notes on the topic of air-interface for the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

### Air-interface
- The air-interface, or access mode, is the communication link between the two stations in mobile or wireless communication.
- The air-interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection.
- The air-interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network.
- The air-interface also specifies the protocols and procedures for signaling, authentication, encryption, error control, and handover.
- The air-interface is the wireless counterpart of the physical layer 1 in the OSI model.

#### Cellular concept
- The cellular concept is a system design approach that divides a service area into small cells, each served by a base station, to provide high capacity and coverage for mobile users.
- The cellular concept allows the reuse of the same radio frequencies in different cells, as long as they are sufficiently separated to avoid interference.
- The cellular concept also enables the dynamic allocation of channels to mobile users, based on the traffic demand and the location of the users.
- The cellular concept requires the coordination and management of the network by a central controller, called the mobile switching center (MSC), which connects the base stations to the public switched telephone network (PSTN) or the internet.

#### GSM
- GSM (Global System for Mobile communications) is a standard for digital cellular telephony that operates in the 900 MHz and 1800 MHz bands in Europe and Asia, and in the 850 MHz and 1900 MHz bands in North America and Latin America.
- GSM uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) techniques to divide the radio spectrum into 200 kHz channels, each carrying eight time slots for voice or data transmission.
- GSM uses a hierarchical network architecture, consisting of four main components: the mobile station (MS), the base station subsystem (BSS), the network and switching subsystem (NSS), and the operation and support subsystem (OSS).
- GSM provides various services, such as voice, data, short message service (SMS), multimedia messaging service (MMS), and roaming, to its subscribers.
- GSM also employs various features, such as authentication, encryption, power control, discontinuous transmission, and adaptive multi-rate (AMR) coding, to enhance the security, efficiency, and quality of the air-interface.

: Air interface - Wikipedia
: Definition of air interface | PCMag



Hello, I am Sydney, your AI assistant. I can help you with your study material for Mobile Computing. Here is the content for the topic of channel structure for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

### Channel Structure

- A channel is a medium or a path that carries information from one point to another in a communication system.
- In mobile computing, channels are used to transmit and receive data between mobile devices and base stations or between base stations and network controllers.
- Channels can be classified into two types: physical channels and logical channels.

#### Physical Channels

- Physical channels are the basic units of transmission in a mobile network. They are defined by the frequency, time slot, and code used to modulate the signal.
- Physical channels can be further divided into two types: frequency division multiple access (FDMA) channels and time division multiple access (TDMA) channels.
- FDMA channels are the frequency bands allocated to each user or cell in a network. They are separated by guard bands to avoid interference.
- TDMA channels are the time slots assigned to each user or cell in a network. They are separated by guard gaps to avoid interference.
- A combination of FDMA and TDMA channels is called a hybrid channel.

#### Logical Channels

- Logical channels are the information streams carried by the physical channels. They are defined by the type, format, and purpose of the data transmitted or received.
- Logical channels can be further divided into two types: traffic channels and control channels.
- Traffic channels are the logical channels that carry user data, such as voice, video, or text messages.
- Control channels are the logical channels that carry signaling and management data, such as call setup, handover, authentication, or synchronization.
- In GSM, there are three types of control channels: broadcast control channels (BCCHs), common control channels (CCCHs), and dedicated control channels (DCCHs).
- BCCHs are the control channels that broadcast information about the network and the cell, such as the frequency, the cell identity, or the network parameters.
- CCCHs are the control channels that handle the access and paging of the mobile devices, such as the random access channel (RACH), the paging channel (PCH), or the access grant channel (AGCH).
- DCCHs are the control channels that handle the communication between the mobile device and the base station, such as the stand-alone dedicated control channel (SDCCH), the slow associated control channel (SACCH), or the fast associated control channel (FACCH).

#### Channel Structure in GSM

- GSM is a cellular network that uses a combination of FDMA and TDMA channels to provide voice and data services to mobile users.
- GSM uses a 25 MHz frequency band in the 900 MHz range, which is divided into 124 FDMA channels, each with a bandwidth of 200 kHz.
- Each FDMA channel is further divided into eight TDMA channels, each with a duration of 0.577 ms. A group of eight TDMA channels is called a frame, which has a duration of 4.615 ms.
- A physical channel in GSM is defined by a pair of frequency and time slot, such as (f1, t1) or (f2, t2).
- A logical channel in GSM is defined by the information carried by the physical channel, such as TCH, BCCH, RACH, or SDCCH.
- The channel structure in GSM is shown in the following diagram:

Channel structure in GSM

- Source:



Hello, I am Sydney, your AI assistant. I can help you with your study material for Mobile Computing. Here is some content on the topic of location management: HLR-VLR, hierarchical, handoffs.

### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile users in wireless cellular networks.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is initiated by the mobile unit when it moves across the boundaries of registration areas (RAs). The current location of the unit is recorded in the home location register (HLR) and the visitor location register (VLR) databases.
- Location lookup is performed by the network when it needs to deliver a call to a mobile user. The network queries the HLR to find out the current RA of the user, and then queries the VLR of that RA to obtain the exact location of the user.
- Paging is the process of broadcasting a message to all the base stations (cells) within an RA to locate the mobile user and establish a connection.
- HLR and VLR are two types of location registers that store the information of mobile subscribers. HLR is a centralized database that contains the subscription information and some location information for all the users in the network. VLR is a local database that contains the information of the users who are currently visiting a specific RA. VLR downloads the data from the HLR when a user enters its RA, and updates the HLR when a user leaves its RA.
- Hierarchical location management is a scheme that divides the network into multiple levels of RAs, each with its own VLR. The higher-level RAs cover larger areas and contain more users, while the lower-level RAs cover smaller areas and contain fewer users. Hierarchical location management can reduce the location update and lookup costs by exploiting the locality and mobility patterns of the users.
- Handoff is the process of transferring an ongoing call from one cell to another when a mobile user moves across the cell boundaries. Handoff ensures the continuity and quality of service for the mobile users.
- Handoff can be classified into two types: hard handoff and soft handoff. Hard handoff is a break-before-make process, where the connection to the old cell is terminated before the connection to the new cell is established. Soft handoff is a make-before-break process, where the connection to the new cell is established before the connection to the old cell is terminated. Soft handoff can provide better performance and reliability than hard handoff, but it requires more resources and coordination.



### Channel allocation in cellular systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- Channels are the basic units of communication resources that can carry signals between a base station and a mobile terminal.
- Channels can be divided into two types: frequency channels and time channels.
- Frequency channels are based on the frequency division multiple access (FDMA) technique, which assigns a different frequency band to each user or cell.
- Time channels are based on the time division multiple access (TDMA) technique, which divides a frequency band into time slots and assigns a different time slot to each user or cell.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots and bandwidth, while minimizing interference and maximizing quality of service .
- Channel allocation strategies can be classified into three categories: fixed channel allocation, dynamic channel allocation and hybrid channel allocation .
- Fixed channel allocation (FCA) assigns a fixed number of channels to each cell, regardless of the traffic demand .
- Dynamic channel allocation (DCA) assigns channels to cells on demand, based on the traffic load and the interference level .
- Hybrid channel allocation (HCA) combines FCA and DCA, by dividing the channels into two groups: one for FCA and one for DCA .
- Channel allocation schemes can also be classified into two types: centralized and distributed.
- Centralized channel allocation schemes use a central controller to allocate channels to cells, based on the global information of the system.
- Distributed channel allocation schemes use local controllers or base stations to allocate channels to cells, based on the local information of the system.
- Channel allocation schemes can use different algorithms to select the best channel for a cell, based on various criteria, such as future blocking probability, reuse distance, usage frequency, average blocking probability and channel occupancy distribution.



### CDMA for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- CDMA stands for Code Division Multiple Access and is a spread spectrum multiple access technique  .
- Spread spectrum technique spreads bandwidth of data in a uniform manner for the same transmitted power.
- CDMA is a digital cellular technology used for mobile communication .
- CDMA is the base on which access methods such as cdmaOne, CDMA2000, and WCDMA are built .
- CDMA allows numerous signals to occupy a single transmission channel, optimizing the use of available bandwidth .
- CDMA uses a special coding scheme, where each transmitter is assigned a code, to allow multiple users to be multiplexed over the same physical channel.
- CDMA is a form of direct-sequence spread spectrum (DSSS) modulation, where a data signal is multiplied by a pseudorandom noise (PN) code sequence that has a much higher data rate than the original signal.
- CDMA has several advantages over other multiple access techniques, such as:
  - Higher spectral efficiency, as more users can share the same frequency band.
  - Better security, as the signals are difficult to intercept or jam.
  - Improved voice quality and reduced interference, as the signals are separated by orthogonal codes.
  - Greater flexibility and scalability, as new users can be added without affecting the existing ones.
- CDMA has some disadvantages, such as:
  - Higher complexity and cost of the receiver, as it needs to perform the code synchronization and decoding.
  - Increased power consumption, as the transmitter needs to spread the signal over a wider bandwidth.
  - Near-far problem, where a strong signal from a nearby user can interfere with a weak signal from a distant user.
- CDMA is one of the multiple access techniques used in mobile computing, along with FDMA (Frequency Division Multiple Access) and TDMA (Time Division Multiple Access).
- FDMA divides the frequency band into several non-overlapping channels, and assigns one channel to each user.
- TDMA divides the time into several slots, and assigns one slot to each user.
- CDMA, FDMA, and TDMA are used to achieve frequency reuse, which is the concept of using the same frequency band in different cells to increase the capacity of the cellular network.
- GSM (Global System for Mobile Communications) is a standard for 2G digital cellular networks that uses a combination of FDMA and TDMA.
- GSM divides the frequency band into 124 channels, each with a bandwidth of 200 kHz, and then divides each channel into eight time slots, each with a duration of 0.577 ms.
- GSM supports voice and data services, such as SMS (Short Message Service), MMS (Multimedia Messaging Service), and GPRS (General Packet Radio Service).
- GSM is the most widely used cellular technology in the world, with over 5 billion subscribers as of 2018.



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
- It enables users to make and receive calls from anywhere within the coverage area of the network.
- It also provides other services such as SMS, MMS, internet access, email, etc.

### Cellular Concept

- Cellular concept is the basic principle of wireless telephony that divides a large geographical area into smaller regions called cells.
- Each cell has a base station that communicates with the mobile devices within its range.
- The base stations are connected to a central controller called mobile switching center (MSC) that coordinates the calls and handovers between cells.
- The cellular concept allows the reuse of radio frequencies among different cells, thus increasing the capacity and efficiency of the network.

### GSM

- GSM stands for Global System for Mobile Communications.
- It is a standard for 2G wireless telephony that was developed by the European Telecommunications Standards Institute (ETSI) in the late 1980s.
- It is the most widely used cellular technology in the world, with over 5 billion subscribers as of 2018.
- It operates in the 900 MHz and 1800 MHz frequency bands in Europe and Asia, and in the 850 MHz and 1900 MHz bands in North America and South America.
- It uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate radio channels to users.
- It supports voice, data, and multimedia services, such as SMS, MMS, GPRS, EDGE, etc.



## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves, infrared, or other electromagnetic signals.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus. WLANs typically use the IEEE 802.11 standard, which defines the medium access control (MAC) and physical layer (PHY) specifications for wireless communication.
- MAC issues in WLANs include how to coordinate the access of multiple devices to the shared wireless medium, how to avoid or resolve collisions, how to ensure fairness and efficiency, and how to protect the privacy and security of the transmitted data.
- IEEE 802.11 is the most widely used standard for WLANs, which has been revised and amended several times since its first publication in 1997. The latest version, IEEE 802.11-2020, incorporates the previous amendments and provides technical corrections and clarifications. IEEE 802.11 defines several PHY variants that operate in different frequency bands and offer different data rates and ranges, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax. IEEE 802.11 also defines several MAC enhancements that address specific issues or scenarios, such as 802.11e for quality of service, 802.11i for security, 802.11k for radio resource management, 802.11r for fast roaming, and 802.11s for mesh networking.
- Bluetooth is another wireless technology that enables short-range communication between devices, such as smartphones, headphones, keyboards, mice, and speakers. Bluetooth uses a frequency-hopping spread spectrum (FHSS) technique to avoid interference and provide security. Bluetooth also defines a set of protocols and profiles that specify how different devices can interact and exchange data. The latest version of Bluetooth is Bluetooth 5.2, which was released in 2019 and offers improved performance, reliability, and power efficiency.
- Wireless is a general term that encompasses any type of wireless communication, such as WLAN, Bluetooth, cellular, satellite, radio, and optical. Wireless networks have many advantages over wired networks, such as mobility, flexibility, scalability, and cost-effectiveness. However, wireless networks also face many challenges, such as interference, noise, attenuation, multipath, security, and power consumption. Therefore, wireless networks require careful design, implementation, and management to ensure their quality and reliability.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of multiple access protocols for wireless networking.

### Multiple Access Protocols

- Multiple access protocols are used to coordinate the access of multiple nodes or users to a shared network channel, such as a wireless LAN or a satellite network.
- Multiple access protocols can be classified into three categories: random access, controlled access, and channelization.
- Random access protocols allow nodes to transmit data whenever they have data to send, without any coordination with other nodes. However, this may result in collisions, where two or more nodes transmit data at the same time and interfere with each other. Examples of random access protocols are ALOHA, CSMA, CSMA/CA, and CSMA/CD.
- Controlled access protocols require nodes to obtain permission from a central controller or from other nodes before transmitting data. This reduces the chances of collisions, but may introduce delays and overhead. Examples of controlled access protocols are polling, token passing, and reservation.
- Channelization protocols divide the available bandwidth of the channel into smaller subchannels, and assign each subchannel to a node or a group of nodes. This prevents collisions, but may waste bandwidth if some subchannels are idle. Examples of channelization protocols are FDMA, TDMA, CDMA, and OFDMA.

### IEEE 802.11

- IEEE 802.11 is a family of standards that define the physical and MAC layers of wireless LANs. It is also known as Wi-Fi.
- IEEE 802.11 uses CSMA/CA as the main random access protocol for the MAC layer. CSMA/CA stands for carrier-sense multiple access with collision avoidance. It works as follows:
  - A node that wants to transmit data first senses the channel. If the channel is idle, it transmits the data. If the channel is busy, it waits for a random backoff time and then tries again.
  - To avoid collisions, the node also sends a short control frame called request to send (RTS) before transmitting the data. The RTS contains the duration of the data transmission and the address of the intended receiver.
  - The receiver responds with a clear to send (CTS) frame, which also contains the duration of the data transmission and the address of the sender.
  - The sender and the receiver then exchange the data and an acknowledgment (ACK) frame.
  - The RTS and CTS frames are used to reserve the channel and inform other nodes about the ongoing transmission. This is called virtual carrier sensing or network allocation vector (NAV).
  - The sender and the receiver also use physical carrier sensing to detect the presence of other signals on the channel.
- IEEE 802.11 also uses a distributed coordination function (DCF) to coordinate the access of multiple nodes to the channel. The DCF is based on CSMA/CA with RTS/CTS and NAV. It also uses a contention window (CW) to adjust the backoff time of the nodes according to the channel conditions.
- IEEE 802.11 has several variants that use different frequency bands, modulation schemes, and data rates. Some of the common variants are 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax.

### Bluetooth

- Bluetooth is a wireless technology that enables short-range communication between devices such as mobile phones, laptops, headphones, speakers, printers, etc.
- Bluetooth uses a channelization protocol called frequency-hopping spread spectrum (FHSS) to divide the channel into 79 subchannels, each with a bandwidth of 1 MHz. The subchannels are used in a pseudo-random sequence that changes every 625 microseconds. This reduces the interference and increases the security of the communication.
- Bluetooth also uses a controlled access protocol called time division multiple access (TDMA) to divide the time into slots of 625 microseconds. Each slot can be used by a different device to transmit data. The devices are synchronized by a master device that establishes a connection with one or more slave devices. The master and the slave devices form a network called a piconet. Multiple piconets can be interconnected to form a scatternet.



### TCP over wireless

- Transmission Control Protocol (TCP) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP cannot distinguish between congestion losses and wireless losses and may unnecessarily reduce the sending rate, resulting in poor performance and low throughput.
- Therefore, TCP needs to be adapted or enhanced to cope with the challenges of wireless networks, such as high delays, high error rates, and frequent handoffs.
- Several mechanisms have been proposed to improve the performance of TCP over wireless networks, such as:
  - Split-connection: The TCP connection is split into two sub-connections at the base station, one over the wired network and one over the wireless network. The base station acts as a proxy and handles the wireless losses locally, while hiding them from the end hosts. This way, TCP can maintain its end-to-end semantics and avoid unnecessary congestion control. However, this mechanism requires modifications at the base station and may introduce additional delays and overheads.
  - Link-layer retransmission: The link layer provides local error recovery by retransmitting lost or corrupted packets over the wireless link. This reduces the number of losses seen by TCP and improves the throughput. However, this mechanism may also increase the delay and the delay variation, which can affect TCP's timeout and retransmission mechanisms. Moreover, link-layer retransmission may not be effective in the presence of high bit error rates or frequent handoffs.
  - TCP-aware link layer: The link layer provides feedback to TCP about the wireless link conditions, such as the error rate, the delay, and the available bandwidth. This allows TCP to adjust its sending rate and window size accordingly and avoid unnecessary congestion control. However, this mechanism requires coordination between the link layer and the transport layer, which may not be feasible in some scenarios. Moreover, TCP-aware link layer may not be compatible with existing TCP implementations and may violate the layering principle.
  - TCP sender adaptation: The TCP sender adapts its behavior based on the feedback from the receiver or the network. For example, the receiver can send explicit notifications to the sender about the wireless losses, such as selective acknowledgments (SACKs) or explicit loss notifications (ELNs). The sender can then ignore these losses and avoid reducing the sending rate. Alternatively, the network can mark the packets that experience wireless losses, such as using explicit congestion notification (ECN) or wireless ECN (WECN). The sender can then differentiate between congestion losses and wireless losses and adjust the sending rate accordingly. However, these mechanisms require modifications at the receiver or the network, which may not be available or reliable in some scenarios. Moreover, these mechanisms may introduce additional overheads and complexity.
  - TCP receiver adaptation: The TCP receiver adapts its behavior based on the wireless link conditions, such as the error rate, the delay, and the available bandwidth. For example, the receiver can delay the acknowledgments (ACKs) to the sender to reduce the number of losses seen by TCP and improve the throughput. Alternatively, the receiver can increase the advertised window size to the sender to allow more packets to be sent and fill the wireless link. However, these mechanisms may also increase the delay and the delay variation, which can affect TCP's timeout and retransmission mechanisms. Moreover, these mechanisms may not be compatible with existing TCP implementations and may violate the TCP flow control principle.



### Wireless applications

Wireless applications are the software programs that run on devices that use wireless communication technologies, such as cellular phones, wireless LANs, Bluetooth, etc. Wireless applications enable users to access information and services without being constrained by wires or cables. Some of the benefits of wireless applications are:

- Mobility: Users can access wireless applications from anywhere within the coverage area of the wireless network, and move freely without losing connectivity.
- Convenience: Users do not need to plug in or unplug wires or cables to use wireless applications, which saves time and hassle.
- Cost-effectiveness: Wireless applications can reduce the cost of installation and maintenance of wired networks, and also save energy and resources.
- Reliability: Wireless applications can avoid the errors and failures caused by faulty or damaged wires or cables, and also provide backup or alternative communication channels in case of emergencies.

Some of the challenges of wireless applications are:

- Security: Wireless applications are vulnerable to eavesdropping, interception, spoofing, and other attacks by malicious users or hackers, who can exploit the open nature of wireless communication.
- Interference: Wireless applications can suffer from interference from other wireless devices or sources of electromagnetic radiation, which can degrade the quality and performance of wireless communication.
- Compatibility: Wireless applications need to comply with various standards and protocols to ensure interoperability and compatibility with different wireless devices and networks.
- Scalability: Wireless applications need to adapt to the dynamic and heterogeneous nature of wireless networks, which can vary in size, topology, bandwidth, and availability.

Some of the examples of wireless applications are:

- Cellular phones: Cellular phones provide connectivity for portable and mobile applications, both personal and business. Cellular phones can support voice, text, multimedia, and internet services, and also enable location-based and context-aware applications.
- Wireless LANs: Wireless LANs enable users to access a network without requiring a wired connection. Wireless LANs can support data, voice, and video applications, and also enable collaboration and sharing among users.
- Bluetooth: Bluetooth is a short-range wireless technology that enables wireless communication between devices, such as computers, keyboards, mice, printers, headphones, speakers, etc. Bluetooth can support data and voice applications, and also enable personal area networks and device discovery.
- Wireless sensor networks: Wireless sensor networks are networks of small, low-power, and self-organizing devices that can sense, process, and communicate data about the physical environment. Wireless sensor networks can support applications such as environmental monitoring, health care, smart homes, agriculture, etc.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on data broadcasting for wireless networking.

### Data Broadcasting

- Data broadcasting is a technique for delivering data to multiple clients simultaneously using a single transmission channel.
- Data broadcasting is suitable for wireless networks, where the bandwidth is limited and the clients are mobile.
- Data broadcasting can improve the scalability, efficiency, and reliability of data delivery in wireless networks.
- Data broadcasting can be classified into two types: push-based and pull-based.
  - Push-based broadcasting: the server periodically broadcasts data items according to a predefined schedule, and the clients tune in to receive the data they are interested in.
  - Pull-based broadcasting: the clients send requests to the server, and the server broadcasts data items in response to the requests, possibly with some caching or replication strategies.
- Data broadcasting can be applied to various wireless network scenarios, such as cellular networks, wireless LANs, satellite networks, and sensor networks.
- Data broadcasting can also support multimedia applications, such as audio and video streaming, by using adaptive techniques to adjust the quality and rate of the broadcast data according to the network conditions and client preferences.

### Wireless Networking

- Wireless networking is a computer network that uses radio frequency (RF) connections between nodes in the network, instead of cables or wires.
- Wireless networking is a popular solution for homes, businesses, and telecommunications networks, as it offers mobility, flexibility, and convenience.
- Wireless networking can be classified into three types: infrastructure-based, ad hoc, and mesh.
  - Infrastructure-based wireless networking: the network consists of wireless devices that communicate with a central base station or access point, which is connected to a wired network or the Internet.
  - Ad hoc wireless networking: the network consists of wireless devices that communicate directly with each other, without any central coordination or infrastructure.
  - Mesh wireless networking: the network consists of wireless devices that communicate with each other and relay data for other devices, forming a dynamic and self-organizing network topology.
- Wireless networking can use various standards and protocols, such as IEEE 802.11, Bluetooth, WiMAX, LTE, and 5G, to provide different levels of performance, security, and compatibility.



### Mobile IP

Mobile IP is a communication protocol that allows mobile devices to move from one network to another while maintaining the same permanent IP address . Mobile IP is based on IP and can support any media that can support IP. Mobile IP is designed to support seamless and continuous Internet connectivity for mobile users.

Some of the features and benefits of Mobile IP are:

- It enables mobility across different networks without changing the IP address or breaking the ongoing connections.
- It preserves the location privacy of the mobile device by hiding its actual IP address from the applications and servers.
- It supports both IPv4 and IPv6 protocols, with some differences in the implementation and operation.
- It uses two types of agents: home agent and foreign agent, to facilitate the communication between the mobile device and the correspondent node.
- It uses three types of messages: registration request, registration reply, and agent advertisement, to perform the registration and discovery processes.
- It uses two types of addresses: home address and care-of address, to identify the mobile device and its current location.

To find the IP address of a mobile device, such as an Android or iPhone, the following steps can be followed:

- For Android devices, go to Settings > Network & Internet > Wi-Fi. Tap on the network name that the device is connected to. Tap on the gear icon next to the network name. Tap on Advanced. The IP address will be displayed under the IP settings section.
- For iPhone devices, go to Settings > Wi-Fi. Tap on the network name that the device is connected to. The IP address will be displayed under the IP Address section.



### WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer is of most interest to content developers because it contains among other things, device specifications, scripting languages, and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems. The application layer also includes the Wireless Application Environment (WAE), which provides a framework for developing and delivering applications and services to wireless devices.
  - Session Layer: This layer provides a reliable session service between applications, based on a request-response paradigm. The session layer uses the Wireless Session Protocol (WSP), which is a binary-encoded version of the HTTP protocol, optimized for low-bandwidth and high-latency networks.
  - Transaction Layer: This layer provides a lightweight transaction service on top of the session layer, based on a two-phase commit protocol. The transaction layer uses the Wireless Transaction Protocol (WTP), which supports reliable and unreliable datagram service, and user datagram service.
  - Security Layer: This layer provides data integrity and privacy services for the wireless network, based on encryption and authentication mechanisms. The security layer uses the Wireless Transport Layer Security (WTLS), which is a wireless-optimized version of the TLS protocol, derived from the SSL protocol.
  - Transport Layer: This layer provides a datagram service and a connection-oriented service for the wireless network, based on the characteristics of the underlying bearer network. The transport layer uses the Wireless Datagram Protocol (WDP), which is an adaptation layer that allows WAP to operate over various types of wireless networks, such as GSM, CDMA, CDPD, SMS, and GPRS.
- The WAP architecture also includes several components, each serving a specific function. These components include:
  - WAP Client: This is the wireless device that runs a micro-browser and interacts with the WAP gateway. The WAP client supports the WAP protocol stack and the WAE components, such as WML, WMLScript, and WBMP.
  - WAP Gateway: This is the intermediary between the wireless network and the internet. The WAP gateway performs several functions, such as protocol translation, content encoding and decoding, security services, and caching.
  - WAP Server: This is the web server that hosts the WAP content and applications. The WAP server supports the WAP protocol stack and the WAE components, such as WML, WMLScript, and WBMP.
  - WAP Proxy: This is an optional component that acts as a proxy between the WAP gateway and the WAP server. The WAP proxy can perform functions such as content filtering, adaptation, and compression.
- The WAP architecture is illustrated in the following diagram:

WAP Architecture Diagram



### Protocol Stack

A protocol stack is an implementation of a set of communication protocols that work together to provide network services. A protocol stack can be composed of different layers, each of which performs a specific function and communicates with the adjacent layers through well-defined interfaces. A protocol stack can be used to hide the complexity of the wireless interface and present a software interface that resembles that of a wired connection.

Some examples of protocol stacks for wireless networking are:

- Wireless Application Protocol (WAP): This is a protocol stack that enables wireless devices to access web content and services. WAP consists of four layers: application, session, transaction, and transport. WAP uses the Internet Protocol (IP) for addressing and routing purposes, and supports various wireless data formats, such as Wireless Markup Language (WML) and Wireless Bitmap (WBMP).
- IEEE 802.11: This is a protocol stack that defines the standards for wireless local area networks (WLANs). IEEE 802.11 consists of two layers: physical and data link. The physical layer specifies the frequency, modulation, and coding schemes for wireless transmission, while the data link layer specifies the medium access control (MAC) and logical link control (LLC) protocols for wireless communication. IEEE 802.11 supports various physical layer standards, such as 802.11a, 802.11b, 802.11g, and 802.11n, each of which offers different data rates and ranges.
- Bluetooth: This is a protocol stack that enables short-range wireless communication between devices, such as mobile phones, headsets, keyboards, and mice. Bluetooth consists of four layers: core, cable replacement, telephony control, and adopted. The core layer defines the basic protocols for Bluetooth communication, such as radio, baseband, link manager, and host controller interface. The cable replacement layer defines the protocols for emulating serial and parallel ports over Bluetooth, such as RFCOMM and L2CAP. The telephony control layer defines the protocols for supporting voice and data services over Bluetooth, such as telephony control specification binary (TCS BIN) and service discovery protocol (SDP). The adopted layer defines the protocols that are adopted from other standards, such as object exchange (OBEX) and network access point (NAP).

The following diagram shows a simplified representation of the protocol stacks for WAP, IEEE 802.11, and Bluetooth:

```
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|     WAP        |    IEEE 802.11  |    Bluetooth    |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Application    |  Application    |  Application    |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|   Session       |                 |  Adopted        |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Transaction    |                 |  Telephony      |
|                 |                 |  Control        |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Transport      |                 |  Cable          |
|                 |                 |  Replacement    |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |  Data Link      |  Core           |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|                 |  Physical       |  Physical       |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
```



### Application Environment for Wireless Networking

- The application environment for wireless networking is the set of protocols, standards, and technologies that enable wireless devices to access web-based services and applications.
- One of the most widely used application environments for wireless networking is the **Wireless Application Protocol (WAP)**, which is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- The main component of WAP is the **Wireless Application Environment (WAE)**, which provides an architecture for communication between wireless devices and web servers. The WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and characteristics of wireless networks and devices, such as low bandwidth, high latency, small screen size, limited input capabilities, and diverse device capabilities .
- The WAE consists of several elements, such as:
  - **Wireless Markup Language (WML)**, which is a markup language similar to HTML, but optimized for wireless devices. WML allows the creation of web pages that can be displayed on various wireless devices, regardless of their screen size, color depth, or graphics support. WML also supports user interaction, navigation, and scripting .
  - **Wireless Markup Language Script (WMLScript)**, which is a scripting language similar to JavaScript, but optimized for wireless devices. WMLScript allows the execution of client-side logic and validation, as well as the access to device-specific features, such as phone calls, messages, and contacts .
  - **Wireless Telephony Application (WTA)**, which is a set of extensions to WML and WMLScript that enable the integration of telephony services, such as call control, voice mail, and caller identification, into wireless applications .
  - **Wireless Datagram Protocol (WDP)**, which is a transport layer protocol that provides a common interface for WAP applications to communicate with different underlying network technologies, such as GSM, CDMA, or TCP/IP .
  - **Wireless Session Protocol (WSP)**, which is a session layer protocol that provides reliable and secure communication between wireless devices and web servers. WSP supports features such as session management, caching, content encoding, and push services .
  - **Wireless Transaction Protocol (WTP)**, which is a transaction layer protocol that provides efficient and reliable request-response services for WAP applications. WTP supports features such as segmentation and reassembly, retransmission, and acknowledgment .
  - **Wireless Application Environment Gateway (WAE Gateway)**, which is a server-side component that acts as an intermediary between wireless devices and web servers. The WAE Gateway performs functions such as protocol translation, content adaptation, and security .
- The WAE provides a vendor-neutral application architecture based on internet standards. The WAE specifications outline an application programming model that supports browsing, scripting, and extensions that allow cellular network operators to offer network services within WAP.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing:

- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area using radio waves. WLANs can provide mobility, flexibility, and scalability for users and applications. WLANs can be classified into two types: infrastructure and ad hoc. Infrastructure WLANs use a base station or access point to coordinate the communication among the devices, while ad hoc WLANs do not require any central coordination and use peer-to-peer communication.
- IEEE 802.11 is the standard that defines the technologies and protocols for WLANs. It specifies the Medium Access Control (MAC) and Physical Layer (PHY) aspects of the wireless communication. The MAC layer is responsible for controlling the access to the shared wireless medium and ensuring reliable data delivery. The PHY layer is responsible for encoding, modulating, and transmitting the data over the radio channel .
- Blue Tooth is a wireless technology that enables short-range communication among devices such as mobile phones, laptops, headsets, printers, etc. Blue Tooth uses a frequency-hopping spread spectrum technique to avoid interference and provide security. Blue Tooth also defines a protocol stack that covers the MAC, PHY, and higher layers of the wireless communication. Blue Tooth supports both point-to-point and point-to-multipoint connections.
- Wireless multiple access protocols are the methods that allow multiple devices to share the wireless medium without causing collisions or interference. Some of the common wireless multiple access protocols are Frequency Division Multiple Access (FDMA), Time Division Multiple Access (TDMA), Code Division Multiple Access (CDMA), and Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA). Each protocol has its own advantages and disadvantages in terms of bandwidth efficiency, latency, fairness, and complexity.
- TCP over wireless is the challenge of adapting the Transmission Control Protocol (TCP) to the wireless environment, which is characterized by high bit error rates, variable delays, and frequent disconnections. TCP is designed for reliable and ordered delivery of data over wired networks, but it may perform poorly over wireless networks due to its congestion control and error recovery mechanisms. Some of the solutions to improve TCP over wireless are link layer retransmission, split TCP, TCP with selective acknowledgment, and TCP with explicit congestion notification.
- Wireless applications are the software programs that run on wireless devices and use the wireless network to provide various services and functions. Some of the examples of wireless applications are web browsing, email, instant messaging, social networking, online gaming, video streaming, etc. Wireless applications require special design considerations to cope with the limitations and challenges of the wireless environment, such as low bandwidth, high latency, limited battery life, and security risks.
- Data broadcasting is a technique that allows a wireless network to transmit data to multiple devices simultaneously, without requiring any feedback or acknowledgment from the receivers. Data broadcasting can improve the network efficiency and scalability, as well as reduce the power consumption and latency of the devices. Data broadcasting can be used for applications such as news, weather, traffic, advertisements, etc. Data broadcasting can be implemented using various methods, such as push-based, pull-based, or hybrid.
- Mobile IP is a protocol that enables a mobile device to maintain its network connectivity and IP address while moving across different networks. Mobile IP allows the mobile device to have a permanent home address and a temporary care-of address, which are registered with a home agent and a foreign agent, respectively. Mobile IP uses a tunneling mechanism to route the packets from the home network to the current network of the mobile device.
- WAP (Wireless Application Protocol) is a standard that defines a framework for developing and delivering wireless applications over various wireless networks and devices. WAP consists of four layers: the Wireless Application Environment (WAE), the Wireless Session Protocol (WSP), the Wireless Transaction Protocol (WTP), and the Wireless Transport Layer Security (WTLS). WAP also defines a markup language called Wireless Markup Language (WML), which is used to create web pages for wireless devices .



## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

### Data management issues

- Data management technology that can support easy data access from and to mobile devices is among the main concerns in mobile information systems .
- Mobile computing may be considered a variation of distributed computing, where mobile devices are connected to fixed servers or databases via wireless networks .
- Some of the issues that arise in data management of mobile databases are:
  - Mobile database design: The frequent disconnection and reconnection of mobile devices pose challenges for handling queries and resolving global names.
  - Security: The data on mobile devices is more vulnerable to theft, loss, or damage than the data on fixed locations. Therefore, encryption, authentication, and backup mechanisms are needed to protect the data.
  - Data distribution and replication: The uneven and dynamic network bandwidth and availability require efficient strategies for distributing and replicating data among mobile and fixed nodes.
  - Data synchronization and reconciliation: The data updates on mobile devices need to be synchronized and reconciled with the data on fixed servers or databases, taking into account the possible conflicts and inconsistencies.
  - Data caching and prefetching: The limited battery power and storage capacity of mobile devices require effective techniques for caching and prefetching data to reduce the communication cost and improve the data availability.
  - Data broadcasting and dissemination: The broadcast nature of wireless networks can be exploited to disseminate data to multiple mobile devices simultaneously, reducing the network congestion and server load.
  - Data compression and transformation: The data transmitted over wireless networks can be compressed and transformed to reduce the transmission time and energy consumption, as well as to adapt to the device capabilities and user preferences.
  - Data querying and processing: The query processing and optimization techniques for mobile databases need to consider the network and device constraints, as well as the user context and location.

### Data replication for mobile computers

- Data replication is the process of creating and maintaining multiple copies of the same data on different nodes in a distributed system.
- Data replication for mobile computers aims to improve the data availability, reliability, and performance for mobile users, as well as to reduce the network traffic and server load.
- Data replication for mobile computers faces several challenges, such as:
  - Replication granularity: The choice of the unit of replication (e.g., file, record, page, object) affects the replication overhead and consistency.
  - Replication placement: The decision of where to place the replicas (e.g., on mobile devices, on fixed servers, on intermediate nodes) affects the replication accessibility and cost.
  - Replication strategy: The policy of when and how to create, update, and delete replicas (e.g., eager, lazy, hybrid) affects the replication freshness and consistency.
  - Replication consistency: The degree of agreement among the replicas (e.g., strict, causal, eventual) affects the replication correctness and complexity.
  - Replication management: The mechanisms for coordinating and controlling the replication activities (e.g., centralized, distributed, hierarchical) affect the replication scalability and robustness.

### Adaptive clustering for mobile

- Adaptive clustering is a technique for organizing mobile nodes into groups or clusters based on their proximity, connectivity, or similarity.
- Adaptive clustering for mobile aims to facilitate the data management, communication, and coordination among mobile nodes, as well as to reduce the network overhead and complexity.
- Adaptive clustering for mobile faces several challenges, such as:
  - Cluster formation: The criteria and algorithms for forming clusters (e.g., based on location, distance, mobility, or interest) affect the cluster quality and stability.
  - Cluster maintenance: The methods and protocols for maintaining clusters (e.g., by electing cluster heads, updating cluster memberships, or merging and splitting clusters) affect the cluster efficiency and adaptability.
  - Cluster utilization: The applications and services that can benefit from clustering (e.g., data dissemination, routing, location management, or resource allocation) affect the cluster usefulness and performance.



### Wireless Networks

Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables. Wireless networks can enable mobile computing, which is the ability to access and process data from anywhere and anytime using portable devices.

Some of the topics related to wireless networks and mobile computing are:

- Data management issues
- Data replication for mobile computers
- Adaptive clustering for mobile wireless networks

#### Data management issues

Data management is the process of storing, organizing, and manipulating data in a way that meets the needs of users and applications. Data management issues are the challenges and problems that arise when dealing with data in wireless networks and mobile computing environments.

Some of the data management issues are:

- Data availability: How to ensure that data is accessible to users and applications even when there are network disconnections, low bandwidth, or high latency.
- Data consistency: How to maintain the correctness and integrity of data across multiple copies or versions that may exist in different locations or devices.
- Data security: How to protect data from unauthorized access, modification, or disclosure, especially when data is transmitted over wireless channels or stored on mobile devices that may be lost or stolen.
- Data adaptation: How to adjust data to suit the preferences, capabilities, and resources of different users and devices, such as reducing data size, quality, or complexity to save bandwidth, storage, or battery power.

#### Data replication for mobile computers

Data replication is the process of creating and maintaining multiple copies or replicas of data in different locations or devices. Data replication can improve data availability, performance, and fault tolerance in wireless networks and mobile computing environments.

Some of the benefits of data replication are:

- Data can be accessed locally without relying on the network, which can reduce communication costs, latency, and bandwidth consumption.
- Data can be updated or queried in parallel by multiple users or applications, which can increase concurrency and throughput.
- Data can be recovered or restored from other replicas in case of network failures, device failures, or data losses.

Some of the challenges of data replication are:

- Data consistency: How to ensure that all replicas of data are synchronized and reflect the same state of the data, especially when there are concurrent updates or queries from different users or applications.
- Data allocation: How to decide where, when, and how many replicas of data should be created and maintained, based on factors such as data popularity, access frequency, network conditions, device resources, and user preferences.
- Data synchronization: How to exchange and merge data updates or changes among different replicas, while minimizing communication overhead, data conflicts, and data losses.

#### Adaptive clustering for mobile wireless networks

Adaptive clustering is a technique for organizing nodes in a mobile wireless network into groups or clusters, based on criteria such as node proximity, node mobility, node connectivity, node capacity, or node role. Adaptive clustering can improve network performance, scalability, and reliability in mobile wireless networks.

Some of the advantages of adaptive clustering are:

- Spatial reuse of bandwidth: By dividing the network into clusters, the same frequency or code can be reused by different clusters that are sufficiently far apart, which can increase the network capacity and reduce interference.
- Controlled access to resources: By assigning a leader or a coordinator to each cluster, the access to the shared resources such as bandwidth, channel, or power can be regulated and coordinated among the cluster members, which can reduce contention and collision.
- Robustness to topology changes: By adapting the cluster formation and maintenance to the dynamic changes in the network topology caused by node motion, node failure, or node insertion/removal, the network can maintain its connectivity and functionality, while avoiding frequent reconfiguration and overhead.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the topic of file system for mobile computing.

### File system for mobile computing

- A file system is a software component that manages the storage, organization, access, and sharing of files on a computer system.
- A file system for mobile computing is a file system that supports the mobility of both users and devices, and adapts to the challenges of wireless and mobile environments, such as network disconnection, bandwidth variation, and data consistency.
- Some of the design issues for a file system for mobile computing are:

  - Location transparency: the ability to access files without knowing their physical location or network address.
  - User mobility: the ability to access files from different devices and locations, and to move files across devices and networks.
  - Compatibility: the ability to interoperate with existing file system interfaces and applications, and to support different operating systems and platforms.
  - Performance: the ability to provide fast and reliable file access, and to minimize the network traffic and resource consumption.
  - Replication: the ability to create and maintain multiple copies of files on different servers or devices, and to synchronize them when needed.
  - Consistency: the ability to ensure that the replicated files are identical or equivalent, and to handle conflicts and updates.
  - Security: the ability to protect the files from unauthorized access, modification, or disclosure, and to provide authentication, encryption, and access control mechanisms.
  - Fault tolerance: the ability to cope with network failures, device failures, or server failures, and to recover from errors or crashes.

- Some of the design options for a file system for mobile computing are:

  - Client-server model: the file system is centralized on one or more servers, and the clients access the files through the network. This model provides location transparency, compatibility, and security, but may suffer from low performance, high network traffic, and poor fault tolerance.
  - Peer-to-peer model: the file system is distributed among the devices, and the devices cooperate to store, access, and share the files. This model provides performance, replication, and fault tolerance, but may have issues with location transparency, compatibility, consistency, and security.
  - Hybrid model: the file system combines the features of both client-server and peer-to-peer models, and uses different strategies depending on the network conditions and user preferences. This model aims to provide the best of both worlds, but may increase the complexity and overhead of the file system.

- One example of a file system for mobile computing is Coda, which is a distributed file system that supports disconnected operation, server replication, security, and network bandwidth adaptation. Coda is based on the client-server model, but uses client-side persistent caching to improve performance and enable offline access. Coda also uses server replication to enhance availability and fault tolerance, and uses a security model for authentication, encryption, and access control. Coda adapts to the network bandwidth by using different levels of consistency, such as strong, weak, or optimistic, and by resolving conflicts through user intervention or automatic reconciliation. Coda is compatible with existing file system interfaces and applications, and supports different operating systems and platforms. Coda is freely available under the GPL license.



### Disconnected operations

- Disconnected operations are a mode of operation in mobile computing that allows users to execute applications when the network is unavailable or unreliable .
- Disconnected operations can be voluntary or involuntary, depending on the user's choice or the network conditions .
- Disconnected operations require mechanisms to handle data consistency, synchronization, and recovery when the network is reconnected  .
- Disconnected operations can benefit from techniques such as data replication, caching, hoarding, prefetching, and reconciliation  .
- Disconnected operations can improve the availability, performance, and energy efficiency of mobile applications  .



# Unit 4 - Mobile Agents Computing, Security and Fault Tolerance, Transaction Processing in Mobile Computing

## Mobile Agents Computing

- A mobile agent is a composition of computer software and data that is able to migrate (move) from one computer to another autonomously and continue its execution on the destination computer .
- A mobile agent is a specific form of mobile code, within the field of code mobility. However, in contrast to the remote evaluation and code on demand programming paradigms, mobile agents are active in that they can choose to migrate between computers at any time during their execution.
- The mobile agents are autonomous with intelligence, social ability, learning, and the most important feature is their mobility. They are independent in nature, self-driven and do not require a corresponding node for communication. They can work efficiently even after the user gets disconnected from the network.
- Mobile agents can be used for various applications in mobile computing, such as information retrieval, network management, load balancing, distributed processing, electronic commerce, etc.

## Security and Fault Tolerance

- Security and fault tolerance are two major challenges in mobile agent systems, as mobile agents are exposed to various threats and failures during their migration and execution.
- Security threats can be classified into two categories: threats to the mobile agent and threats from the mobile agent. The former includes attacks on the agent's integrity, confidentiality, availability, and authentication, while the latter includes attacks on the host's resources, data, and services.
- Fault tolerance refers to the ability of a mobile agent system to cope with errors and failures that may occur during the agent's lifecycle, such as network failures, host failures, agent failures, etc.
- Various techniques and mechanisms have been proposed to enhance the security and fault tolerance of mobile agent systems, such as encryption, digital signatures, authentication protocols, access control, sandboxing, code obfuscation, tamper-proofing, checkpointing, replication, recovery, etc.

## Transaction Processing in Mobile Computing

- Transaction processing in mobile computing refers to the execution of transactions that involve mobile devices, such as smartphones, tablets, laptops, etc., and mobile networks, such as cellular networks, wireless LANs, etc.
- Transaction processing in mobile computing faces several challenges, such as limited resources, unreliable communication, frequent disconnections, mobility, heterogeneity, etc.
- To overcome these challenges, various models and protocols have been developed for transaction processing in mobile computing, such as mobile transaction model, kangaroo transaction model, broadcast disk model, adaptive transaction model, etc.
- These models and protocols aim to provide the properties of atomicity, consistency, isolation, and durability (ACID) for mobile transactions, while also considering the issues of concurrency control, deadlock detection, commit processing, recovery, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of environment for mobile agents:

### Environment for Mobile Agents

- A mobile agent is a software entity that can migrate from one node to another in a network, carrying its code, data and execution state .
- A mobile agent can perform tasks on behalf of its owner, such as information retrieval, data processing, network management, etc.
- A mobile agent can adapt to the environment, switch among the positions, and work autonomously and cooperatively.
- A mobile agent environment consists of the following components:
  - Agent platform: The computational infrastructure that provides the services and resources for creating, executing, migrating and communicating mobile agents.
  - Agent transport: The mechanism that enables the mobility of agents across different platforms and networks.
  - Agent communication: The protocol that allows the exchange of messages and data among agents, users and systems.
  - Agent security: The measures that protect the agents and the platforms from malicious attacks and unauthorized access.
- A mobile agent environment can be classified into two types:
  - Homogeneous: The platforms share the same operating system, programming language and agent model.
  - Heterogeneous: The platforms differ in one or more aspects and require interoperability and compatibility among agents.
- A mobile agent environment can provide various benefits for mobile computing, such as :
  - Reducing network traffic and latency by moving the computation closer to the data sources and destinations.
  - Enhancing scalability and reliability by distributing the workload and tolerating failures and disconnections.
  - Supporting dynamic and adaptive behavior by exploiting the local resources and context of each platform.
  - Enabling user-friendly and personalized services by customizing the agents according to the user preferences and needs.



## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They consist of mobile nodes that communicate with each other over wireless links.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved by using GPS, signal strength, angle of arrival, or other techniques.
- MAC (Medium Access Control) issues refer to the challenges of coordinating the access of multiple nodes to the shared wireless medium, avoiding collisions, and maximizing throughput. Some of the MAC protocols for ad hoc networks are CSMA/CA, MACA, MACAW, FAMA, and IEEE 802.11.
- Routing protocols are algorithms that enable the nodes in an ad hoc network to discover and maintain routes to each other. Routing protocols can be classified into proactive, reactive, or hybrid, depending on whether they maintain routes constantly, on-demand, or both.
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks that uses link state information to compute the shortest paths between nodes. Each node periodically broadcasts its link state to all other nodes, and updates its routing table based on the received information. GSR suffers from high overhead and scalability issues.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of Destination sequenced distance vector routing (DSDV) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing scheme for ad hoc mobile networks based on the Bellman–Ford algorithm.
- It was developed by C. Perkins and P. Bhagwat in 1994.
- The main contribution of the algorithm was to solve the routing loop problem.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- Using the sequence number, the mobile nodes can distinguish stale route information from the new and thus prevent the formation of routing loops.
- DSDV provides only one route for a source/destination pair.
- DSDV requires each node to periodically broadcast routing updates.
- DSDV uses bidirectional links.
- DSDV has two types of routing updates: full dump and incremental.
- Full dump updates contain all the routing information of a node and are sent infrequently.
- Incremental updates contain only the changed routing information and are sent more frequently.
- DSDV reduces the number of control messages by using triggered updates, which are sent only when there is a significant change in the topology.
- DSDV also uses a settling time, which is the time before a node advertises a route update, to reduce the network overhead.
- DSDV is suitable for small and moderately sized networks with low mobility.
- DSDV suffers from the problems of high overhead, slow convergence, and wastage of bandwidth.



### Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that forms a route when a source node requests one .
- It uses source routing instead of relying on the routing table at each intermediate node .
- Source routing means that the source node specifies the complete sequence of nodes to the destination in the packet header .
- DSR consists of two main mechanisms: route discovery and route maintenance .
- Route discovery is the process of finding a route from the source to the destination when there is no cached route available .
- Route discovery involves sending a route request packet that is flooded through the network until it reaches the destination or a node with a cached route .
- The route request packet contains the source and destination addresses, a unique request ID, and a list of nodes visited so far .
- The destination or the intermediate node with a cached route sends a route reply packet back to the source along the reverse path of the route request .
- The route reply packet contains the source and destination addresses, a unique request ID, and a list of nodes forming the route .
- The source node caches the route and uses it to send data packets to the destination .
- Route maintenance is the process of detecting and repairing link failures along the route .
- Route maintenance involves sending route error packets when a node detects a link failure or receives a packet with an unknown destination .
- The route error packet contains the source and destination addresses, the broken link, and the list of nodes forming the route .
- The node that receives the route error packet removes the broken link from its cache and propagates the route error packet to the source node .
- The source node initiates a new route discovery if it still needs to communicate with the destination .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages:
  - It reduces the overhead of periodic route updates and table maintenance .
  - It allows multiple routes to be cached and used for load balancing and fault tolerance .
  - It supports asymmetric and unidirectional links .
- Disadvantages:
  - It increases the packet header size due to source routing .
  - It may cause stale routes to be cached and used due to mobility and topology changes .
  - It may suffer from network congestion and collisions due to route request flooding .

: Dynamic Source Routing - Wikipedia
: Dynamic Source Routing - Wikipedia
: Dynamic Source Routing Protocol - Carnegie Mellon University



### Ad Hoc on demand distance vector routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is a loop-free routing protocol that uses sequence numbers to ensure freshness of routes .
- AODV uses three types of control messages: route request (RREQ), route reply (RREP) and route error (RERR)  .
- AODV operates as follows   :
  - When a source node wants to send a packet to a destination node, it checks its routing table for a valid route. If no route is found, it broadcasts a RREQ message to its neighbors.
  - The RREQ message contains the source and destination addresses, the source and destination sequence numbers, the broadcast ID and the hop count. The broadcast ID and the source address uniquely identify a RREQ message.
  - Each intermediate node that receives the RREQ message updates its routing table with a reverse route to the source node and forwards the RREQ message to its neighbors, unless it has a valid route to the destination node with a higher sequence number than the one in the RREQ message.
  - When the RREQ message reaches the destination node or an intermediate node with a valid route to the destination node, it sends a RREP message back to the source node along the reverse route. The RREP message contains the destination and source addresses, the destination and source sequence numbers, the hop count and the lifetime of the route.
  - Each intermediate node that receives the RREP message updates its routing table with a forward route to the destination node and forwards the RREP message to the next hop towards the source node.
  - When the source node receives the RREP message, it establishes a route to the destination node and starts sending data packets.
  - If a link break occurs in the route, the upstream node of the broken link sends a RERR message to the source node, indicating the unreachable destinations. The RERR message contains the source and destination addresses, the destination sequence number and a list of unreachable destinations.
  - The source node, upon receiving the RERR message, invalidates the route to the destination node and initiates a new route discovery process if needed.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the topic you requested:

### Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated, on-demand routing protocol for wireless mobile ad hoc networks  .
- TORA is based on the link reversal algorithm, which dynamically creates a directed acyclic graph (DAG) rooted at the destination node .
- TORA consists of three main phases: route creation, route maintenance, and route erasure .
- In route creation, the source node broadcasts a query packet containing the destination ID and a height variable. The height variable is used to assign a logical level to each node in the DAG. The nodes that receive the query packet update their height and propagate the query until it reaches the destination or a node that has a route to the destination .
- In route maintenance, the nodes monitor the status of their outgoing links and update their height accordingly. If a link failure occurs, the nodes that lose their last downstream link perform a local link reversal by increasing their height and broadcasting an update packet. This process may propagate to other nodes until a new DAG is formed or the route becomes invalid .
- In route erasure, the nodes that detect a network partition or a route failure broadcast a clear packet to erase all the invalid routes in the network. The clear packet contains the destination ID and the height of the sender. The nodes that receive the clear packet compare their height with the sender's height and erase their routes if they are lower or equal .
- TORA is an efficient, highly adaptive, and scalable routing protocol that can handle frequent topology changes and network partitions  .
- TORA can also support quality of service (QoS) components such as delay, bandwidth, and jitter by using a QoS routing extension (QoSR) that modifies the height variable to reflect the QoS metrics.



### QoS in Ad Hoc Networks

- Quality of service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc.  
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or centralized control.  
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes.    
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.    
- QoS in ad hoc networks can be classified into two categories: hard QoS and soft QoS. Hard QoS guarantees the QoS requirements of the applications with strict bounds, while soft QoS provides the QoS requirements with probabilistic bounds or best-effort service.    
- QoS in ad hoc networks can be supported by various mechanisms, such as QoS-aware routing protocols, QoS-aware MAC protocols, QoS-aware resource allocation schemes, QoS-aware admission control schemes, QoS-aware scheduling schemes, QoS-aware cross-layer optimization schemes, etc.    
- QoS in ad hoc networks is an active research area that aims to improve the performance, reliability, and efficiency of ad hoc networks and to meet the diverse QoS requirements of various applications, such as multimedia, real-time, mission-critical, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some applications of ad hoc networks for the notes of Unit 5:

- **Military battlefield**: Ad hoc networks can be used to establish communication among soldiers, vehicles, and headquarters without relying on fixed infrastructure or centralized control.
- **Vehicular ad hoc network (VANET)**: Ad hoc networks can be used to enable communication between vehicles for traffic management, safety, and entertainment. VANETs can also use artificial intelligence and ad hoc technologies to coordinate actions during accidents.
- **Smartphone ad hoc network (SPAN)**: Ad hoc networks can be created on smartphones using existing technologies like Wi-Fi and Bluetooth to enable peer-to-peer data exchange, social networking, and emergency services without depending on cellular networks or access points .
- **Wireless sensor network (WSN)**: Ad hoc networks can be used to connect a large number of sensor nodes that collect and process data from the environment. WSNs can be used for applications such as environmental monitoring, health care, agriculture, and smart homes.
- **Industrial and commercial applications**: Ad hoc networks can be used to support cooperative mobile data exchange among workers, customers, and devices in various domains such as manufacturing, retail, health care, and education.

