### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction is executed as if it were the only one running in the system.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

### Concurrency Control
- Concurrency control is the process of managing the simultaneous execution of transactions in a shared database, to ensure the ACID properties of the transactions are maintained.
- Concurrency control is needed because concurrent transactions may interfere with each other, leading to incorrect or inconsistent results.
- For example, two transactions may try to update the same data item, or one transaction may read a data item that is being updated by another transaction.
- Concurrency control techniques can be broadly classified into two categories: locking-based and non-locking-based.
- Locking-based techniques use locks to prevent transactions from accessing or modifying data items that are already being accessed or modified by other transactions.
- Non-locking-based techniques use timestamps, validation, or multiversioning to order or validate the transactions based on their logical start times or commit times.

### Distributed Transactions and Distributed Concurrency Control
- A distributed transaction is a transaction that accesses data from multiple data servers that are connected by a computer network.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction is committed if and only if all its subtransactions are committed.
- A distributed transaction is aborted if any of its subtransactions is aborted.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control techniques can be classified into two categories: centralized and decentralized.
- Centralized techniques use a single coordinator to manage the locks or timestamps of the data items accessed by the distributed transactions.
- Decentralized techniques use multiple coordinators or no coordinators to manage the locks or timestamps of the data items accessed by the distributed transactions.