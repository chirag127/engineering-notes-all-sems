# Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of the system can execute concurrently, without interfering with each other.
  - No global clock: The components of the system do not share a common notion of time, and may have different local clocks.
  - Independent failures: The components of the system can fail independently, without affecting the whole system.
  - Heterogeneity: The components of the system can have different hardware, software, network, and data formats.
- A distributed system has the following advantages:
  - Scalability: The system can grow in size and complexity, by adding more components or resources.
  - Availability: The system can tolerate failures and provide continuous service, by replicating or recovering the components.
  - Performance: The system can exploit parallelism and locality, by distributing the workload and data among the components.
  - Resource sharing: The system can allow the components to access and share common resources, such as files, printers, databases, etc.
- A distributed system has the following challenges:
  - Transparency: The system should hide the complexity and diversity of the components, and provide a uniform and consistent view to the users.
  - Coordination: The system should synchronize and coordinate the actions and states of the components, and ensure consistency and correctness.
  - Security: The system should protect the components and the data from unauthorized access, modification, or damage.
  - Fault tolerance: The system should detect and handle the failures of the components, and ensure reliability and availability.