 Here is the content in markdown format for the topic - ### Service-oriented Analysis and Design (SOAD) Process for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture:

### Service-oriented Analysis and Design (SOAD) Process

The Service-oriented Analysis and Design (SOAD) process involves the following main steps:

1. **Identify candidate services:** This involves analyzing the problem domain and identifying the main business processes, data, and functions that could be delivered as services. Some techniques for identifying candidate services include:
- Identifying noun phrases in the problem description
- Looking for processes/functions that could be reusable across multiple business scenarios
- Identifying core data entities that could be exposed as services

2. ** Specify service interfaces:** For each candidate service, the inputs, outputs, preconditions, and postconditions are specified. The service contract is defined in a standard interface description language like WSDL. Functional and non-functional requirements for services are also specified.

3. **Design service implementations:** For each service, the backend implementation is designed. This could involve orchestrating other services, accessing databases, invoking legacy systems, etc. The service implementation should meet the specified functional and non-functional requirements.

4. **Composition of services:** The identified services are composed together to build complete business processes and applications. Service orchestration and choreography techniques are used to compose services.

Some additional activities in the SOAD process include:

- Analyzing existing systems and software for reuse opportunities
- Defining governance processes for the services
- Simulating and prototyping services and service compositions
- Testing and deploying the services

The SOAD process is iterative and incremental. As new requirements emerge or changes occur, the analysis and design steps can be revisited to update/redesign the services and service compositions.

[Include additional details/examples/diagrams if needed...]