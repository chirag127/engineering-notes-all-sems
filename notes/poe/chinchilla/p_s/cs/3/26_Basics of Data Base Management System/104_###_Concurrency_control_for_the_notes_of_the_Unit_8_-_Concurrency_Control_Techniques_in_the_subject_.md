### Concurrency Control for the Notes of Unit 8 - Concurrency Control Techniques in the Subject of Basics of Database Management System

Concurrency control is an essential aspect of database management systems, especially in scenarios where multiple users simultaneously access the same data. Without proper concurrency control, the database system may encounter problems such as data inconsistency, data loss, and transaction failures. In this unit, we will learn about various concurrency control techniques used in database management systems.

#### Definition of Concurrency Control

Concurrency control refers to the mechanism that ensures that multiple users or transactions accessing the same data do not interfere with each other, resulting in incorrect or inconsistent data. Concurrency control ensures that the database system maintains data consistency and integrity while allowing concurrent access.

#### Types of Concurrency Control Techniques

There are two types of concurrency control techniques:

1. Pessimistic Concurrency Control: This technique assumes that conflicts between transactions are likely to occur and hence locks the data item until the transaction completes its execution. Pessimistic concurrency control techniques include two-phase locking (2PL), multiple granular locking, and timestamp ordering.

2. Optimistic Concurrency Control: This technique assumes that conflicts between transactions are rare and hence allows multiple transactions to access the same data item simultaneously. Optimistic concurrency control techniques include timestamp-based concurrency control (TBCC) and validation-based concurrency control (VBCC).

#### Two-Phase Locking (2PL)

Two-phase locking (2PL) is a pessimistic concurrency control technique that involves two phases:

1. The Growing Phase: In this phase, the transaction acquires the locks for the data items it needs to access. Once a lock is acquired, it cannot be released until the transaction completes its execution.

2. The Shrinking Phase: In this phase, the transaction releases the locks it acquired during the growing phase. Once a lock is released, it cannot be reacquired.

#### Timestamp Ordering

Timestamp ordering is another pessimistic concurrency control technique that assigns a unique timestamp to each transaction. The timestamp determines the order in which the transactions are executed. If two transactions request the same data item, the transaction with the higher timestamp is given priority.

#### Validation-Based Concurrency Control (VBCC)

Validation-based concurrency control (VBCC) is an optimistic concurrency control technique that allows multiple transactions to execute concurrently. VBCC involves the following steps:

1. Read Phase: In this phase, the transaction reads the data items it needs to access.

2. Validation Phase: In this phase, the transaction checks if any other transaction has modified the data item since it was last read. If the data item is not modified, the transaction proceeds to the write phase. Otherwise, the transaction is aborted.

3. Write Phase: In this phase, the transaction writes the updated data items to the database.

#### Advantages of Concurrency Control

1. Improved system performance by allowing multiple transactions to execute concurrently.
2. Improved data consistency and integrity.
3. Reduced risk of data loss and transaction failures.

#### Disadvantages of Concurrency Control

1. Increased complexity in the database management system.
2. Increased system overhead due to the use of locks and timestamps.
3. Possible reduction in system throughput if the number of transactions requesting the same data item is high.

#### Conclusion

Concurrency control is an essential aspect of database management systems that ensures data consistency and integrity while allowing concurrent access. There are various concurrency control techniques, including pessimistic and optimistic techniques, each with its advantages and disadvantages. Understanding these techniques is essential for effective database management.