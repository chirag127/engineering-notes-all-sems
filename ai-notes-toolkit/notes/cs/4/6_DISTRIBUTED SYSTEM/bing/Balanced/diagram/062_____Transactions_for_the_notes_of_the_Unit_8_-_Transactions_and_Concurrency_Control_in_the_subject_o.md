### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction is not affected by the concurrent execution of other transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.

### Distributed Transactions

- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that manages the execution of distributed transactions across the data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires coordination and communication among the data servers.

### Distributed Concurrency Control

- Distributed concurrency control is the concurrency control of a system distributed over a computer network.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- Centralized concurrency control relies on a single coordinator to manage the locks and timestamps of the data items accessed by the distributed transactions.
- Decentralized concurrency control allows each data server to manage its own locks and timestamps, and uses a distributed algorithm to ensure global consistency.