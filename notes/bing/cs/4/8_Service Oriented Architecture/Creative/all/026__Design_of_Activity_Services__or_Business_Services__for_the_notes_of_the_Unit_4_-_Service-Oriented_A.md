### Design of Activity Services (or Business Services) for the notes of the Unit 4 - Service-Oriented Analysis and Design in the subject of Service Oriented Architecture

- Activity services, also known as business services, are services that perform specific business functions or processes, such as order processing, inventory management, or customer service.
- Activity services are designed to be reusable, interoperable, and loosely coupled, following the principles of service-oriented architecture (SOA).
- The design of activity services involves the following steps :
  - Identify the business entities and processes that are relevant for the service domain, such as customers, orders, products, etc.
  - Model the business entities and processes using appropriate techniques, such as entity-relationship diagrams, business process models, use cases, etc.
  - Analyze the business entities and processes to identify the common and reusable functionalities that can be provided by activity services, such as create, read, update, delete, validate, etc.
  - Define the service contracts for the activity services, specifying the inputs, outputs, preconditions, postconditions, and quality attributes of each service operation, such as availability, reliability, security, etc.
  - Design the service logic for the activity services, using appropriate patterns, such as service facade, service controller, service orchestrator, etc., to implement the service contracts and coordinate the interactions among other services and resources.
  - Design the service interface for the activity services, using standard protocols and formats, such as SOAP, REST, XML, JSON, etc., to expose the service operations and enable communication with service consumers.
  - Design the service implementation for the activity services, using suitable technologies, such as Java, .NET, PHP, etc., to realize the service logic and interface and deploy the service on a service platform, such as a web server, an application server, a cloud platform, etc.

- A possible mnemonic to remember the steps of activity service design is **IMADDSI** (Identify, Model, Analyze, Define, Design, Implement).
- An example of an activity service is a Customer Service, which provides operations such as createCustomer, getCustomer, updateCustomer, deleteCustomer, validateCustomer, etc. The service contract, logic, interface, and implementation of this service can be designed following the steps above.