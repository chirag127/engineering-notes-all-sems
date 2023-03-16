### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of a distributed system can execute concurrently, without interfering with each other.
  - No global clock: There is no global notion of time in a distributed system. Each component has its own local clock, which may not be synchronized with others.
  - Independent failures: The components of a distributed system can fail independently, without affecting the whole system. The system should be able to tolerate and recover from failures.
  - Heterogeneity: The components of a distributed system can have different hardware, software, network, and data formats. The system should be able to cope with the diversity and complexity of the components.
- A distributed system has the following advantages:
  - Scalability: A distributed system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: A distributed system can provide continuous service, even in the presence of failures, by replicating and distributing the components across different locations.
  - Fault tolerance: A distributed system can handle partial failures, by detecting and masking them, or by providing alternative solutions.
  - Transparency: A distributed system can hide the details of the distribution from the users, by providing a uniform and consistent view of the system.
  - Resource sharing: A distributed system can enable the sharing of resources, such as data, files, devices, and services, among the components and the users of the system.