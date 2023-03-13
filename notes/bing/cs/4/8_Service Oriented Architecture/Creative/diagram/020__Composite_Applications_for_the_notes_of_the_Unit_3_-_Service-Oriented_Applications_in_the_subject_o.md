A composite application is an application that consists of functionality drawn from several different sources, such as other applications, systems, or web services. A service-oriented architecture (SOA) is an architectural style that enables applications to be composed of loosely coupled and interoperable services. A service component architecture (SCA) is a software technology that provides a model for building applications and systems using SOA principles.

The following diagram illustrates the basic architecture of a composite application using SCA in a SOA context:

```
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  Service Client   |     |  Service Provider |     |  Service Provider |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  SCA Component    |     |  SCA Component    |     |  SCA Component    |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  SCA Reference    |---->|  SCA Service      |---->|  SCA Reference    |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  SCA Properties   |     |  SCA Properties   |     |  SCA Properties   |
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
|  SCA Implementation|    |  SCA Implementation|    |  SCA Implementation|
|                   |     |                   |     |                   |
+-------------------+     +-------------------+     +-------------------+
```

In this diagram, the service client and the service providers are SCA components that implement some business logic using a specific technology, such as Java, BPEL, or web services. The service client invokes the service providers using SCA references, which are abstract interfaces that define the contract and the policies for the service invocation. The service providers expose their functionality using SCA services, which are also abstract interfaces that define the contract and the policies for the service provision. The service client and the service providers can use SCA properties to configure their behavior and dependencies. The SCA references and services are connected by SCA bindings, which specify the protocol and the transport mechanism for the service communication. The SCA bindings can be based on open standards, such as web services, or proprietary technologies, such as JMS or RMI. The SCA components are deployed in SCA containers, which provide the runtime environment and the infrastructure for the SCA components. The SCA containers can be hosted by different platforms, such as application servers, web servers, or cloud platforms. The SCA containers can communicate with each other using SCA wires, which are logical connections that enable the service invocation across different SCA containers. The SCA wires can be configured and managed by SCA domains, which are administrative units that govern the SCA components and their interactions. The SCA domains can be federated or distributed to support scalability and reliability of the composite application.