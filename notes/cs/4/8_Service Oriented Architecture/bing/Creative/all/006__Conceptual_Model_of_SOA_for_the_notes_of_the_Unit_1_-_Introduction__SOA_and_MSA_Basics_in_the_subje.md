### Conceptual Model of SOA for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture

- SOA stands for Service-Oriented Architecture, which is a software development model that allows services to communicate across different platforms and languages to form applications.
- A service is a self-contained unit of software designed to complete a specific task.
- Services are exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications.
- SOA is based on some defining concepts:
  - The business value is more important than the technical strategy.
  - The strategic goals are more important than benefits related to specific projects.
  - Basic interoperability is more important than custom integration.
  - Shared services are more important than implementations with a specific purpose.
  - Continued improvement is more important than immediate perfection.
- SOA has three major objectives:
  - To enable the reuse of existing applications and components in new business processes.
  - To facilitate the integration of applications and components across heterogeneous environments.
  - To improve the agility and flexibility of business processes in response to changing requirements and opportunities.
- A conceptual model of SOA can be represented by UML as shown in Figure 1.
- The model consists of the following entities and their relationships:
  - Service: A software component that provides a specific functionality and can be accessed through a well-defined interface.
  - Service Provider: An entity that owns and manages one or more services and exposes them to potential consumers.
  - Service Consumer: An entity that uses one or more services provided by service providers to achieve a business goal.
  - Service Registry: A repository that stores information about available services and their interfaces, and allows service discovery and lookup by service consumers.
  - Service Contract: A specification that defines the interface, behavior, quality, and policies of a service.
  - Service Invocation: A communication mechanism that enables a service consumer to request and receive a service from a service provider.
  - Service Composition: A process of combining multiple services to create a new service or application that provides higher-level functionality.
  - Service Orchestration: A coordination of service invocations in a predefined sequence or flow to achieve a business goal.
  - Service Choreography: A collaboration of service invocations in a decentralized manner without a central coordinator.

```
+-----------------+       +-----------------+       +-----------------+
| Service Provider|       | Service Consumer|       | Service Registry|
+-----------------+       +-----------------+       +-----------------+
| + Service       |       |                 |       | + Service       |
| + Service       |       |                 |       | + Service       |
| + Service       |       |                 |       | + Service       |
+-----------------+       +-----------------+       +-----------------+
| + publish       |       | + find          |       | + register      |
| + update        |       | + bind          |       | + update        |
| + delete        |       | + invoke        |       | + delete        |
+-----------------+       +-----------------+       +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +---------------------->|                       |
        |                       |                       |
        |                       +---------------------->|
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |<----------------------+
        |                       |                       |
        |<----------------------+                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +---------------------->|                       |
        |                       |                       |
        |                       |                       |
        |