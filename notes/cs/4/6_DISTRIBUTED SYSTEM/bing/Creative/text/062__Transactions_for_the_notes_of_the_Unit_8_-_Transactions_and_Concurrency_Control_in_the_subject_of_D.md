### Transactions

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction has the following properties:

- Atomicity: A transaction is either executed in its entirety or not at all.
- Consistency: A transaction preserves the consistency of the database by transforming it from one valid state to another.
- Isolation: A transaction is executed as if it is the only one running on the database, without interference from other concurrent transactions.
- Durability: The effects of a transaction are permanent and survive any system failures.

Transactions are important for ensuring the reliability and correctness of database operations, especially in distributed systems where data is replicated or partitioned across multiple nodes.

### Concurrency Control

Concurrency control is the technique of managing concurrent operations on the database without violating the consistency and isolation properties of transactions. Concurrency control is necessary because multiple transactions may access and update the same data items at the same time, leading to potential conflicts and anomalies.

There are different methods of concurrency control, such as:

- Lock-based protocols: These protocols use locks to prevent concurrent transactions from accessing the same data item. A lock is a mechanism that grants exclusive or shared access to a data item to a transaction. A transaction must acquire a lock before reading or writing a data item, and release the lock after finishing its operation. Locks can be implemented at different levels of granularity, such as records, pages, tables, or databases.
- Timestamp-based protocols: These protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that reflects the start time of a transaction. A transaction must obtain a timestamp before executing any operation, and use it to compare with the timestamps of other transactions that access the same data item. A transaction can proceed with its operation only if its timestamp is older than the timestamps of other conflicting transactions, otherwise it must abort and restart with a new timestamp.
- Validation-based protocols: These protocols use a validation phase to check whether a transaction can commit without violating the consistency and isolation properties. A transaction is divided into three phases: read phase, write phase, and validation phase. In the read phase, the transaction reads the data items from the database and stores them in a private workspace. In the write phase, the transaction modifies the data items in its workspace but does not write them back to the database. In the validation phase, the transaction checks whether its read and write sets overlap with the read and write sets of other concurrent transactions that have committed. If there is no overlap, the transaction can commit and write its updates to the database, otherwise it must abort and restart.

### Distributed Transactions and Distributed Concurrency Control

A distributed transaction is a transaction that spans multiple nodes in a distributed system, where each node hosts a part of the database. A distributed transaction consists of a set of subtransactions, each of which is executed by one node. A distributed transaction must satisfy the same properties as a local transaction, but also ensure that all subtransactions are coordinated and consistent across the nodes.

Distributed concurrency control is the concurrency control of a distributed transaction. It provides a mechanism to synchronize distributed transactions in such a way that the ACID properties are not violated by their interleaved execution. Distributed concurrency control faces additional challenges, such as:

- Network delays and failures: The communication between nodes may be slow, unreliable, or unavailable, which can affect the performance and correctness of distributed transactions.
- Data replication and consistency: The data in a distributed system may be replicated or partitioned across multiple nodes, which can improve availability and scalability, but also introduce the problem of maintaining data consistency and resolving conflicts among different copies of the data.
- Distributed deadlock detection and resolution: A deadlock is a situation where a set of transactions are waiting for each other to release their locks, resulting in a circular wait. A deadlock can occur in a distributed system when transactions lock data items that are located on different nodes. Detecting and resolving deadlocks in a distributed system is more complex and costly than in a centralized system.

There are different approaches to distributed concurrency control, such as:

- Two-phase locking (2PL): This is a lock-based protocol that extends the 2PL protocol for local transactions to distributed transactions. A distributed transaction must acquire locks on all the data items it needs before releasing any lock, and release all the locks after committing or aborting. A distributed transaction can use a centralized lock manager or a distributed lock manager to manage the locks across the nodes.
- Two-phase commit (2PC): This is a validation-based protocol that ensures the atomicity and consistency of distributed transactions. A distributed transaction involves a coordinator node and a set of participant nodes. The coordinator node initiates the