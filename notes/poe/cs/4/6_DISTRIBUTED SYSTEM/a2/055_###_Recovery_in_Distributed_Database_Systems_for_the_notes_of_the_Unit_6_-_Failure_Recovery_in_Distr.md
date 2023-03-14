 Here is the content in markdown format for the given topic:

### Recovery in Distributed Database Systems

For the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Recovery in distributed database systems involves recovering from failures of individual nodes or the communication between nodes in the system. The goal is to restore the database to a correct and consistent state after a failure.
- The key challenges in distributed database recovery are:
 - Ensuring that transactions are atomic, consistent, isolated, and durable (ACID properties) even in the face of failures.
 - Replicating data for fault tolerance can lead to consistency issues that need to be handled during recovery.
 - Limited bandwidth and the large amount of data that may need to be processed during recovery can lead to performance bottlenecks.

Some approaches to distributed database recovery:

- Log-based recovery: Maintain a log of operations that can be replayed to restore consistency. The log must be persistent and replicated/distributed for fault tolerance.
- Checkpointing: Periodically save state to stable storage. If a failure occurs, recovery starts from the latest checkpoint rather than having to replay all operations from the beginning of time. Checkpoints must be coordinated across nodes.
- Replication: Maintain multiple copies of the data, and during recovery reconstruct any missing or out-of-date data from other replicas. The replication strategy (synchronous vs. asynchronous, etc.) affects recovery performance and data consistency.

Advantages: Increased availability and fault tolerance.
Disadvantages: Complexity of coordination and more opportunities for inconsistency.

Applications: Databases that need high availability, e.g., banking systems, reservation systems.

Mnemonics:
- Think ACID for properties to maintain
- Log, check, replicate for approaches