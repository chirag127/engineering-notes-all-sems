 Here is the content in markdown format for Unit 1 - Characterization of Distributed Systems:

## Unit 1 - Characterization of Distributed Systems

- A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.
- The components interact with one another in order to achieve a common goal.
- The three significant characteristics of a distributed system are:
    - Concurrency: The components of a distributed system can work concurrently. They don't have to wait for each other to complete a task or finish an operation. This increases the performance and efficiency.
    - Lack of a global clock: There is no single clock in a distributed system that is shared by all components. Each computer has its own clock which can lead to issues like clock synchronization problems.
    - Independent failure: The components of a distributed system can fail independently. So, the system must be robust enough to handle such failures and continue functioning. This is achieved through redundancy and replication of components.
- Key properties of distributed systems:
    - Transparency: The distributed nature of the system should be hidden or transparent to the users. The system should appear as a single system to its users.
    - Reliability: The system should be fault-tolerant and reliable even in the presence of failures and unpredictable conditions.
    - Scalability: The system should be able to handle growth in the number of components and users efficiently.
    - Performance: The system should have adequate performance in terms of response time, throughput, and resource utilization.
- Advantages:
    - Increases resource sharing: Various resources can be shared across the system.
    - Improves reliability: The failure of one component does not affect the system as a whole. The system is fault-tolerant.
    - Scales easily: It is easy to add more machines and resources to handle growth.
    - Ostensible locality: Components can be placed close to the resources or users that they serve, thereby reducing latency.
- Disadvantages:
    - Complexity: Distributed systems are more complex to design, implement, and maintain due to issues like network delays, congestion, security threats, etc.
    - Difficult debugging and monitoring: It is harder to debug and monitor the system as a whole because of its distributed and asynchronous nature.
    - Inconsistent states: The system can lead to inconsistent states due to latency in message passing and lack of a global clock. Ensuring data consistency is challenging.