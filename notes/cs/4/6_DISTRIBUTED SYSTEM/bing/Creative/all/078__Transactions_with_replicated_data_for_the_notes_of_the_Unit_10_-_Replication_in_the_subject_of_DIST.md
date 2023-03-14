### Transactions with replicated data for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Transactions are a sequence of operations that are executed as a single logical unit of work.
- Transactions have the ACID properties: atomicity, consistency, isolation, and durability.
- Transactions in distributed systems involve multiple nodes that communicate and coordinate to execute the operations.
- Transactions with replicated data are transactions that access or modify data that is stored in multiple locations.
- Replicated data is data that is copied and distributed across different nodes in a distributed system.
- Replication is a technique to improve data availability, performance, and fault-tolerance in distributed systems.
- Replication can be done synchronously or asynchronously, depending on the consistency and latency requirements.
- Synchronous replication ensures that all replicas are updated at the same time as the primary data source, but it introduces more overhead and delay.
- Asynchronous replication updates the replicas after the primary data source has been updated, but it allows for temporary inconsistencies and data loss.
- Replication can also be done actively or passively, depending on the role of the replicas.
- Active replication involves multiple replicas that execute the same operations and produce the same results.
- Passive replication involves a primary replica that executes the operations and sends the results to the backup replicas.
- Replication can also be classified based on the server model: primary-copy, update-anywhere, or hybrid.
- Primary-copy replication assigns a primary server for each data item, and only the primary server can update the data item.
- Update-anywhere replication allows any server to update any data item, and the updates are propagated to other servers.
- Hybrid replication combines the features of primary-copy and update-anywhere replication.
- Replication can also be done using different schemes: snapshot, transactional, or merge.
- Snapshot replication copies a snapshot of the data at a certain point in time, and does not track the changes to the data.
- Transactional replication copies the data and applies the changes in the same order as they occur in the primary data source.
- Merge replication combines the data from different sources and resolves the conflicts.

Some mnemonics and learning tricks for transactions with replicated data are:

- To remember the ACID properties of transactions, think of a transaction as a bottle of acid that cannot be broken, spilled, mixed, or evaporated.
- To remember the difference between synchronous and asynchronous replication, think of a sync button that makes all the replicas match the primary data source instantly, or an async button that makes the replicas catch up later.
- To remember the difference between active and passive replication, think of an active replica as a clone that does the same thing as the original, or a passive replica as a backup that waits for the original to tell it what to do.
- To remember the difference between primary-copy, update-anywhere, and hybrid replication, think of a primary-copy as a king that rules over a data item, an update-anywhere as a democracy that allows any server to vote on a data item, or a hybrid as a mix of both.
- To remember the difference between snapshot, transactional, and merge replication, think of a snapshot as a picture that captures the data at a moment, a transactional as a video that records the data over time, or a merge as a collage that combines the data from different sources.