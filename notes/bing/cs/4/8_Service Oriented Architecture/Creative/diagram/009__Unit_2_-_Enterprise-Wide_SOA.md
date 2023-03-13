## Unit 2 - Enterprise-Wide SOA

Service-Oriented Architecture (SOA) is an integration architectural style and an enterprise-wide concept that enables existing applications to be exposed over loosely-coupled interfaces, each corresponding to a business function, that enables applications in one part of an extended enterprise to reuse functionality in other applications.

A basic diagram of an enterprise-wide SOA is shown below, using ASCII characters:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Application A  |     |  Application B  |     |  Application C  |
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
       |                      |                      |
       |                      |                      |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Service A      |     |  Service B      |     |  Service C      |
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
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Enterprise     |     |  Enterprise     |     |  Enterprise     |
|  Service Bus    |     |  Service        |     |  Service        |
|                 |     |  Registry       |     |  Repository     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram illustrates the following components of an enterprise-wide SOA:

- Applications: These are the existing software systems that provide business functionality and data. They can be legacy systems, packaged applications, custom applications, or web applications. They can be written in different languages, run on different platforms, and use different protocols and data formats.
- Services: These are the interfaces that expose the functionality and data of the applications in a standardized and reusable way. They can be implemented using web services standards, such as SOAP, WSDL, and UDDI, or other technologies, such as REST, JSON, and XML. Services are loosely coupled, meaning that they do not depend on the implementation details of the applications they interact with.
- Enterprise Service Bus (ESB): This is the middleware layer that enables communication and integration among the services. It provides capabilities such as routing, transformation, mediation, orchestration, security, and monitoring. It can also connect to other systems and services outside the enterprise, such as cloud services, partners, or customers.
- Service Registry: This is the directory that stores and publishes the information about the available services, such as their names, descriptions, locations, and contracts. It allows service consumers to discover and select the services they need.
- Service Repository: This is the repository that stores and manages the artifacts related to the services, such as their schemas, policies, contracts, and documentation. It supports the governance and lifecycle management of the services.