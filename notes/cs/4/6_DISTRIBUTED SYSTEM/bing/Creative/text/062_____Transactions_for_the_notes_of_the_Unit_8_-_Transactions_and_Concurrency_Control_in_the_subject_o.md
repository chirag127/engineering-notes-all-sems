### Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it is the only one in the system, without interference from other transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

### Concurrency Control

- Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the serializability and correctness of the transactions.
- Concurrency control is needed to prevent conflicts and anomalies that may arise when multiple transactions access and update the same data concurrently.
- Concurrency control techniques can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item.
- Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that indicates the time at which a transaction is started.

### Distributed Transactions and Distributed Concurrency Control

- A distributed transaction is a transaction that accesses and updates data stored in multiple data servers that are connected by a computer network.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- A distributed transaction has the same ACID properties as a local transaction, but it also requires two additional properties: atomic commitment and global serializability.
- Atomic commitment means that either all the subtransactions of a distributed transaction are committed or none of them are.
- Global serializability means that the execution of a set of distributed transactions is equivalent to some serial execution of the same transactions.
- Distributed concurrency control is the process of synchronizing distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved.
- Distributed concurrency control techniques can be based on locks, timestamps, or other methods, such as optimistic concurrency control, voting protocols, or quorum consensus.