#### Transaction Processing in JDBC

- Transaction processing is a mandatory requirement of all applications that must guarantee consistency of their persistent data .
- Transactions are atomic, consistent, isolated, and durable (ACID) modules of execution .
- Atomicity means either all successful or none.
- Consistency ensures bringing the database from one consistent state to another consistent state.
- Isolation ensures that transaction is isolated from other transaction.
- Durability ensures that the changes made by the transaction are permanent.
- In JDBC, every SQL query will be considered as a transaction.
- When we create a Database connection in JDBC, it will run in auto-commit mode (auto-commit value is TRUE) .
- Auto-commit mode means that after the execution of the SQL statement, it will be committed automatically .
- To disable auto-commit mode, we can use the setAutoCommit(false) method of the Connection interface .
- To commit a transaction, we can use the commit() method of the Connection interface .
- To rollback a transaction, we can use the rollback() method of the Connection interface .
- To set and rollback to savepoints, we can use the setSavepoint() and rollback(Savepoint) methods of the Connection interface.
- Transaction processing can either be performed locally or distributed .
- Local transactions are typically managed explicitly by the application or automatically by the Java Platform, Enterprise Edition (Java EE) application server.
- Distributed transactions are managed by a transaction manager that coordinates the work of multiple resource managers.