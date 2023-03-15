## Unit 7 - Transaction Processing Concepts

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four main properties: **atomicity, consistency, isolation, and durability** (ACID).
- **Atomicity** means that a transaction either completes all of its operations or none of them. If a transaction fails, the database is restored to its state before the transaction started.
- **Consistency** means that a transaction preserves the integrity constraints of the database. A transaction can only transform the database from one consistent state to another.
- **Isolation** means that a transaction executes as if it were the only one running on the database. The intermediate results of a transaction are not visible to other transactions.
- **Durability** means that the effects of a committed transaction are permanent and will not be lost even in the event of a system failure.
- Transaction processing systems are systems with large databases and hundreds of concurrent users executing database transactions.
- Transaction processing systems have to ensure the ACID properties of transactions while allowing a high degree of concurrency and performance.
- Transaction processing systems use various techniques to achieve these goals, such as locking, logging, recovery, concurrency control, and deadlock handling  .