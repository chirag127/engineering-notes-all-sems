## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently without affecting the whole system, so fault tolerance and recovery are important.
  - Heterogeneity: The components can have different hardware, software, network, data, and protocols, so interoperability and compatibility are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components without affecting the existing ones.
  - Availability: The system can tolerate failures of some components and still provide services to the users.
  - Transparency: The system can hide the complexity and diversity of the components from the users and provide a consistent and uniform interface.
  - Resource sharing: The system can allow the components to access and utilize the resources of other components, such as files, printers, sensors, etc.
- The main challenges of distributed systems are:
  - Communication: The system has to ensure reliable, efficient, and secure communication among the components over the network.
  - Coordination: The system has to coordinate the actions and states of the components to achieve a common goal or consistency.
  - Consistency: The system has to maintain a consistent view of the data and the system state among the components, despite concurrent updates and failures.
  - Security: The system has to protect the data and the system from unauthorized access, modification, or damage by malicious users or components.
  - Performance: The system has to optimize the use of the resources and the network to provide high-quality services to the users.