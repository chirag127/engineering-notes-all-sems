Patterns for SOA are common architectures, implementations, and their areas of application to help in the planning, implementation, deployment, operation, and ongoing management and maintenance of complex systems. Some of the patterns for SOA are:

- Agnostic Services: Agnostic services implement logic that is common to multiple business problems. They are reusable and loosely coupled. They can be declared as agnostic by using a naming convention or a metadata attribute.
- Atomic Service Transaction: Atomic service transactions ensure that a service can execute its logic in a single transactional unit, either succeeding or failing as a whole. They can be implemented by using a transaction manager or a compensation mechanism.
- Enterprise Service Bus (ESB): ESB is a middleware platform that provides services for integration, routing, transformation, and mediation of messages between service consumers and providers. It can also provide additional capabilities such as security, monitoring, and governance .
- Service Façade: Service façade is a service that acts as an intermediary between service consumers and providers. It can abstract, simplify, or enhance the service contract or the service logic of the underlying services. It can also provide additional features such as caching, throttling, or logging .
- Service Callback: Service callback is a pattern that allows a service to invoke another service asynchronously and receive a response at a later time. It can be implemented by using a callback contract, a callback endpoint, and a correlation mechanism .
- Multiple Service Contracts: Multiple service contracts allow a service to have different contracts for different consumers or scenarios. They can be based on different levels of abstraction, granularity, or functionality. They can also support different protocols, formats, or standards .
- Authentication Broker: Authentication broker is a service that centralizes the authentication logic for multiple services. It can validate the credentials of the service consumers and issue security tokens that can be used to access other services. It can also support different authentication mechanisms and policies .

The following diagram illustrates the basic architecture of a SOA system using some of these patterns:

```
+-----------------+     +-----------------+     +-----------------+
| Service Consumer|     | Service Consumer|     | Service Consumer|
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
        +----------------------|----------------------+
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
| Service Provider|     | Service Provider|     | Service Provider|
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
        +----------------------|----------------------+
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
| Authentication  |     | Service Façade  |     | ESB             |
| Broker          |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

: 10 Soa Design Patterns Every Architect Should Know
: SOA Patterns - DZone Refcardz
: SOA Patterns - Manning Publications
: SOA design patterns | Service oriented architecture | MuleSoft
[^5