## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system can tolerate some degree of failures.
  - Heterogeneity: The components can have different hardware, software, network, and data formats, and the system can cope with the diversity.
  - Scalability: The system can grow in size and complexity without losing its functionality and performance.
  - Transparency: The system can hide the details of its internal structure and behavior from the users, and provide a uniform interface and service.
- The main challenges of distributed systems are:
  - Coordination: The components need to synchronize their actions and share their states in order to achieve a common goal.
  - Consistency: The system needs to maintain a coherent view of the data and the processes among the components, despite the concurrency, failures, and heterogeneity.
  - Fault tolerance: The system needs to detect, isolate, and recover from the failures of the components, and provide reliable and available services.
  - Security: The system needs to protect the data and the processes from unauthorized access, modification, and disruption, and ensure the confidentiality, integrity, and authenticity of the information.