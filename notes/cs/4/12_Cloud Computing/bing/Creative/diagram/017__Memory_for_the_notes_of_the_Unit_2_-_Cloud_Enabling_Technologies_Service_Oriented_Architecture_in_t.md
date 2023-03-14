The following is a detailed ascii diagram for Memory for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing.

### Memory for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Service        |      |  Service        |      |  Service        |
|  Consumer       |      |  Consumer       |      |  Consumer       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       +-----------------------+-----------------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Service        |      |  Service        |      |  Service        |
|  Provider       |      |  Provider       |      |  Provider       |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The diagram illustrates the basic architecture of a Service Oriented Architecture (SOA) in which multiple service consumers and service providers interact through a common interface. The service consumers are applications that request services from the service providers, which are applications that expose functions or data as services. The service interface is a contract that defines the inputs, outputs, and protocols for the service communication. The service interface can be implemented using standards like Web Service Definition Language (WSDL), SOAP, or RESTful HTTP. The service consumers and providers can be written in different programming languages, run on different platforms, and use different data formats, as long as they adhere to the service interface. The service consumers and providers can also be deployed as Docker containers, which provide isolation, portability, and scalability. The service communication can be mediated by an Enterprise Service Bus (ESB), which is a software component that performs integration, routing, transformation, and orchestration of the service messages. The ESB can also provide additional features like security, monitoring, logging, and governance of the service interactions. The