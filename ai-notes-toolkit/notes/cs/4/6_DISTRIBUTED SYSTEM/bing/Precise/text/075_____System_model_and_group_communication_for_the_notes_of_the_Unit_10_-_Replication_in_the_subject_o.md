### System model and group communication for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- A system model is a representation of the components and interactions within a distributed system.
- Group communication is a method of communication in which messages are sent to multiple recipients simultaneously.
- In the context of replication in distributed systems, group communication is used to ensure consistency among replicas.
- Replication is the process of creating and maintaining multiple copies of data or services in a distributed system.
- Replication can improve availability, reliability, and performance of the system.
- Group communication protocols can be used to implement replication strategies such as primary-backup, active replication, and quorum-based replication.
- Primary-backup replication involves designating one replica as the primary and the others as backups. The primary is responsible for processing requests and updating the backups.
- Active replication involves all replicas processing requests simultaneously and independently.
- Quorum-based replication involves a subset of replicas, called a quorum, processing requests and updating the other replicas.
- Group communication protocols can also be used to implement consistency models such as sequential consistency, causal consistency, and eventual consistency.
- Sequential consistency requires that the order of operations be preserved across all replicas.
- Causal consistency requires that causally related operations be ordered across all replicas.
- Eventual consistency requires that all replicas eventually converge to the same state.