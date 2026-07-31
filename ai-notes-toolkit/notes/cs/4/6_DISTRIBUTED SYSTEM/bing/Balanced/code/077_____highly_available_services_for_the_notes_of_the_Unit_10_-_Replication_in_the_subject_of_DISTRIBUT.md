### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- Replication is the process of creating and maintaining multiple copies of data or services across different nodes or locations in a distributed system.
- Replication can improve the availability, reliability, performance, and scalability of distributed systems by reducing the impact of failures, network latency, and load imbalance.
- Replication can also enable fault tolerance, disaster recovery, and data consistency in distributed systems.
- Replication can be classified into different types based on the following criteria:
  - The degree of replication: full replication (all nodes have a copy of the data or service) or partial replication (only some nodes have a copy of the data or service).
  - The timing of replication: eager replication (updates are propagated to all replicas as soon as they occur) or lazy replication (updates are propagated to some or all replicas after a delay or on demand).
  - The consistency of replication: strong consistency (all replicas have the same view of the data or service at all times) or weak consistency (replicas may have different views of the data or service at some times).
- Replication can be implemented at different levels of abstraction in distributed systems, such as:
  - Data replication: replicating data items or files across storage nodes or databases.
  - Service replication: replicating application-level processes or components across compute nodes or servers.
  - System replication: replicating entire systems or virtual machines across physical machines or clusters.
- Replication can be coordinated by different protocols or algorithms, such as:
  - Primary-backup protocol: one replica is designated as the primary and the others are backups. The primary receives and executes all requests and sends updates to the backups. The backups take over the primary role in case of failure.
  - Quorum protocol: each replica has a vote and a quorum is a subset of replicas whose votes are needed to perform an operation. A read quorum is needed to read data or service state and a write quorum is needed to update data or service state.
  - State machine protocol: each replica is modeled as a deterministic state machine that executes the same sequence of commands. A leader replica is elected to order and broadcast commands to the other replicas. The leader can be replaced in case of failure.
  - Gossip protocol: each replica periodically exchanges information with a random subset of other replicas. The information can be updates, acknowledgments, or summaries. The protocol converges to a consistent state over time.