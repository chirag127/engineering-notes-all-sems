## Unit 9 - Distributed Transactions

- A distributed transaction is a database transaction that involves two or more network hosts.
- A transaction is a logical unit of work that guarantees the ACID properties (atomicity, consistency, isolation, durability) of a database.
- A distributed transaction requires a transaction manager that coordinates the operations on different hosts and ensures the ACID properties are maintained .
- A distributed transaction can be implemented using different protocols, such as two-phase commit, three-phase commit, or optimistic concurrency control.
- A distributed transaction can improve the performance, availability, and scalability of a database system, but also introduces challenges such as network failures, concurrency conflicts, and data inconsistency.