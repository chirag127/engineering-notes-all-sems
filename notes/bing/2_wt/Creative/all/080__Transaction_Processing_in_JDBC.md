#### Transaction Processing in JDBC

- Transaction processing is a mandatory requirement of all applications that must guarantee consistency of their persistent data.
- A transaction is a set of one or more statements that is executed as a unit, so either all of the statements are executed, or none of the statements is executed.
- Transactions are atomic, consistent, isolated, and durable (ACID) modules of execution.
- Atomicity means either all successful or none.
- Consistency ensures bringing the database from one consistent state to another consistent state.
- Isolation ensures that transaction is isolated from other transaction.
- Durability ensures that once a transaction has been committed, it will remain so, even in the event of power loss, crashes, or errors.
- In JDBC, every SQL query will be considered as a transaction. When we create a Database connection in JDBC, it will run in auto-commit mode (auto-commit value is TRUE). After the execution of the SQL statement, it will be committed automatically.
- To disable auto-commit mode and manage transactions manually, we can use the `setAutoCommit(false)` method of the `Connection` interface.
- To commit a transaction, we can use the `commit()` method of the `Connection` interface.
- To roll back a transaction, we can use the `rollback()` method of the `Connection` interface.
- To set and roll back to savepoints, we can use the `setSavepoint()` and `rollback(Savepoint)` methods of the `Connection` interface. A savepoint is a point within a transaction that allows us to roll back part of a transaction, instead of the full transaction.
- The JDBC driver supports local transactions by using various methods of the `SQLServerConnection` class, including `setAutoCommit`, `commit`, and `rollback`. Local transactions are typically managed explicitly by the application or automatically by the Java Platform, Enterprise Edition (Java EE) application server.
- The JDBC driver also supports distributed transactions by using the `SQLServerXADataSource` class, which implements the `XADataSource` interface. Distributed transactions are transactions that span multiple data sources and are coordinated by a transaction manager, such as the Java EE application server.

A simple example of transaction processing in JDBC is given below:

```java
// Create a connection object
Connection con = DriverManager.getConnection(url, user, password);

// Disable auto-commit mode
con.setAutoCommit(false);

try {
  // Create a statement object
  Statement stmt = con.createStatement();

  // Execute some SQL statements
  stmt.executeUpdate("INSERT INTO emp VALUES (101, 'John')");
  stmt.executeUpdate("UPDATE emp SET sal = 5000 WHERE id = 102");

  // Commit the transaction
  con.commit();
  System.out.println("Transaction committed successfully");
} catch (SQLException e) {
  // Roll back the transaction in case of any error
  con.rollback();
  System.out.println("Transaction rolled back due to: " + e.getMessage());
} finally {
  // Close the connection
  con.close();
}
```