# ND for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

## Data Link Layer Protocols
- The data link layer provides service to the network layer and is responsible for reliable transmission of data frames over a physical medium.
- There are various protocols and standard technologies specified by different organizations for data link protocols in IoT.
- Some of the common data link layer protocols in IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It allows devices to form a personal area network (PAN) and exchange data and voice. It supports low-power and low-cost devices and has different versions such as Bluetooth Low Energy (BLE) and Bluetooth Mesh.
  - **Ethernet**: A wired LAN technology that uses a bus or star topology and a carrier sense multiple access with collision detection (CSMA/CD) protocol. It provides data transfer rates as high as 100 Mbps. It is a little bit costly and complex to set up and manage for IoT ecosystems.
  - **Wi-Fi**: A wireless LAN technology that uses radio waves to provide high-speed internet and network connections. It follows the IEEE 802.11 standards and supports various security protocols such as WEP, WPA, and WPA2. It is widely used for home and office networks and can connect multiple devices.
  - **WiMAX**: A wireless broadband technology that provides high-speed internet access over long distances. It follows the IEEE 802.16 standards and can support up to 75 Mbps data rates. It can be used for fixed or mobile wireless networks and can cover a large area.
  - **Low-rate WPAN**: A wireless personal area network that operates in the unlicensed frequency bands and supports low data rates and low power consumption. It follows the IEEE 802.15.4 standards and can support up to 250 kbps data rates. It can be used for sensor networks, smart home, and health care applications.
  - **Mobile communication**: A wireless communication network that uses cellular towers and satellites to provide voice and data services. It supports various generations of technologies such as 3G, 4G, and 5G. It can provide high-speed, low-latency, and reliable connectivity for IoT devices.
  - **NFC**: A short-range wireless communication technology that enables devices to exchange data by bringing them close to each other. It operates at 13.56 MHz frequency and can support up to 424 kbps data rates. It can be used for contactless payments, access control, and device pairing.

## Network Layer Protocols
- The network layer provides service to the transport layer and is responsible for addressing and routing of data packets over a network.
- There are various protocols and standard technologies specified by different organizations for network layer protocols in IoT.
- Some of the common network layer protocols in IoT are:

  - **IPv4**: The fourth version of the internet protocol that uses 32-bit addresses to identify devices on a network. It supports up to 4.3 billion addresses and uses various techniques such as NAT and DHCP to overcome the address exhaustion problem. It is widely used for internet communication and supports various routing protocols such as RIP, OSPF, and BGP.
  - **IPv6**: The sixth version of the internet protocol that uses 128-bit addresses to identify devices on a network. It supports up to 3.4 x 10^38 addresses and provides various features such as auto-configuration, security, and mobility. It is designed to support the growing number of IoT devices and supports various routing protocols such as RIPng, OSPFv3, and BGP4+.
  - **6LoWPAN**: A network layer protocol that enables IPv6 packets to be transmitted over low-power and low-bandwidth wireless networks such as IEEE 802.15.4. It uses header compression, fragmentation, and adaptation techniques to reduce the packet size and overhead. It can be used for sensor networks, smart grid, and smart city applications.
  - **RPL**: A routing protocol for low-power and lossy networks (LLNs) that operates on top of 6LoWPAN. It uses a directed acyclic graph (DAG) structure to form a routing topology and supports various routing metrics and objectives. It can be used for data collection, data dissemination, and multicast communication in IoT networks.
  - **CoAP**: A