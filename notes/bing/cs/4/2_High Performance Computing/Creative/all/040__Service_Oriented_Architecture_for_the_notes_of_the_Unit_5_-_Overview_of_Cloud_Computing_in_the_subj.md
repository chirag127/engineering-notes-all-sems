### Service Oriented Architecture for the notes of the Unit 5 - Overview of Cloud Computing in the subject of High Performance Computing

- Service Oriented Architecture (SOA) is an architectural style that focuses on discrete services instead of a monolithic design.
- A service is a self-contained unit of functionality that provides a specific business capability  .
- Services can be composed and orchestrated to form applications that are built purely from existing services and combining them in an ad hoc manner.
- Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications and communicate with each other across platforms and languages .
- SOA aims to increase the agility, reusability, scalability, and interoperability of software systems  .

Some of the advantages of SOA are:

- It reduces the complexity and cost of software development and maintenance by enabling reuse of existing services and avoiding duplication of functionality  .
- It improves the alignment of business and IT by allowing services to be designed and implemented based on business requirements and processes  .
- It enhances the flexibility and adaptability of software systems by allowing services to be easily modified, replaced, or added without affecting the existing applications that use them  .
- It facilitates the integration and interoperability of heterogeneous systems and platforms by using standard protocols and formats for service communication  .

Some of the challenges of SOA are:

- It requires a significant cultural and organizational change to adopt a service-oriented mindset and governance model  .
- It introduces additional complexity and overhead in terms of service design, development, testing, deployment, and management  .
- It depends on the availability, reliability, performance, and security of the underlying network and infrastructure that support the service interactions  .
- It may face compatibility and interoperability issues due to the diversity and evolution of service standards and technologies  .

A simple example of SOA is a web-based application that uses services to perform various tasks, such as:

- A user interface service that provides the graphical user interface (GUI) for the application and handles the user input and output  .
- A business logic service that implements the core functionality and business rules of the application and processes the user requests  .
- A data access service that accesses and manipulates the data stored in a database or another data source and provides the data to the business logic service  .
- A security service that authenticates and authorizes the users and services and enforces the security policies and controls  .

The following diagram illustrates the example of SOA:

```
+-----------------+        +-----------------+        +-----------------+
| User Interface  |        | Business Logic  |        | Data Access     |
| Service         |        | Service         |        | Service         |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
| +-------------+ |        | +-------------+ |        | +-------------+ |
| | GUI         | |        | | Business    | |        | | Data        | |
| |             | |        | | Logic       | |        | | Access      | |
| +-------------+ |        | +-------------+ |        | +-------------+ |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
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
       +-------------------------+----------------