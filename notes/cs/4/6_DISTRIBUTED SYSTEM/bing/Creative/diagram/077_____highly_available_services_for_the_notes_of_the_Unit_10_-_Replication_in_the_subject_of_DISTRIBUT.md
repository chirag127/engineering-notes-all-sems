### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable functionality to its clients, even in the presence of failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service across different nodes or locations in a distributed system.
- Replication can improve the availability, performance, scalability, and fault tolerance of a distributed system, but it also introduces challenges such as consistency, concurrency, and communication.
- Replication can be classified into different types based on the following criteria:
  - The degree of replication: how many copies of the data or service are maintained and where they are located.
  - The timing of replication: when the copies are updated or synchronized with each other.
  - The granularity of replication: what is the unit of replication, such as a file, a record, a block, or a service.
  - The location of replication: where the copies are stored, such as in the same or different sites, networks, or regions.
  - The direction of replication: whether the updates are propagated from one master copy to the others, or from any copy to the others, or both.
  - The mode of replication: whether the updates are applied eagerly or lazily, synchronously or asynchronously, or optimistically or pessimistically.
- Some examples of replication techniques are :
  - Primary-backup replication: a master copy is designated as the primary, and the other copies are backups. The primary receives and executes all the requests from the clients, and sends the updates to the backups. The backups apply the updates in the same order as the primary. If the primary fails, one of the backups takes over as the new primary.
  - Quorum-based replication: each copy has a vote, and a quorum is a subset of copies that has enough votes to perform an operation. For example, a read quorum is a subset of copies that can provide a consistent read, and a write quorum is a subset of copies that can ensure a consistent write. A quorum-based system can tolerate failures as long as a quorum is available.
  - Lazy replication: the copies are updated asynchronously and periodically, rather than synchronously and immediately. This can improve the performance and availability of the system, but it can also cause temporary inconsistencies and conflicts among the copies. A lazy replication system needs to resolve the conflicts and reconcile the copies eventually.