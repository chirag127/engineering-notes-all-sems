## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can operate in parallel and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the ordering of events is based on logical clocks or timestamps.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system can tolerate partial failures.
  - Heterogeneity: The components can have different hardware, software, network, and data formats, and the system can handle the diversity and interoperability issues.
  - Transparency: The system can hide the complexity and diversity of the components from the users and provide a uniform interface and behavior.
- The main challenges of distributed systems are:
  - Communication: The system has to deal with network latency, bandwidth, reliability, and security issues, and provide efficient and reliable communication protocols and mechanisms.
  - Coordination: The system has to synchronize the actions and states of the components, and ensure consistency, atomicity, and durability of the data and operations.
  - Fault tolerance: The system has to detect, mask, and recover from the failures of the components, and provide availability, reliability, and resilience.
  - Scalability: The system has to cope with the increasing number of components, users, and requests, and provide performance, load balancing, and resource management.
  - Security: The system has to protect the data and operations from unauthorized access, modification, and disclosure, and provide authentication, authorization, confidentiality, integrity, and non-repudiation.