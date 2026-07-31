 Here is the content in markdown format without any emojis or external links:

### Recovery in Distributed Database Systems

- Failure detection: Failure detectors are used to detect node failures in a distributed system. They use heartbeat messages or timeout mechanisms to detect failed nodes.
- Log-based recovery: The state of a database is maintained by logging all updates to a persistent log. In case of failure, the log is used to redo committed transactions and undo uncommitted transactions to recover the database state.
- Checkpointing: Periodically, a consistent snapshot of the database state is saved as a checkpoint. In case of failure, the database can be rolled back to the latest checkpoint and only transactions after the checkpoint need to be recovered using the log. This reduces recovery time.
- Replication-based recovery: Multiple replicas of the same data are maintained at different nodes. On failure of a node, one of the replicas can be chosen as the new primary replica. This provides fast recovery but has higher space and update overhead.
- Eager vs Lazy recovery: In eager recovery, failed nodes are recovered quickly but it can lead to rolling back of committed transactions. In lazy recovery, failed nodes are recovered lazily to avoid rolling back committed transactions but it can lead to higher recovery times. Trade-offs exist between eager and lazy recovery.

The above points cover the key concepts involved in recovery of distributed database systems. The content is written in a formal tone with points and without any emojis or external links as requested. Let me know if you would like me to elaborate on any of the points or modify the content in any way.