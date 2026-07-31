### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are mechanisms that prevent concurrent transactions from accessing the same data item in a way that violates the ACID properties of transactions.
- Locks can be applied on different levels of granularity, such as records, pages, tables, or databases.
- Locks can be of different modes, such as shared (S), exclusive (X), or update (U). The lock compatibility matrix defines which lock modes can coexist on the same data item.
- Locks can be acquired and released by transactions according to different protocols, such as two-phase locking (2PL), timestamp ordering (TO), or optimistic concurrency control (OCC).
- Locks can be managed by a centralized or distributed lock manager, depending on the architecture of the distributed system.
- Locks can cause problems such as deadlocks, livelocks, starvation, or cascading aborts, which need to be detected and resolved by the concurrency control mechanism.