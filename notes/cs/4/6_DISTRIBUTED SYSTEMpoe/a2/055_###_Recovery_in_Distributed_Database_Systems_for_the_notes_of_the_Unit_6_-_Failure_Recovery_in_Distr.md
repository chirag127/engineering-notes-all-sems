 Here is the content in markdown format:

### Recovery in Distributed Database Systems

For the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- **Log-Based Recovery**: Distributed database systems maintain logs of transactions to recover from failures. The logs contain a record of all transactions that have been committed. In case of a failure, the log is analyzed and any committed but not yet reflected in the database transactions are redone to recover the system to a consistent state. The logs can be maintained centrally or in a decentralized fashion. Centralized logging is simpler but can become a bottleneck. Decentralized logging avoids the bottleneck but makes recovery more complex.
- **Checkpointing**: Periodically, the state of the distributed database is captured in a checkpoint. In case of a failure, recovery is done by rolling back to the latest checkpoint and redoing the transactions after the checkpoint. This avoids redoing all the transactions in the log and speeds up recovery. However, checkpointing requires coordination among the nodes and incurs some overhead. The frequency of checkpointing is a trade-off between the overhead and the amount of work needed for recovery.
- **Shadow Paging**: Parts of the database are maintained in a "shadow" copy in addition to the primary copy. The shadow copy is updated asynchronously. In case of a failure, the primary database can be reconstructed from the shadow copy, which may be slightly out-of-date but eliminates the need to analyze the log. Shadow paging works well for read-mostly data or when strict consistency is not required.
- **Replication**: Databases or parts of the database are replicated across multiple nodes. In case of a failure, the system can switch to a replica. Replication provides high availability but requires mechanisms to maintain consistency across the replicas and handle updates. Eventual consistency models can be used when strong consistency is not required.

 Mnemonics and learning tricks:

- Think of log-based recovery as redoing a transaction log or ledger
- Checkpointing is like saving a game state in video games for retry on failure
- Shadow paging is like a shadow or ghost of the primary database
- Replication is like having multiple backup copies

Does this help? Let me know if you would like me to elaborate on any of the points or add additional details.