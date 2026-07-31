# Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of a distributed system.
- Replication can also introduce challenges such as consistency, concurrency, and fault tolerance.
- There are different types of replication, such as:
  - **Eager replication**: The updates are propagated to all the replicas as soon as they occur, ensuring strong consistency but increasing communication and synchronization overhead.
  - **Lazy replication**: The updates are propagated to the replicas periodically or on demand, allowing temporary inconsistency but reducing communication and synchronization overhead.
  - **Full replication**: All the data or services are replicated on all the nodes, maximizing availability and fault tolerance but consuming more resources and bandwidth.
  - **Partial replication**: Only a subset of the data or services are replicated on some of the nodes, saving resources and bandwidth but requiring more complex management and coordination.
- There are different techniques for implementing replication, such as:
  - **Primary-backup replication**: One of the replicas is designated as the primary, which receives all the updates and propagates them to the backups. The backups are passive and only become active when the primary fails. This technique ensures strong consistency but introduces a single point of failure and a performance bottleneck.
  - **Active replication**: All the replicas are active and receive the same updates in the same order. The updates are executed by all the replicas independently and the results are compared to detect and correct faults. This technique ensures strong consistency and fault tolerance but requires more communication and synchronization among the replicas.
  - **Quorum-based replication**: The updates are executed by a subset of the replicas, called a write quorum, and the reads are performed by another subset of the replicas, called a read quorum. The quorums are chosen such that they overlap, ensuring consistency and availability. This technique reduces the communication and synchronization overhead but requires more complex quorum management and coordination.
  - **Gossip-based replication**: The updates are propagated to the replicas randomly or probabilistically, using a gossip protocol. The replicas exchange their updates with each other and eventually converge to a consistent state. This technique is scalable and resilient to failures but allows temporary inconsistency and may not guarantee eventual consistency.