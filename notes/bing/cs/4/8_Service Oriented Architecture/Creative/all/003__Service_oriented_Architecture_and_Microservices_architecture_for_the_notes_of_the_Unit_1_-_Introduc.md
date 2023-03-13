### Service oriented Architecture and Microservices architecture for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture

- Service oriented Architecture (SOA) is a software design approach that aims to create reusable and interoperable software components, or services, that can be accessed and composed across different applications and platforms .
- Microservices architecture (MSA) is a software design approach that builds applications as a collection of loosely coupled, fine-grained services, communicating through lightweight protocols .
- Both SOA and MSA rely on services as the main component, but they differ in terms of service characteristics, such as size, scope, granularity, autonomy, coupling, communication, governance, and deployment  .
- Some of the main differences between SOA and MSA are:

| SOA | MSA |
| --- | --- |
| Enterprise-wide scope | Application-specific scope |
| Services are coarse-grained and complex | Services are fine-grained and simple |
| Services are highly reusable and shareable | Services are highly specialized and independent |
| Services are tightly coupled and depend on a central service registry or bus | Services are loosely coupled and discoverable through service discovery mechanisms |
| Services communicate through standard protocols, such as SOAP or REST | Services communicate through lightweight protocols, such as HTTP, AMQP, or gRPC |
| Services are governed by a centralized authority or framework | Services are governed by a decentralized and agile approach |
| Services are deployed as a monolithic unit | Services are deployed as independent units |

- Some of the advantages of SOA are:

  - It promotes modularity and reusability of software components
  - It facilitates interoperability and integration of heterogeneous systems
  - It enables scalability and reliability of applications
  - It supports business agility and alignment of IT with business goals

- Some of the disadvantages of SOA are:

  - It introduces complexity and overhead in service design and development
  - It requires a high level of coordination and governance across the enterprise
  - It increases the risk of service failures and performance issues
  - It may lead to vendor lock-in and lack of flexibility

- Some of the advantages of MSA are:

  - It enables faster and easier development and deployment of services
  - It supports continuous delivery and innovation of applications
  - It enhances scalability and resilience of services
  - It fosters autonomy and collaboration of development teams

- Some of the disadvantages of MSA are:

  - It increases the operational and testing complexity of services
  - It requires a high level of service discovery and coordination
  - It introduces network latency and bandwidth consumption
  - It may result in data inconsistency and transaction management challenges

- Some of the examples of applications that use SOA are:

  - Enterprise Resource Planning (ERP) systems, such as SAP or Oracle
  - Customer Relationship Management (CRM) systems, such as Salesforce or Microsoft Dynamics
  - E-commerce platforms, such as Amazon or eBay

- Some of the examples of applications that use MSA are:

  - Streaming platforms, such as Netflix or Spotify
  - Social media platforms, such as Facebook or Twitter
  - Cloud computing platforms, such as AWS or Google Cloud

- Some of the mnemonics and learning tricks for SOA and MSA are:

  - SOA is like a library, where you can borrow and return books (services) from different shelves (applications) using a catalog (service registry) and a librarian (service broker).
  - MSA is like a market, where you can buy and sell goods (services) from different stalls (applications) using a map (service discovery) and a messenger (service communication).
  - SOA is more suitable for large and complex applications that need to integrate with multiple systems and platforms, while MSA is more suitable for small and simple applications that need to be agile and innovative.