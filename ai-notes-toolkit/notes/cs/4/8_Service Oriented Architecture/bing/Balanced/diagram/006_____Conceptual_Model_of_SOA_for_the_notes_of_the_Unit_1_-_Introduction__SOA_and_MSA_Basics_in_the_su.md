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
- A conceptual model of SOA can be represented by UML, as shown in the following diagram:

```
+-----------------+       +-----------------+       +-----------------+
|  Service        |       |  Service        |       |  Service        |
|  Provider       |       |  Consumer       |       |  Registry       |
+-----------------+       +-----------------+       +-----------------+
|  + Service      |       |  + Service      |       |  + Service      |
|  + Service      |       |  + Service      |       |  + Service      |
|  + Service      |       |  + Service      |       |  + Service      |
+-----------------+       +-----------------+       +-----------------+
|  + Publish      |       |  + Find         |       |  + Register     |
|  + Unpublish    |       |  + Bind         |       |  + Unregister   |
|  + Invoke       |       |  + Invoke       |       |  + Lookup       |
+-----------------+       +-----------------+       +-----------------+
```

- The service provider is the entity that offers one or more services to the service consumer.
- The service consumer is the entity that requests and uses the services offered by the service provider.
- The service registry is the entity that maintains a repository of information about the available services and facilitates the discovery and binding of services.
- The publish, unpublish, find, bind, invoke, register, unregister, and lookup are the operations that enable the interaction and communication among the service provider, consumer, and registry.