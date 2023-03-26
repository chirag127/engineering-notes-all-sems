 Here is the content in markdown format without any emojis or external links:

## Unit 8 - Transactions and Concurrency Control

1. Transactions - Transactions are logical units of work that must be executed completely or not at all. This ensures data integrity and consistency. Some key properties of transactions are:

- Atomicity - Either all operations in a transaction succeed or all fail.
- Consistency - A transaction moves data from one consistent state to another.
- Isolation - Transactions execute independently and separately from other transactions.
- Durability - Once a transaction commits, its changes persist even in the event of a system failure.

2. ACID Properties - ACID is an acronym that stands for the key properties of a transaction:

- Atomicity - Either all operations succeed or all fail.
- Consistency - Data is in a valid state after the transaction.
- Isolation - Transactions execute separately from other transactions.
- Durability - Changes from committed transactions persist even after a system failure.

3. Transaction Processing - How a DBMS handles transaction processing includes:

- Scheduling - Determining the order in which transactions will be processed.
- Concurrency Control - Managing simultaneous access to data to maintain consistency. This can be done using locks, timestamps, or other methods.
- Recovery - Ensuring that the database is restored to a consistent state after a system failure. The DBMS will undo incomplete transactions or redo completed transactions as needed.

4. Locks - A lock is a mechanism used to restrict access to a resource in a database. Common types of locks include:

- Shared Locks - Used for read-only transactions. Multiple transactions can hold a shared lock on the same resource simultaneously.
- Exclusive Locks - Used for writing data. Only one transaction can hold an exclusive lock on a resource at a time.
- Intention Locks - Used to indicate a transaction plans to place a shared or exclusive lock on a lower-level resource.

Does this look okay? Let me know if you would like me to modify or add anything.