# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are a mechanism used to ensure that only one transaction can access a data item at a time.
- Locks can be shared or exclusive. Shared locks allow multiple transactions to read a data item simultaneously, while exclusive locks allow only one transaction to write to a data item.
- Locks can be applied at different levels of granularity, such as at the row, page, or table level.
- Locks can be acquired and released explicitly by the transaction, or they can be managed automatically by the database system.
- Deadlocks can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques are used to handle this situation.
- Locks are an important part of concurrency control in distributed systems, as they help to ensure the consistency and correctness of data in the presence of concurrent transactions.