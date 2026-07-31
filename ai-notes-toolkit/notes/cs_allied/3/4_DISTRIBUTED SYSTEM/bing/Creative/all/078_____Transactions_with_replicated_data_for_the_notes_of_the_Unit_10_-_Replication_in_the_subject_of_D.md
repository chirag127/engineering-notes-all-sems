# Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations, such as different servers or nodes, to improve data availability, reliability, and performance.
- Transactions with replicated data are transactions that involve accessing or modifying data that is replicated across a distributed system.
- Transactions with replicated data pose some challenges, such as:
  - How to ensure that the replicas are consistent and synchronized with each other and with the source data?
  - How to handle concurrency control and recovery of replicated data in the presence of failures or network partitions?
  - How to balance the trade-off between data consistency and availability in a distributed system?
- There are different approaches to address these challenges, such as:
  - Replication protocols: These are algorithms that define how the replicas are updated and synchronized with each other and with the source data. Some examples are primary-backup, quorum-based, gossip-based, and log-based replication protocols.
  - Transaction models: These are abstractions that define the semantics and guarantees of transactions with replicated data. Some examples are one-copy serializability, snapshot isolation, eventual consistency, and causal consistency.
  - Replication architectures: These are design choices that affect the performance and scalability of transactions with replicated data. Some examples are master-slave, peer-to-peer, hierarchical, and hybrid replication architectures.