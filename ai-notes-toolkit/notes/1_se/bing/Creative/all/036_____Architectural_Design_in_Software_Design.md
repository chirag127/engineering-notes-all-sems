### Architectural Design in Software Design

- Architectural design is the process of defining the high-level structure and behavior of a software system, as well as the principles and guidelines for its development and evolution.
- Architectural design is concerned with finding a solution that satisfies the functional and non-functional requirements of the system, as well as the constraints and assumptions of the problem domain.
- Architectural design involves making decisions about the following aspects of a software system:
  - The components or modules that constitute the system and their interfaces.
  - The relationships and interactions among the components or modules.
  - The distribution and deployment of the components or modules across different platforms and environments.
  - The architectural styles or patterns that guide the design and implementation of the system.
  - The quality attributes or properties that the system should exhibit, such as performance, reliability, security, usability, etc.
  - The trade-offs and risks involved in the design choices and alternatives.
- Architectural design can be performed at different levels of abstraction and granularity, depending on the scope and complexity of the system and the stakeholders' needs and preferences.
- Architectural design can be documented using various notations and models, such as UML diagrams, architecture description languages, views and viewpoints, etc.
- Architectural design can be evaluated using various methods and techniques, such as reviews, analysis, simulation, testing, etc.

- A possible mnemonic to remember the aspects of architectural design is **CRISP-DAT**:
  - **C**omponents and interfaces
  - **R**elationships and interactions
  - **I**ntegration and deployment
  - **S**tyles and patterns
  - **P**roperties and attributes
  - **D**ecisions and trade-offs
  - **A**lternatives and risks
  - **T**ools and methods

- An example of an architectural design for a web-based e-commerce system is shown below:

```
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Web Browser   |<---->|   Web Server    |<---->|   Database      |
    |                 |      |                 |      |   Server        |
    +-----------------+      +-----------------+      +-----------------+
         |  ^                      |  ^                      |  ^
         |  |                      |  |                      |  |
         v  |                      v  |                      v  |
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   User          |      |   Business      |      |   Data          |
    |   Interface     |      |   Logic         |      |   Access        |
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+
```

- The system consists of three components: a web browser, a web server, and a database server.
- The web browser provides the user interface for the customers to browse and purchase products.
- The web server implements the business logic for processing the requests and transactions from the customers.
- The database server stores and manages the data related to the products, customers, orders, etc.
- The components communicate with each other using HTTP and SQL protocols.
- The system follows a client-server architectural style, where the web browser is the client and the web server and the database server are the servers.
- The system aims to achieve the following quality attributes: usability, availability, scalability, security, etc.