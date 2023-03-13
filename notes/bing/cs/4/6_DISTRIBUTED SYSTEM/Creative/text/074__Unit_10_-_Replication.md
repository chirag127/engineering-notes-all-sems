## Unit 10 - Replication

Replication is the process of creating and maintaining multiple copies of the same data on different servers or devices. Replication can be used for various purposes, such as:

- Improving availability and performance by distributing the workload among multiple servers or devices.
- Enhancing fault tolerance and disaster recovery by providing backup copies of the data in case of failure or loss of the primary server or device.
- Supporting distributed applications and data processing by allowing data access and updates from different locations or networks.

There are different types of replication, depending on the level of consistency, synchronization, and autonomy of the replicated data. Some common types are:

- Synchronous replication: The data is replicated to all the servers or devices simultaneously, ensuring that they have the same data at all times. This type of replication provides the highest level of consistency, but also the highest latency and overhead.
- Asynchronous replication: The data is replicated to the servers or devices periodically or on demand, allowing some delay or divergence between the copies. This type of replication provides lower latency and overhead, but also lower consistency.
- Snapshot replication: The data is replicated to the servers or devices at a specific point in time, creating a static copy of the data. This type of replication is useful for backup or archival purposes, but does not reflect the changes in the data after the snapshot.
- Merge replication: The data is replicated to the servers or devices independently, allowing them to make local changes and updates. The changes are then merged with the other copies, resolving any conflicts or discrepancies. This type of replication provides the highest level of autonomy, but also the highest complexity and risk of data loss or corruption.