## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has the following properties:
  - **Atomicity**: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to the state before the transaction started.
  - **Consistency**: A transaction preserves the integrity constraints of the database. After a transaction completes, the database is in a consistent state.
  - **Isolation**: A transaction is executed as if it is the only one running on the database. The intermediate results of a transaction are not visible to other transactions.
  - **Durability**: The effects of a transaction are permanent and persist even in the case of system failures.
- **Concurrency control** is the technique of managing the simultaneous execution of transactions on a shared database, such that the consistency and isolation properties are maintained.
- Concurrency control can be implemented using various methods, such as:
  - **Locking**: A lock is a mechanism that grants exclusive access to a data item to a transaction. A transaction must acquire a lock before reading or writing a data item, and release the lock after it is done. Locks can be shared or exclusive, depending on the type of operation. Shared locks allow multiple transactions to read the same data item, while exclusive locks allow only one transaction to write a data item.
  - **Timestamping**: A timestamp is a unique identifier that reflects the order of transaction execution. A transaction is assigned a timestamp when it starts, and every data item has a read timestamp and a write timestamp, indicating the last transaction that read or wrote the data item. A transaction can read or write a data item only if its timestamp is compatible with the data item's timestamps, otherwise it is aborted and restarted with a new timestamp.
  - **Optimistic**: An optimistic concurrency control method assumes that conflicts among transactions are rare, and allows transactions to execute without locking or checking timestamps. However, before committing, a transaction must validate that it has not violated the consistency or isolation properties. If a validation fails, the transaction is aborted and restarted.