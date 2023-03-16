### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations to improve availability, performance, and fault tolerance of a distributed system.
- Transactions with replicated data involve executing operations on multiple copies of the same data item, while ensuring that the copies remain consistent and synchronized with each other.
- Some of the challenges and trade-offs of transactions with replicated data are:
  - How to propagate updates to all the replicas without causing conflicts or inconsistencies?
  - How to ensure serializability and isolation of concurrent transactions on different replicas?
  - How to handle failures and recoveries of replicas without losing or corrupting data?
  - How to balance the benefits of replication (such as availability, scalability, and locality) with the costs of replication (such as communication, synchronization, and storage overhead)?
- Some of the techniques and protocols for transactions with replicated data are:
  - Primary-copy replication: One replica is designated as the primary copy, which receives all the updates and propagates them to the other replicas (called secondary copies). The primary copy ensures serializability and isolation of transactions, while the secondary copies provide read-only access to the data. This approach simplifies the update propagation and consistency maintenance, but introduces a single point of failure and a bottleneck for write operations.
  - Quorum-based replication: Each replica has a vote on the validity of an update, and a quorum (a majority or a subset) of replicas must agree on the update before it is committed. This approach allows for fault tolerance and load balancing, but requires more communication and coordination among replicas, and may result in lower availability or consistency depending on the quorum size and composition.
  - Optimistic replication: Each replica can update its local copy independently, without waiting for the other replicas to agree. The updates are then reconciled periodically or on demand, using conflict detection and resolution mechanisms. This approach enables high availability and performance, but may incur more storage and computation overhead, and may lead to data divergence or loss if conflicts are not resolved correctly.