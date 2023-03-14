## Unit 5 - Technologies for SOA

- SOA, or service-oriented architecture, defines a way to make software components reusable and interoperable via service interfaces.
- Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications.
- Each service in an SOA embodies the code and data required to execute a complete, discrete business function (e.g. checking a customer’s credit, calculating a monthly loan payment, or processing a mortgage application).
- The service interfaces provide loose coupling, meaning they can be called with little or no knowledge of how the service is implemented underneath, reducing the dependencies between applications.
- Service interfaces are frequently defined using Web Service Definition Language (WSDL) which is a standard tag structure based on xml (extensible markup language).
- The services are exposed using standard network protocols—such as SOAP (simple object access protocol)/HTTP or Restful HTTP (JSON/HTTP)—to send requests to read or change data.
- Service governance controls the lifecycle for development and at the appropriate stage the services are published in a registry that enables developers to quickly find them and reuse them to assemble new applications or business processes.
- SOA benefits organizations by creating interoperability between apps and services. SOA will also ensure existing applications can be easily scaled, while simultaneously reducing costs related to the development of business service solutions.
- Some standard protocols to implement SOA include the following:
  - Simple Object Access Protocol (SOAP)
  - RESTful HTTP
  - Apache Thrift
  - Apache ActiveMQ
  - Java Message Service (JMS)
- You can even use more than one protocol in your SOA implementation.
- SOA is independent of vendors and technologies. This means a wide variety of products can be used to implement the architecture. The decision of what to use depends on the end goal of the system.
- SOA is typically implemented with web services such as simple object access protocol (SOAP) and web services description language (WSDL).
- An ESB, or enterprise service bus, is an architectural pattern whereby a centralized software component performs integrations between applications.
- The ESB provides a common communication channel for all the services, and handles the routing, transformation, security, and mediation of the service requests and responses.
- The ESB also enables service orchestration, which is the process of composing multiple services into a higher-level business process.
- The ESB can also provide service discovery, monitoring, and management capabilities.
- The ESB is not a mandatory component of SOA, but it can simplify the implementation and maintenance of complex service interactions.
- A diagram of a typical SOA with an ESB is shown below:

```
+-----------------+       +-----------------+       +-----------------+
|  Application A  |       |  Application B  |       |  Application C  |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
+-----------------+       +-----------------+       +-----------------+
|   Service A     |       |   Service B     |       |   Service C     |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
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
+-----------------+       +-----------------+       +-----------------+
|   Service D     |       |   Service E     |       |   Service F     |
+-----------------+       +-----------------+       +-----------------+
       |                         |                         |
       |                         |                         |
       |