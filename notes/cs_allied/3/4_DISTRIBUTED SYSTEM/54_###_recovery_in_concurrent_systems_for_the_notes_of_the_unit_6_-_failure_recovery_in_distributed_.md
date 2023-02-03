### Recovery in Concurrent systems for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

Recovery in concurrent systems refers to the process of restoring a system to a consistent state after a failure. In a concurrent system, multiple transactions may be executing simultaneously, and a failure may cause some transactions to be incomplete or inconsistent. Recovery is the process of ensuring that the system is restored to a consistent state, and that any incomplete transactions are either completed or rolled back.

There are several approaches to recovery in concurrent systems, including:
1. Rollback recovery: incomplete transactions are rolled back to their previous state, and the system is restored to a consistent state.
2. Commit recovery: completed transactions are committed, and the system is restored to a consistent state.
3. Checkpoint-based recovery: the state of the system is periodically saved to disk, and the system is restored to a consistent state from the most recent checkpoint.

In summary, recovery in concurrent systems refers to the process of restoring a system to a consistent state after a failure. There are several approaches to recovery, including rollback recovery, commit recovery, and checkpoint-based recovery.
