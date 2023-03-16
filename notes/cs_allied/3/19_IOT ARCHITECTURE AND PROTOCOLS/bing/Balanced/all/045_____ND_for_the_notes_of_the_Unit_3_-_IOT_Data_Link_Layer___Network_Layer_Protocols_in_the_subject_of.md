# Unit 3 - IOT Data Link Layer & Network Layer Protocols

## Data Link Layer Protocols

- The data link layer provides service to the network layer and is responsible for reliable and efficient transmission of data frames between nodes on the same network.
- There are various protocols and standard technologies specified by different organizations for data link protocols in IoT.
- Some of the common data link layer protocols in IoT are:

  - **Bluetooth**: A short-range wireless communication network over a radio frequency. It allows devices to connect and exchange data with low power consumption and high security. Bluetooth supports different profiles for different applications, such as audio, health, smart home, etc. Bluetooth Low Energy (BLE) is a variant of Bluetooth that is optimized for IoT devices with low data rates and long battery life.
  - **Wi-Fi**: A wireless LAN technology that uses radio waves to provide high-speed internet access and network connectivity. Wi-Fi is widely used for home and office networks, as well as public hotspots. Wi-Fi supports various standards, such as 802.11a/b/g/n/ac/ax, that differ in frequency, bandwidth, range, and data rates. Wi-Fi is suitable for IoT applications that require high data throughput and low latency, such as video streaming, smart appliances, etc.
  - **Zigbee**: A low-power wireless mesh network protocol that operates in the 2.4 GHz frequency band. Zigbee is based on the IEEE 802.15.4 standard and supports various network topologies, such as star, tree, and mesh. Zigbee is designed for IoT applications that require low data rates, long battery life, and large network size, such as smart lighting, security, and environmental monitoring.
  - **Z-Wave**: A low-power wireless network protocol that operates in the sub-GHz frequency band. Z-Wave is based on the ITU-T G.9959 standard and supports a mesh network topology. Z-Wave is designed for IoT applications that require low data rates, long battery life, and interoperability, such as smart home, energy management, and healthcare.
  - **LoRa**: A long-range wireless network protocol that operates in the sub-GHz frequency band. LoRa is based on the LoRaWAN specification and supports a star-of-stars network topology. LoRa is designed for IoT applications that require low data rates, long range, and low power consumption, such as smart agriculture, smart city, and asset tracking.

## Network Layer Protocols

- The network layer provides service to the transport layer and is responsible for addressing and routing of data packets between nodes on different networks.
- There are various protocols and standard technologies specified by different organizations for network layer protocols in IoT.
- Some of the common network layer protocols in IoT are:

  - **IPv4**: The fourth version of the Internet Protocol that uses 32-bit addresses to identify nodes on a network. IPv4 is the most widely used network protocol on the internet and supports various features, such as fragmentation, checksum, and quality of service. IPv4 is suitable for IoT applications that require high reliability and compatibility, such as web services, cloud computing, and multimedia.
  - **IPv6**: The sixth version of the Internet Protocol that uses 128-bit addresses to identify nodes on a network. IPv6 is the successor of IPv4 and supports various features, such as auto-configuration, security, and mobility. IPv6 is suitable for IoT applications that require large address space and scalability, such as smart grid, smart transportation, and smart city.
  - **6LoWPAN**: A network protocol that enables IPv6 packets to be transmitted over low-power wireless personal area networks (LoWPANs), such as IEEE 802.15.4, Bluetooth, and Zigbee. 6LoWPAN is based on the RFC 4944 standard and supports various features, such as header compression, fragmentation, and adaptation. 6LoWPAN is suitable for IoT applications that require low power consumption and interoperability, such as sensor networks, smart home, and industrial automation.
  - **RPL**: A routing protocol that enables data packets to be routed over low-power and lossy networks (LLNs), such as IEEE 802.15.4, Bluetooth, and Zigbee. RPL is based on the RFC 6550 standard and supports various features, such as loop avoidance, multipath routing, and objective function. RPL is suitable for IoT applications that require low power consumption and robustness, such as sensor networks, smart home, and industrial automation.
  - **CoAP**: A network protocol that enables constrained devices to communicate with