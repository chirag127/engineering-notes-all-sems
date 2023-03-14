 Here is the content in markdown format for ### Theoretical Foundation for Distributed System for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Theoretical Foundation for Distributed System

The theoretical foundations of distributed systems include:

- Concurrency: Multiple processors executing simultaneously and interacting with each other. Need to handle race conditions and deadlocks.
- Modularity: System is divided into modules that interact. Need to define clean interfaces and handle faults at interfaces.
- Latency: Significant time delays in communication between components. Need to design systems that tolerate latency and make progress.
- Partial failure: Components may fail and recover, and different components may have different availability. Need to design fault-tolerant systems and handle partial failures.
- Lack of shared memory: Components do not share memory and must communicate via messages. Need to handle the additional complexity introduced by explicit communication.

Some key techniques used in distributed systems include:

- Consensus algorithms: Algorithms to achieve agreement among components in the presence of faults (e.g., Paxos, Raft).
- Atomic broadcast: Reliable delivery of messages to all components in the same order (e.g., total order broadcast).
- Replication: Maintaining copies of data or services on multiple machines to increase availability and performance. Need to handle consistency of replicated data.
- Distributed transactions: Performing transactions that access data on multiple machines in an atomic and consistent way (e.g., two-phase commit).
- Distributed file systems: Providing a file system interface to shared storage that is distributed across multiple machines.
- Distributed processing: Splitting up computational tasks across multiple machines to increase performance. Need to handle load balancing and fault tolerance.

Advantages of distributed systems include:

- Increased performance: Processing distributed across multiple machines can be faster.
- Increased availability: Redundancy can be used to handle machine failures and keep service running.
- Scalability: Easy to add more machines to handle growth.

Disadvantages include:

- Complexity: Distributed systems are more complex to program and debug.
- Partial failure: Complex to handle situation where only some components fail.
- Concurrency issues: Race conditions and deadlocks can be harder to avoid in distributed systems.
- Latency: Response times can be higher due to delays in communication.

Distributed systems are used in many applications, including:

- Web services: Using multiple servers to handle large numbers of users and requests.
- Cloud computing: Providing convenient access to large-scale computing resources.
- Databases: Distributed database systems provide scalability, high availability, and partitions tolerance.
- Peer-to-peer systems: Decentralized systems where nodes share resources directly.