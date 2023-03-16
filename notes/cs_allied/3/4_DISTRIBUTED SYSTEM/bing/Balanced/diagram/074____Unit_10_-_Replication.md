## Unit 10 - Replication

- Replication is the process of copying data from one database server to another, either synchronously or asynchronously.
- Replication can be used for various purposes, such as:
  - High availability: Replication can provide redundancy and fault tolerance by maintaining multiple copies of data on different servers.
  - Load balancing: Replication can distribute the workload among multiple servers, reducing the load on a single server and improving performance.
  - Data distribution: Replication can enable data access across different locations, regions, or networks, facilitating data sharing and collaboration.
  - Backup and recovery: Replication can provide a backup copy of data that can be used for recovery in case of data loss or corruption.
- Replication can be classified into different types, based on the following criteria:
  - The number of servers involved: Replication can be either one-to-one, one-to-many, many-to-one, or many-to-many.
  - The direction of data flow: Replication can be either unidirectional, bidirectional, or multidirectional.
  - The timing of data transfer: Replication can be either synchronous, asynchronous, or semi-synchronous.
  - The granularity of data transfer: Replication can be either snapshot, transactional, or merge.
- Replication can also be categorized into different models, based on the role and responsibility of each server involved:
  - Master-slave replication: In this model, one server (the master) is the primary source of data, and the other servers (the slaves) are the secondary copies of data. The master is responsible for accepting write operations, and the slaves are responsible for accepting read operations. The master propagates the changes to the slaves, either synchronously or asynchronously. The master-slave replication can be either one-to-many or many-to-one.
  - Peer-to-peer replication: In this model, all servers are equal and can accept both read and write operations. The servers propagate the changes to each other, either synchronously or asynchronously. The peer-to-peer replication can be either bidirectional or multidirectional.
  - Multi-master replication: In this model, multiple servers (the masters) can accept write operations, and the other servers (the slaves) can accept read operations. The masters propagate the changes to the slaves, either synchronously or asynchronously. The multi-master replication can be either one-to-many or many-to-many.