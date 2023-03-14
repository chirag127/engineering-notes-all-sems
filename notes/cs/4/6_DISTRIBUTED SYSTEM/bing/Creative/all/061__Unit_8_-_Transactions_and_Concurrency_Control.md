## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that accesses or modifies the data in a database. A transaction can consist of one or more operations, such as reading, writing, inserting, deleting, or updating data. A transaction should have the following properties, known as **ACID**:

  - **Atomicity**: A transaction should either be executed completely or not at all. If any part of the transaction fails, the entire transaction should be aborted and the database should be restored to its previous state before the transaction started.
  - **Consistency**: A transaction should preserve the integrity and validity of the data in the database. A transaction should not violate any constraints, rules, or triggers that are defined on the data. A transaction should only transform the database from one consistent state to another.
  - **Isolation**: A transaction should not be affected by the concurrent execution of other transactions. A transaction should execute as if it is the only transaction in the system. A transaction should not see the intermediate or uncommitted results of other transactions.
  - **Durability**: A transaction should ensure that the changes it makes to the database are permanent and not lost due to system failures or crashes. A transaction should commit its changes to the database only when it is sure that the changes are safely written to the disk or other persistent storage.

- **Concurrency control** is the technique of managing the simultaneous execution of transactions in a shared database. Concurrency control ensures that correct results for concurrent operations are generated while getting those results as quickly as possible. Concurrency control is needed because concurrent transactions may interfere with each other and cause data inconsistencies, anomalies, or violations of integrity constraints. Some of the problems that may arise due to concurrency are:

  - **Lost update**: A transaction overwrites the changes made by another transaction that has not yet committed, resulting in the loss of data.
  - **Dirty read**: A transaction reads the uncommitted changes made by another transaction, resulting in inconsistent or incorrect data.
  - **Non-repeatable read**: A transaction reads the same data twice, but gets different results because another transaction has modified the data in between, resulting in inconsistent or incorrect data.
  - **Phantom read**: A transaction reads a set of data that satisfies some condition, but gets different results when it repeats the read because another transaction has inserted or deleted some data that satisfies the condition, resulting in inconsistent or incorrect data.

- Concurrency control techniques can be broadly classified into two categories:

  - **Lock-based protocols**: These protocols use locks to prevent transactions from accessing or modifying data that is being used by other transactions. A lock is a mechanism that grants or denies access to a data item or a set of data items. A lock can be either shared or exclusive. A shared lock allows a transaction to read a data item, but not to modify it. An exclusive lock allows a transaction to both read and write a data item, but not to share it with other transactions. A transaction must acquire the appropriate lock before accessing a data item, and release the lock after finishing the access. A transaction must also follow some rules to ensure the correct locking and unlocking of data items, such as:

    - **Two-phase locking (2PL)**: A transaction must acquire all the locks it needs before it releases any lock. This ensures that a transaction holds all the locks it needs for its entire duration, and does not interfere with other transactions. 2PL can be further divided into:

      - **Basic 2PL**: A transaction can acquire locks at any point during its execution, but must release all the locks at the end of the transaction.
      - **Conservative 2PL**: A transaction must acquire all the locks it needs before it starts its execution, and release all the locks at the end of the transaction.
      - **Strict 2PL**: A transaction must acquire locks at any point during its execution, but must release all the locks only after it commits or aborts.
      - **Rigorous 2PL**: A transaction must acquire all the locks it needs before it starts its execution, and release all the locks only after it commits or aborts.

    - **Deadlock prevention**: A transaction must follow some ordering or timing constraints to avoid deadlock situations, where two or more transactions are waiting for each other to release locks. Some of the methods to prevent deadlock are:

      - **Timestamp ordering**: A transaction is assigned a unique timestamp when it starts, and must access data items in the order of their timestamps. A transaction can only lock a data item if its timestamp is smaller than the timestamp of any other transaction