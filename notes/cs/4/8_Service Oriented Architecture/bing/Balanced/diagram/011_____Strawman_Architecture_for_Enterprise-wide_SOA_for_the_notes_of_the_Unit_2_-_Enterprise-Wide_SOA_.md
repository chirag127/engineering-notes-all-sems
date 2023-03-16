### Strawman Architecture for Enterprise-wide SOA

- Strawman Architecture is the initial architecture that serves as a starting point for developing the target architecture. It is refined over number of iterations and results in the development of the target architecture .
- Strawman Architecture for Enterprise-wide SOA consists of four layers: Presentation Layer, Business Process Layer, Service Layer and Data Layer.
- Presentation Layer: This layer provides the user interface for accessing the business processes and services. It can be implemented using various technologies such as web browsers, mobile devices, portals, etc.
- Business Process Layer: This layer defines the business logic and workflows that orchestrate the services. It can be implemented using business process management (BPM) tools, enterprise service bus (ESB) or other integration technologies.
- Service Layer: This layer exposes the business functionality as reusable and interoperable services. It can be implemented using web services, RESTful services, microservices, etc.
- Data Layer: This layer provides the data access and persistence for the services. It can be implemented using relational databases, NoSQL databases, data warehouses, etc.
- Strawman Architecture for Enterprise-wide SOA can be represented as a diagram as shown below:

```
+-----------------+
| Presentation    |
| Layer           |
+-----------------+
        |
        |
        V
+-----------------+
| Business Process|
| Layer           |
+-----------------+
        |
        |
        V
+-----------------+
| Service Layer   |
+-----------------+
        |
        |
        V
+-----------------+
| Data Layer      |
+-----------------+
```