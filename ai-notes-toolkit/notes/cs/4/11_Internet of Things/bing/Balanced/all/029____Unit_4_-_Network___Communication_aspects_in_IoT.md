# Unit 4 - Network & Communication aspects in IoT

- IoT stands for Internet of Things, which refers to the interconnection of physical devices, sensors, actuators, and applications over the internet.
- IoT devices communicate with each other and with cloud services using various network and communication protocols, depending on the requirements and constraints of the application domain.
- Network and communication aspects in IoT include the following topics:

  - **Components for IoT device communication**: These are the elements that enable data transmission and reception among IoT devices and cloud services. They include:
    - IoT device: anything from the tiniest temperature sensor to a giant industrial robot
    - Local communications: the method the device uses to speak with neighboring devices, such as Bluetooth, Zigbee, Wi-Fi, etc.
    - Application protocol: the framework that defines how information content is transported, such as MQTT, CoAP, HTTP, etc.
    - Gateways: translate and re-transmit information, typically linking local device networks to the internet, such as routers, bridges, etc.
  - **Communication protocols in IoT**: These are the rules and standards that govern the data exchange and communication among IoT devices and cloud services. They vary in terms of functionality, reliability, security, scalability, and power consumption. Some of the common communication protocols in IoT are:
    - IPv6: the latest internet protocol version that is used for transferring data and communication. Each IoT device has an IP address and networking is the key aspect in the Internet of Things. Communication layer provides service to the network layer.
    - TCP/UDP: the transport layer protocols that ensure reliable and efficient data delivery. TCP is connection-oriented and guarantees data delivery, while UDP is connectionless and faster but less reliable.
    - MQTT: a lightweight publish-subscribe protocol that is designed for low-bandwidth and high-latency networks. It is widely used for IoT applications that require real-time data exchange and low power consumption.
    - CoAP: a web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and supports asynchronous communication and multicast requests.
    - HTTP: a ubiquitous web protocol that is used for transferring data and documents over the internet. It is based on the request-response model and supports various data formats and methods.
  - **Networking technologies in IoT**: These are the technologies that enable IoT devices to communicate with other devices, applications, and services running in the cloud. The internet relies on standardized protocols to ensure communication between heterogeneous devices is secure and reliable. Some of the networking technologies in IoT are:
    - Ethernet: a wired technology that connects devices using cables and switches. It is widely used for local area networks (LANs) and supports high-speed and reliable data transmission.
    - Wi-Fi: a wireless technology that connects devices using radio waves and access points. It is widely used for wireless local area networks (WLANs) and supports various standards and frequencies.
    - Cellular: a wireless technology that connects devices using cellular towers and mobile networks. It is widely used for wide area networks (WANs) and supports various generations and technologies, such as 2G, 3G, 4G, 5G, LTE, etc.
    - Bluetooth: a wireless technology that connects devices using short-range radio waves and personal area networks (PANs). It is widely used for device-to-device communication and supports various profiles and versions, such as Bluetooth Low Energy (BLE), Bluetooth Mesh, etc.
    - Zigbee: a wireless technology that connects devices using low-power radio waves and mesh networks. It is widely used for home automation and smart energy applications and supports various standards and frequencies, such as Zigbee 3.0, Zigbee PRO, etc.
  - **Challenges and opportunities in IoT networking and communication**: These are the issues and prospects that arise from the rapid growth and development of IoT applications and devices. They include:
    - Security and privacy: the protection of data and devices from unauthorized access, modification, or disclosure. IoT networks face various threats and vulnerabilities, such as eavesdropping, spoofing, denial-of-service, etc. IoT protocols and technologies need to provide encryption, authentication, authorization, and access control mechanisms to ensure security and privacy.
    - Scalability and interoperability: the ability to handle the increasing number and diversity of IoT devices and applications. IoT networks need to support various protocols, standards, and architectures to ensure seamless communication and integration among heterogeneous devices and services.
    - Reliability and quality of service: the assurance of consistent and satisfactory performance and functionality of IoT devices and applications