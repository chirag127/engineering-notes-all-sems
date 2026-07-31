### ETSI M2M

- ETSI M2M stands for European Telecommunications Standards Institute Machine-to-Machine. It is a standardization body that develops standards for IoT and M2M technologies.
- ETSI M2M is one of the founding partners of oneM2M, a global standards initiative that covers requirements, architecture, API specifications, security solutions and interoperability for M2M and IoT technologies.
- ETSI M2M defines a high-level architecture for an M2M system, as shown in the diagram below:

![ETSI M2M high-level architecture](https://www.researchgate.net/profile/Andrea-Ceselli/publication/308828235/figure/fig1/AS:414841648414720@1475585470432/ETSI-M2M-high-level-architecture.png)

- The architecture consists of three main layers: the Application Layer, the Service Capability Layer (SCL) and the Network Layer.
- The Application Layer contains the M2M applications that provide specific services to the end users or other applications. The applications can be hosted on different types of devices, such as M2M gateways, servers, smartphones or sensors.
- The Service Capability Layer provides common functions and capabilities to the applications, such as data management, device management, security, discovery, subscription and notification. The SCL is implemented as a software component that can run on different types of nodes, such as M2M gateways, servers or cloud platforms .
- The Network Layer provides the connectivity and transport services for the M2M communications. It can include different types of networks, such as M2M area networks, access networks, core networks or external networks .
- The architecture also defines a set of interfaces for the interactions between the different layers and nodes. The main interface is the Mca interface, which is a RESTful interface that allows the applications to access the SCL resources using HTTP methods. The SCL resources are structured as a hierarchical tree, where each resource has a unique identifier, attributes and sub-resources .
- The architecture also supports interworking with other M2M or IoT systems, such as ZigBee, Bluetooth, CoAP or OMA LWM2M, using the Mcn interface. The Mcn interface allows the SCL to exchange information with other systems using different protocols and data models .
- Security in the ETSI M2M framework is based on a combination of mechanisms, such as authentication, authorization, encryption, integrity, confidentiality and non-repudiation. The security mechanisms can be applied at different levels, such as the application layer, the SCL layer or the network layer .