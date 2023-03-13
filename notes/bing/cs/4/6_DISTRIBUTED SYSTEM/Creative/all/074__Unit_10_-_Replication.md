## Unit 10 - Replication

Replication is the process of creating and maintaining multiple copies of the same data or database object on different servers or locations. Replication can be used for various purposes, such as:

- Improving availability and fault tolerance by providing redundancy and backup for data.
- Enhancing performance and scalability by distributing the workload among multiple servers or locations.
- Supporting distributed applications and data analysis by allowing local access to data.
- Facilitating data migration and synchronization by enabling data transfer and updates between servers or locations.

There are different types of replication, depending on the direction, frequency, and consistency of data transfer and updates between the source and the target servers or locations. Some common types of replication are:

- **Snapshot replication**: This type of replication involves copying the entire data or database object from the source to the target at a specific point in time or at regular intervals. Snapshot replication is suitable for static or slowly changing data that does not require frequent updates. Snapshot replication is simple and efficient, but it does not provide real-time synchronization or concurrency control.
- **Transactional replication**: This type of replication involves copying the changes or transactions that occur on the source to the target as they happen or in batches. Transactional replication is suitable for dynamic or frequently changing data that requires real-time or near-real-time synchronization and consistency. Transactional replication is more complex and resource-intensive than snapshot replication, but it provides better concurrency control and conflict resolution.
- **Merge replication**: This type of replication involves allowing both the source and the target to make changes or transactions independently, and then merging the changes or transactions periodically or on demand. Merge replication is suitable for distributed or disconnected environments where the source and the target may not be always connected or accessible. Merge replication is the most complex and flexible type of replication, but it also requires the most conflict resolution and reconciliation.

Some mnemonics and learning tricks for Unit 10 - Replication are:

- To remember the types of replication, use the acronym **STM** (Snapshot, Transactional, Merge).
- To remember the advantages and disadvantages of each type of replication, use the following table:

| Type | Advantages | Disadvantages |
| --- | --- | --- |
| Snapshot | Simple, efficient, suitable for static data | No real-time synchronization, no concurrency control |
| Transactional | Real-time synchronization, concurrency control, suitable for dynamic data | Complex, resource-intensive, requires continuous connection |
| Merge | Flexible, suitable for distributed data, allows offline changes | Most complex, requires conflict resolution, may have data inconsistency |

- To remember the difference between replication and backup, use the following sentence: **Replication is for availability, backup is for recovery**. Replication provides redundancy and fault tolerance for data, but it does not protect against data corruption or deletion. Backup provides a copy of data that can be restored in case of data loss or damage, but it does not improve performance or scalability.