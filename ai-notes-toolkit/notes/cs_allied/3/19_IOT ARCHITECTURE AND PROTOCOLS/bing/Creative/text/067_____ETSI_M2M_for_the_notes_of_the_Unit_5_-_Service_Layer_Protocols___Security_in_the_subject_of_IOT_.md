### ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine.
- It is a standardization body that develops standards for IoT and M2M technologies.
- It is one of the founding partners of oneM2M, the global standards initiative that covers requirements, architecture, API specifications, security solutions and interoperability for M2M and IoT technologies.
- ETSI M2M defines a high-level architecture for an M2M system, as shown in the figure below.

![ETSI M2M high-level architecture](https://www.researchgate.net/profile/Andrea-Ceselli/publication/308828235/figure/fig1/AS:413671906406400@1475580880000/ETSI-M2M-high-level-architecture.png)

- The architecture consists of three main layers: the network layer, the service layer and the application layer.
- The network layer provides connectivity and transport services for M2M devices and gateways.
- The service layer provides common functions and capabilities for M2M applications, such as device management, data management, security, discovery and subscription.
- The service layer is implemented by the Service Capability Layer (SCL), which is a software component that exposes a RESTful API to the application layer and the network layer.
- The SCL can be deployed in different entities, such as M2M devices, gateways, network nodes or cloud servers, depending on the use case and the deployment scenario.
- The application layer provides the business logic and the user interface for M2M applications, such as smart home, smart grid, e-health, etc.
- The application layer interacts with the service layer through the SCL API, which is based on HTTP and CoAP protocols.
- The SCL API defines a resource-oriented data model, where each resource represents an M2M entity, such as a device, a sensor, a container, a subscription, etc.
- The SCL API supports CRUD operations (Create, Retrieve, Update, Delete) on the resources, as well as notifications and group management.
- The SCL API also supports semantic interoperability, by allowing the use of ontologies and data models to describe the resources and their properties.
- Security in the ETSI M2M framework is based on the following principles:
  - Security by design: security requirements are considered from the beginning of the system design and implementation.
  - Defense in depth: security mechanisms are applied at different layers and domains of the system, such as the network, the service and the application layers.
  - End-to-end security: security mechanisms are applied to protect the data and the communication from the source to the destination, regardless of the intermediate nodes or entities.
  - Security adaptation: security mechanisms are adapted to the context and the environment of the system, such as the device capabilities, the network conditions, the user preferences, etc.
- Some of the security mechanisms that are used in the ETSI M2M framework are:
  - Authentication: the process of verifying the identity of an entity or a user that wants to access the system or a resource.
  - Authorization: the process of granting or denying access rights to an entity or a user based on their identity, role, policy, etc.
  - Encryption: the process of transforming the data into an unreadable form, using a secret key, to prevent unauthorized access or modification.
  - Integrity: the process of ensuring that the data has not been altered or corrupted during the transmission or the storage.
  - Non-repudiation: the process of ensuring that an entity or a user cannot deny their involvement in an action or a transaction.
  - Privacy: the process of protecting the personal or sensitive data of an entity or a user from unauthorized disclosure or misuse.