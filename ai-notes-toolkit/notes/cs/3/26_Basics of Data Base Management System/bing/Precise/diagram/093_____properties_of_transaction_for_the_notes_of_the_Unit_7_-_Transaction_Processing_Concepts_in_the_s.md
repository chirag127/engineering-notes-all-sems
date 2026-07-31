### Properties of Transaction

A transaction is a logical unit of work that must be either completed in its entirety or aborted. In the context of a database management system, a transaction represents a sequence of operations that are executed as a single unit. The properties of a transaction are often referred to as the ACID properties, which stands for Atomicity, Consistency, Isolation, and Durability.

1. **Atomicity**: This property ensures that a transaction is treated as an indivisible unit of work. Either all the operations in the transaction are completed successfully, or none of them are applied. If a transaction fails at any point, all changes made by the transaction are rolled back to their previous state.

2. **Consistency**: This property ensures that a transaction brings the database from one valid state to another. The database must satisfy a set of integrity constraints, and any transaction that violates these constraints is aborted.

3. **Isolation**: This property ensures that concurrent transactions do not interfere with each other. Each transaction must execute as if it is the only transaction in the system. Intermediate results of a transaction are not visible to other transactions until the transaction is committed.

4. **Durability**: This property ensures that once a transaction is committed, its changes to the database are permanent. Even in the event of a system failure, the changes made by the transaction must be recoverable.

These properties are essential for ensuring the reliability and integrity of data in a database management system. Transactions that satisfy these properties are said to be ACID-compliant.