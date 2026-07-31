### Introduction for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, and the clocks may drift apart over time.
  - Independent failures: Each component can fail independently without affecting the whole system, and the system can tolerate some degree of failures.
  - Heterogeneity: The components can have different hardware, software, network, and data formats, and the system can accommodate the diversity.
- The main challenges of distributed systems are:
  - Transparency: The system should hide the complexity and heterogeneity of the components from the users and provide a consistent and uniform interface.
  - Scalability: The system should be able to grow in size and performance without degrading the quality of service or requiring major changes in the design and implementation.
  - Reliability: The system should be able to cope with failures and errors of the components and ensure the correctness and consistency of the data and operations.
  - Security: The system should protect the data and resources from unauthorized access and malicious attacks, and ensure the confidentiality, integrity, and availability of the system.
- The main benefits of distributed systems are:
  - Resource sharing: The system can enable the access and utilization of distributed resources, such as files, printers, databases, and services, across the network.
  - Performance: The system can improve the speed and efficiency of the computation and communication by exploiting the parallelism and locality of the components.
  - Fault tolerance: The system can enhance the availability and reliability of the system by replicating and recovering the data and components in case of failures.
  - Flexibility: The system can adapt to the changing requirements and environments by adding, removing, or modifying the components without affecting the whole system.