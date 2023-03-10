 Here is the content in markdown format for the topic ## Unit 8 - Concurrency Control Techniques:

## Unit 8 - Concurrency Control Techniques

### What is Concurrency Control?
Concurrency control refers to the techniques used to manage access to shared data in a system where multiple users may access and update the data simultaneously. It ensures that the following properties are enforced:

- Atomicity: Transactions are executed completely or not at all.
- Consistency: Data is consistent across the system.
- Isolation: Transactions are isolated from one another.
- Durability: Committed transactions are permanently stored.

Some common concurrency control techniques are:

1. Locking: Prevents other transactions from accessing data that has been locked by another transaction. Can lead to deadlocks.
- Shared locks: Prevent other transactions from modifying data. Allow reads.
- Exclusive locks: Prevent any other access to locked data.

2. Timestamp ordering: Each transaction is tagged with a timestamp and transactions are executed in timestamp order to avoid conflicts. Can lead to starvation.

3. Optimistic concurrency control: Transactions execute without acquiring locks, but their changes are verified before commit. If a conflict is detected, the transaction is aborted and retried.

Advantages and disadvantages of each technique and examples of their applications can be discussed in detail. Diagrams to show the working of each technique may also be included. The content can be expanded with more details and points as required.