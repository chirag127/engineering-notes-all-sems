## Unit 10 - Replication

- Replication is the process of creating and maintaining multiple copies of the same data on different database servers.
- Replication provides benefits such as high availability, fault tolerance, load balancing, and scalability.
- Replication can also enable data distribution across different locations, platforms, or organizations.
- Replication can be classified into different types based on the direction, timing, and granularity of data transfer.
- The main types of replication are:
  - Snapshot replication: A snapshot of the data is taken at a point in time and copied to the destination server. This type of replication is suitable for static or slowly changing data.
  - Transactional replication: Each transaction that modifies the data is captured and applied to the destination server. This type of replication ensures that the data is consistent and up-to-date across the servers.
  - Merge replication: Each server can make changes to the data independently, and the changes are merged periodically or on demand. This type of replication allows for data synchronization and conflict resolution.
  - Peer-to-peer replication: Each server acts as both a source and a destination for the data, and the changes are propagated to all the servers. This type of replication enables high availability and scalability.
- Replication can be implemented using different methods or technologies, such as:
  - Log shipping: The transaction log of the source database is backed up and restored to the destination database. This method is simple and reliable, but it has a high latency and does not support read-only access to the destination database.
  - Database mirroring: The transaction log of the source database is sent and applied to the destination database in real time. This method provides high availability and automatic failover, but it does not support load balancing or multiple destinations.
  - Always On availability groups: A group of databases is replicated across multiple servers using a combination of database mirroring and failover clustering. This method provides high availability, disaster recovery, and read-only access to the secondary databases, but it requires more resources and configuration.
  - Replication services: A set of components and agents that manage the replication of data across multiple servers. This method supports various types of replication, such as snapshot, transactional, merge, and peer-to-peer, and it allows for customization and monitoring of the replication process.