## Unit 1 - Introduction: SOA and MSA Basics

Service-oriented architecture (SOA) and microservice architecture (MSA) are two common service-based architectures that rely on services as the main component of an application. Services are self-contained, discrete, and repeatable units of software that perform specific tasks or functions. Services communicate with each other through service interfaces, which define the protocols and contracts for the interaction.

SOA and MSA have some similarities, such as:

- They both aim to increase modularity, scalability, and maintainability of applications by decomposing them into smaller and independent services.
- They both support service reuse and composition, which means that services can be used by multiple applications or combined to create new functionalities.
- They both follow some common design principles, such as abstraction, statelessness, discovery, and standardized contract.

However, SOA and MSA also have some significant differences, such as:

- SOA follows a "share as much as possible" approach, which means that services are designed to be generic and reusable across different domains and contexts. MSA follows a "share as little as possible" approach, which means that services are designed to be specific and bounded to a single domain or context.
- SOA emphasizes on business functionality reuse, which means that services are aligned with business processes and goals. MSA emphasizes on the concept of bounded context, which means that services are aligned with the domain model and language of a particular subdomain.
- SOA relies on a common governance and standards, which means that services are subject to the same rules and policies for development, deployment, and management. MSA relies on a relaxed governance and more freedom, which means that services can have different rules and policies depending on the team and the technology choices.
- SOA uses an enterprise service bus (ESB) for communication, which means that services are connected through a centralized middleware that handles routing, transformation, and orchestration. MSA uses a simple and less elaborate messaging system, which means that services are connected through a decentralized and lightweight mechanism that handles only basic communication.
- SOA uses multiple message protocols, such as SOAP, REST, and XML, which means that services can have different formats and styles for data exchange. MSA uses mostly REST and JSON, which means that services have a uniform and simple format and style for data exchange.
- SOA uses a common platform for all services deployed to it, which means that services have the same operating system, database, and runtime environment. MSA uses different platforms for different services, which means that services can have different operating systems, databases, and runtime environments.
- SOA is multi-threaded with more overheads to handle I/O, which means that services have more complexity and resource consumption for processing requests. MSA is single-threaded with less overheads to handle I/O, which means that services have less complexity and resource consumption for processing requests.
- SOA has a maximum application service reusability, which means that services can be used by many applications across different domains and contexts. MSA has a minimum application service reusability, which means that services are used by few applications within the same domain or context.
- SOA is more likely to use traditional relational databases, which means that services have a structured and normalized data model. MSA is more likely to use NoSQL databases, which means that services have an unstructured and denormalized data model.
- SOA is not preferred in a DevOps model, which means that services have a longer and more rigid development and deployment cycle. MSA is preferred in a DevOps model, which means that services have a shorter and more flexible development and deployment cycle.

The following diagram illustrates the basic architecture of a SOA and a MSA using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Application 1  |       |  Application 2  |       |  Application 3  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
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