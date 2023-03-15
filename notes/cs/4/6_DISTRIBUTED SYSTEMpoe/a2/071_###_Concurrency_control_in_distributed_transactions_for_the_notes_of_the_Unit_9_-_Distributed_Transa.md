 Here is the content in markdown format for the topic -

### Concurrency control in distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Concurrency control in distributed transactions ensures that simultaneous execution of transactions does not result in inconsistent state of the database. Following are the techniques used:

**Locking** - Prevents simultaneous access to data by multiple transactions. There are two types of locks:

- **Shared lock** - Allows multiple transactions to read data simultaneously but not update.
- **Exclusive lock** - Allows only one transaction to access data at a time, both for reading and updating.

Locking has following issues:

- Deadlock - Two transactions waiting for each other to release locks.
- Starvation - A transaction may have to wait indefinitely to get a lock.

**Timestamp ordering** - Each transaction is assigned a timestamp and transactions are executed in timestamp order to avoid conflicts. However, clocks at different sites may not be synchronized leading to anomalies.

**Optimistic concurrency control** - Transactions execute without locking, validating at commit time. If no conflicts are detected, transaction commits, else it rolls back and retries. Performance is better but more prone to rollback.

Following are some advantages and disadvantages of the concurrency control techniques:

Advantages:

- Increased throughput due to parallel execution of transactions.
- Improved resource utilization.

Disadvantages:

- Increased aborts and rollbacks reducing performance.
- Increased complexity of concurrency control algorithms.

Diagrams and examples can be included to explain the concepts in a better way. Applications of these techniques can be mentioned in database systems to manage concurrent access to data.