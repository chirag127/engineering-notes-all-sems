### Concurrency Control

- Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the database.
- Concurrency control is especially important for real-time database systems, where transactions have timing constraints and must be completed before their deadlines.
- Concurrency control in real-time database systems should consider both data consistency and timing constraints, and also adapt to changes in the operating environment and guarantee the completion of critical transactions.

### Concurrency Control Methods

- There are two main methods of concurrency control: locking-based and timestamp-based.
- Locking-based methods use locks to prevent concurrent transactions from accessing the same data item in conflicting modes (read or write).
- Timestamp-based methods use timestamps to order the transactions and ensure that older transactions are not affected by newer ones.
- Both methods have advantages and disadvantages, and different variants and extensions have been proposed to improve their performance and suitability for real-time database systems  .

### Locking-Based Methods

- Locking-based methods use two types of locks: shared locks and exclusive locks.
- Shared locks allow multiple transactions to read the same data item, but prevent any transaction from writing it.
- Exclusive locks allow only one transaction to access the data item, either in read or write mode.
- A transaction must acquire the appropriate lock before accessing a data item, and release it after finishing the operation.
- A transaction can be blocked if it requests a lock that is already held by another transaction in a conflicting mode.
- A deadlock can occur if two or more transactions are waiting for each other to release their locks.
- Locking-based methods can use different protocols to grant and release locks, such as two-phase locking, strict two-phase locking, rigorous two-phase locking, etc.
- Locking-based methods can also use different techniques to prevent or resolve deadlocks, such as deadlock prevention, deadlock detection, deadlock avoidance, etc.
- Locking-based methods can be integrated with real-time scheduling protocols, such as priority ceiling protocol, to improve the performance and predictability of real-time transactions.

### Timestamp-Based Methods

- Timestamp-based methods use timestamps to order the transactions and ensure that older transactions are not affected by newer ones.
- A timestamp is a unique identifier that reflects the start time or the priority of a transaction.
- A transaction must have a timestamp before accessing any data item, and the timestamp is fixed throughout the execution of the transaction.
- A data item has two timestamps: read timestamp and write timestamp, which record the latest timestamps of the transactions that have read or written the data item.
- A transaction can access a data item only if its timestamp is compatible with the timestamps of the data item, according to some rules.
- A transaction can be aborted if it violates the timestamp ordering rules, and restarted with a new timestamp.
- Timestamp-based methods can avoid deadlocks, but may cause more aborts and restarts than locking-based methods.
- Timestamp-based methods can use different variants and extensions, such as optimistic concurrency control, multiversion concurrency control, etc .