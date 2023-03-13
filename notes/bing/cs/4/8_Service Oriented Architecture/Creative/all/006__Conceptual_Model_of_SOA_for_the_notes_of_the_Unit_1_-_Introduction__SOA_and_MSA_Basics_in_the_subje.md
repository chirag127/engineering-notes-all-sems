### Conceptual Model of SOA for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture

- Service-oriented architecture (SOA) is a software development model that allows services to communicate across different platforms and languages to form applications.
- A service is a self-contained unit of software designed to complete a specific task.
- SOA is an integration architectural style and an enterprise-wide concept .
- It enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications .
- The defining concepts of SOA are:
  - The business value is more important than the technical strategy.
  - The strategic goals are more important than benefits related to specific projects.
  - Basic interoperability is more important than custom integration.
  - Shared services are more important than implementations with a specific purpose.
- The conceptual model of SOA consists of four main components :
  - Service consumer: The entity that requests and uses a service.
  - Service provider: The entity that offers and delivers a service.
  - Service description: The metadata that defines the functionality, interface, quality, and policies of a service.
  - Service broker: The entity that facilitates the discovery and binding of services.
- The conceptual model of SOA can be illustrated as follows:

```
+-----------------+     +-----------------+     +-----------------+
| Service         |     | Service         |     | Service         |
| Consumer        |     | Provider        |     | Broker          |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| - Requests      |     | - Offers        |     | - Facilitates   |
|   service       |     |   service       |     |   discovery     |
| - Uses service  |     | - Delivers      |     | - Facilitates   |
|                 |     |   service       |     |   binding       |
+-----------------+     +-----------------+     +-----------------+
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
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------->                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        +---------------------------------------------->
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        <----------------------------------------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        <----------------------+                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
+-----------------+     +-----------------+     +-----------------+
| Service         |     | Service         |     | Service         |
| Consumer        |     | Provider        |     | Broker          |
+-----------------+     +-----------------+     +-----------------+
```
- A possible mnemonic to remember the four components of SOA is: **C**an **P**eople **B**e **D**ifferent? (**C**onsumer, **P**rovider, **B**roker, **D**escription).
- A possible learning trick to