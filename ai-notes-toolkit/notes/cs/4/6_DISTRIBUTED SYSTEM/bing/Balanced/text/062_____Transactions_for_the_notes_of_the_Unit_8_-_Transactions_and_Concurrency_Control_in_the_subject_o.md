### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.

### Distributed Transactions
- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is a component that manages the execution of distributed transactions across the data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it is more complex and challenging to implement.

### Concurrency Control
- Concurrency control is the technique of ensuring the correct and consistent execution of multiple transactions that access the same data concurrently.
- Concurrency control prevents problems such as lost updates, dirty reads, unrepeatable reads, and phantom reads, which can compromise the integrity and consistency of the database.
- Concurrency control can be implemented using various methods, such as locking, timestamping, validation, and multiversioning.

### Distributed Concurrency Control
- Distributed concurrency control is the concurrency control of a distributed database system, where relevant data is hosted by a group of linked data servers.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be classified into two categories: centralized and decentralized.
- Centralized distributed concurrency control relies on a single coordinator to manage the locks and timestamps of the data items across the data servers.
- Decentralized distributed concurrency control relies on a distributed algorithm to coordinate the locks and timestamps of the data items among the data servers.