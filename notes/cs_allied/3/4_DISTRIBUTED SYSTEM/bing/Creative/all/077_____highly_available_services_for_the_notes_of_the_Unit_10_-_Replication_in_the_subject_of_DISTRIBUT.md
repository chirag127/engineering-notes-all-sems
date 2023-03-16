# Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data in different locations in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of distributed services.
- Replication can also introduce challenges such as consistency, concurrency, and fault tolerance.
- There are different types of replication, such as:
  - Synchronous replication: The updates are propagated to all replicas before the operation is considered complete. This ensures strong consistency, but increases latency and reduces availability.
  - Asynchronous replication: The updates are propagated to some or all replicas after the operation is considered complete. This improves availability and performance, but may cause inconsistency or data loss.
  - Lazy replication: The updates are propagated to the replicas only when they are needed or requested. This reduces network traffic and storage overhead, but may increase response time and inconsistency.
- There are different strategies for managing replication, such as:
  - Primary-backup: One replica is designated as the primary, and the others are backups. The primary receives all the updates and propagates them to the backups. The backups take over the primary role in case of failure.
  - Quorum-based: Each replica has a vote, and a quorum is a subset of replicas that can decide on the outcome of an operation. The operation is considered complete if a quorum of replicas agrees on it. This can tolerate failures and improve availability, but may increase communication overhead and complexity.
  - Group communication: The replicas are organized into groups, and use multicast communication to exchange updates and coordinate actions. This can simplify the replication protocol and reduce network traffic, but may introduce ordering and delivery issues.
- There are different techniques for implementing replication, such as:
  - State machine replication: The replicas are modeled as deterministic state machines that execute the same sequence of commands. This ensures consistency and fault tolerance, but requires agreement on the command order and execution.
  - Data replication: The replicas store copies of the same data, and use update or query operations to access and modify them. This can improve performance and scalability, but requires consistency maintenance and conflict resolution.
  - Hybrid replication: The replicas combine state machine and data replication, and use different levels of consistency and synchronization depending on the application requirements. This can optimize the trade-offs between availability, performance, and consistency, but may increase complexity and overhead.