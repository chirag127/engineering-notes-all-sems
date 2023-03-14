## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and independently, without interfering with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail or recover independently, without affecting the rest of the system.
  - Heterogeneity: The components may have different hardware, software, network, data formats, or protocols.
  - Scalability: The system can accommodate an increasing number of components, users, or resources, without degrading the performance or functionality.
  - Transparency: The system hides the complexity and diversity of its components from the users, and provides a consistent and uniform interface.
- The main challenges of distributed systems are:
  - Communication: The components need to exchange messages over unreliable and heterogeneous networks, and deal with issues such as latency, bandwidth, congestion, or loss.
  - Coordination: The components need to synchronize their actions and states, and agree on common decisions, without relying on a global clock or a central authority.
  - Fault tolerance: The system needs to cope with the failures of some components, and ensure the availability, consistency, and reliability of the services and data.
  - Security: The system needs to protect the confidentiality, integrity, and authenticity of the messages and data, and prevent unauthorized access or malicious attacks.
  - Resource management: The system needs to allocate and share the resources among the components, and balance the load and performance of the system.