## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication can improve the availability, performance, and scalability of a database system.
- Replication can also provide data redundancy and backup, as well as facilitate data distribution and synchronization across different locations.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all changes made to the data on one server are immediately applied to the copies on the other servers, before the transaction is committed. This guarantees data consistency, but may incur high network latency and overhead.
  - Asynchronous replication allows changes made to the data on one server to be applied to the copies on the other servers after the transaction is committed. This improves performance and availability, but may result in data inconsistency or conflicts in case of network failures or concurrent updates.
- Replication can be implemented using different methods, such as:
  - Snapshot replication: a full copy of the data is periodically transferred from one server to another.
  - Transactional replication: only the changes made to the data are transferred from one server to another, using a log or a queue.
  - Merge replication: changes made to the data on different servers are merged and synchronized, using a conflict resolution mechanism.
  - Peer-to-peer replication: changes made to the data on any server are propagated to all the other servers, creating a distributed system with no single point of failure.