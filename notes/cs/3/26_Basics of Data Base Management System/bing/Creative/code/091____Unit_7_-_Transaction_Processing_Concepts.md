## Unit 7 - Transaction Processing Concepts

- A transaction is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either completes all of its operations or none of them.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction executes as if it were the only one running on the database, without interference from other transactions.
- Durability means that the effects of a transaction persist even in the case of system failures.
- Transaction processing is the execution of transactions by a database management system (DBMS) that ensures ACID properties.
- Transaction processing systems are systems with large databases and hundreds of concurrent users executing database transactions.
- Transaction processing systems support applications such as banking, reservation, e-commerce, and inventory management.
- Transaction processing systems can be classified into two types: online transaction processing (OLTP) and batch transaction processing (BTP).
- OLTP systems process transactions in real time, as they arrive, and provide immediate feedback to the users.
- BTP systems process transactions in batches, at regular intervals, and do not require immediate feedback to the users.
- Transaction processing systems require concurrency control and recovery mechanisms to ensure ACID properties.
- Concurrency control is the technique of coordinating the execution of multiple transactions on the same database, to prevent conflicts and ensure isolation.
- Recovery is the technique of restoring the database to a consistent state after a failure, to ensure atomicity and durability.
- Concurrency control and recovery mechanisms can be implemented using various methods, such as locking, timestamping, logging, and checkpointing.