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
- A conceptual model of SOA can be represented by UML (Unified Modeling Language), which is a standard notation for describing software systems.
- A conceptual model of SOA consists of entities and their relationships, such as:
  - Service: a software component that provides a specific functionality and can be invoked by other components.
  - Service provider: an entity that owns and manages one or more services.
  - Service consumer: an entity that uses one or more services provided by other entities.
  - Service contract: a specification of the interface, behavior, quality, and policies of a service.
  - Service registry: a repository that stores and publishes information about available services and their contracts.
  - Service bus: a middleware layer that facilitates communication and integration among services and service consumers.
  - Service composition: a process of combining multiple services to create a new functionality or a higher-level service.
  - Service orchestration: a process of coordinating the execution of multiple services to achieve a business goal.
  - Service choreography: a process of defining the interactions and dependencies among multiple services without a central coordinator.
- A conceptual model of SOA can be illustrated by the following diagram:

```
+-----------------+       +-----------------+
| Service         |       | Service         |
| Consumer        |       | Provider        |
+-----------------+       +-----------------+
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | Service     | |       | | Service     | |
| | Contract    | |       | | Contract    | |
| +-------------+ |       | +-------------+ |
|                 |       |                 |
+-----------------+       +-----------------+
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         |                       |
         +-----------------------+
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |
                 |