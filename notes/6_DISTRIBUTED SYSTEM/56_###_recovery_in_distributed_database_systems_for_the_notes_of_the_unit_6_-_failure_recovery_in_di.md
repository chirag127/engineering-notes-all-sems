### Recovery in Distributed Database Systems for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM
Recovery in Distributed Database Systems:
- Distributed database systems are vulnerable to failures due to the complexity of their architecture.
- Recovery refers to the process of restoring the system to its normal state after a failure.
- Types of failures: node failures, network failures, and software failures.
- Recovery techniques: checkpointing, replication, and rollback.
- Checkpointing: periodic saving of the state of the system to disk.
- Replication: maintaining multiple copies of data to provide redundancy.
- Rollback: undoing the effects of a failed transaction.
- Two-phase commit protocol: coordination mechanism for ensuring atomicity in distributed transactions.
- Distributed recovery algorithms: primary-backup, voting, and ring algorithms.
- Recovery time objective (RTO) and recovery point objective (RPO) are important metrics to evaluate the effectiveness of recovery techniques.
