#### Transaction Processing in JDBC

- A transaction is a logical unit of work that consists of one or more SQL statements executed on a database.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the statements in a transaction are executed successfully, or none of them are executed at all.
- Consistency means that a transaction preserves the integrity constraints and business rules of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions, and vice versa.
- Durability means that the effects of a transaction are permanent and persist even in the event of a system failure.
- By default, JDBC uses auto-commit mode, which means that each SQL statement is executed as a separate transaction and committed immediately after execution.
- To disable auto-commit mode and execute multiple statements as a single transaction, use the `setAutoCommit(false)` method of the `Connection` object.
- To commit a transaction, use the `commit()` method of the `Connection` object.
- To roll back a transaction, use the `rollback()` method of the `Connection` object.
- To set the isolation level of a transaction, use the `setTransactionIsolation(int level)` method of the `Connection` object, where `level` is one of the following constants: `TRANSACTION_READ_UNCOMMITTED`, `TRANSACTION_READ_COMMITTED`, `TRANSACTION_REPEATABLE_READ`, or `TRANSACTION_SERIALIZABLE`.
- To check the current isolation level of a transaction, use the `getTransactionIsolation()` method of the `Connection` object, which returns one of the above constants.
- To enable or disable the savepoint feature, use the `setSavepoint()` and `releaseSavepoint()` methods of the `Connection` object, respectively.
- A savepoint is a point in a transaction that allows partial rollback of the transaction.
- To create a savepoint, use the `setSavepoint()` method of the `Connection` object, which returns a `Savepoint` object.
- To roll back to a savepoint, use the `rollback(Savepoint savepoint)` method of the `Connection` object, where `savepoint` is the `Savepoint` object returned by the `setSavepoint()` method.
- To release a savepoint, use the `releaseSavepoint(Savepoint savepoint)` method of the `Connection` object, where `savepoint` is the `Savepoint` object returned by the `setSavepoint()` method.