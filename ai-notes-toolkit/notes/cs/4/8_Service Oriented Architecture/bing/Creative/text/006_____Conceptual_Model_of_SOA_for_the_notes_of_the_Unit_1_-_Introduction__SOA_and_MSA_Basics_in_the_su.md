### Conceptual Model of SOA

- Service-oriented architecture (SOA) is a software development model that allows services to communicate across different platforms and languages to form applications.
- A service is a self-contained unit of software designed to complete a specific task.
- SOA is an integration architectural style and an enterprise-wide concept .
- It enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications .
- The defining concepts of SOA are:
  - The business value is more important than the technical strategy.
  - The strategic goals are more important than benefits related to specific projects.
  - Basic interoperability is more important than custom integration.
  - Shared services are more important than implementations with a specific purpose.
- A conceptual model of SOA can be represented by UML (Unified Modeling Language) diagrams that show the entities and their relationships in a SOA system.
- A conceptual model of SOA can consist of the following entities:
  - Service: A software component that provides a specific functionality and can be accessed through a standard interface.
  - Service provider: A software component that implements and exposes one or more services.
  - Service consumer: A software component that invokes and consumes one or more services.
  - Service registry: A software component that stores and publishes information about available services and their interfaces.
  - Service broker: A software component that facilitates the discovery and binding of services between service providers and service consumers.
  - Service contract: A specification of the interface, quality of service, and policies of a service.
  - Service composition: A process of combining multiple services to create a new functionality or a higher-level service.
  - Service orchestration: A process of coordinating the execution and interaction of multiple services to achieve a business goal.
  - Service choreography: A process of defining the global behavior and collaboration of multiple services without a central coordinator.
- A conceptual model of SOA can be illustrated by the following UML diagram:

![SOA conceptual model](https://www.researchgate.net/profile/Carlos-Parra-Caldern/publication/235720456/figure/fig1/AS:669972710932480@1536640620984/Conceptual-model-of-a-SOA-architectural-style.png)