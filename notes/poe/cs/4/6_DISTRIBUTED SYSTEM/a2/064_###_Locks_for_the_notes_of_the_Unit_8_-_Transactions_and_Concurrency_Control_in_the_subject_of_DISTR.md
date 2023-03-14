 Here is the content in markdown format:

### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Locks are used to ensure consistency and correctness of data in a distributed system when multiple transactions are trying to access/update the same data concurrently. Some key points about locks are:

- Shared locks: Allow multiple transactions to read a data item concurrently but prohibit write access. Useful for read-only transactions.
- Exclusive locks: Allow only one transaction to access a data item at a time, either for reading or writing. Prevents dirty reads but can lead to deadlocks.
- Deadlocks: When two or more transactions hold locks on resources that the other transaction needs, leading to both being stuck indefinitely. Can be avoided using ordering/timeout strategies.
- Two-phase locking: A protocol where transactions get all the locks they need in one phase and then release them in the second phase. Guarantees serializability but can lead to low concurrency.
- Timestamp ordering: Transactions are ordered based on their start time to avoid conflicts. The earlier transaction is executed first. Does not guarantee serializability in all cases.

Some mnemonics for remembering lock types:

- "Readers don't block writers, writers block readers" - Shared locks
- "One at a time!" - Exclusive locks

Advantages of locks: Ensures data consistency, prevents dirty reads.
Disadvantages: Can lead to deadlocks and low concurrency.

 locks are commonly used in databases and distributed systems to coordinate access to shared data. They are a key concept in maintaining data integrity in such systems with multiple concurrent transactions.