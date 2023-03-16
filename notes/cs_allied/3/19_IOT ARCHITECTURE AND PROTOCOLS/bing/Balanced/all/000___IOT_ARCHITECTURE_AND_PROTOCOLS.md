# IOT ARCHITECTURE AND PROTOCOLS

- IoT architecture refers to the many ways that IoT devices are structured to meet user needs. Based on complexity, IoT system elements are grouped into 3 to 7 layers, each with its own role.
- IoT protocols are the set of rules that enable communication between IoT devices, gateways, services, and data centers. Different IoT protocols have been designed and optimized for different scenarios and usage.
- The following are some of the common layers and protocols in IoT architecture:

## Device layer
- This layer consists of the physical devices and sensors that collect and transmit data. They can be embedded, wearable, mobile, or stationary.
- Some of the device layer protocols are:
  - Bluetooth: A short-range wireless protocol that enables data exchange between devices within a personal area network (PAN).
  - Zigbee: A low-power, low-data-rate wireless protocol that supports mesh networking and device-to-device communication.
  - Z-Wave: A wireless protocol that operates in the sub-GHz frequency band and is mainly used for home automation and smart appliances.
  - LoRa: A long-range, low-power wireless protocol that uses spread spectrum modulation and supports star and mesh topologies.

## Gateway layer
- This layer acts as a bridge between the device layer and the network layer. It performs data aggregation, filtering, preprocessing, and protocol translation.
- Some of the gateway layer protocols are:
  - MQTT: A lightweight, publish-subscribe protocol that enables bidirectional communication between devices and gateways.
  - CoAP: A web-based protocol that uses HTTP methods and RESTful architecture to enable constrained devices to interact with web services.
  - AMQP: An open, binary protocol that supports reliable, secure, and scalable messaging between devices, gateways, and data centers.

## Network layer
- This layer consists of the network devices and infrastructure that transport data from the gateway layer to the cloud or data center layer. It can use wired or wireless technologies, such as Ethernet, Wi-Fi, cellular, or satellite.
- Some of the network layer protocols are:
  - IPv4: The fourth version of the internet protocol that assigns 32-bit addresses to network devices and supports packet switching and routing.
  - IPv6: The sixth version of the internet protocol that assigns 128-bit addresses to network devices and supports end-to-end connectivity, security, and quality of service.
  - 6LoWPAN: A protocol that enables IPv6 packets to be transmitted over low-power wireless networks, such as Zigbee or Bluetooth.

## Cloud or data center layer
- This layer consists of the servers and databases that store, process, and analyze the data received from the network layer. It can use cloud computing platforms, such as Azure, AWS, or Google Cloud, or on-premise data centers.
- Some of the cloud or data center layer protocols are:
  - HTTP: A widely used protocol that enables data exchange between web browsers and web servers using request-response messages.
  - HTTPS: A secure version of HTTP that encrypts the data using SSL or TLS protocols.
  - WebSocket: A protocol that enables full-duplex, persistent communication between web browsers and web servers over a single TCP connection.

## Application layer
- This layer consists of the software applications and services that provide the user interface and functionality for the IoT system. It can use web, mobile, or desktop applications, or voice or chat assistants.
- Some of the application layer protocols are:
  - REST: A software architectural style that defines a set of constraints and principles for creating web services that are stateless, uniform, and cacheable.
  - SOAP: A protocol that uses XML-based messages to enable communication between web services and clients.
  - GraphQL: A query language and a runtime system that enables clients to specify the data they need from web services and receive it in a structured format.

## Security layer
- This layer consists of the mechanisms and techniques that ensure the confidentiality, integrity, and availability of the data and devices in the IoT system. It can use encryption, authentication, authorization, and auditing methods.
- Some of the security layer protocols are:
  - SSL: A protocol that creates a secure channel between two parties using asymmetric cryptography and digital certificates.
  - TLS