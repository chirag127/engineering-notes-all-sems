### Comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM
Comparison of methods for concurrency control in distributed systems:
1. Two-Phase Locking (2PL): ensures serializability by acquiring locks on resources before accessing them and releasing them after transaction completion.
2. Optimistic Concurrency Control (OCC): allows transactions to proceed optimistically, checking for conflicts only before commit.
3. Conflict-serializable Optimistic Concurrency Control (CSOCC): combines OCC with conflict serializability checking.
4. Serializable Snapshot Isolation (SSI): allows transactions to operate on a snapshot of the database, reducing locking overhead.
5. Timestamp Ordering (TO): assigns timestamps to transactions and orders their execution based on timestamps.
6. Multi-Version Concurrency Control (MVCC): maintains multiple versions of data items, allowing transactions to access past versions.
