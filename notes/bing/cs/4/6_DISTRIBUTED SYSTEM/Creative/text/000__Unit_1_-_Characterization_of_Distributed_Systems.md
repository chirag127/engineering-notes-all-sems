## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and ordering of events are challenging.
  - Independent failures: Each component can fail independently, without affecting the whole system. Fault tolerance and recovery mechanisms are essential.
  - Heterogeneity: The components can have different hardware, software, network, data formats, etc. Interoperability and standardization are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: The system can tolerate failures of some components, and still provide the service to the users.
  - Transparency: The system can hide the complexity and diversity of the components from the users, and present a uniform interface and behavior.
- The main challenges of distributed systems are:
  - Coordination: The components need to coordinate their actions and share information, while dealing with concurrency, failures, and heterogeneity.
  - Consistency: The system needs to ensure that the data and the state of the components are consistent, despite concurrent updates and replication.
  - Security: The system needs to protect the data and the resources from unauthorized access, modification, or disclosure, while allowing legitimate access and communication.