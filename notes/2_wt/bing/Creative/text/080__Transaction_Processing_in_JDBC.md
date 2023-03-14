#### Transaction Processing in JDBC

- Transaction processing is a mandatory requirement of all applications that must guarantee consistency of their persistent data.
- A transaction is a set of one or more statements that is executed as a unit, so either all of the statements are executed, or none of the statements is executed.
- Transactions are atomic, consistent, isolated, and durable (ACID) modules of execution.
- With the Microsoft JDBC Driver for SQL Server, transaction processing can either be performed locally or distributed.
- When a connection is created, it is in auto-commit mode. This means that each individual SQL statement is treated as a transaction and is automatically committed right after it is executed.
- The way to allow two or more statements to be grouped into a transaction is to disable the auto-commit mode by calling `con.setAutoCommit(false)`.
- After the auto-commit mode is disabled, no SQL statements are committed until you call the method `commit` explicitly. All statements executed after the previous call to the method `commit` are included in the current transaction and committed together as a unit.
- If an error occurs during the execution of a transaction, you can call the method `rollback` to undo all the changes made by the statements in the current transaction.
- The JDBC driver also supports transaction savepoints, which allow you to mark a point within a transaction that you can roll back to without affecting the preceding statements.
- The JDBC driver also supports result set holdability, which determines whether a result set is closed or not when a transaction is committed or rolled back.
- The JDBC driver also supports XA transactions, which are distributed transactions that span multiple databases or resource managers.