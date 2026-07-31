# Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is the process of copying and maintaining data in multiple locations to increase availability, performance, and fault tolerance.
- Transactions with replicated data are transactions that involve accessing and updating data that is replicated across multiple servers or nodes in a distributed system.
- Transactions with replicated data pose several challenges, such as:
  - How to ensure that the replicas are consistent and synchronized with each other?
  - How to handle concurrency and conflicts among transactions that access the same or different replicas?
  - How to recover from failures and maintain the ACID properties of transactions?
- There are different approaches to address these challenges, such as:
  - Primary-copy replication: One replica is designated as the primary or master, and the others are secondary or slave replicas. All updates are performed on the primary replica, and then propagated to the secondary replicas. Read operations can be performed on any replica. This approach simplifies consistency and concurrency control, but introduces a single point of failure and a bottleneck for updates.
  - Update-everywhere replication: All replicas are equal, and updates can be performed on any replica. The replicas communicate with each other to coordinate and propagate the updates. Read operations can be performed on any replica. This approach improves availability and performance, but complicates consistency and concurrency control, and requires more communication overhead.
  - Quorum-based replication: Each replica has a vote, and a quorum is a subset of replicas that has enough votes to perform an operation. For example, a read quorum is a subset of replicas that can provide a consistent read, and a write quorum is a subset of replicas that can perform a consistent update. A transaction needs to obtain a read quorum and a write quorum to execute. This approach balances availability and consistency, but requires a trade-off between the size and the overlap of the quorums.