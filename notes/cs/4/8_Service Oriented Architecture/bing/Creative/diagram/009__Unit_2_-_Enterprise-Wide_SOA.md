## Unit 2 - Enterprise-Wide SOA

An enterprise-wide SOA is an architectural style that defines a way to make software components reusable and interoperable via service interfaces. Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications. This removes tasks from the application developer who previously redeveloped or duplicated existing functionality or had to know how to connect or provide interoperability with existing functions.

An enterprise-wide SOA enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications.

An enterprise-wide SOA also facilitates collaboration and integration across enterprises, by allowing services to be composed and orchestrated into business processes that span organizational boundaries.

The following diagram illustrates the basic architecture of an enterprise-wide SOA:

```
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Service         |       |  Service         |       |  Service         |
|  Consumer        |       |  Consumer        |       |  Consumer        |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Service         |       |  Service         |       |  Service         |
|  Registry        |       |  Registry        |       |  Registry        |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Service         |       |  Service         |       |  Service         |
|  Provider        |       |  Provider        |       |  Provider        |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
```

The diagram shows three service consumers, three service registries, and three service providers. Each service consumer is an application that needs to use some functionality provided by a service. Each service registry is a repository that stores information about the available services and their interfaces. Each service provider is an application that exposes some functionality as a service.

The service consumers use the service registries to discover and locate the services they need. The service registries act as brokers between the service consumers and the service providers. The service providers register their services and their interfaces with the service registries. The service consumers invoke the services through the service interfaces, which define the contract between the service consumer and the service provider.

The diagram is simplified for illustration purposes. In reality, there may be more or fewer service consumers, service registries, and service providers. There may also be other components involved in the enterprise-wide SOA, such as an enterprise service bus (ESB) that provides integration and mediation capabilities between the services, or a business process management (BPM) system that orchestrates the services into end-to-end business processes.