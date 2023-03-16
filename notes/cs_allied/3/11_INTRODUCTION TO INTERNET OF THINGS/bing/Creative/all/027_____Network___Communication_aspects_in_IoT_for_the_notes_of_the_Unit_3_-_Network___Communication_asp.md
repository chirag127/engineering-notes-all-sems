# Network & Communication aspects in IoT

- IoT devices communicate with other devices, applications, and services over the internet using various protocols and technologies .
- IoT communication can be classified into three types: device-to-device, device-to-cloud, and device-to-gateway.
- Device-to-device communication enables direct data exchange between IoT devices without any intermediary. It can use short-range wireless technologies such as Bluetooth, Zigbee, or Wi-Fi, or long-range technologies such as cellular or satellite networks.
- Device-to-cloud communication connects IoT devices to cloud-based platforms or applications that provide data storage, processing, and analytics. It can use wired or wireless technologies such as Ethernet, Wi-Fi, cellular, or LPWAN.
- Device-to-gateway communication connects IoT devices to local or edge gateways that act as intermediaries between devices and the cloud. Gateways can translate and re-transmit data, provide security and authentication, and perform local processing and analytics .
- IoT communication involves several components, such as IoT devices, local communications, application protocols, and gateways.
- IoT devices are anything from the tiniest temperature sensor to a giant industrial robot that can sense, actuate, and communicate over the internet.
- Local communications are the methods that IoT devices use to speak with neighboring devices. They can be wired or wireless, and can use different standards and frequencies depending on the application and environment.
- Application protocols are the frameworks that define how information content is transported over the internet. They can be classified into two types: message-oriented and stream-oriented. Message-oriented protocols, such as MQTT, CoAP, and AMQP, are suitable for IoT applications that require low bandwidth, low latency, and high reliability. Stream-oriented protocols, such as HTTP, WebSocket, and XMPP, are suitable for IoT applications that require high throughput, bidirectional communication, and multimedia support .
- Gateways are devices that translate and re-transmit data between different networks, protocols, and formats. They can link local device networks to the internet, or connect different IoT platforms and applications. They can also provide security, authentication, and local processing and analytics for IoT devices.

## Wireless Medium access issues

- Wireless medium access issues refer to the challenges and trade-offs involved in sharing the wireless channel among multiple IoT devices that want to communicate simultaneously.
- Wireless medium access issues can affect the performance, reliability, and energy efficiency of IoT communication.
- Some of the wireless medium access issues are:

  - Interference: Interference occurs when multiple wireless signals overlap and degrade each other. Interference can be caused by other IoT devices using the same frequency band, or by external sources such as microwave ovens, cordless phones, or radio stations.
  - Collision: Collision occurs when two or more IoT devices transmit data at the same time and cause a loss of information. Collision can result in retransmissions, delays, and increased energy consumption.
  - Hidden terminal: Hidden terminal occurs when two IoT devices that are out of range of each other try to communicate with a common receiver and cause a collision. Hidden terminal can be mitigated by using techniques such as RTS/CTS (Request to Send/Clear to Send) or carrier sensing.
  - Exposed terminal: Exposed terminal occurs when an IoT device that is in range of a receiver refrains from transmitting data because it senses another transmission, even though the receiver is not affected by it. Exposed terminal can result in underutilization of the wireless channel and reduced throughput.
  - Fading: Fading occurs when the wireless signal strength varies due to changes in the environment, such as distance, obstacles, or mobility. Fading can cause errors, packet losses, and reduced signal-to-noise ratio.
  - Scalability: Scalability refers to the ability of the wireless network to accommodate a large number of IoT devices without compromising the quality of service. Scalability can be affected by factors such as network topology, routing protocols, medium access protocols, and resource allocation.

## MAC protocol survey

- MAC (Medium Access Control) protocols are the rules and mechanisms that coordinate the access and transmission of data over the wireless channel among multiple IoT devices.
- MAC protocols can be classified into two types: contention-based and contention-free.
- Contention-based MAC protocols allow IoT devices to compete for the wireless channel and transmit data