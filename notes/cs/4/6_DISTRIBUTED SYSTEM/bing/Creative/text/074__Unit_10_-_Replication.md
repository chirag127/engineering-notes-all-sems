## Unit 10 - Replication

Replication is the process of creating and maintaining multiple copies of the same data on different servers or devices. Replication can be used for various purposes, such as:

- Improving availability and performance by distributing the workload among multiple servers or devices.
- Enhancing fault tolerance and disaster recovery by providing backup copies of the data in case of failure or loss of the primary server or device.
- Facilitating data sharing and synchronization among different locations or applications.

There are different types of replication, such as:

- Synchronous replication: The data is replicated to the secondary server or device as soon as it is written to the primary server or device. This ensures that the data is consistent and up-to-date on both sides, but it also introduces latency and network overhead.
- Asynchronous replication: The data is replicated to the secondary server or device after a certain delay or interval from the primary server or device. This reduces the latency and network overhead, but it also creates the possibility of data inconsistency or loss in case of failure or network partition.
- Snapshot replication: The data is replicated to the secondary server or device at a specific point in time or on a scheduled basis. This provides a consistent and stable copy of the data, but it also consumes more storage space and bandwidth.
- Continuous replication: The data is replicated to the secondary server or device continuously or in near real-time. This provides a high level of availability and performance, but it also requires more resources and complexity.

There are also different modes of replication, such as:

- Full replication: The entire data set is replicated to the secondary server or device. This provides a complete and identical copy of the data, but it also consumes more storage space and bandwidth.
- Partial replication: Only a subset of the data set is replicated to the secondary server or device. This reduces the storage space and bandwidth requirements, but it also requires more logic and configuration to determine which data to replicate and how to handle conflicts or updates.
- Bidirectional replication: The data can be updated on both the primary and secondary server or device, and the changes are propagated to the other side. This allows for data sharing and synchronization, but it also introduces the risk of data inconsistency or conflicts.
- Unidirectional replication: The data can be updated only on the primary server or device, and the changes are replicated to the secondary server or device. This ensures data consistency and integrity, but it also limits the functionality and flexibility of the secondary server or device.