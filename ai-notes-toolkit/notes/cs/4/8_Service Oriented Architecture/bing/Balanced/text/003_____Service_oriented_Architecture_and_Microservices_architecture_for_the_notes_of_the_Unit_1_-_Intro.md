### Service oriented Architecture and Microservices architecture

- Service oriented architecture (SOA) is an enterprise-wide approach to software development of application components that takes advantage of reusable software components, or services.
- Microservices architecture (MSA) is an architectural pattern that arranges an application as a collection of loosely coupled, fine-grained services, communicating through lightweight protocols.
- The main distinction between the two approaches comes down to scope. SOA has an enterprise scope, while MSA has an application scope.
- SOA and MSA share some common principles, such as:
  - Service abstraction: Services hide their internal logic and expose only their interfaces to the outside world.
  - Service autonomy: Services are independent and self-contained, and can be deployed and updated without affecting other services.
  - Service reusability: Services can be reused across different applications or business domains, reducing duplication and increasing consistency.
  - Service composability: Services can be composed together to form higher-level business processes or functionalities.
- SOA and MSA differ in some aspects, such as:
  - Service granularity: SOA services tend to be coarse-grained, meaning they perform complex and comprehensive business functions, while MSA services tend to be fine-grained, meaning they perform simple and specific tasks.
  - Service governance: SOA services are governed by a central authority that defines and enforces standards, policies, and contracts, while MSA services are governed by a decentralized and agile approach that empowers teams to make their own decisions.
  - Service communication: SOA services communicate through a common enterprise service bus (ESB) that provides integration, orchestration, and mediation capabilities, while MSA services communicate through lightweight and simple protocols, such as REST or messaging.
  - Service deployment: SOA services are deployed as monolithic applications that require coordination and synchronization across the enterprise, while MSA services are deployed as independent and isolated units that can be scaled and updated independently.