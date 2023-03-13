### Design of Activity Services (or Business Services) for Service Oriented Architecture

- Activity services (or business services) are software components that provide business capabilities and can communicate with each other across platforms and languages.
- Activity services are designed using service-oriented design methods, which are composition centric and focus on reusing existing services to create new applications.
- Activity services are based on common interface standards and an architectural pattern that enable interoperability and loose coupling.
- Activity services can be classified into three types: entity services, task services, and utility services.
  - Entity services are responsible for managing business entities and their data, such as customers, products, orders, etc. They provide CRUD (create, read, update, delete) operations and business rules for the entities.
  - Task services are responsible for orchestrating business processes and workflows, such as order processing, payment processing, inventory management, etc. They coordinate the interactions between entity services and utility services.
  - Utility services are responsible for providing common functionalities that are not specific to a business domain, such as logging, security, encryption, validation, etc. They support the entity services and task services.
- Activity services are designed following some principles and best practices, such as :
  - Service abstraction: hiding the implementation details of a service and exposing only the service interface to the consumers.
  - Service reusability: designing a service that can be used by multiple consumers and for multiple purposes, without modifying the service.
  - Service autonomy: designing a service that has control over its own logic and resources, and minimizing the dependencies on other services.
  - Service statelessness: designing a service that does not maintain any state information between requests, and relying on the consumers or a central repository to store the state information.
  - Service discoverability: designing a service that can be easily discovered and understood by the consumers, using metadata and documentation.
  - Service composability: designing a service that can be composed with other services to create new applications and functionalities.