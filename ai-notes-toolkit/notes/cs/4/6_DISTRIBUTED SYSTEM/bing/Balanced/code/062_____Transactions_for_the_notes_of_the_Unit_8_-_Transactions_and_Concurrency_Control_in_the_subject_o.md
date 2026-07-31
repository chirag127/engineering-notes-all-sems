# Transactions

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a transaction are permanent even in the case of failures.

# Concurrency Control

- Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the consistency and isolation properties of transactions.
- Concurrency control techniques can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to prevent conflicting operations from accessing the same data item. A lock is a variable associated with a data item that describes the status of the item with respect to possible operations that can be applied to it.
- Timestamp-based protocols use timestamps to order the transactions and ensure serializability. A timestamp is a unique identifier assigned to each transaction that reflects its start time. Timestamps can be either logical or physical.

# Distributed Transactions and Distributed Concurrency Control

- A distributed transaction is a transaction that accesses data from multiple data servers that are connected by a computer network.
- A distributed transaction consists of a set of subtransactions, each of which is executed by one data server.
- Distributed concurrency control provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution.
- Distributed concurrency control makes sure that all subtransactions of a set of distributed transactions are serialized identically in all data servers involved. Therefore, not only local dependencies need to be taken into account, but also dependencies involving multiple data servers.
- Distributed concurrency control techniques can be classified into two categories: centralized and decentralized.
- Centralized techniques use a single coordinator to manage the locks or timestamps of all data servers. The coordinator is responsible for granting or denying requests from transactions, and for detecting and resolving conflicts and deadlocks.
- Decentralized techniques use a distributed algorithm to coordinate the locks or timestamps of all data servers. Each data server communicates with other data servers to exchange information and reach a consensus on the serialization order of transactions.