Service Oriented Architecture (SOA) is an architectural style that aims to achieve loose coupling among interacting software agents. A service is a unit of work done by a service provider to achieve desired end results for a service consumer. Both provider and consumer are roles played by software agents on behalf of their owners.

Standards and guidelines for SOA are the specifications and protocols that enable services to communicate and interoperate with each other and with other systems. Standards and guidelines can help achieve interoperability, compatibility, portability, and integration across different platforms, languages, and vendors.

There are various organizations that publish standards and guidelines for SOA, such as the Organization for the Advancement of Structured Information Standards (OASIS), the Object Management Group (OMG), and The Open Group. These organizations have different scopes and focuses, but they also collaborate and align their work to some extent.

The following diagram illustrates the basic architecture of a SOA system and some of the standards and guidelines that apply to different layers and components:

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Service        |  |  Service        |  |  Service        |
|  Consumer       |  |  Consumer       |  |  Consumer       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Service        |  |  Service        |  |  Service        |
|  Provider       |  |  Provider       |  |  Provider       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
       |                  |                  |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Service        |  |  Service        |  |  Service        |
|  Implementation |  |  Implementation |  |  Implementation |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+

Service Consumer Layer: This layer represents the software agents that invoke services to fulfill their business or technical needs. Service consumers can be applications, components, or other services. Service consumers need to discover, bind, and invoke services using standard protocols and formats.

Some of the standards and guidelines that apply to this layer are:

- Service Component Architecture (SCA): A set of specifications that define a model for building applications and systems using a SOA approach. SCA aims to simplify the creation, implementation, and deployment of service consumers and providers. SCA is developed by OASIS.
- Service Oriented Modeling Framework (SOMF): A methodology for modeling and designing service-oriented systems. SOMF provides a set of concepts, principles, and best practices for identifying, specifying, and realizing services. SOMF is developed by the Methodologies Corporation.
- SOA Competency Framework: A framework that defines the knowledge, skills, and abilities required for professionals working in a SOA environment. The framework covers various roles and levels of expertise, such as service consumer, service provider, service architect, service analyst, service developer, service tester, service manager, and service governance. The framework is developed by the SOA Consortium.

Service Provider Layer: This layer represents the software agents that offer services to fulfill the requests of service consumers. Service providers can be applications, components, or