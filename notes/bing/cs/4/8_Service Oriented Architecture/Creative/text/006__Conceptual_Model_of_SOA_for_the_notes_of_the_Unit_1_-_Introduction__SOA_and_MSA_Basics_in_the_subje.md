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
- A conceptual model of SOA consists of four main components :
  - Service consumer: the entity that requests and uses a service.
  - Service provider: the entity that offers and delivers a service.
  - Service description: the metadata that defines the functionality, interface, quality, and policies of a service.
  - Service broker: the entity that facilitates the discovery, binding, and invocation of services.
- A conceptual model of SOA can be depicted as follows:

```
+-----------------+     +-----------------+
| Service Consumer|     | Service Provider|
+-----------------+     +-----------------+
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
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
| Service Request |     | Service Response|
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
| Service Binding |     | Service Delivery|
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
| Service Discovery|    | Service Registry|
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
| Service Contract|     | Service Description|
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
| Service Broker  |     | Service Broker  |
+-----------------+     +-----------------+
```