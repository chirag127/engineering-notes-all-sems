### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- A distributed system has the following characteristics:
  - Concurrency: The components of a distributed system can execute concurrently, without interfering with each other.
  - No global clock: There is no global notion of time in a distributed system. Each component has its own local clock, which may not be synchronized with others.
  - Independent failures: The components of a distributed system can fail independently, without affecting the whole system. The system should be able to tolerate and recover from failures.
  - Heterogeneity: The components of a distributed system can have different hardware, software, network, and data formats. The system should be able to hide the heterogeneity from the users and provide a uniform interface.
- A distributed system has the following advantages:
  - Scalability: A distributed system can grow in size and performance by adding more components, without affecting the existing ones.
  - Availability: A distributed system can provide continuous service, even in the presence of failures, by replicating and distributing the data and computation across multiple components.
  - Fault tolerance: A distributed system can cope with failures, by detecting, masking, and recovering from them, without compromising the correctness and consistency of the system.
  - Transparency: A distributed system can hide the complexity and diversity of its components from the users, and provide a simple and consistent view of the system.
  - Resource sharing: A distributed system can allow the users to access and share the resources (such as data, files, devices, services, etc.) that are distributed across the system.