 Here is the content in markdown format for the topic -

### Comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

The following are the major methods for concurrency control in distributed databases -

1. Locking -
- Exclusive lock - Only one transaction can access the data at a time. Prevents dirty reads but can cause deadlocks.
- Shared lock - Multiple transactions can read the data simultaneously but only one can write. Prevents dirty reads.
- Advantage - Simple to implement.
- Disadvantage - Can cause deadlocks and reduce concurrency.

2. Timestamp ordering -
- Each transaction is assigned a timestamp.
- Transactions are executed in timestamp order.
- Advantage - Prevents inconsistent analysis and lost updates.
- Disadvantage - May lead to starvation if low priority transactions get timestamps much later.

3. Optimistic methods -
- Transactions execute without acquiring locks.
- Validation is done at the end to check for conflicts.
- If conflict occurs, transaction is rolled back and retried.
- Advantage - High concurrency.
- Disadvantage - Extra overhead of validation and rollback in case of conflicts.

The choice of method depends on -
- Level of concurrency required.
- Importance of throughput vs consistency.
- Complexity of transactions.

Detailed diagrams and examples can be included if required to understand the concepts better. The methods can be compared in a table listing pros and cons which can aid in memorization. Mnemonics can be created based on the first letters of words in points to remember the list easily.