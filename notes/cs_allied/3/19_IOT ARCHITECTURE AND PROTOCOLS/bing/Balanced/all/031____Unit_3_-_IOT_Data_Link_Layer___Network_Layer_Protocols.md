# Unit 3 - IOT Data Link Layer & Network Layer Protocols

## Data Link Layer Protocols

- The data link layer provides service to the network layer and is responsible for reliable transmission of data frames between nodes on the same network.
- There are various protocols and standard technologies specified by different organizations for data link protocols in IoT.
- Some of the common data link layer protocols in IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It allows devices to form a personal area network (PAN) and exchange data and voice. It supports low-power and low-cost devices and has different versions such as Bluetooth Low Energy (BLE) and Bluetooth Mesh.
  - **Ethernet**: A wired LAN technology that uses twisted pair or coaxial cables to connect devices. It provides data transfer rates as high as 100 Mbps and supports multiple topologies such as bus, star, and ring. It is widely used for industrial and enterprise IoT applications that require high reliability and security.
  - **Wi-Fi**: A wireless LAN technology that uses radio waves to provide internet access to devices. It supports various standards such as IEEE 802.11a/b/g/n/ac/ax and offers high data rates, range, and bandwidth. It is suitable for home and office IoT applications that require internet connectivity and interoperability.
  - **WiMAX**: A wireless broadband technology that provides high-speed internet access over long distances. It uses microwave frequencies and supports various standards such as IEEE 802.16d/e/m. It is designed for metropolitan area networks (MANs) and rural IoT applications that require wide coverage and mobility.
  - **Low-rate WPAN**: A wireless personal area network that operates at low data rates, low power, and short range. It uses various technologies such as Zigbee, Z-Wave, 6LoWPAN, and Thread. It is ideal for smart home and building IoT applications that require low-cost, low-complexity, and mesh networking.

## Network Layer Protocols

- The network layer is responsible for addressing and routing of data packets between nodes on different networks. It provides service to the transport layer and uses the data link layer for physical transmission.
- There are various protocols and standard technologies specified by different organizations for network layer protocols in IoT.
- Some of the common network layer protocols in IoT are:

  - **IPv4**: The most widely used internet protocol that assigns 32-bit addresses to devices and uses various routing protocols such as RIP, OSPF, and BGP. It supports various features such as fragmentation, checksum, and options. It suffers from address exhaustion and security issues in IoT.
  - **IPv6**: The next generation internet protocol that assigns 128-bit addresses to devices and uses various routing protocols such as RIPng, OSPFv3, and BGP4+. It supports various features such as auto-configuration, mobility, and security. It is designed to overcome the limitations of IPv4 and enable IoT scalability and interoperability.
  - **ICMP**: The internet control message protocol that is used to send error and control messages between devices. It supports various types of messages such as echo, destination unreachable, time exceeded, and parameter problem. It is used for diagnostic and troubleshooting purposes in IoT.
  - **CoAP**: The constrained application protocol that is a lightweight version of HTTP for resource-constrained devices. It uses UDP as the transport protocol and supports various features such as caching, discovery, and observation. It is used for RESTful web services and machine-to-machine communication in IoT.
  - **MQTT**: The message queuing telemetry transport protocol that is a publish-subscribe messaging protocol for IoT. It uses TCP as the transport protocol and supports various features such as quality of service, retain, and last will. It is used for data collection and distribution in IoT.