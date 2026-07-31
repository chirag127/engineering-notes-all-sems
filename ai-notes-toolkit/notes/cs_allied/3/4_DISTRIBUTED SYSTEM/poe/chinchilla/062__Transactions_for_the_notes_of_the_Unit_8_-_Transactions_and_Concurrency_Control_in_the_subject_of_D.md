### Transactions

A transaction is a unit of work that is performed on a database. It consists of a collection of operations that are executed as a single, indivisible unit. Transactions are important in distributed systems because they ensure data consistency and integrity across multiple nodes.

#### ACID Properties

Transactions in distributed systems are expected to adhere to the ACID properties, which stand for:

- Atomicity: A transaction must be treated as a single, indivisible unit of work. Either all of the operations in the transaction are executed, or none of them are executed.

- Consistency: A transaction must leave the database in a consistent state. This means that the database must satisfy all of its constraints after the transaction is completed.

- Isolation: Each transaction must be executed in isolation from other transactions. This ensures that the results of one transaction do not interfere with the results of another transaction.

- Durability: Once a transaction is committed, its changes must be permanent and survive any subsequent failures.

#### Transaction States

Transactions can be in one of three states: 

- Active: The transaction is executing its operations.

- Partially Committed: The transaction has executed all of its operations and is waiting for confirmation from the system to commit the changes.

- Committed: The transaction has successfully completed and its changes have been permanently saved to the database.

- Aborted: The transaction has failed and its changes have been rolled back.

#### Transaction Management

Transaction management in distributed systems is more complex than in centralized systems because transactions may span multiple nodes. To ensure that transactions maintain the ACID properties, the system must support distributed concurrency control and distributed recovery.

#### Distributed Concurrency Control

Distributed concurrency control ensures that transactions execute in a serializable order, even though they may be executed on different nodes. The two main approaches to distributed concurrency control are:

- Two-Phase Locking: Transactions acquire locks on data items and release them when they are no longer needed. If a transaction cannot acquire a lock, it must wait until the lock is released.

- Timestamp Ordering: Each transaction is assigned a unique timestamp and transactions are executed in timestamp order. To ensure serializability, transactions must abide by a set of rules that dictate when they can read and write data items.

#### Distributed Recovery

Distributed recovery ensures that transactions are either committed or aborted, even if there are node or network failures during the transaction. The two main approaches to distributed recovery are:

- Two-Phase Commit: A coordinator node is responsible for managing the transaction and ensuring that all nodes either commit or abort the transaction. This approach is easy to implement but can be slow and can create bottlenecks.

- Three-Phase Commit: A coordinator node sends a prepare message to all nodes to ensure that they are ready to commit. If all nodes are ready, the coordinator sends a commit message. If any nodes are not ready, the coordinator sends an abort message. This approach is more complex but can be more efficient and can avoid bottlenecks.