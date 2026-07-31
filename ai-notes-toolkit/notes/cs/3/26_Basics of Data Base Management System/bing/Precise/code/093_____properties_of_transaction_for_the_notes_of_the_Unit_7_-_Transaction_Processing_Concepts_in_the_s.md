### Properties of Transaction

A transaction is a logical unit of work that must be either completed in its entirety or aborted. In the context of a database management system, a transaction represents a sequence of database operations that are executed as a single unit. The properties of a transaction are often referred to as the ACID properties, which stands for Atomicity, Consistency, Isolation, and Durability.

1. **Atomicity**: This property ensures that a transaction is treated as an indivisible unit of work. Either all the operations in the transaction are completed successfully, or none of them are applied. If a transaction fails at any point, all the changes made by the transaction are rolled back to their previous state.

2. **Consistency**: This property ensures that a transaction brings the database from one valid state to another. The database must satisfy a set of integrity constraints, and a transaction must preserve these constraints. If a transaction would violate any of these constraints, it is aborted and all changes are rolled back.

3. **Isolation**: This property ensures that each transaction is executed in isolation from other transactions. The intermediate states of a transaction are not visible to other transactions, and the final state of a transaction is only visible to other transactions once the transaction has been committed.

4. **Durability**: This property ensures that once a transaction has been committed, its changes are permanent and will survive any subsequent failures. This is typically achieved by storing the transaction's changes in a durable storage medium, such as a hard disk, and writing them to a log that can be used to recover the database in the event of a failure.

These properties are essential for ensuring the reliability and consistency of a database system. They provide a strong foundation for building robust and scalable transaction processing systems.