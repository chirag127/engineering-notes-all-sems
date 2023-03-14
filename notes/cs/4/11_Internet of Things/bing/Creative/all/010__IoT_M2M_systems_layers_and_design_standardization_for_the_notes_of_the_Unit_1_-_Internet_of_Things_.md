### IoT/M2M systems layers and design standardization for the notes of the Unit 1 - Internet of Things (IoT) in the subject of Internet of Things

- IoT/M2M systems are systems that enable communication and data exchange between devices, applications, and services without human intervention.
- IoT/M2M systems require standardization to ensure interoperability, security, scalability, and efficiency of the solutions.
- One of the leading standardization initiatives for IoT/M2M systems is oneM2M, which was launched in 2012 by ETSI and 13 other founding members .
- The oneM2M architecture divides IoT functions into three major domains: the application layer, the service layer, and the network layer   .

#### Application layer
- The application layer is the domain where the end-user applications and services reside, such as smart home, smart city, e-health, etc.
- The application layer interacts with the service layer through a common Application Programming Interface (API) that abstracts the underlying network and device heterogeneity.
- The application layer can also use semantic interoperability standards, such as SAREF, to exchange data and context information with other applications and services.

#### Service layer
- The service layer is the domain that provides common functionalities and services for IoT/M2M systems, such as device management, data management, security management, discovery, subscription, notification, etc.
- The service layer acts as a middleware between the application layer and the network layer, and enables cross-domain and cross-platform interoperability.
- The service layer is composed of Common Service Entities (CSEs) that implement the oneM2M service layer functions and communicate with each other using a common protocol, such as HTTP, CoAP, MQTT, etc.
- The service layer also supports Context Information Management (CIM) protocols, such as NGSI-LD, that allow the exchange of data and context information among different IoT platforms and applications.

#### Network layer
- The network layer is the domain that provides the connectivity and transport mechanisms for IoT/M2M systems, such as cellular, Wi-Fi, Bluetooth, Zigbee, LoRa, etc.
- The network layer is responsible for addressing, routing, and delivering the data packets from the source to the destination devices or applications.
- The network layer can also provide Quality of Service (QoS), security, and reliability features for the IoT/M2M communication.

#### Mnemonics and learning tricks
- To remember the three domains of the oneM2M architecture, you can use the acronym **ASN** (Application, Service, Network).
- To remember the common functionalities and services of the service layer, you can use the acronym **DDSNS** (Device, Data, Security, Notification, Subscription).
- To remember the common protocols used in the service layer, you can use the acronym **HCM** (HTTP, CoAP, MQTT).
- To remember the semantic interoperability standards, you can use the acronym **SCN** (SAREF, CIM, NGSI-LD).