# ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, the global standards initiative that covers requirements, architecture, API specifications, security solutions and interoperability for M2M and IoT technologies.
- ETSI M2M defines a high-level architecture for an M2M system, as shown in the figure below.

![ETSI M2M high-level architecture](https://www.researchgate.net/profile/Andrea-Ceselli/publication/308828235/figure/fig1/AS:416666302668800@1475840500000/ETSI-M2M-high-level-architecture.png)

- The architecture consists of three main layers: the M2M Device and Gateway layer, the M2M Network layer, and the M2M Service layer.
- The M2M Device and Gateway layer includes local networks of connected devices, sensors, and actuators, also called "objects". These objects can communicate with each other or with a gateway that acts as a proxy to connect them to the M2M Network layer.
- The M2M Network layer provides connectivity and transport services for the M2M data and control messages. It can use various network technologies, such as cellular, Wi-Fi, Bluetooth, ZigBee, etc.
- The M2M Service layer provides the core functionality of the M2M system, such as service discovery, data management, security, and application enablement. It consists of a set of service capabilities that are exposed through a common API.
- The M2M Service layer is based on a resource-oriented architecture, where each resource (such as a device, an application, a subscription, etc.) is identified by a unique URI and can be accessed or manipulated using RESTful methods (such as GET, PUT, POST, DELETE, etc.).
- The M2M Service layer also supports semantic interoperability, which means the ability to exchange and understand data across different domains and applications. It does so by defining a reference ontology and a common data model that describe the concepts and relationships of the M2M domain.
- The M2M Service layer also provides security mechanisms, such as authentication, authorization, encryption, and integrity protection, for the M2M communications and data. It uses various security protocols, such as TLS, DTLS, OAuth, etc..
- The M2M Service layer can interwork with different Machine Area Networks (MANs), which are local networks of devices that use specific protocols or standards, such as ZigBee, CoAP, MQTT, etc. It does so by using interworking proxies that translate the messages and data between the M2M Service layer and the MANs.