# IoT/M2M systems layers and design standardization

- IoT/M2M systems are composed of various components that communicate and interact with each other to provide services and applications for different domains and use cases.
- To enable interoperability and scalability of IoT/M2M systems, it is important to have a standardized architecture that defines the roles, functions, interfaces, and protocols of each component and layer.
- One of the most widely adopted IoT/M2M standardized architectures is the oneM2M architecture, which was developed by a global initiative of 14 standards development organizations (SDOs) and industry partners.
- The oneM2M architecture divides IoT/M2M functions into three major domains: the application layer, the service layer, and the network layer  .

## Application layer
- The application layer is the domain where the IoT/M2M applications reside and interact with the end users and devices.
- The application layer provides the business logic, user interface, data processing, and analytics for the IoT/M2M services and applications.
- The application layer can be hosted on different platforms, such as cloud, edge, or device, depending on the requirements and constraints of the use case.
- The application layer communicates with the service layer through standardized application programming interfaces (APIs), such as the oneM2M Common Service Functions (CSFs) and the oneM2M Base Ontology .

## Service layer
- The service layer is the domain that provides the common and generic functions and capabilities for the IoT/M2M systems, such as device management, data management, security, discovery, and notification.
- The service layer acts as an abstraction layer that hides the heterogeneity and complexity of the underlying network layer and devices from the application layer.
- The service layer can be distributed across different nodes, such as gateways, servers, or devices, depending on the deployment scenario and the network topology.
- The service layer communicates with the network layer through standardized network protocols, such as HTTP, CoAP, MQTT, or WebSocket .

## Network layer
- The network layer is the domain that provides the connectivity and transport for the IoT/M2M systems, such as wireless, wired, or cellular networks.
- The network layer supports different communication technologies and standards, such as Bluetooth, Zigbee, Wi-Fi, LoRa, LTE-M, NB-IoT, or EC-GSM-IoT .
- The network layer enables the data transmission and reception between the devices and the service layer nodes, as well as between the service layer nodes themselves.
- The network layer also provides the network management, routing, addressing, and security functions for the IoT/M2M systems .

## References
: https://www.linkedin.com/pulse/onem2m-iot-standardized-architecture-nikita-suchak
: https://educatech.in/onem2m-iot-standardized-architecture/
: https://www.slideshare.net/FabMinds/m2m-systems-layers-and-designs-standardizations
: https://www.digikey.com/en/articles/application-layer-protocol-options-for-m2m-and-iot-functionality
: https://www.etsi.org/technologies/internet-of-things