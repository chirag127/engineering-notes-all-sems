## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system should be able to tolerate and recover from failures.
  - Heterogeneity: The components may have different hardware, software, network, data formats, and protocols.
  - Scalability: The system should be able to grow in size and complexity without degrading its performance or functionality.
  - Transparency: The system should hide the details of its distribution from the users and provide a consistent and uniform interface.
- The main challenges of distributed systems are:
  - Communication: The components need to exchange messages over unreliable and heterogeneous networks, and deal with issues such as latency, bandwidth, congestion, and routing.
  - Coordination: The components need to synchronize their actions and agree on a consistent view of the system state, and cope with issues such as concurrency control, deadlock, and consensus.
  - Fault tolerance: The system needs to detect, mask, and recover from failures of components or communication links, and provide guarantees such as reliability, availability, and consistency.
  - Security: The system needs to protect its resources and data from unauthorized access, modification, or disclosure, and provide mechanisms such as authentication, authorization, encryption, and auditing.