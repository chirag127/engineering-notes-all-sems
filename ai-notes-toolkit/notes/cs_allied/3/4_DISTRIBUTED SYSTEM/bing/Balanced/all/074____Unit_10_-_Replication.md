## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can be classified into two types: synchronous and asynchronous.
  - Synchronous replication ensures that all changes made to the data on one server are immediately applied to the copies on other servers. This guarantees data consistency, but may incur performance overhead and network latency.
  - Asynchronous replication allows changes made to the data on one server to be applied to the copies on other servers at a later time. This improves performance and network efficiency, but may result in data inconsistency or conflicts.
- Replication can be implemented using different methods, such as snapshot, transactional, merge, and peer-to-peer replication.
  - Snapshot replication creates a full copy of the data on one server and distributes it to other servers at specified intervals. This is suitable for static or slowly changing data, but may consume a lot of network bandwidth and storage space.
  - Transactional replication captures and distributes only the changes made to the data on one server to other servers. This is suitable for dynamic or frequently changing data, but may require a lot of processing and logging resources.
  - Merge replication allows changes made to the data on different servers to be merged and synchronized. This is suitable for distributed or disconnected environments, but may require conflict resolution and reconciliation mechanisms.
  - Peer-to-peer replication allows changes made to the data on any server to be propagated to all other servers. This is suitable for high availability and scalability, but may require complex configuration and management.