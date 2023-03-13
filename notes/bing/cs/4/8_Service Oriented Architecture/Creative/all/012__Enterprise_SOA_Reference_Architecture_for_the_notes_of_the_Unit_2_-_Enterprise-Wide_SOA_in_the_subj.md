### Enterprise SOA Reference Architecture for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture

- Enterprise SOA Reference Architecture (SOA RA) is a set of guidelines and options for designing and implementing solutions based on Service-Oriented Architecture (SOA) principles and techniques.
- SOA RA has nine layers representing nine key clusters of considerations and responsibilities that typically emerge in the process of creating an SOA solution or defining an enterprise architecture standard.
- The nine layers of SOA RA are:

  - **Consumer Layer**: This layer represents the users or applications that consume the services provided by the SOA solution. It includes the consumer interface, the consumer components, and the consumer mediation.
  - **Business Process Layer**: This layer represents the business logic and workflows that orchestrate the services to achieve the business goals. It includes the process components, the process mediation, and the process management.
  - **Service Layer**: This layer represents the core functionality and capabilities that are exposed as services by the SOA solution. It includes the service components, the service mediation, and the service management.
  - **Service Component Layer**: This layer represents the implementation of the service components that provide the service functionality and capabilities. It includes the component implementation, the component context, and the component interaction.
  - **Operational Systems Layer**: This layer represents the existing systems and applications that are leveraged by the service components to access the data and functionality. It includes the system adapters, the system mediation, and the system management.
  - **Integration Layer**: This layer represents the integration technologies and patterns that enable the communication and interaction between the different layers and components of the SOA solution. It includes the messaging, the routing, the transformation, and the connectivity.
  - **Quality of Service Layer**: This layer represents the cross-cutting concerns and non-functional requirements that affect the quality and performance of the SOA solution. It includes the security, the reliability, the availability, the scalability, the monitoring, and the governance.
  - **Information Layer**: This layer represents the data and information that are used and exchanged by the SOA solution. It includes the data model, the data access, the data mediation, and the data management.
  - **Infrastructure Layer**: This layer represents the physical and logical resources and platforms that support the SOA solution. It includes the hardware, the software, the network, and the cloud.

- A possible mnemonic to remember the nine layers of SOA RA is: **C**an **B**ob **S**ell **S**ome **O**range **I**ce **Q**uickly **I**n **I**ndia? (Consumer, Business Process, Service, Service Component, Operational Systems, Integration, Quality of Service, Information, Infrastructure).
- A possible ascii diagram to illustrate the SOA RA layers is:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Consumer       |    |  Business       |    |  Service        |
|  Layer          |    |  Process        |    |  Layer          |
|                 |    |  Layer          |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Operational    |    |  Integration    |
|  Component      |    |  Systems        |    |  Layer          |
|  Layer          |    |  Layer          |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+    +-----------------+    +