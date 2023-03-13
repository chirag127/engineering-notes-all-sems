Service-Oriented Architecture (SOA) is an architectural style that enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications. SOA also defines a way to make software components reusable and interoperable via service interfaces that use common interface standards and an architectural pattern.

Some of the considerations for enterprise-wide SOA are:

- The scope and boundaries of the SOA initiative, which should align with the business goals and vision of the enterprise.
- The SOA roadmap, which should clearly delineate the phases and timelines for achieving SOA goals, and the metrics and criteria for measuring the success and value of SOA.
- The SOA governance, which should establish the roles, responsibilities, policies, standards, and processes for managing the design, development, deployment, and evolution of SOA services and solutions.
- The SOA infrastructure, which should provide the technical capabilities and platforms for enabling, securing, monitoring, and optimizing the service interactions and integrations.
- The SOA service portfolio, which should identify the existing and potential services that can be exposed, reused, and composed to support the business processes and functions of the enterprise.
- The SOA service design, which should follow the principles and best practices of service-orientation, such as loose coupling, abstraction, reusability, statelessness, discoverability, and composability.

The following diagram illustrates the basic architecture of a enterprise-wide SOA:

```
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  Business Process   |     |  Service Portfolio  |     |  Service Consumers  |
|  Management (BPM)   |     |  Management (SPM)   |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  Business Process   |     |  Service Registry   |     |  Service Discovery  |
|  Execution (BPE)    |     |  and Repository     |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  Service Orchestration  |  Service Mediation   |     |  Service Invocation |
|  and Choreography   |     |  and Routing        |     |                     |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
|                     |     |                     |     |                     |
|  Service Providers  |     |  Service Bus        |     |  Service Consumers  |
|                     |     |                     |     |                     |
+---------------------+     +---------------------+     +---------------------+
```