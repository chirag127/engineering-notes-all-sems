### ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for M2M and IoT technologies.
- It is one of the founding partners of oneM2M, the global standards initiative for M2M and IoT interoperability.
- ETSI M2M defines a high-level architecture for M2M systems, as shown in the figure below.

![ETSI M2M high-level architecture](https://www.researchgate.net/profile/Andrea-Ceselli/publication/308828235/figure/fig1/AS:409948075819008@1475580724496/ETSI-M2M-high-level-architecture.png)

- The architecture consists of three main layers: the M2M Device and Gateway layer, the M2M Network layer, and the M2M Service layer.
- The M2M Device and Gateway layer includes the devices, sensors, and actuators that communicate with each other or with the M2M Network layer through M2M Area Networks (MANs).
- The M2M Network layer provides connectivity and routing services for the M2M Device and Gateway layer and the M2M Service layer. It can use various network technologies, such as cellular, Wi-Fi, or Ethernet.
- The M2M Service layer provides the core functionality and intelligence of the M2M system. It consists of the M2M Service Capability Layer (SCL) and the M2M Applications.
- The M2M SCL is a middleware that enables the management, discovery, and access of M2M resources and services. It exposes a common Application Programming Interface (API) for the M2M Applications and the M2M Network layer.
- The M2M Applications are the software components that implement the specific logic and functionality of the M2M system. They can run on the M2M Devices, the M2M Gateways, or the M2M SCL.
- ETSI M2M also defines a resource structure for the M2M SCL, which is based on a hierarchical tree model. Each resource has a unique identifier, a set of attributes, and a set of sub-resources. The resources can be accessed and manipulated through the M2M API using CRUD (Create, Retrieve, Update, Delete) operations.
- ETSI M2M also specifies the interactions and protocols for the communication between the different layers and components of the M2M system. It supports various protocols, such as HTTP, CoAP, MQTT, or WebSocket.
- ETSI M2M also addresses the security aspects of the M2M system, such as authentication, authorization, encryption, and integrity. It defines a security framework that covers the M2M Device and Gateway layer, the M2M Network layer, and the M2M Service layer.
- ETSI M2M also supports the semantic interoperability of the M2M system, which is the ability to exchange and understand data and information across different domains and applications. It proposes a reference ontology and a semantic annotation mechanism for the M2M resources and services.