## Unit 4 - Network & Communication aspects in IoT

The network and communication aspects in IoT are concerned with how IoT devices communicate with each other, with applications, and with services running in the cloud. The internet relies on standardized protocols to ensure communication between heterogeneous devices is secure and reliable. Protocols define the rules and formats that devices use to establish and manage networks and transmit data across those networks.

The following diagram illustrates the basic architecture of a network and communication layer in IoT:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Application   |      |   Application   |      |   Application   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Transport     |      |   Transport     |      |   Transport     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Internet      |      |   Internet      |      |   Internet      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Network       |      |   Network       |      |   Network       |
|   Access        |      |   Access        |      |   Access        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   Physical      |      |   Physical      |      |   Physical      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|    IoT Device   |      |    IoT Device   |      |    IoT Device   |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The network and communication layer in IoT can be divided into four sub-layers:

- Physical layer: This layer governs how each device is physically connected to the network with hardware, such as wires, cables, or radio waves in the case of wireless networks. Examples of physical layer technologies for IoT include Bluetooth, Wi-Fi, ZigBee, Z-Wave, LoRa, and cellular networks.
- Network access layer: This layer is responsible for physical addressing and delivering data frames to devices on the network. Each device is identified by a MAC address, which is a unique identifier assigned by the manufacturer. Examples of network access layer protocols for IoT include Ethernet, IEEE 802.11 (Wi-Fi), IEEE 802.15.4 (ZigBee), and IEEE 802.15.1 (Bluetooth).
- Internet layer: This layer is concerned with logical addressing and routing of data packets between source and destination hosts identified by IP addresses. IP addresses are assigned by the network administrator or dynamically by a protocol such as DHCP. The internet layer also handles fragmentation and reassembly of packets, as well as error detection and correction. Examples of internet layer protocols for IoT include IPv4, IPv6, ICMP, and UDP.
- Transport layer: This layer focuses on end-to-end communication and provides features such as reliability, congestion avoidance, and guaranteeing that packets will be delivered in the same order that they were sent. The transport layer also enables multiplexing and demultiplexing of data streams from different applications using port numbers. Examples of transport layer protocols for IoT include TCP, UDP, CoAP, and MQTT.