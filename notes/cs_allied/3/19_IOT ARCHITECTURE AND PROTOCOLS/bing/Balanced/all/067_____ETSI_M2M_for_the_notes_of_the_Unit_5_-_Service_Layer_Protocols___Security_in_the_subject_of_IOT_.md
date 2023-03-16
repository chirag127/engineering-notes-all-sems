# ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, a global standards initiative that covers requirements, architecture, API specifications, security solutions and interoperability for M2M and IoT technologies.
- ETSI M2M defines a high-level architecture for an M2M system, as shown in the figure below.

![ETSI M2M high-level architecture](https://www.researchgate.net/profile/Andrea-Ceselli/publication/308828235/figure/fig1/AS:412973649305600@1475075283902/ETSI-M2M-high-level-architecture.png)

- The architecture consists of three main layers: the network layer, the service layer and the application layer.
- The network layer provides connectivity and transport services for M2M devices and gateways.
- The service layer provides common functions and capabilities for M2M applications, such as device management, data management, security, discovery and subscription.
- The service layer is implemented by the Service Capability Layer (SCL), which is a software component that exposes a RESTful API to the application layer and the network layer.
- The application layer provides specific functions and logic for M2M applications, such as smart metering, smart home, smart city, etc.
- The application layer interacts with the service layer through the M2M Application Entity (AE), which is a software component that represents an M2M application and its resources.
- The architecture supports different types of M2M networks, such as M2M area networks, M2M access networks and M2M core networks.
- The architecture also supports interworking with other standards and protocols, such as CoAP, MQTT, ZigBee, etc.

## Service Layer Protocols

- The service layer protocols are the protocols used by the SCL and the AE to communicate with each other and with the network layer.
- The service layer protocols are based on HTTP and CoAP, which are application layer protocols that support RESTful interactions.
- HTTP and CoAP are chosen because they are widely used, lightweight, scalable and interoperable protocols for web services and constrained devices.
- The service layer protocols define a common data model and a common resource structure for M2M resources, such as devices, applications, containers, subscriptions, etc.
- The service layer protocols also define a common set of operations and methods for creating, retrieving, updating and deleting M2M resources, such as POST, GET, PUT and DELETE.
- The service layer protocols use XML and JSON as the data formats for exchanging M2M resources and messages.
- The service layer protocols support different types of interactions, such as request/response, publish/subscribe and notification.

## Security

- Security is a key aspect of the ETSI M2M architecture, as it involves the protection of M2M devices, data, services and applications from unauthorized access, modification and disclosure.
- Security is addressed at different levels of the architecture, such as the network layer, the service layer and the application layer.
- Security is also addressed at different phases of the M2M lifecycle, such as the provisioning, the operation and the decommissioning of M2M devices and services.
- Security is based on a combination of mechanisms and techniques, such as encryption, authentication, authorization, access control, integrity, confidentiality, non-repudiation and auditability.
- Security is supported by different standards and protocols, such as TLS, DTLS, IPSec, OAuth, X.509, etc.
- Security is implemented by different components and entities, such as the M2M Security Entity (SE), the M2M Certificate Authority (CA), the M2M Trust Anchor (TA), etc.