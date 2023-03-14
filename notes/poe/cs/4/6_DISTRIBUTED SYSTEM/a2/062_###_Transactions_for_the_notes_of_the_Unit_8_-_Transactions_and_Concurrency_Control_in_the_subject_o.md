 Here is the content in markdown format for the topic ### Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM:

### Transactions

- A transaction is a logical unit of work that consists of one or more operations. Either all operations of a transaction are executed successfully or none. This is known as atomicity.
- Transactions must adhere to ACID properties:
    - Atomicity: Either all operations succeed or none.
    - Consistency: Transaction moves data from one valid state to another.
    - Isolation: Transactions execute independently.
    - Durability: Changes made by a transaction are permanent.
- Example: Transferring money from one bank account to another. This involves debiting one account and crediting the other. Either both operations must complete successfully or rollback in case of failure.
- Concurrency issues: When multiple transactions access and update the same data simultaneously, concurrency control is needed to maintain consistency. This can be achieved using mechanisms like locking, timestamp ordering, etc.
- Locking: Acquiring locks on data to prevent conflicting transactions from accessing it simultaneously. This ensures isolation but can lead to deadlocks and reduced concurrency.
- Timestamp ordering: Assigning timestamps to transactions and executing them in timestamp order to achieve serializability. The overhead of organizing transactions by timestamps may affect performance.
- Advantages of transactions: Support for atomicity, consistency, and durability. Increased concurrency with proper control mechanisms.
- Disadvantages of transactions: Overhead of concurrency control can affect performance. Complexity of rollback and recovery in case of failures. Deadlocks can occur with locking.

[Detailed diagrams and examples can be added here if required.]