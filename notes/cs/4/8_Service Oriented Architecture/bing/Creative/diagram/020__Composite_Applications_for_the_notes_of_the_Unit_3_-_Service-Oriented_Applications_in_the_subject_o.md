A composite application is a software application built by combining multiple existing functions into a new application. A composite application can be built using any technology or architecture, but service-oriented architecture (SOA) is a common approach that uses web services as the building blocks of the application .

A composite application consists of components that offer and consume services using service-oriented interfaces. A component can be a new or existing function that implements the business logic of the application. A component can have one or more services and references, which are the points of interaction with other components. A service is an addressable interface that can contain one or more operations, and a reference is a dependency on a service that is provided by another component.

A composite application is described by a composite, which is the unit of deployment in service component architecture (SCA). A composite is an XML document that defines the components, services, references, properties, and wiring of the application. A composite can also contain other composites, allowing for a hierarchical construction of the application.

The following diagram illustrates the basic architecture of a composite application using SCA:

```
+-----------------+    +-----------------+    +-----------------+
| Composite       |    | Composite       |    | Composite       |
| Service         |    | Service         |    | Service         |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Component   | |    | | Component   | |    | | Component   | |
| | Service     | |    | | Service     | |    | | Service     | |
| | Reference   | |    | | Reference   | |    | | Reference   | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Component   | |    | | Component   | |    | | Component   | |
| | Service     | |    | | Service     | |    | | Service     | |
| | Reference   | |    | | Reference   | |    | | Reference   | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
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
+-----------------+    +-----------------+    +-----------------+
| External Client |    | External Client |    | External Client |
+-----------------+    +-----------------+    +-----------------+
```

The diagram shows three composites, each with two components. The components have services and references that are used for internal communication within the composite. The composites also have services that are used for external communication with other composites or clients. The external clients can access the composite services using bindings that describe the access mechanism. The wiring between the components and the composites defines the connections and dependencies between the services and references.