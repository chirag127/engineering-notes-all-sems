## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all copies of the data are updated at the same time, but it may incur performance overhead and network latency.
  - Asynchronous replication allows updates to be applied to the copies at different times, but it may introduce data inconsistency and conflict resolution issues.
- Replication can be implemented using different architectures, such as master-slave, peer-to-peer, multi-master, and hybrid.
  - Master-slave replication involves one primary server (master) that receives all the updates and propagates them to one or more secondary servers (slaves) that only read the data.
  - Peer-to-peer replication involves multiple servers that can both read and write the data, and exchange updates among themselves using a gossip protocol.
  - Multi-master replication involves multiple servers that can both read and write the data, and coordinate updates using a consensus protocol or a conflict detection and resolution mechanism.
  - Hybrid replication combines different replication architectures to achieve the desired trade-offs between consistency, availability, and performance.
- Replication can be applied at different levels of granularity, such as statement-based, row-based, or logical.
  - Statement-based replication replicates the SQL statements that modify the data, and executes them on the replicas.
  - Row-based replication replicates the changes made to individual rows of the data, and applies them on the replicas.
  - Logical replication replicates the changes made to the logical entities of the data, such as tables, indexes, or views, and applies them on the replicas.