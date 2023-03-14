### Strawman Architecture for Enterprise-wide SOA for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture

- Strawman Architecture is the initial architecture that serves as a starting point for developing the target architecture .
- It is a high-level and abstract architecture that defines the main components and their interactions in an enterprise-wide SOA .
- It is not a complete or detailed architecture, but rather a conceptual model that can be refined and customized according to the specific requirements and constraints of the enterprise .
- The main components of the Strawman Architecture for Enterprise-wide SOA are :
  - Service Consumers: These are the applications or systems that invoke or consume the services provided by the SOA. They can be internal or external to the enterprise, and they can use various protocols and standards to communicate with the services. Examples of service consumers are web applications, mobile applications, desktop applications, etc.
  - Service Providers: These are the applications or systems that implement or provide the services in the SOA. They can be internal or external to the enterprise, and they can use various technologies and platforms to realize the services. Examples of service providers are legacy systems, databases, web services, etc.
  - Service Registry: This is a centralized repository that stores and manages the metadata and descriptions of the services in the SOA. It enables the discovery and lookup of the services by the service consumers and providers. It also facilitates the governance and monitoring of the services. Examples of service registry are UDDI, WSIL, etc.
  - Service Bus: This is a middleware layer that provides the connectivity and integration between the service consumers and providers. It enables the routing, transformation, mediation, orchestration, and security of the service interactions. It also provides the scalability, reliability, and performance of the SOA. Examples of service bus are ESB, JBI, SCA, etc.
- The main interactions of the Strawman Architecture for Enterprise-wide SOA are :
  - Service Publication: This is the process of registering and publishing the service metadata and descriptions to the service registry by the service providers. It enables the visibility and availability of the services to the service consumers and the service bus.
  - Service Discovery: This is the process of querying and finding the service metadata and descriptions from the service registry by the service consumers. It enables the selection and binding of the services by the service consumers.
  - Service Invocation: This is the process of sending and receiving the service requests and responses between the service consumers and providers through the service bus. It enables the execution and delivery of the services by the service providers and the service consumers.
- The main benefits of the Strawman Architecture for Enterprise-wide SOA are :
  - It provides a common and consistent architecture for the enterprise-wide SOA that can be reused and adapted across different domains and scenarios.
  - It enables the loose coupling and interoperability of the service consumers and providers, regardless of their technologies and platforms.
  - It facilitates the reuse and composition of the services, resulting in reduced development and maintenance costs and improved agility and flexibility.
  - It supports the governance and management of the services, ensuring the quality and reliability of the SOA.
- The main challenges of the Strawman Architecture for Enterprise-wide SOA are :
  - It requires a clear and comprehensive understanding of the business and technical requirements and constraints of the enterprise and the SOA.
  - It involves a significant amount of planning, design, development, testing, deployment, and maintenance of the SOA components and interactions.
  - It demands a high level of coordination and collaboration among the stakeholders and participants of the SOA, such as the business owners, service consumers, service providers, service registry, service bus, etc.

- A possible mnemonic to remember the main components of the Strawman Architecture for Enterprise-wide SOA is **SPRSB** (Service Providers, Service Registry, Service Bus). A possible learning trick is to associate each component with a word that starts with the same letter, such as **S**ervices, **P**roviders, **R**egistry, **S**ervice, **B**us.
- A possible ascii diagram to illustrate the Strawman Architecture for Enterprise-wide SOA is:

```
+-----------------+     +-----------------+     +-----------------+
| Service         |     | Service         |     | Service         |