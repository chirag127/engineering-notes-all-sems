The following is a detailed ASCII diagram for Standards and Guidelines for SOA for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture.

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Service        |    |  Service        |
|  Consumer       |    |  Provider       |    |  Registry       |
|                 |    |                 |    |                 |
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
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Service        |    |  Service        |
|  Request        |    |  Description    |    |  Description    |
|                 |    |                 |    |                 |
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
       |                     |                     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Service        |    |  Service        |
|  Response       |    |  Contract       |    |  Discovery      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The diagram illustrates the basic architecture of a service-oriented system, which consists of three main components: service consumer, service provider, and service registry. The service consumer is the entity that requests and consumes the services offered by the service provider. The service provider is the entity that provides and implements the services. The service registry is the entity that maintains and publishes the information about the available services, such as their descriptions, contracts, and locations.

The diagram also shows the interactions among the components, which follow these steps:

1. The service consumer sends a service request to the service provider, specifying the service name, parameters, and expected output.
2. The service provider validates the service request and checks if it can fulfill it. If yes, it sends a service description to the service consumer, which contains the details of the service, such as its functionality, quality, and constraints. The service description is based on a standardized service contract, which is a formal agreement between the service provider and the service consumer on the terms and conditions of the service delivery.
3. The service consumer evaluates the service description and decides whether to accept or reject it. If accepted, it sends a service invocation to the service provider, which triggers the execution of the service logic.
4. The service provider performs the service logic and returns a service response to the service consumer, which contains the output and status of the service execution.
5. The service consumer receives the service response and processes the output and status accordingly.

The diagram also shows the role of the service registry, which facilitates the service discovery process. The service discovery is the process of finding and selecting the appropriate services for a given task or goal. The service registry enables the service discovery by storing and publishing the service descriptions of the registered service providers. The service consumer can query the service registry to find the services that match its requirements and preferences. The service registry can also notify the service consumer of any changes or updates in the service descriptions.

The diagram is based on the guiding principles of SOA, which are:

- Standardized service contract: Specified through one or more service description documents.
- Loose coupling: Services are designed as self-contained components, maintain relationships that minimize dependencies on other services.
- Abstraction: A service is completely defined by service contracts