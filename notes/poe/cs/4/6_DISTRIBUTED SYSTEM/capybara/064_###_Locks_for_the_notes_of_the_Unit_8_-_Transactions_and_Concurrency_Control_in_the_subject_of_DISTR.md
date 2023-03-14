### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

In a distributed system, multiple processes can access the same data concurrently. This leads to the problem of data inconsistency, where the data may be modified by one process while another process is reading or modifying the same data. To prevent this problem, locks are used to ensure that only one process can access the data at a time.

#### Types of Locks

1. Shared Lock: This lock is used when multiple processes want to read the same data. A shared lock allows multiple processes to access the data simultaneously but prevents any process from modifying the data until all the shared locks have been released.

2. Exclusive Lock: This lock is used when a process wants to modify a piece of data. An exclusive lock allows the process to modify the data but prevents any other process from accessing the data until the lock has been released.

#### Locking Techniques

1. Two-Phase Locking: This technique ensures serializability by dividing the execution of a transaction into two phases. In the first phase, the transaction acquires all the necessary locks before modifying any data. In the second phase, the transaction releases all the locks after it has completed the modifications.

2. Timestamp Ordering: This technique assigns a unique timestamp to each transaction and orders the transactions based on their timestamps. The transactions are executed in the order of their timestamps, and the locks are acquired and released accordingly.

#### Advantages of Locking

1. Prevents data inconsistency.
2. Ensures serializability.
3. Allows multiple processes to access the data simultaneously (in the case of shared locks).

#### Disadvantages of Locking

1. Can lead to deadlocks if not implemented correctly.
2. Can cause delays if a process is waiting for a lock to be released.

#### Learning Trick

Remember the acronym "STELD" to recall the advantages of locking: Serializability, prevents data inconsistency, allows multiple access (shared locks), and Ensures data consistency.