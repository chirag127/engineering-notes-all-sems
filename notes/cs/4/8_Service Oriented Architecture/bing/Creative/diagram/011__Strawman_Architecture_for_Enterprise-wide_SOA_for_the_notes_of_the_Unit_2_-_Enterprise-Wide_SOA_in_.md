The Strawman Architecture for Enterprise-wide SOA is a high-level architecture that serves as a starting point for developing the target architecture for SOA based applications. It consists of the following components:

- Enterprise Service Bus (ESB): A middleware layer that provides communication, integration, routing, transformation, and orchestration capabilities for services.
- Service Registry: A repository that stores the metadata and policies of the services, and enables service discovery and governance.
- Service Providers: The applications or systems that expose their functionality as services, either through web services or other protocols.
- Service Consumers: The applications or systems that invoke the services provided by the service providers, either through web services or other protocols.
- Service Management: A component that monitors, controls, and secures the service interactions, and provides service level agreements, auditing, logging, and reporting features.

The following diagram illustrates the basic architecture of a Strawman Architecture for Enterprise-wide SOA using ASCII characters:

```
+-----------------+       +-----------------+
| Service         |       | Service         |
| Consumer        |       | Provider        |
+-----------------+       +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
| Enterprise      |       | Service         |
| Service Bus     |<----->| Registry        |
+-----------------+       +-----------------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-----------------+       +-----------------+
| Service         |       | Service         |
| Management      |       | Provider        |
+-----------------+       +-----------------+
```