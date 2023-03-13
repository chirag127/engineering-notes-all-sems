## Unit 2 - Cloud Enabling Technologies Service Oriented Architecture

Service-oriented architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design. Services are self-contained, loosely coupled, and communicate with each other using standard protocols and formats. Services can be composed and orchestrated to form complex business processes or applications.

A service-oriented architecture consists of the following components:

- Service consumer: The entity that requests and consumes a service from a service provider. It can be a human user, an application, or another service.
- Service provider: The entity that provides and exposes a service to a service consumer. It can be a software component, a system, or an organization.
- Service registry: The entity that maintains a directory of available services and their metadata, such as service description, location, interface, and quality of service. It enables service discovery and dynamic binding between service consumers and providers.
- Service broker: The entity that mediates the interaction between service consumers and providers. It can perform tasks such as routing, load balancing, security, and policy enforcement.
- Service bus: The entity that provides a common communication channel for service consumers and providers. It can support various protocols, formats, and message patterns, such as request/reply, publish/subscribe, and event-driven.

The following diagram illustrates the basic architecture of a service-oriented architecture using ASCII art:

```
+----------------+     +----------------+     +----------------+
| Service        |     | Service        |     | Service        |
| Consumer       |     | Registry       |     | Broker         |
+----------------+     +----------------+     +----------------+
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
       |                      +---------------------->                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |
       |                      |                      |                      |