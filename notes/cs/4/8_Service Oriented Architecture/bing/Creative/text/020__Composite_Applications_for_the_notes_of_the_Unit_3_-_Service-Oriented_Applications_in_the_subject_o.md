### Composite Applications

- A composite application is a software application built by combining multiple existing functions into a new application.
- A composite application can use business sources (e.g., existing modules or even web services) of information, while mashups usually rely on web-based, and often free, sources.
- A composite application can be built using any technology or architecture, but it is often associated with service-oriented architecture (SOA).
- In SOA, a composite application is created by combining one or more components that together implement the business logic of the new application.
- A component is an application program that implements the business logic and configuration information.
- A component offers a service to other components and in turn consumes functions offered by other services using service-oriented interfaces.
- A component can have one or more services and references, which are the internal interfaces for the component.
- A service is an addressable interface for the component that can contain one or more operations.
- A reference is a dependency on a service that is provided by another component.
- A component can also use bindings to describe the access mechanism that is used to communicate with other components.
- A composite is the unit of deployment in SCA and is described in an XML language called SCDL.
- A composite can contain components, services, references, property declarations, and the wiring that describes the connections between these elements.
- A composite can also be nested inside another composite, allowing for a hierarchical construction of composite applications.
- A composite can have external services and references, which are the interfaces for the composite that can be accessed by external clients or services.
- A composite can also use bindings to describe the access mechanism that is used to communicate with external entities.