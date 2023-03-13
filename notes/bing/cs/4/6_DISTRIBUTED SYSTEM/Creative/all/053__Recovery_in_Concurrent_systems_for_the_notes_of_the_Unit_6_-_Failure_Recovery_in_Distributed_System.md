### Recovery in Concurrent systems for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Recovery is the process of restoring a system to a consistent and correct state after a failure.
- Recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite failures.
- Recovery in concurrent systems is challenging because of the following reasons :
  - Partial failures: Some components may fail while others continue to function, making it difficult to detect and isolate failures.
  - Concurrency: Multiple clients may access or update a shared resource at the same time, leading to inconsistencies or conflicts.
  - Distributed state: The state of the system may be spread across multiple nodes, making it hard to synchronize and coordinate recovery actions.
- Recovery in concurrent systems can be classified into two types:
  - Backward recovery: The system is rolled back to a previous error-free state using checkpoints or logs. This may require undoing or aborting some operations that have already been executed.
  - Forward recovery: The system is repaired by correcting the erroneous state using redundancy or replication. This may require performing some compensating or retrying operations that have not been executed.
- Recovery in concurrent systems can be implemented using different techniques, such as  :
  - Stable storage: A pair of regular disks can be used to store the state of the system in a way that can resist failures. The disks are updated in a synchronous or asynchronous manner to ensure consistency.
  - Checkpointing: The system periodically saves its state to stable storage or memory. Checkpoints can be local (per node) or global (across nodes). Global checkpoints need to be consistent, meaning that they do not contain any partial or conflicting operations.
  - Logging: The system records its operations to stable storage or memory. Logs can be undo (recording the old state before an operation) or redo (recording the new state after an operation). Logs can be used to roll back or replay operations during recovery.
  - Replication: The system maintains multiple copies of its state or data on different nodes. Replication can be passive (one primary node and multiple backup nodes) or active (multiple primary nodes). Replication can be used to mask or correct failures by switching or voting among replicas.
  - Regenerating codes: The system encodes its data using erasure codes that can recover from multiple failures. Regenerating codes can reduce the storage and bandwidth overhead of replication by allowing partial recovery of data from surviving nodes. Regenerating codes can be used to speed up and parallelize the recovery process.