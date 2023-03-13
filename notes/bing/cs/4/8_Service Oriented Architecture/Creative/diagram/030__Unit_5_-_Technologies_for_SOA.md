## Unit 5 - Technologies for SOA

Service-Oriented Architecture (SOA) is a software development model that allows services to communicate across different platforms and languages to form applications. In SOA, a service is a self-contained unit of software designed to complete a specific task.

SOA is independent of vendors and technologies. This means a wide variety of products can be used to implement the architecture. The decision of what to use depends on the end goal of the system. SOA is typically implemented with web services such as simple object access protocol (SOAP) and web services description language (WSDL).

The following diagram illustrates the basic architecture of a SOA system using web services:

```
+-----------------+     +-----------------+     +-----------------+
| Service Request |     | Service Broker  |     | Service Provider|
|or Service Client|     | or Service      |     | or Service      |
|                 |     | Registry        |     | Implementation  |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
      |<----------------------|---------------------->|
      |   Find Service        |   Publish Service     |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |---------------------->|---------------------->|
      |   Bind Service        |   Bind Service        |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |<--------------------------------------------->|
      |   Invoke Service      |   Invoke Service      |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |<--------------------------------------------->|
      |   Receive Response    |   Receive Response    |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      V                       V                       V
```

The diagram shows the following steps:

1. The service provider publishes the service to the service broker using WSDL.
2. The service requestor finds the service from the service broker using UDDI (Universal Description, Discovery and Integration).
3. The service requestor binds to the service provider using SOAP.
4. The service requestor invokes the service using SOAP messages.
5. The service provider executes the service and returns the response using SOAP messages.