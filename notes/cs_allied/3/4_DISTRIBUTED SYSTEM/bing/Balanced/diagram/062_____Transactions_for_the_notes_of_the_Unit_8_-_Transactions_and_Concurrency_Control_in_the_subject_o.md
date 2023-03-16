### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

### Concurrency Control
- Concurrency control is the process of managing simultaneous access to shared data in a database by multiple transactions.
- Concurrency control ensures that the transactions are executed in a correct and consistent manner, without violating the ACID properties.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.

### Distributed Transactions and Distributed Concurrency Control
- A distributed transaction is a transaction that spans multiple data servers in a distributed database system.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction coordinator is responsible for coordinating the execution and commitment of the subtransactions across the data servers.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires global atomicity and global consistency.
- Global atomicity means that either all the subtransactions of a distributed transaction are committed or all of them are aborted.
- Global consistency means that a distributed transaction preserves the integrity constraints of the distributed database.
- Distributed concurrency control is the concurrency control of a distributed database system, where relevant data is hosted by a group of linked data servers.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control can be implemented using various techniques, such as two-phase locking, two-phase commit, distributed timestamping, distributed validation, and distributed multiversioning.