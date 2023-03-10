 Here is the content in markdown format for the given topic:

### Concurrency control for the notes of the Unit 8 - Concurrency Control Techniques in the subject of Basics of Data Base Management System

- Concurrency control refers to the management of simultaneous operations on a database to ensure data integrity. It allows multiple users to access and manipulate the database concurrently. Some important concurrency control techniques are:

1. Locking: It prevents destructive interaction between concurrent transactions by regulating access to data. There are two types of locks:

- Shared lock: Allows multiple transactions to read a data item concurrently but not write to it.
- Exclusive lock: Allows only one transaction to access a data item whether for reading or writing.

Advantages: Simple and efficient if locks are held for short durations.
Disadvantages: May cause deadlocks and reduce concurrency.

2. Timestamp ordering: Each transaction is assigned a timestamp when it begins. Transactions are executed in timestamp order to avoid conflicts. The transaction with the earliest timestamp is executed first.
Advantage: Avoids deadlocks.
Disadvantage: May lead to starvation if new transactions keep getting earlier timestamps.

3. Optimistic concurrency control: Transactions are executed without locking the data items. Before committing, each transaction validates that no other transaction has modified its read data items. If validation fails, the transaction is aborted and reexecuted.
Advantage: Allows high concurrency.
Disadvantage: Risk of wasted work due to frequent aborts and reexecutions.

[Diagrams and examples can be added here to explain the concepts better.]

The choice of a technique depends on the system requirements such as throughput, response time, degree of concurrency, and simplicity. A combination of techniques may also be used to benefit from their individual advantages.