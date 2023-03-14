Service-Oriented Architecture (SOA) is an architectural style for building software applications that use services available in a network such as the web. It promotes loose coupling between software components so that they can be reused. Applications in SOA are built based on services. A service is an implementation of a well-defined business functionality, and such services can then be consumed by clients in different applications or business processes.

There are different tools and mechanisms for implementing SOA, such as web services, enterprise service bus, service registry, service orchestration, and service governance. Web services are the preferred standards-based way to realize SOA, as they use technologies such as XML, WSDL, SOAP, and UDDI to enable interoperability between heterogeneous systems. Enterprise service bus (ESB) is a middleware component that connects service consumers to services, and provides features such as routing, transformation, security, and monitoring. Service registry is a repository that stores information about the available services, such as their location, description, and policies. Service orchestration is the process of composing multiple services into a higher-level business process, using tools such as Business Process Execution Language (BPEL) or Business Process Model and Notation (BPMN). Service governance is the set of policies and practices that ensure the quality, consistency, and security of the services, and involves aspects such as service design, development, testing, deployment, and management.

The following diagram illustrates the basic architecture of a SOA-based system using web services, ESB, service registry, and service orchestration:

```
+-----------------+    +-----------------+    +-----------------+
| Service         |    | Service         |    | Service         |
| Consumer        |    | Consumer        |    | Consumer        |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
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
+-----------------+    +-----------------+    +-----------------+
| Web Service     |    | Web Service     |    | Web Service     |
+-----------------+    +-----------------+    +-----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +---------------------+---------------------+
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
+-----------------+    +-----------------+    +-----------------+
| Enterprise      |    | Service         |    | Service         |
| Service Bus     |    | Registry        |    | Orchestration   |
+-----------------+    +-----------------+    +-----------------+
```