## Unit 8 - Concurrency Control Techniques

Concurrency control is a fundamental concept in database management systems that ensures that multiple transactions can execute concurrently without compromising the consistency and integrity of the database. In this unit, we will discuss various concurrency control techniques that are used to manage concurrent transactions efficiently.

### Lock-Based Concurrency Control
- Lock-based concurrency control is a technique that ensures that a transaction can access a data item only if it holds the appropriate lock on that item.
- Locks can be of two types: shared locks and exclusive locks. A shared lock allows multiple transactions to read a data item, whereas an exclusive lock allows only one transaction to write to a data item.
- Lock-based concurrency control can be implemented using two-phase locking (2PL) protocol, where a transaction acquires all the required locks before it starts executing and releases all the locks after it completes its execution.
- Deadlocks can occur in a lock-based concurrency control system when two or more transactions are waiting for locks that are held by each other. To avoid deadlocks, various deadlock prevention and detection techniques can be used.

### Timestamp-Based Concurrency Control
- Timestamp-based concurrency control is a technique that assigns a unique timestamp to each transaction and data item in the database.
- Transactions are executed in increasing order of timestamp, and a transaction can access a data item only if its timestamp is less than the timestamp of the data item.
- Timestamp-based concurrency control can be implemented using either a wait-die or wound-wait protocol to handle conflicting transactions.
- Wait-die protocol allows older transactions to wait for younger transactions to release the required locks, whereas wound-wait protocol allows younger transactions to abort older transactions that hold the required locks.

### Optimistic Concurrency Control
- Optimistic concurrency control is a technique that assumes that conflicts between transactions are rare and allows multiple transactions to execute concurrently without acquiring any locks.
- Each transaction is executed in a separate copy of the database, and conflicts between transactions are detected and resolved during the commit phase.
- If two transactions conflict, one of them is rolled back and restarted with the updated database state.
- Optimistic concurrency control is efficient for databases with low contention, but it can result in a lot of rollbacks if there are frequent conflicts between transactions.

### Multi-Version Concurrency Control
- Multi-version concurrency control is a technique that allows multiple versions of a data item to exist in the database at the same time.
- Each transaction sees a snapshot of the database at a specific time, and multiple versions of a data item can exist in the database at different times.
- Multi-version concurrency control can be implemented using either a timestamp ordering or a snapshot isolation protocol.
- In timestamp ordering, each transaction sees the version of a data item that has the nearest timestamp that is less than or equal to the transaction's timestamp.
- In snapshot isolation, each transaction sees a snapshot of the database that corresponds to a specific timestamp without acquiring any locks.

In conclusion, concurrency control is an essential aspect of database management systems, and various techniques can be used to manage concurrent transactions efficiently. Lock-based concurrency control is the most common technique, but other techniques like timestamp-based concurrency control, optimistic concurrency control, and multi-version concurrency control can also be used depending on the requirements of the database application.