## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has the following properties:
  - **Atomicity**: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to the state before the transaction started.
  - **Consistency**: A transaction preserves the integrity constraints of the database. If the database is consistent before the transaction, it is also consistent after the transaction.
  - **Isolation**: A transaction is executed as if it is the only one running on the database. The intermediate results of a transaction are not visible to other transactions.
  - **Durability**: The effects of a transaction are permanent and survive any system failures.
- **Concurrency control** is the technique of managing the simultaneous execution of transactions on a shared database, such that the consistency and isolation properties are maintained.
- Concurrency control can be implemented using various methods, such as:
  - **Locking**: A transaction acquires locks on the data items it accesses, and releases them when it is done. A lock can be either shared (for read-only access) or exclusive (for read-write access). A transaction can only access a data item if it has the appropriate lock on it, and no other transaction has a conflicting lock on it.
  - **Timestamping**: A transaction is assigned a unique timestamp when it starts, and the timestamp is used to order the transactions. A transaction can only access a data item if its timestamp is greater than the timestamp of the last transaction that wrote to the data item, and less than the timestamp of the last transaction that read the data item.
  - **Optimistic**: A transaction executes without acquiring any locks, and checks for conflicts at the end. If a conflict is detected, the transaction is aborted and restarted with a new timestamp.
  - **Multiversion**: A transaction accesses a version of the data item that corresponds to its timestamp, and creates a new version of the data item if it modifies it. A transaction can only access a version of the data item if its timestamp is greater than or equal to the timestamp of the version, and less than the timestamp of the next version.