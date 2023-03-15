## Unit 7 - Transaction Processing Concepts

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has four main properties: **atomicity**, **consistency**, **isolation**, and **durability** (ACID).
- **Atomicity** means that a transaction either completes all of its operations or none of them. If a transaction fails, the database is restored to its state before the transaction started.
- **Consistency** means that a transaction preserves the integrity constraints of the database. A transaction can only bring the database from one valid state to another valid state.
- **Isolation** means that a transaction executes as if it were the only transaction in the system. The intermediate results of a transaction are not visible to other transactions, and a transaction does not see the effects of other transactions that are executed concurrently.
- **Durability** means that the effects of a committed transaction are permanent and will not be lost in the event of a system failure.
- Transaction processing systems are systems that support large-scale, concurrent, and reliable execution of transactions on a database. They use various techniques such as locking, logging, recovery, and concurrency control to ensure the ACID properties of transactions.