According to the web search results, a pattern-based architecture for service-oriented applications is a way of designing and developing software systems that use reusable and interoperable components called services. Each service provides a specific business functionality and communicates with other services using standard protocols and interfaces. A pattern-based architecture follows some common principles and best practices to achieve the benefits of service orientation, such as faster time to market, efficient maintenance, and greater adaptability.

The following diagram illustrates the basic architecture of a pattern-based service-oriented application using ASCII characters:

```
+-----------------+       +-----------------+       +-----------------+
|  Service        |       |  Service        |       |  Service        |
|  Consumer       |       |  Provider       |       |  Registry       |
+-----------------+       +-----------------+       +-----------------+
|  - Application  |       |  - Business     |       |  - Service      |
|    logic        |       |    logic        |       |    descriptions |
|  - Service      |       |  - Service      |       |  - Service      |
|    interface    |       |    interface    |       |    discovery    |
|  - Service      |       |  - Service      |       |  - Service      |
|    discovery    |       |    contract     |       |    governance   |
|  - Service      |       |  - Service      |       |                 |
|    invocation   |       |    invocation   |       |                 |
+-----------------+       +-----------------+       +-----------------+
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
       |----------------------->|                        |
       |   Find service        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |----------------------->|
       |                        |   Publish service      |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |<-----------------------|
       |                        |   Return service       |
       |                        |   description          |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |<-----------------------|                        |
       |   Invoke service      |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |----------------------->|                        |
       |   Send request        |                        |
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
       |<-----------------------|                        |
       |   Receive response    |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       v                        v                        v
```

The diagram shows three main components of a pattern-based service-oriented application: the service consumer, the service provider, and the service registry. The service consumer is the application that needs to use the functionality of a service. The service provider is the component that implements the business logic of a service and exposes it through a service interface. The service registry is the component that stores the descriptions of the available services and allows the service consumer to discover and access them.

The diagram also shows the interactions between the components using arrows. The service consumer first finds the service it needs by sending a request to the service registry.