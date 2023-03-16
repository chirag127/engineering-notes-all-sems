### Concurrency control in distributed transactions

- Concurrency control is the process of ensuring that concurrent operations on a shared data do not violate the consistency and isolation properties of transactions.
- Distributed transactions are transactions that span multiple data servers that are connected by a network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution .
- There are different types of distributed concurrency control protocols, such as locking-based, timestamp-based, optimistic, and consensus-based  .
- Locking-based protocols use the concept of locking data items to prevent conflicting operations from different transactions.
- Timestamp-based protocols use a transaction’s timestamp to determine the order of operations and to detect and resolve conflicts.
- Optimistic protocols assume that conflicts are rare and allow transactions to execute without any synchronization, but validate them before committing.
- Consensus-based protocols use a distributed agreement protocol, such as two-phase commit (2PC) or three-phase commit (3PC), to coordinate the commit or abort decision of distributed transactions.