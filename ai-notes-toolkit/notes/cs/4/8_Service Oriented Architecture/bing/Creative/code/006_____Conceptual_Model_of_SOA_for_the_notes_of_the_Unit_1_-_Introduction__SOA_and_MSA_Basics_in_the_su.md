# Conceptual Model of SOA

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
  - Service: a software component that provides a specific functionality and can be accessed through a standard interface.
  - Service provider: an entity that owns and manages one or more services and exposes them to service consumers.
  - Service consumer: an entity that requests and uses services provided by service providers.
  - Service registry: a repository that stores information about available services and their interfaces, and allows service discovery and lookup.
  - Service broker: an intermediary that facilitates the communication and coordination between service providers and service consumers.
  - Service contract: a specification that defines the interface, quality of service, and policies of a service.
  - Service composition: a process of combining multiple services to create a new functionality or a higher-level service.
  - Service orchestration: a process of coordinating the execution of multiple services to achieve a business goal.
  - Service choreography: a process of defining the interactions and collaborations among multiple services without a central coordinator.
- A conceptual model of SOA can be illustrated by the following diagram:

![Conceptual model of SOA](https://www.researchgate.net/profile/Carlos-Parra-Caldern/publication/235720456/figure/fig1/AS:669784108728320@1536641543478/Conceptual-model-of-a-SOA-architectural-style.png)