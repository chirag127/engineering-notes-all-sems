

## Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

- Mobile computing is the use of portable devices, such as smartphones, tablets, laptops, etc., that can access data and services over wireless networks, without being bound to a fixed location.
- Mobile computing enables users to communicate, work, learn, and entertain anytime and anywhere, using various applications and services.
- Mobile computing also poses some challenges and issues, such as:
  - Limited battery life and power consumption of mobile devices.
  - Limited bandwidth and network coverage of wireless networks.
  - Security and privacy of data and communication over wireless networks.
  - Heterogeneity and interoperability of mobile devices and wireless networks.
  - Mobility and location management of mobile devices and users.
  - Adaptability and scalability of mobile applications and services.
- Wireless telephony is the transmission of voice and data over wireless networks, using radio waves or electromagnetic signals.
- Wireless telephony can be classified into different generations, based on the technology and standards used:
  - First generation (1G): Analog cellular networks that used frequency division multiple access (FDMA) to allocate channels to users. Examples are AMPS, NMT, TACS, etc.
  - Second generation (2G): Digital cellular networks that used time division multiple access (TDMA) or code division multiple access (CDMA) to multiplex users. Examples are GSM, IS-95, D-AMPS, etc.
  - Third generation (3G): Digital cellular networks that used wideband CDMA (WCDMA) or CDMA2000 to provide higher data rates and multimedia services. Examples are UMTS, HSPA, EV-DO, etc.
  - Fourth generation (4G): Digital cellular networks that used orthogonal frequency division multiple access (OFDMA) or single carrier FDMA (SC-FDMA) to provide higher data rates and broadband services. Examples are LTE, WiMAX, etc.
  - Fifth generation (5G): Digital cellular networks that use new radio (NR) technology to provide higher data rates, lower latency, and massive connectivity. Examples are 5G NR, 5G New Core, etc.
- Cellular concept is the basic principle of wireless telephony, which divides a geographical area into smaller regions called cells, each served by a base station that communicates with mobile devices within its coverage area.
- Cellular concept enables efficient use of radio spectrum, by allowing frequency reuse, i.e., the same frequency can be used by different cells that are sufficiently far apart to avoid interference.
- Cellular concept also enables handover, i.e., the transfer of a mobile device's connection from one base station to another, as the device moves across cell boundaries.
- GSM (Global System for Mobile communication) is a 2G digital cellular network that is widely used by mobile phone users in Europe and other parts of the world.
- GSM uses a combination of FDMA and TDMA to multiplex users. It uses four different frequency bands: 850 MHz, 900 MHz, 1800 MHz, and 1900 MHz.
- GSM has a hierarchical network architecture, consisting of the following components:
  - Mobile station (MS): The mobile device that communicates with the network, such as a mobile phone or a modem.
  - Base station subsystem (BSS): The part of the network that manages the radio communication with the mobile stations, consisting of base transceiver stations (BTS) and base station controllers (BSC).
  - Network and switching subsystem (NSS): The part of the network that performs the switching and routing of calls and data, consisting of mobile switching centers (MSC), home location registers (HLR), visitor location registers (VLR), authentication centers (AUC), and equipment identity registers (EIR).
  - Operation and support subsystem (OSS): The part of the network that performs the management and maintenance of the network, consisting of operation and maintenance centers (OMC), network management centers (NMC), and billing centers (BC).
- GSM supports various services, such as:
  - Voice services: Basic telephony, emergency calls, voice mail, etc.
  - Data services: Short message service (SMS), circuit-switched data (CSD), general packet radio service (GPRS), enhanced data rates for GSM evolution (EDGE), etc.
  - Supplementary services: Call forwarding, call waiting, call barring, caller identification, etc.



### Air-Interface for Mobile Computing

- The air interface is the communication link between the two stations in mobile or wireless communication.
- The air interface involves both the physical and data link layers (layer 1 and 2) of the OSI model for a connection  .
- The air interface defines the frequency, channel bandwidth and modulation scheme for the radio transmission between mobile devices and the base station in a cellular network .
- Different air interface technologies are used for different cellular standards, such as TDMA and CDMA for GSM, OFDMA for LTE, and CP-OFDM for NR .
- The air interface is a key component of the radio access network (RAN) that enables wireless connectivity and mobility for mobile computing.



### Channel Structure

- Channel structure is the way of organizing the communication channels in a mobile network.
- A channel is a logical or physical path for transmitting data between a mobile device and a base station.
- Channel structure affects the performance, efficiency, and reliability of the mobile network.

#### Physical Channels and Logical Channels

- Physical channels are the radio frequency (RF) carriers that are divided into time slots. Each time slot can carry one or more bits of data.
- Logical channels are the information streams that are carried within the physical channels. Logical channels can be classified into traffic channels and control channels.
- Traffic channels (TCHs) are used to carry voice or data between the mobile device and the base station.
- Control channels (CCHs) are used to carry signaling and management information between the mobile device and the base station. Control channels can be further divided into broadcast channels, common control channels, and dedicated control channels.

#### Broadcast Channels

- Broadcast channels are used to transmit information from the base station to all mobile devices in the cell. Broadcast channels include:
  - Frequency correction channel (FCCH): used to synchronize the frequency of the mobile device with the base station.
  - Synchronization channel (SCH): used to synchronize the time slot and frame number of the mobile device with the base station.
  - Broadcast control channel (BCCH): used to broadcast information about the cell identity, frequency allocation, and network parameters.
  - Cell broadcast channel (CBCH): used to broadcast short messages to all mobile devices in the cell.

#### Common Control Channels

- Common control channels are used to establish and maintain the connection between the mobile device and the base station. Common control channels include:
  - Random access channel (RACH): used by the mobile device to request access to the network.
  - Paging channel (PCH): used by the base station to page the mobile device for an incoming call or data.
  - Access grant channel (AGCH): used by the base station to assign a traffic channel or a dedicated control channel to the mobile device.
  - Stand-alone dedicated control channel (SDCCH): used to exchange authentication, encryption, and location update information between the mobile device and the base station.

#### Dedicated Control Channels

- Dedicated control channels are used to carry signaling and management information between the mobile device and the base station during an active call or data session. Dedicated control channels include:
  - Slow associated control channel (SACCH): used to exchange power control, timing advance, and quality measurement information between the mobile device and the base station.
  - Fast associated control channel (FACCH): used to exchange handover, call setup, and call release information between the mobile device and the base station.
  - Enhanced full rate (EFR) SACCH: used to exchange enhanced power control, timing advance, and quality measurement information between the mobile device and the base station.



### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile devices in wireless cellular networks.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is the process of informing the network about the current location of a mobile device, usually initiated by the device itself.
- Location lookup is the process of finding the current location of a mobile device, usually initiated by the network or another device.
- Paging is the process of sending a message to a mobile device to notify it of an incoming call or data.
- Location management involves two types of databases: Home Location Register (HLR) and Visitor Location Register (VLR).
- HLR is a centralized database that stores the subscription information and some location information of all mobile devices in the network.
- VLR is a local database that stores the information of the mobile devices that are currently visiting a specific service area.
- HLR and VLR communicate with each other to update and query the location information of mobile devices.
- HLR-VLR scheme is a hierarchical location management scheme that divides the service coverage area into registration areas (RAs), each with a VLR.
- Each RA covers a group of base stations (cells) that provide wireless communication to the mobile devices.
- When a mobile device moves from one RA to another, it performs a location update to the new VLR, which then contacts the HLR to update the location information.
- When a call or data is destined to a mobile device, the network performs a location lookup by querying the HLR, which then returns the address of the VLR that serves the current RA of the device.
- The network then sends a paging message to the VLR, which broadcasts it to all the cells in the RA, until the device responds.
- Handoff is the process of transferring an ongoing call or data session from one base station to another, without interrupting the communication.
- Handoff is necessary when a mobile device moves out of the coverage area of one base station and into the coverage area of another.
- Handoff can be classified into two types: hard handoff and soft handoff.
- Hard handoff is the process of breaking the connection with the old base station before establishing a connection with the new base station.
- Soft handoff is the process of maintaining the connection with both the old and the new base stations until the connection with the old base station is dropped.
- Handoff can also be classified into two types: horizontal handoff and vertical handoff.
- Horizontal handoff is the process of transferring a call or data session from one base station to another within the same network or technology.
- Vertical handoff is the process of transferring a call or data session from one network or technology to another, such as from cellular to Wi-Fi.
- Handoff involves three main phases: initiation, decision, and execution.
- Initiation is the phase where the mobile device or the network detects the need for a handoff, based on some criteria such as signal strength, quality, or load.
- Decision is the phase where the network or the mobile device selects the best candidate base station for the handoff, based on some criteria such as availability, capacity, or cost.
- Execution is the phase where the network or the mobile device performs the necessary signaling and resource allocation to complete the handoff.
- Handoff performance can be measured by some metrics such as handoff delay, handoff failure rate, handoff dropping rate, or handoff overhead.
- Handoff delay is the time required to complete a handoff.
- Handoff failure rate is the probability that a handoff attempt fails.
- Handoff dropping rate is the probability that a call or data session is dropped due to a handoff failure.
- Handoff overhead is the amount of resources consumed by the handoff process.

: Location Management in Wireless Cellular Networks
: Location, Handoff Management and HLR-VLR Location and Handoff Management
: Visitor Location Register - an overview | ScienceDirect Topics
: Lecture 1: Mobility Management in Mobile Wireless



### Channel allocation in cellular systems

- Channel allocation means to allocate the available channels to the cells in a cellular system .
- Channels are the basic units of communication resources that can carry signals between a base station and a mobile terminal.
- Channels can be divided into two types: frequency channels and time channels. Frequency channels use different frequencies to transmit signals, while time channels use different time slots to transmit signals.
- Channel allocation strategies are designed to achieve efficient use of frequencies, time slots and bandwidth, while minimizing interference and maximizing quality of service .
- Channel allocation strategies can be classified into three categories: fixed channel allocation, dynamic channel allocation and hybrid channel allocation .
- Fixed channel allocation (FCA) assigns a fixed number of channels to each cell, regardless of the traffic demand. FCA is simple and easy to implement, but it may result in low channel utilization and high blocking probability .
- Dynamic channel allocation (DCA) assigns channels to cells on demand, based on the traffic load and the interference level. DCA is more flexible and adaptive, but it requires more complex algorithms and coordination among cells .
- Hybrid channel allocation (HCA) combines FCA and DCA, by dividing the channels into two sets: a fixed set and a dynamic set. The fixed set is allocated to each cell permanently, while the dynamic set is allocated to cells temporarily, based on the traffic and interference conditions .
- Some examples of channel allocation algorithms are: borrowing, locking, channel segregation, channel reassignment, channel ordering, channel borrowing with locking, channel borrowing with ordering, etc .
- Channel allocation is an important aspect of cellular system design, as it affects the system capacity, performance, quality and cost .



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
  - Better security, as the code sequence makes the signal difficult to intercept or jam  .
  - Improved voice quality, as the signal can be recovered from noise and fading by using error correction and diversity techniques  .
  - Greater flexibility, as the code sequence can be dynamically changed to accommodate different services and user demands  .
- CDMA has some disadvantages, such as:
  - Higher complexity, as the transmitter and receiver need to synchronize the code sequence and perform complex signal processing  .
  - Higher power consumption, as the transmitter needs to spread the signal over a wide bandwidth and the receiver needs to perform correlation and decoding  .
  - Near-far problem, where a strong signal from a nearby transmitter can interfere with a weak signal from a distant transmitter if they use the same code sequence  .
- CDMA is one of the multiple access techniques used in mobile computing, along with FDMA (Frequency Division Multiple Access) and TDMA (Time Division Multiple Access).
- FDMA divides the available bandwidth into frequency bands, and assigns each user a different band.
- TDMA divides the available bandwidth into time slots, and assigns each user a different slot.
- CDMA, FDMA, and TDMA can be compared based on the following parameters:
  - Bandwidth efficiency: CDMA > TDMA > FDMA
  - Power efficiency: FDMA > TDMA > CDMA
  - Complexity: CDMA > TDMA > FDMA
  - Security: CDMA > TDMA > FDMA
  - Interference: FDMA > TDMA > CDMA
- CDMA is used in wireless telephony, which is the transmission of voice and data over radio waves  .
- Wireless telephony is based on the cellular concept, which divides a geographical area into cells, each served by a base station  .
- The base stations are connected to a mobile switching center (MSC), which coordinates the communication between the mobile users and the public switched telephone network (PSTN)  .
- The mobile users can roam from one cell to another, and the MSC can handover the call to the appropriate base station  .
- GSM (Global System for Mobile Communications) is a standard for wireless telephony that uses TDMA as the multiple access technique  .
- GSM operates in the 900 MHz and 1800 MHz frequency bands in



### GPRS for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- GPRS stands for **General Packet Radio Service** .
- It is a **packet oriented** wireless data communication service for mobile communications on **2G and 3G cellular networks**  .
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
- SGSN is responsible for **authentication**, **encryption**, **mobility management**, **session management**, and **routing** of data packets.
- GGSN is responsible for **interfacing** with external packet data networks, such as the internet, and **translating** between different protocols.
- It has four main modes of operation: **Idle mode**, **Ready mode**, **Standby mode**, and **Transfer mode**.
- Idle mode is when the mobile station is **not attached** to the GPRS network and **cannot** send or receive data packets.
- Ready mode is when the mobile station is **attached** to the GPRS network and has a **temporary logical link** with the SGSN.
- Standby mode is when the mobile station is **attached** to the GPRS network but has a **dormant logical link** with the SGSN.
- Transfer mode is when the mobile station is **sending or receiving** data packets over the PDCHs.
- It has several advantages, such as:
  - **Higher data rates** than circuit-switched services.
  - **Efficient use of radio resources** by sharing channels among multiple users.
  - **Always-on connectivity** without occupying a dedicated channel.
  - **Flexible billing** based on volume or duration of data transfer.
  - **Seamless integration** with other packet data networks.
- It has several applications, such as:
  - **Mobile internet access** via web browsers, email clients, etc..
  - **Machine-to-machine (M2M) communication** for IoT devices, such as smart meters, sensors, etc..
  - **Location-based services** for navigation, tracking, etc..
  - **Multimedia messaging service (MMS)** for sending and receiving images, videos, etc..
  - **Wireless application protocol (WAP)** for accessing information and services from mobile devices.



## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves, infrared, or other electromagnetic signals.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus. WLANs typically use the IEEE 802.11 standard, which defines the medium access control (MAC) and physical layer (PHY) specifications for wireless communication.
- MAC issues in WLANs include how to coordinate the access of multiple devices to the shared wireless medium, how to avoid or resolve collisions, how to ensure fairness and efficiency, and how to protect the privacy and security of the transmitted data.
- IEEE 802.11 is the most widely used standard for WLANs, which has been revised and updated several times since its first publication in 1997. The latest version, IEEE 802.11-2020, incorporates amendments 1 to 5 published in 2016 and 2018, and specifies technical corrections and enhancements to the MAC and PHY functions.
- IEEE 802.11 defines several variants of the MAC and PHY layers, which differ in terms of frequency band, modulation scheme, data rate, range, and compatibility. Some of the common variants are 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax.
- IEEE 802.11 uses the Ethernet protocol and CSMA/CA (carrier sense multiple access with collision avoidance) for MAC layer access control. CSMA/CA is a technique that allows devices to sense the wireless medium before transmitting, and to back off and retry later if the medium is busy or a collision is detected.
- IEEE 802.11 also supports optional features such as power management, quality of service, security, and roaming, which enhance the performance and functionality of WLANs.
- Bluetooth is another wireless technology that enables short-range communication between devices, such as smartphones, headphones, keyboards, and mice. Bluetooth uses the 2.4 GHz frequency band and a frequency-hopping spread spectrum (FHSS) technique to avoid interference and enhance security.
- Bluetooth defines a protocol stack that consists of several layers, such as the radio layer, the baseband layer, the link manager layer, the logical link control and adaptation protocol (L2CAP) layer, and the application layer. The application layer includes various profiles that define the specific functions and services that Bluetooth devices can offer, such as audio, file transfer, networking, and printing.
- Wireless is a general term that refers to any type of communication that does not require wires or cables, such as WLANs, Bluetooth, cellular networks, satellite networks, and radio networks. Wireless technologies have various advantages and disadvantages, such as mobility, flexibility, scalability, cost, reliability, security, and interference. Wireless technologies are widely used in various domains, such as personal, business, industrial, military, and medical.



### Multiple Access Protocols

- Multiple access protocols are techniques that allow multiple nodes or users to share a common communication channel or medium in a wireless network.
- The main challenge of multiple access protocols is to avoid or minimize collisions, which occur when two or more nodes transmit at the same time and interfere with each other.
- There are different types of multiple access protocols, such as random access, controlled access, and channelization protocols.
- Random access protocols allow nodes to transmit whenever they have data to send, without any coordination or reservation. Examples of random access protocols are ALOHA, CSMA, CSMA/CA, and CSMA/CD  .
- Controlled access protocols require nodes to obtain permission or a grant before transmitting. Examples of controlled access protocols are polling, token passing, and reservation protocols .
- Channelization protocols divide the channel into smaller sub-channels or time slots and assign them to different nodes or users. Examples of channelization protocols are FDMA, TDMA, CDMA, and OFDMA .
- IEEE 802.11 is a standard for wireless LANs that uses CSMA/CA as the default multiple access protocol for the MAC layer. CSMA/CA stands for carrier-sense multiple access with collision avoidance, which means that nodes sense the channel before transmitting and back off if the channel is busy. CSMA/CA also uses a mechanism called distributed coordination function (DCF) to reduce collisions by exchanging control frames such as request-to-send (RTS) and clear-to-send (CTS) before data transmission .
- Bluetooth is a wireless technology that enables short-range communication between devices such as phones, laptops, headsets, and speakers. Bluetooth uses a channelization protocol called frequency-hopping spread spectrum (FHSS), which means that nodes change their frequency of transmission according to a predefined sequence or pattern. FHSS helps to avoid interference and improve security by making the signal harder to detect or jam.
- Wireless in the context of mobile computing refers to the use of wireless technologies to enable mobile devices to access network services and resources. Wireless technologies can be classified into different categories based on their range, such as personal area network (PAN), local area network (LAN), metropolitan area network (MAN), and wide area network (WAN). Examples of wireless technologies are Bluetooth, Wi-Fi, WiMAX, and cellular networks.



### TCP over wireless

- Transmission Control Protocol (TCP) is a reliable and connection-oriented protocol that provides end-to-end data delivery over the Internet.
- TCP assumes that most packet losses are due to network congestion and responds by reducing the sending rate to avoid further losses.
- However, in wireless networks, packet losses can also occur due to wireless link errors, such as fading, shadowing, interference, and mobility.
- TCP over wireless networks faces several challenges, such as:
  - TCP cannot distinguish between congestion losses and wireless losses, and may unnecessarily reduce the sending rate when wireless losses occur.
  - TCP may experience frequent timeouts and retransmissions due to the high delay and variability of wireless links.
  - TCP may suffer from spurious retransmissions and duplicate acknowledgements due to packet reordering and out-of-order delivery in wireless networks.
  - TCP may not fully utilize the available bandwidth of wireless links due to the slow start and congestion avoidance mechanisms.
- Several solutions have been proposed to improve the performance of TCP over wireless networks, such as:
  - Link layer solutions: These solutions aim to hide the wireless losses from TCP by using techniques such as error correction, retransmission, and packet scheduling at the link layer. For example, the Wireless Link Protocol (WLP)  provides reliable and in-order delivery of TCP packets over wireless links.
  - Split-connection solutions: These solutions divide the TCP connection into two segments: one over the wired network and one over the wireless network. The wireless segment uses a different protocol that is optimized for wireless conditions, while the wired segment uses standard TCP. For example, the Indirect TCP (I-TCP)  protocol splits the TCP connection at the base station, which acts as a proxy between the mobile host and the destination.
  - End-to-end solutions: These solutions modify the TCP behavior at the end hosts to adapt to wireless conditions, without changing the intermediate nodes or the TCP semantics. For example, the TCP Selective Acknowledgement (SACK)  option allows the sender to recover from multiple losses in a window without retransmitting all the packets.



### Wireless applications

Wireless applications are the software or services that use wireless communication technologies to provide functionality or benefits to the users or the network. Wireless applications can be classified into different categories based on the type, purpose, and scope of the wireless communication involved. Some of the common categories are:

- Wireless personal area network (WPAN) applications: These are the applications that use short-range wireless technologies to connect devices within a personal area, such as a room or a car. Examples of WPAN applications are Bluetooth, wireless mouse, keyboard, headset, etc.
- Wireless local area network (WLAN) applications: These are the applications that use medium-range wireless technologies to connect devices within a local area, such as a building or a campus. Examples of WLAN applications are Wi-Fi, wireless routers, wireless printers, etc.
- Wireless metropolitan area network (WMAN) applications: These are the applications that use long-range wireless technologies to connect devices within a metropolitan area, such as a city or a region. Examples of WMAN applications are WiMAX, wireless broadband, etc.
- Wireless wide area network (WWAN) applications: These are the applications that use global wireless technologies to connect devices across the world. Examples of WWAN applications are cellular networks, satellite networks, GPS, etc.

Some of the benefits of wireless applications are:

- Mobility: Wireless applications enable users to access information and services from anywhere and anytime, without being restricted by wires or cables.
- Reliability: Wireless applications reduce the risk of network failures or interruptions caused by physical damages or interference to the wires or cables.
- Cost-effectiveness: Wireless applications reduce the cost of installation, maintenance, and operation of the network infrastructure, as well as the devices and equipment involved.
- Scalability: Wireless applications can easily accommodate the growth or change of the network size, topology, or configuration, without requiring significant modifications or additions to the network infrastructure.
- Flexibility: Wireless applications can support a variety of network architectures, protocols, and standards, as well as a range of devices and services, depending on the needs and preferences of the users or the network.



### Data Broadcasting

- Data broadcasting is a group communication, where a sender sends data to receivers simultaneously .
- Data broadcasting can be used for efficient information dissemination in wireless networks, where the client demands are local or correlated.
- Data broadcasting can be performed using different techniques, such as network coding, cooperation, smart antennas, etc.
- Data broadcasting can reduce the bandwidth consumption, power consumption, and latency of wireless networks.
- Data broadcasting can also pose some challenges, such as security, reliability, scalability, and synchronization.

### Wireless Networking

- Wireless networking refers to a computer network that makes use of radio frequency (RF) connections between nodes in the network .
- Wireless networking can be classified into different types, such as wireless personal area network (WPAN), wireless local area network (WLAN), wireless metropolitan area network (WMAN), and wireless wide area network (WWAN).
- Wireless networking can offer some advantages, such as mobility, flexibility, scalability, and cost-effectiveness.
- Wireless networking can also face some challenges, such as interference, security, quality of service, and compatibility.

### Wireless LAN Overview

- Wireless LAN (WLAN) is a type of wireless network that covers a small geographic area, such as a home, office, or campus.
- WLAN uses a wireless access point (AP) to connect the wireless devices to a wired network or the internet.
- WLAN follows the IEEE 802.11 standard, which defines the physical and medium access control (MAC) layers of the network.
- WLAN supports different frequency bands, such as 2.4 GHz, 5 GHz, and 6 GHz, and different modulation schemes, such as OFDM, DSSS, and FHSS.
- WLAN supports different data rates, ranging from 1 Mbps to 10 Gbps, depending on the standard version, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax.

### MAC Issues

- MAC issues refer to the challenges and solutions of coordinating the access of multiple wireless devices to the shared wireless medium.
- MAC issues can be divided into two categories: contention-based and contention-free.
- Contention-based MAC issues involve the use of random access protocols, such as CSMA/CA, to avoid or resolve collisions among the wireless devices.
- Contention-free MAC issues involve the use of reservation or polling protocols, such as TDMA, FDMA, CDMA, or SDMA, to allocate the wireless medium to the wireless devices.
- MAC issues can also involve the use of power control, rate adaptation, and channel assignment techniques to optimize the performance of the wireless network.

### IEEE 802.11

- IEEE 802.11 is the standard that defines the WLAN technology and its specifications.
- IEEE 802.11 consists of several sub-standards, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that differ in terms of frequency band, data rate, modulation scheme, and other features.
- IEEE 802.11 defines the physical layer (PHY) and the medium access control (MAC) layer of the WLAN network.
- IEEE 802.11 PHY layer specifies the characteristics of the wireless signal, such as frequency, bandwidth, power, modulation, and coding.
- IEEE 802.11 MAC layer specifies the rules and procedures of accessing the wireless medium, such as frame format, addressing, error control, and security.

### Bluetooth

- Bluetooth is a type of wireless personal area network (WPAN) that enables short-range wireless communication among devices, such as smartphones, laptops, headphones, speakers, printers, etc.
- Bluetooth uses the 2.4 GHz frequency band and supports data rates up to 3 Mbps.
- Bluetooth follows the IEEE 802.15.1 standard, which defines the physical layer and the MAC layer of the network.
- Bluetooth physical layer uses frequency hopping spread spectrum (FHSS) to avoid interference and enhance security.
- Bluetooth MAC layer uses a master-slave



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
  - The foreign agent or the mobile node decapsulates the packets and delivers them to the mobile node.
  - When the mobile node wants to communicate with the CN, it sends packets to the CN using its home address as the source address.
  - The foreign agent or the mobile node tunnels the packets to the home agent using IP encapsulation.
  - The home agent decapsulates the packets and forwards them to the CN using normal IP routing.
- Mobile IP has some advantages and disadvantages:
  - Advantages:
    - It preserves the existing IP addressing scheme and does not require any changes to the CN or the routers.
    - It supports transparent mobility and session continuity for the mobile node across different networks.
    - It is scalable and compatible with the Internet infrastructure and protocols.
  - Disadvantages:
    - It introduces additional overhead and latency due to the tunneling and registration processes.
    - It may cause suboptimal routing and triangular routing, which increase the network congestion and delay.
    - It may suffer from security issues such as spoofing, replay, and denial-of-service attacks.



### WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer is of most interest to content developers because it contains among other things, device specifications, scripting languages, and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems. The application layer also includes the Wireless Application Environment (WAE), which provides a framework for developing and delivering applications and services to wireless devices.
  - Session Layer: This layer provides session and transaction support for the application layer. It consists of two protocols: the Wireless Session Protocol (WSP) and the Wireless Transaction Protocol (WTP). WSP is a binary-encoded version of HTTP that offers fast connection suspension and reconnection, and supports both connection-oriented and connectionless services. WTP is a lightweight transaction-oriented protocol that provides reliable request/response transactions over datagram services.
  - Transaction Layer: This layer provides security and data transfer services for the session layer. It consists of two protocols: the Wireless Transport Layer Security (WTLS) and the Wireless Datagram Protocol (WDP). WTLS is a security protocol that provides data integrity, privacy, and authentication for wireless communications. It is based on the Transport Layer Security (TLS) protocol, but optimized for low-bandwidth and high-latency networks. WDP is a data transfer protocol that provides a common interface for the transport layer, and allows WAP to be bearer-independent. It can operate over various network technologies, such as GSM, CDMA, CDPD, SMS, and IP.
  - Transport Layer: This layer provides the actual transport of data between the wireless device and the network. It consists of various bearer services, such as GSM, CDMA, CDPD, SMS, and IP, that are responsible for delivering WDP datagrams to the appropriate destination.
  - Physical Layer: This layer provides the physical connection and transmission of data between the wireless device and the network. It consists of various hardware components, such as antennas, modems, and radio transmitters, that are specific to each network technology.
- The WAP architecture also comprises several components, each serving a specific function. These components include:
  - Wireless Device: This is the end-user device that runs a micro-browser and communicates with the WAP gateway using the WAP protocol stack. Examples of wireless devices are mobile phones, PDAs, and pagers.
  - WAP Gateway: This is the intermediary component that connects the wireless network and the internet. It performs various functions, such as protocol translation, content encoding and decoding, security, and caching. It also hosts the WAP proxy, which acts as a proxy server for the wireless device and handles the WSP requests and responses.
  - Origin Server: This is the component that hosts the web content and applications for the wireless device. It runs a web server and communicates with the WAP gateway using the HTTP protocol. It also supports the WML and WMLScript languages, which are used to create dynamic and interactive content for the wireless device.



### Protocol Stack for Wireless Networking

- A protocol stack is an implementation of a set of communication protocols that work together to provide network functionality.
- A protocol stack consists of different layers, each of which performs a specific function and interacts with the adjacent layers through well-defined interfaces.
- A protocol stack for wireless networking aims to hide the complexity of the wireless interface and present a software interface that resembles that of a wired connection.
- However, some differences between a wired and a wireless interface cannot be hidden, such as the steps required to find and connect to other devices, the variability of the channel quality, and the limited power and bandwidth resources.
- Therefore, a protocol stack for wireless networking needs to address some additional challenges, such as mobility management, power management, security, and quality of service.
- A protocol stack for wireless networking can be divided into four main layers: physical layer, data link layer, network layer, and application layer.
- The physical layer is responsible for transmitting and receiving raw bits over the wireless medium, using modulation, coding, and multiplexing techniques.
- The data link layer is responsible for providing reliable and efficient data transfer between two devices, using framing, error control, flow control, and medium access control (MAC) techniques.
- The network layer is responsible for routing packets across multiple hops, using addressing, forwarding, and routing protocols.
- The application layer is responsible for providing end-to-end services to the users, using various protocols and standards, such as HTTP, FTP, SMTP, etc.
- Different wireless networking technologies may use different protocol stacks, depending on their design goals and requirements .
- For example, IEEE 802.11 is a standard for wireless local area networks (WLANs) that uses a protocol stack similar to the TCP/IP model, with some modifications in the data link layer to support MAC issues, such as carrier sense multiple access with collision avoidance (CSMA/CA), distributed coordination function (DCF), and point coordination function (PCF).
- Bluetooth is a standard for wireless personal area networks (WPANs) that uses a protocol stack consisting of five layers: radio layer, baseband layer, link manager layer, logical link control and adaptation protocol (L2CAP) layer, and application layer.
- Wireless is a term that refers to any type of communication that does not use wires or cables, such as radio, infrared, microwave, satellite, cellular, etc.



### Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, processing power, and user interface .
- WAE consists of several components, such as:
  - Wireless Markup Language (WML), which is a markup language similar to HTML, but optimized for small screens and low bandwidth.
  - Wireless Markup Language Script (WMLScript), which is a scripting language similar to JavaScript, but with a smaller footprint and less functionality.
  - Wireless Telephony Application Interface (WTAI), which is an extension that allows WAP applications to access phone-specific features, such as dialing, messaging, and call control.
  - Wireless Datagram Protocol (WDP), which is a transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS.
  - Wireless Session Protocol (WSP), which is a session layer protocol that provides reliable and secure communication between WAP clients and servers.
  - Wireless Transaction Protocol (WTP), which is a transaction layer protocol that supports both reliable and unreliable request-response transactions.
  - Wireless Application Protocol Binary XML (WBXML), which is a binary encoding of XML that reduces the size and complexity of WML and WMLScript documents  .
- WAE enables wireless devices to access various internet-based services, such as browsing, scripting, email, news, instant messaging, and network services. WAE also supports content adaptation, which is the process of tailoring the content and presentation of web pages to the capabilities and preferences of different wireless devices  .



### Applications for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- Wireless networking is the technology that enables devices to communicate without wires or cables, using radio waves or infrared signals.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs can be classified into two types: infrastructure and ad hoc. Infrastructure WLANs use a base station, such as a wireless access point or router, to coordinate the communication among the devices. Ad hoc WLANs do not use a base station, but rely on peer-to-peer communication among the devices.
- The IEEE 802.11 standard defines the protocols and specifications for WLANs. It consists of two layers: the medium access control (MAC) layer and the physical (PHY) layer. The MAC layer is responsible for controlling the access to the shared wireless medium, while the PHY layer is responsible for encoding, modulating, and transmitting the data over the wireless channel.
- The IEEE 802.11 standard has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, that differ in terms of data rates, frequency bands, modulation schemes, and other features.
- Bluetooth is another wireless technology that enables short-range communication among devices, such as mobile phones, headsets, keyboards, mice, printers, and speakers. It uses the 2.4 GHz frequency band and supports data rates up to 3 Mbps.
- Bluetooth also follows the IEEE 802.15.1 standard, which defines the MAC and PHY layers for Bluetooth. It employs a frequency-hopping spread spectrum (FHSS) technique to avoid interference and enhance security. It also uses a master-slave architecture, where one device acts as the master and controls the communication with up to seven slaves in a network called a piconet. Multiple piconets can form a larger network called a scatternet.
- Wireless multiple access protocols are the methods that enable multiple devices to share the wireless medium without causing collisions or interference. Some of the common wireless multiple access protocols are frequency division multiple access (FDMA), time division multiple access (TDMA), code division multiple access (CDMA), and orthogonal frequency division multiple access (OFDMA).
- TCP over wireless is the challenge of adapting the transmission control protocol (TCP), which was designed for wired networks, to the wireless environment, which is characterized by high bit error rates, variable delays, and frequent disconnections. Some of the techniques to improve TCP performance over wireless are selective acknowledgments (SACK), fast retransmit and recovery (FRR), and TCP splitting.
- Wireless applications are the software programs that run on wireless devices and utilize the wireless network capabilities. Some of the examples of wireless applications are email, web browsing, social media, online gaming, video streaming, and location-based services.
- Data broadcasting is the technique of transmitting data to multiple receivers simultaneously over a wireless channel. It can be used to disseminate information, such as news, weather, traffic, and advertisements, to a large number of users. It can also be used to support interactive applications, such as online quizzes, polls, and auctions.
- Mobile IP is the protocol that enables mobile devices to maintain their network connectivity and IP address while moving across different networks. It uses two types of agents: a home agent and a foreign agent. The home agent is located in the home network of the mobile device and keeps track of its current location. The foreign agent is located in the visited network of the mobile device and provides routing and forwarding services. Mobile IP uses a technique called tunneling to deliver the packets to the mobile device.
- WAP (Wireless Application Protocol) is a suite of protocols that enables wireless devices to access web content and services. It consists of four layers: the wireless application environment (WAE), the wireless session protocol (WSP), the wireless transaction protocol (WTP), and the wireless transport layer security (WTLS). WAP uses a markup language called wireless markup language (WML) to create web pages for wireless devices. WAP also supports applications, such as email, calendar, contacts, and games.



## Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile

- Data management issues in mobile computing refer to the challenges and opportunities of storing, accessing, and processing data in a mobile environment, where users and devices are constantly moving and changing their connectivity and availability.
- Some of the main data management issues in mobile computing are:
  - Data availability: how to ensure that mobile users can access the data they need, even when they are disconnected from the network or have intermittent connectivity.
  - Data consistency: how to maintain the correctness and integrity of the data, especially when multiple users and devices may update the same data in different locations and times.
  - Data security: how to protect the data from unauthorized access, modification, or disclosure, especially when the data is stored or transmitted over wireless networks or on mobile devices that may be lost or stolen.
  - Data adaptation: how to tailor the data to the needs and preferences of the mobile users, such as reducing the size, complexity, or quality of the data to fit the device capabilities, network bandwidth, or user preferences.
- Data replication for mobile computers is a technique that aims to improve the data availability and consistency in mobile computing by creating and maintaining multiple copies of the data on different devices or locations .
- Some of the benefits of data replication for mobile computers are:
  - It allows mobile users to access the data locally, without relying on the network connectivity or the availability of the data source .
  - It reduces the network traffic and communication cost, by avoiding frequent data transfers between the mobile devices and the data source .
  - It enhances the data consistency, by applying concurrency control and conflict resolution mechanisms to synchronize the updates among the replicas .
- Some of the challenges of data replication for mobile computers are:
  - It requires additional storage space and processing power on the mobile devices, which may be limited or scarce .
  - It introduces the possibility of data conflicts, when different replicas have divergent updates that need to be reconciled .
  - It involves trade-offs between the data availability, consistency, and communication cost, depending on the replication strategy and the synchronization frequency .
- Adaptive clustering for mobile is a technique that aims to improve the data management and communication efficiency in mobile computing by grouping the mobile devices into clusters based on their proximity, connectivity, or similarity  .
- Some of the benefits of adaptive clustering for mobile are:
  - It reduces the network overhead and latency, by enabling local communication and data exchange within the clusters, instead of relying on the global network or the data source  .
  - It increases the data availability and reliability, by allowing the clusters to share and replicate the data among their members, and to tolerate the failures or disconnections of some devices  .
  - It supports the data adaptation and personalization, by allowing the clusters to customize the data according to the needs and preferences of their members, and to exploit the common interests or behaviors of the devices  .
- Some of the challenges of adaptive clustering for mobile are:
  - It requires dynamic and efficient algorithms to form and maintain the clusters, considering the mobility and heterogeneity of the devices, and the changing network conditions  .
  - It involves trade-offs between the cluster size, stability, and performance, depending on the clustering criteria and the application requirements  .
  - It raises security and privacy issues, by exposing the data and the communication of the devices to the other members of the cluster, who may be malicious or untrustworthy  .



### Wireless Networks

- Wireless networks are networks that use radio waves or other wireless technologies to connect devices without cables or wires.
- Wireless networks can be classified into different types based on their coverage, topology, architecture, and access methods.
- Some common types of wireless networks are:
  - Wireless personal area network (WPAN): A network that connects devices within a short range, such as Bluetooth or infrared.
  - Wireless local area network (WLAN): A network that covers a small area, such as a home or an office, using Wi-Fi or other standards.
  - Wireless metropolitan area network (WMAN): A network that covers a larger area, such as a city or a campus, using technologies like WiMAX or LTE.
  - Wireless wide area network (WWAN): A network that covers a very large area, such as a country or a continent, using cellular or satellite technologies.

### Data Management Issues

- Data management is the process of storing, retrieving, updating, and analyzing data in a network.
- Data management in wireless networks faces some challenges and issues, such as:
  - Data availability: The data should be accessible to the users or applications, even when the network is disconnected, partitioned, or unreliable.
  - Data consistency: The data should be coherent and accurate, even when there are concurrent updates, conflicts, or failures.
  - Data security: The data should be protected from unauthorized access, modification, or disclosure, even when the network is vulnerable to attacks or eavesdropping.
  - Data efficiency: The data should be transferred and processed with minimal cost, delay, and overhead, even when the network has limited bandwidth, power, or resources.

### Data Replication for Mobile Computers

- Data replication is a technique that creates and maintains multiple copies of the same data in different locations or devices.
- Data replication for mobile computers is a way to improve data availability, consistency, and efficiency in wireless networks, by allowing the mobile devices to access local copies of the data instead of remote ones.
- Data replication for mobile computers can be classified into different types based on their replication unit, replication granularity, replication strategy, and replication consistency.
- Some common types of data replication for mobile computers are:
  - File replication: The replication unit is a file, which can be either a whole file or a file fragment.
  - Database replication: The replication unit is a database, which can be either a whole database or a database partition.
  - Object replication: The replication unit is an object, which can be either a whole object or an object attribute.
  - Page replication: The replication unit is a web page, which can be either a whole page or a page component.
- Some common types of replication granularity are:
  - Full replication: All the copies of the data are identical and complete.
  - Partial replication: Some copies of the data are incomplete or different from others.
- Some common types of replication strategy are:
  - Eager replication: The data is replicated as soon as it is updated or requested.
  - Lazy replication: The data is replicated only when it is needed or convenient.
- Some common types of replication consistency are:
  - Strong consistency: The data is always coherent and accurate across all the copies.
  - Weak consistency: The data may be temporarily incoherent or inaccurate across some copies.
  - Eventual consistency: The data will eventually become coherent and accurate across all the copies.

### Adaptive Clustering for Mobile Wireless Networks

- Clustering is a technique that groups nodes in a network into clusters, where each cluster has a leader or a coordinator, called a clusterhead, and some members or followers, called clustermembers.
- Clustering for mobile wireless networks is a way to improve network scalability, stability, and performance, by reducing the complexity, overhead, and interference of the network.
- Adaptive clustering for mobile wireless networks is a way to dynamically adjust the cluster structure and parameters according to the network conditions and requirements, such as node mobility, node density, node heterogeneity, and node functionality.
- Adaptive clustering for mobile wireless networks can be classified into different types based on their cluster formation, cluster maintenance, cluster reconfiguration, and cluster evaluation.
- Some common types of adaptive clustering for mobile wireless networks are:
  - Weight-based clustering: The clusterhead is selected based on a weight function that considers multiple factors, such as node degree, node ID, node mobility, node battery, etc.
  - Mobility-based clustering: The clusterhead is selected based on the node mobility, such as node speed, node direction, node stability, etc.
  - Energy-based clustering: The clusterhead is selected



### File system for mobile computing

- A file system is a software component that manages the storage and retrieval of data on a persistent device, such as a hard disk, flash memory, or optical disc.
- A file system for mobile computing is a file system that supports the mobility of both users and devices, and adapts to the challenges of wireless and mobile environments, such as network disconnection, low bandwidth, high latency, and limited battery power.
- Some of the design issues for a file system for mobile computing are:
  - How to provide location transparency, i.e., the ability to access files regardless of their physical location or the location of the user or device.
  - How to support user mobility, i.e., the ability to access files from different devices and locations, and to migrate files across devices and networks.
  - How to ensure data consistency and availability, i.e., the ability to access the latest version of a file and to handle concurrent updates and conflicts, especially in the presence of network disconnection or partition.
  - How to optimize network and device resources, i.e., the ability to reduce network traffic and storage overhead, and to conserve battery power and bandwidth.
- Some of the design options for a file system for mobile computing are:
  - Client-server model, where a central server stores and manages the files, and the clients access them over the network. This model provides location transparency and data consistency, but requires a reliable and high-speed network connection, and may incur high network and server load.
  - Replication model, where multiple servers store and manage copies of the files, and the clients access them from the nearest or most available server. This model provides location transparency and data availability, but requires a mechanism to synchronize the replicas and to resolve conflicts, and may incur high storage and network overhead.
  - Caching model, where the clients store and manage local copies of the files, and the servers store and manage the master copies. This model provides data availability and network and device optimization, but requires a mechanism to validate and update the caches and to resolve conflicts, and may incur data inconsistency and staleness.
  - Hybrid model, where the clients and the servers store and manage partial or full copies of the files, and use a combination of replication and caching techniques. This model provides a trade-off between the benefits and drawbacks of the other models, but requires a complex and adaptive mechanism to coordinate the file operations and to balance the resource utilization.
- One example of a file system for mobile computing is Coda , which is a distributed file system that uses a hybrid model of replication and caching, and supports disconnected operation for mobile computing. Some of the features of Coda are:
  - It is freely available under the GPL license.
  - It provides high performance through client-side persistent caching, which allows the clients to access and modify the files locally even when the network is unavailable or slow.
  - It provides server replication, which allows the servers to store and manage multiple copies of the files, and to handle partial network failures and load balancing.
  - It provides a security model for authentication, encryption and access control, which ensures the integrity and confidentiality of the files and the file operations.
  - It provides network bandwidth adaptation, which allows the clients and the servers to adjust the amount and frequency of data transfer according to the network conditions.
  - It provides good scalability, which allows the system to handle a large number of clients and servers, and a large amount of data.



### Disconnected operations

- Disconnected operation is a mode of operation in mobile computing that allows users to execute applications during temporary failures in networks or when they explicitly decide to work off-line .
- Disconnected operation is a key enabling technology for mobile computing, as it increases the availability and reliability of data and services in the presence of network limitations such as short range, inability to operate underground and in steel-framed buildings, or line-of-sight constraints .
- Disconnected operation requires mechanisms to handle the following issues :
  - Data consistency: how to ensure that the data accessed by the mobile client is up-to-date and consistent with the data stored in the server, and vice versa.
  - Data replication: how to replicate data between the mobile client and the server, and among multiple servers, to improve data availability and performance.
  - Data reconciliation: how to resolve conflicts that may arise due to concurrent updates on the same data by different clients or servers, or due to network partitions and merges.
  - Data adaptation: how to adapt the data to the varying resource constraints and preferences of the mobile client, such as bandwidth, battery, storage, screen size, etc.
  - Data caching: how to cache data locally on the mobile client to reduce network traffic and latency, and to enable offline access.
  - Data hoarding: how to select and prefetch data that is likely to be needed by the mobile client in the future, based on the user's profile, behavior, and context.
  - Data dissemination: how to push data from the server to the mobile client, or from one mobile client to another, based on the user's interests, subscriptions, and location.
- Disconnected operation can be classified into two types :
  - Voluntary disconnection: when the user intentionally decides to work offline, for example, to save battery power, to avoid network charges, or to have more privacy.
  - Involuntary disconnection: when the user is forced to work offline, for example, due to network failures, congestion, or mobility.
- Disconnected operation can be implemented using different techniques, such as :
  - Mobile computation: using mobile agents or code to migrate between the mobile client and the server, or among multiple servers, to perform tasks on behalf of the user.
  - Server replication: replicating the server functionality on the mobile client, or on multiple servers, to provide local or distributed services to the user.
  - Client caching: caching data or code on the mobile client, or on multiple clients, to provide fast and offline access to the user.
  - Data synchronization: synchronizing data or code between the mobile client and the server, or among multiple clients or servers, to ensure data consistency and reconciliation.
  - Data adaptation: adapting data or code to the resource constraints and preferences of the mobile client, or to the network conditions and context of the user.
  - Data dissemination: disseminating data or code from the server to the mobile client, or from one mobile client to another, to provide timely and relevant information to the user.



## Unit 4 - Mobile Agents Computing, Security and Fault Tolerance, Transaction Processing in Mobile Computing

- Mobile agents are a form of mobile code that can migrate from one computer to another autonomously and continue their execution on the destination computer .
- Mobile agents are autonomous, intelligent, social, and self-learning. They can work efficiently even when the user or the network is disconnected .
- Mobile agents can be used for various applications in mobile computing, such as information retrieval, network management, load balancing, distributed processing, and e-commerce .
- Mobile agents face several challenges and risks in mobile computing, such as security, fault tolerance, and transaction processing .
- Security issues include protecting the mobile agent from malicious hosts, protecting the host from malicious agents, and ensuring the confidentiality, integrity, and authenticity of the agent's data and code .
- Fault tolerance issues include detecting and recovering from agent failures, ensuring the availability and reliability of the agent's services, and coping with network failures and disconnections .
- Transaction processing issues include ensuring the atomicity, consistency, isolation, and durability of the agent's operations, managing the concurrency and locking of shared resources, and handling the commit and rollback of transactions .
- Various techniques and mechanisms have been proposed and developed to address these issues, such as encryption, authentication, digital signatures, firewalls, checkpoints, replication, logging, compensation, and coordination .



### Environment for Mobile Agents

- A mobile agent is a software entity that can migrate from one host to another in a network, carrying its code and state, and executing autonomously .
- A mobile agent environment is the software infrastructure that supports the creation, execution, migration, and communication of mobile agents.
- A mobile agent environment consists of the following components:
  - An agent platform, which provides the computational resources and services for hosting and executing mobile agents on a host.
  - An agent transport system, which enables the mobility of agents across different hosts and networks.
  - An agent communication system, which facilitates the interaction and coordination of agents with other agents, users, and systems.
  - An agent security system, which protects the agents and the hosts from malicious attacks and unauthorized access.
  - An agent management system, which monitors and controls the behavior and performance of agents and the environment.
- A mobile agent environment can be classified into two types based on the programming language and execution model of the agents:
  - A language-based environment, which supports agents written in a specific programming language, such as Java, and executes them in a virtual machine, such as the Java Virtual Machine (JVM).
  - A system-based environment, which supports agents written in any programming language, and executes them in a native environment, such as the operating system.
- A mobile agent environment can provide various benefits for mobile computing applications, such as  :
  - Reducing network traffic and latency by moving the computation closer to the data sources and sinks.
  - Enhancing scalability and reliability by distributing the workload and tolerating network failures and disconnections.
  - Adapting to dynamic and heterogeneous environments by adjusting the behavior and location of agents according to the context and preferences.
  - Improving user convenience and productivity by delegating tasks to autonomous and personalized agents.



## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of mobile nodes that communicate with each other using wireless links.
- Localization is the process of determining the position of a node in an ad hoc network, either relative to other nodes or to a global coordinate system. Localization can be achieved using various techniques, such as GPS, triangulation, multilateration, or beacon-based methods.
- MAC (Medium Access Control) issues refer to the challenges of coordinating the access of multiple nodes to a shared wireless channel, while avoiding collisions, interference, and hidden terminal problems. Some MAC protocols for ad hoc networks are CSMA/CA, TDMA, CDMA, and MACAW.
- Routing protocols are algorithms that enable the nodes in an ad hoc network to discover and maintain routes to other nodes. Routing protocols can be classified into proactive, reactive, or hybrid, depending on whether they maintain routes in advance, on demand, or both.
- Global state routing (GSR) is an example of a proactive routing protocol for ad hoc networks. It requires each node to maintain a complete and consistent view of the network topology, which is periodically exchanged with other nodes. GSR can achieve optimal routes, but at the cost of high overhead and scalability issues.



### Destination sequenced distance vector routing (DSDV)

- DSDV is a table-driven routing protocol for ad hoc mobile networks based on the Bellman–Ford algorithm.
- DSDV adds a new attribute, sequence number, to each route table entry of the conventional RIP.
- The sequence number is used to distinguish stale route information from the new and thus prevent the formation of routing loops.
- Each node maintains a routing table that contains the following information for each destination: the next hop, the number of hops, the sequence number, and the installation time.
- Each node periodically broadcasts its routing table to its neighbors, and updates its own table based on the received information.
- If a node detects a link break, it increments the sequence number of the destination and advertises the metric as infinity.
- DSDV provides only one route for a source/destination pair, and does not support multipath routing.
- DSDV reduces the control overhead and latency compared to the classical Bellman-Ford algorithm, but still suffers from frequent updates and wasted bandwidth.



### Dynamic Source Routing (DSR)

- Dynamic Source Routing (DSR) is a routing protocol for wireless mesh networks .
- It is an on-demand protocol that does not require periodic table updates or link state advertisements.
- It uses source routing, which means that the sender of a packet determines the complete sequence of nodes through which the packet has to pass .
- The sender explicitly lists this route in the packet's header, identifying each forwarding hop by the address of the next node to which to transmit the packet on its way to the destination host.
- DSR has two main mechanisms: route discovery and route maintenance .
- Route discovery is the process by which a sender node finds a route to a destination node when it has a packet to send .
- Route discovery involves broadcasting a route request packet, which is forwarded by intermediate nodes until it reaches the destination or a node that knows a route to the destination .
- The route request packet contains the address of the sender, the address of the destination, and a unique identification number .
- The route reply packet contains the route from the sender to the destination, and is sent back to the sender either by reversing the route request packet or by piggybacking on a route request packet going in the opposite direction .
- Route maintenance is the process by which a sender node detects and repairs link failures along an active route .
- Route maintenance involves sending route error packets, which inform the sender and other nodes that a link has broken and that they should discard any routes that contain that link .
- Route maintenance also involves using route caches, which store routes that have been learned or overheard by a node .
- Route caches can be used to avoid route discovery, to find alternative routes, or to reply to route requests .
- DSR has some advantages and disadvantages over other routing protocols .
- Advantages include:
  - No need for periodic messages, which reduces the network overhead and saves bandwidth and energy .
  - Ability to support multiple routes to a destination, which increases the reliability and load balancing .
  - Ability to adapt quickly to topology changes, which improves the performance in highly dynamic networks .
- Disadvantages include:
  - Large packet headers, which increase the transmission delay and consume more bandwidth .
  - Potential for stale routes, which may cause routing loops or packet losses .
  - Lack of scalability, which limits the applicability to large networks .



### Ad Hoc On-Demand Distance Vector Routing (AODV)

- AODV is a routing protocol designed for wireless and mobile ad hoc networks .
- AODV establishes routes to destinations on demand and supports both unicast and multicast routing .
- AODV is based on the principle of distance vector routing, where each node maintains a routing table with the next hop and the distance (in terms of hops) to each destination .
- AODV uses three types of control messages: route request (RREQ), route reply (RREP) and route error (RERR)  .
- AODV uses sequence numbers to ensure loop-free and up-to-date routes  .
- AODV uses two timers: active route timeout and hello interval. Active route timeout is the time after which a route is considered invalid if no data packets are sent or received through it. Hello interval is the time between two consecutive hello messages that are used to detect link failures  .
- AODV is the routing protocol used in Zigbee – a low power, low data rate wireless ad hoc network. There are various implementations of AODV such as MAD-HOC, Kernel-AODV, AODV-UU, AODV-UCSB and AODV-UIUC.
- AODV has some advantages such as low overhead, quick adaptation to network changes, loop-free routes and scalability . AODV also has some disadvantages such as high latency, vulnerability to attacks, lack of quality of service (QoS) support and frequent route breaks .



### Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source initiated on-demand routing protocol that was developed by Vincent Park and Scott Corson in 1997 .
- TORA is based on the concept of link reversal, which is a technique to dynamically change the direction of links in a network to avoid routing loops and maintain connectivity .
- TORA consists of three main phases: route creation, route maintenance, and route erasure .
- Route creation: When a source node wants to send data to a destination node, it broadcasts a query packet containing the destination ID. The query packet propagates through the network until it reaches the destination or a node that has a route to the destination. The nodes that receive the query packet assign themselves a height metric based on their distance from the destination. The height metric is used to create a directed acyclic graph (DAG) rooted at the destination. The nodes that have a lower height than their neighbors are downstream nodes, and the nodes that have a higher height than their neighbors are upstream nodes. The upstream nodes send update packets to their downstream neighbors to inform them of their height and establish links. The update packets propagate back to the source node, which can then choose a downstream neighbor to send data packets .
- Route maintenance: When a link failure occurs in the network, the nodes that are affected by the failure adjust their height metrics to reflect the change in topology. The node that detects the failure increases its height to the maximum value and broadcasts a clear packet to its neighbors. The clear packet informs the neighbors to invalidate their routes that use the failed link. The neighbors then increase their height to a value higher than the node that sent the clear packet and propagate the clear packet further. This process creates a new DAG rooted at the node that detected the failure. The node then tries to find a new route to the destination by sending a new query packet. If a new route is found, the node decreases its height to a value lower than its new downstream neighbor and sends an update packet to its upstream neighbors. This process restores the connectivity of the network and repairs the broken route .
- Route erasure: When a source node no longer needs a route to a destination node, it broadcasts an erase packet containing the destination ID. The erase packet propagates through the network and erases all the routes to the destination. The nodes that receive the erase packet reset their height metrics to null and delete their routing tables .
- TORA is an efficient, highly adaptive, and scalable routing protocol that can handle frequent topology changes and large network sizes. However, TORA also has some drawbacks, such as high control overhead, multiple routes, and possible network partitioning .



### QoS in Ad Hoc Networks

- Quality of service (QoS) refers to the level of quality of service that a network can provide to its users, such as bandwidth, delay, jitter, packet loss, etc. 
- QoS is an essential component of ad hoc networks, which are networks that consist of mobile nodes that communicate with each other without any fixed infrastructure or centralized control. 
- QoS in ad hoc networks is challenging due to the dynamic topology, limited resources, interference, mobility, and heterogeneity of the nodes and applications.  
- QoS in ad hoc networks can be achieved at different layers of the network stack, such as the application layer, the transport layer, the network layer, the MAC layer, and the physical layer.  
- QoS in ad hoc networks can be classified into two categories: hard QoS and soft QoS. Hard QoS guarantees the QoS requirements of the applications with strict bounds, while soft QoS provides the QoS requirements with probabilistic bounds or best-effort service.  
- QoS in ad hoc networks can be supported by various mechanisms, such as QoS-aware routing protocols, QoS-aware MAC protocols, QoS-aware scheduling algorithms, QoS-aware admission control, QoS-aware resource reservation, QoS-aware cross-layer optimization, etc.   
- QoS in ad hoc networks can be evaluated by various metrics, such as throughput, delay, jitter, packet delivery ratio, packet loss rate, energy consumption, etc.   
- QoS in ad hoc networks is an active research area that aims to provide better service quality for various applications, such as multimedia, voice, video, data, etc.



### Applications for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Ad hoc networks are wireless networks that do not rely on any fixed infrastructure or centralized control. They are composed of mobile nodes that communicate with each other using wireless links. Ad hoc networks have applications in various scenarios, such as disaster relief, military operations, vehicular networks, sensor networks, etc.
- Localization is the process of determining the position of a node in an ad hoc network, based on the information from other nodes or external sources. Localization is important for many applications that require location-awareness, such as routing, geocasting, tracking, etc. Localization can be achieved using various techniques, such as GPS, triangulation, range-based methods, etc.
- MAC issues refer to the challenges of designing a medium access control (MAC) protocol for ad hoc networks, which is responsible for coordinating the access to the shared wireless channel among the nodes. MAC issues include dealing with hidden and exposed terminals, collision avoidance, power control, fairness, etc. MAC protocols can be classified into contention-based and reservation-based protocols, depending on how they allocate the channel resources.
- Routing protocols are the algorithms that enable the nodes in an ad hoc network to discover and maintain routes to other nodes. Routing protocols can be categorized into proactive, reactive, and hybrid protocols, depending on how they update the routing information. Proactive protocols maintain routes to all destinations at all times, while reactive protocols discover routes on demand. Hybrid protocols combine the features of both proactive and reactive protocols.
- Global state routing (GSR) is a proactive routing protocol for ad hoc networks, which is based on the link state algorithm. GSR maintains a global view of the network topology at each node, by periodically exchanging link state packets among the nodes. GSR uses a shortest path algorithm to compute the routes to all destinations, based on the global topology information. GSR has advantages such as loop-free routing, low delay, and high reliability, but also disadvantages such as high overhead, scalability issues, and frequent updates.

