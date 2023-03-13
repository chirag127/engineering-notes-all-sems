## Unit 1 - Characterization of Distributed Systems

- A distributed system is a collection of independent computers that appear to the users as a single coherent system.
- The main characteristics of distributed systems are:
  - Concurrency: Multiple components can execute simultaneously and interact with each other.
  - No global clock: There is no shared physical clock among the components, so synchronization and coordination are challenging.
  - Independent failures: Each component can fail independently, without affecting the whole system. Fault tolerance and recovery are essential.
  - Heterogeneity: The components can have different hardware, software, network, data formats, etc. Interoperability and compatibility are required.
- The main advantages of distributed systems are:
  - Scalability: The system can grow in size and performance by adding more components.
  - Availability: The system can tolerate failures and provide continuous service.
  - Resource sharing: The system can share data, hardware, software, etc. among the components and users.
  - Transparency: The system can hide the complexity and diversity of the components and provide a uniform interface to the users.
- The main disadvantages of distributed systems are:
  - Complexity: The system is more difficult to design, implement, debug, and maintain than a centralized system.
  - Security: The system is more vulnerable to attacks and unauthorized access, as there are more points of entry and communication channels.
  - Inconsistency: The system may have conflicting or outdated data, as there is no global state or agreement among the components.
  - Unpredictability: The system may have variable performance and behavior, as there are many factors that affect the communication and computation.

- A mnemonic to remember the characteristics of distributed systems is: **C**oncurrency, **N**o global clock, **I**ndependent failures, **H**eterogeneity (CNIH).
- A mnemonic to remember the advantages of distributed systems is: **S**calability, **A**vailability, **R**esource sharing, **T**ransparency (SART).
- A mnemonic to remember the disadvantages of distributed systems is: **C**omplexity, **S**ecurity, **I**nconsistency, **U**npredictability (CSIU).

- An example of a distributed system is the World Wide Web (WWW), which consists of web servers, web browsers, web pages, and other web resources that communicate over the Internet.
- An application of distributed systems is cloud computing, which provides on-demand access to shared computing resources, such as servers, storage, networks, software, etc.