The following is a detailed ASCII diagram for SOA Methodology for Enterprise for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture.

The diagram shows the main components and relationships of a SOA system, such as services, service consumers, service providers, service registry, service bus, and service governance.

The diagram uses the following symbols:

- [ ] : a service, which is a self-contained unit of functionality that can be invoked by a service consumer
- < > : a service consumer, which is an application or component that requests and uses services
- { } : a service provider, which is an application or component that implements and exposes services
- ( ) : a service registry, which is a repository that stores and publishes information about services
- - : a service bus, which is a communication channel that connects service consumers and providers
- + : a service governance, which is a set of policies and processes that manage the quality, security, and lifecycle of services

The diagram is as follows:

```
+-----------------+     +-----------------+
| Service         |     | Service         |
| Consumer 1      |     | Consumer 2      |
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
         v                       v
+-------------------------------------------------+
| Service Bus                                     |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
|                                                 |
+-------------------------------------------------+
         ^                       ^
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
| Service         |     | Service         |
| Provider 1      |     | Provider 2      |
+-----------------+     +-----------------+
         ^                       ^
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
         v                       v
+-----------------+     +-----------------+
| Service         |     | Service         |
| Registry 1      |     | Registry 2      |
+-----------------+     +-----------------+
         ^                       ^
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
         v                       v
+-----------------+     +-----------------+
| Service         |     | Service         |
| Governance 1    |     | Governance 2    |
+-----------------+     +-----------------+
```