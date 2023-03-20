 Here is the formal content written in Markdown format without any emojis or external links:

## Unit 4 - Transaction Processing Concept

1. Transaction: A transaction is a unit of work performed within a database management system (DBMS) against a database, and treated in a coherent and reliable way independent of other transactions. Transactions ensure that all parts of a database are updated together and successfully, or all parts are returned to the state before the transaction started (if there is a failure).
2. ACID Properties: Transactions exhibit four properties referred to as ACID properties:

A - Atomicity: All changes to the state are done at once. Either all happen or none happen.
C - Consistency: The database moves from one consistent state to another. The transaction never leaves the database in an inconsistent state.
I - Isolation: Transactions are isolated from one another. The intermediate state of transactions are not visible to other transactions.
D - Durability: Once a transaction completes successfully, its changes persist, even in the face of system failures.

3. Concurrency & Locks: When multiple transactions are executing simultaneously, concurrency control techniques are necessary to ensure the ACID properties and data consistency. Common techniques for concurrency control include locking and versioning. Locks are mechanisms to restrict access to resources based on a process ownership. They are used to maintain data consistency in a concurrent environment.
4. Transaction Processing Monitors: For efficiency and throughput, transaction processing is often supported by transaction processing monitors. They are specialized software components that support the processing of transactions, including:

Buffering and spooling data
Connection pooling
Load balancing
Fault tolerance
Recovery mechanisms
Contention management and concurrency control