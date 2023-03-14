 Here is the content in markdown format for the topic -

### Comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

The following are the major methods used for concurrency control in distributed database systems -

1. Locking - It is a synchronization mechanism to prevent concurrent transactions from accessing shared data simultaneously. Following are the types of locking -

- Exclusive lock - Only one transaction can obtain the lock. Prevents dirty reads but can lead to deadlocks.
- Shared lock - Multiple transactions can obtain the lock for read-only access. Prevents dirty reads.
- Intention locks - Used to obtain locks on lower-level data.

Advantages - Prevents dirty reads and ensures consistency.
Disadvantages - Can lead to deadlocks and low concurrency.

2. Time stamp ordering - Each transaction is assigned a timestamp and transactions are executed in timestamp order. No deadlocks but can lead to starvation.

3. Optimistic methods - Transactions are executed without synchronization and consistency is verified at commit time. If conflict occurs, transactions are rolled back and retried.
High concurrency but more aborts and wasted work.

Mnemonics -
Locking - Exclusive (X), Shared (S), Intention (IX, IS)
Time stamp - Ordering by time
Optimistic - Hope for the best, verify and retry

Applications - Locking used in banking systems. Time stamp ordering used in scientific databases. Optimistic methods used in collaborative systems with less contention.

Detailed diagrams and examples can be included if required. The advantages, disadvantages and applications help in understanding the concepts better and strengthening the memory of the topics. Please let me know if you would like me to elaborate on any part of the answer.