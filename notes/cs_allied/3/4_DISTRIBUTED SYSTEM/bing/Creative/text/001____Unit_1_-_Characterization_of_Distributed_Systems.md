## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently, without affecting the whole system. Fault tolerance and recovery are essential.
  - Heterogeneity: The components can have different hardware, software, network, and data formats. Interoperability and compatibility are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: The system can tolerate failures of some components, and still provide the service to the users.
  - Transparency: The system can hide the complexity and diversity of the components, and present a uniform and consistent interface to the users.
- The main challenges of distributed systems are:
  - Communication: The components need to exchange messages over unreliable and insecure networks, with variable delays and bandwidths.
  - Coordination: The components need to agree on common goals, actions, and states, despite the lack of global clock and the possibility of failures.
  - Consistency: The system needs to maintain a coherent and correct view of the data and the state, despite the concurrent and distributed updates.
  - Security: The system needs to protect the data and the resources from unauthorized access, modification, or disclosure.