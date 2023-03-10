 Here is the content in markdown format for the given topic:

### Locking Techniques for Concurrency Control

- **Locks** are used to restrict access to data in order to maintain consistency and integrity of data. There are two main types of locks:

1. Shared locks - Allow multiple transactions to read a data item simultaneously.
2. Exclusive locks - Allow only one transaction to access a data item at a time.

- **Two phase locking protocol** is the most common locking protocol. It requires that all locks be obtained before any locks are released. It guarantees serializability and avoids deadlocks. The two phases are:

1. Growing phase - Transactions obtain all the locks they need.
2. Shrinking phase - Transactions release all their locks.

- **Deadlocks** can occur when two or more transactions hold locks on resources the other transaction needs and are waiting to acquire locks held by the other. Deadlocks can be handled using:

1. Deadlock prevention - Never allow a transaction to acquire a lock if it may lead to a deadlock. Eg. Request resources in a fixed order.
2. Deadlock avoidance - Allow locking but detect and resolve deadlocks when they occur.
3. Deadlock detection and recovery - Allow locking and deadlocks to occur but detect them and recover by rolling back one of the deadlocked transactions.

- **Granularity of locks** refers to the size of the data item being locked. Coarse-grained locking locks large data items and reduces lock overhead but limits concurrency. Fine-grained locking locks small data items and increases concurrency but increases lock overhead.

- Advantages: Simplicity, ensures serializability.
- Disadvantages: Reduced concurrency and risk of deadlocks.
- Applications: Widely used in practice for concurrency control.

[Include diagrams/codes/tables etc. if required to explain the concepts]