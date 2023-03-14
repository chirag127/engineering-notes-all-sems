### Memory for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

- Service Oriented Architecture (SOA) is a method of software development that uses software components called services to create business applications  .
- Each service provides a business capability, and services can also communicate with each other across platforms and languages  .
- Developers use SOA to reuse services in different systems or combine several independent services to perform complex tasks  .
- SOA is a key enabling technology for cloud computing as it enables the creation of loosely coupled services that can be easily integrated and reused.
- SOA has several benefits over the traditional monolithic architectures, such as faster time to market, efficient maintenance, and greater adaptability .
- SOA follows some basic principles, such as interoperability, loose coupling, reusability, and service contract  .
- SOA services are often defined using Web Service Definition Language (WSDL) and exposed using standard network protocols, such as SOAP/HTTP or RESTful HTTP  .
- SOA services are controlled by service governance and published in a service registry that enables developers to find and reuse them.
- SOA services can be built from scratch or by exposing functions from legacy systems of record as service interfaces.
- SOA services can be connected through an enterprise service bus (ESB), which is an architectural pattern that performs integrations between applications.

A possible mnemonic to remember the basic principles of SOA is:

**I Love Reading Stories**

- **I**nteroperability
- **L**oose coupling
- **R**eusability
- **S**ervice contract

A possible diagram to illustrate the SOA architecture is:

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
       v                         v                         v
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
                                 v
+-----------------+
|      ESB        |
+-----------------+
```