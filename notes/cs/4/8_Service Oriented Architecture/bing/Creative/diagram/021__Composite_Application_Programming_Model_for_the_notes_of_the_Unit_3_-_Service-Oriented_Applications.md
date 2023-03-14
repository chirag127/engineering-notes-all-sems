A composite application is a software application built by combining multiple existing functions into a new application. A composite application consists of functionality drawn from several different sources, such as existing modules, web services, or other applications. A composite application can also incorporate orchestration of local application logic to control how the composed functions interact with each other to produce the new, derived functionality. A composite application can be based on a service-oriented architecture (SOA), which is a design paradigm that promotes the use of loosely coupled, reusable, and interoperable services.

The following diagram illustrates the basic architecture of a composite application based on SOA:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application 1  |     |  Application 2  |     |  Application 3  |
|                 |     |                 |     |                 |
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
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Service 1      |     |  Service 2      |     |  Service 3      |
|                 |     |                 |     |                 |
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
       v                      v                      v
+---------------------------------------------------------------+
|                                                               |
|  Composite Application                                        |
|                                                               |
|  +-----------------+     +-----------------+     +----------+ |
|  |                 |     |                 |     |          | |
|  |  Component 1    |---->|  Component 2    |---->|  Output  | |
|  |                 |     |                 |     |          | |
|  +-----------------+     +-----------------+     +----------+ |
|                                                               |
+---------------------------------------------------------------+
```

The diagram shows how three existing applications (Application 1, Application 2, and Application 3) expose their functionality as services (Service 1, Service 2, and Service 3) that can be accessed by a composite application. The composite application consists of two components (Component 1 and Component 2) that orchestrate the services and produce an output. The components can be implemented using any technology or architecture, such as Java, .NET, or Web Services. The components can also communicate with each other using standard protocols, such as SOAP or REST. The composite application can be deployed on any platform that supports the components and the services. The composite application can also leverage other composite applications as sources of functionality.

The benefits of using a composite application programming model based on SOA are:

- Reusability: Existing applications and services can be reused to create new applications without modifying them.
- Flexibility: Components and services can be easily added, removed, or replaced to meet changing business requirements.
- Interoperability: Components and services can communicate with each other using standard protocols and formats, regardless of the underlying technology or platform.
- Scalability: Components and services can be distributed across multiple nodes to improve performance and availability.
- Maintainability: Components and services can be independently developed, tested, and deployed, reducing the complexity and cost of maintenance.