### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it were the only one in the system, without interference from other transactions.
- Durability means that the effects of a transaction are permanent and survive any system failures.

### Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator (DTC) is a component that manages the coordination and execution of distributed transactions across multiple data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires two additional properties: atomic commitment and global serializability.
- Atomic commitment means that either all the subtransactions of a distributed transaction commit or none of them do.
- Global serializability means that the concurrent execution of distributed transactions is equivalent to some serial execution of them.

### Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control techniques can be broadly classified into two categories: locking-based and non-locking-based.
- Locking-based techniques use locks to prevent conflicting operations on the same data item by different subtransactions.
- Non-locking-based techniques use timestamps, validation, or optimistic methods to detect and resolve conflicts among subtransactions.
- Distributed concurrency control techniques can also be classified into centralized, decentralized, or hierarchical, depending on the location and structure of the DTC.