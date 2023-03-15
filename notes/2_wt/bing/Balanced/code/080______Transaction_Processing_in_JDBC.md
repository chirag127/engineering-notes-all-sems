#### Transaction Processing in JDBC

Transaction processing is a mandatory requirement of all applications that must guarantee consistency of their persistent data. With JDBC, transaction processing can either be performed locally or distributed. Transactions are atomic, consistent, isolated, and durable (ACID) modules of execution.

Local transactions are typically managed explicitly by the application or automatically by the Java Platform, Enterprise Edition (Java EE) application server. To perform a local transaction in JDBC, you need to use the following steps:

- Disable the auto-commit mode of the connection object by calling the `setAutoCommit(false)` method. This means that the SQL statements will not be committed automatically after execution.
- Execute one or more SQL statements using the connection object or a statement object created from it. You can use any of the `execute`, `executeQuery`, or `executeUpdate` methods of the statement object.
- If all the SQL statements are executed successfully, commit the transaction by calling the `commit()` method of the connection object. This will make the changes permanent in the database.
- If any of the SQL statements fails or throws an exception, roll back the transaction by calling the `rollback()` method of the connection object. This will undo all the changes made by the transaction in the database.
- Restore the auto-commit mode of the connection object by calling the `setAutoCommit(true)` method. This will enable the automatic commit of the subsequent SQL statements.

Here is an example of a local transaction in JDBC that transfers money from one account to another:

```java
// Assume conn is an active connection object
conn.setAutoCommit(false); // disable auto-commit
Statement stmt = conn.createStatement(); // create a statement object
try {
  // subtract 100 from account A
  stmt.executeUpdate("UPDATE accounts SET balance = balance - 100 WHERE name = 'A'");
  // add 100 to account B
  stmt.executeUpdate("UPDATE accounts SET balance = balance + 100 WHERE name = 'B'");
  conn.commit(); // commit the transaction
  System.out.println("Transaction completed successfully.");
} catch (SQLException e) {
  conn.rollback(); // roll back the transaction
  System.out.println("Transaction failed: " + e.getMessage());
} finally {
  conn.setAutoCommit(true); // restore auto-commit
  stmt.close(); // close the statement object
}
```

Distributed transactions are transactions that span multiple data sources or resource managers, such as databases, message queues, or file systems. Distributed transactions are typically managed by a transaction manager that coordinates the commit or rollback of the participating resources. To perform a distributed transaction in JDBC, you need to use the following steps:

- Obtain a reference to the transaction manager, such as the `UserTransaction` interface in Java EE.
- Begin the transaction by calling the `begin()` method of the transaction manager.
- Obtain one or more connection objects from the data sources involved in the transaction. The connection objects must support the `XAResource` interface, which enables the transaction manager to control the commit or rollback of the resources.
- Execute one or more SQL statements using the connection objects or statement objects created from them. You can use any of the `execute`, `executeQuery`, or `executeUpdate` methods of the statement object.
- If all the SQL statements are executed successfully, commit the transaction by calling the `commit()` method of the transaction manager. This will make the changes permanent in all the participating resources.
- If any of the SQL statements fails or throws an exception, roll back the transaction by calling the `rollback()` method of the transaction manager. This will undo all the changes made by the transaction in all the participating resources.

Here is an example of a distributed transaction in JDBC that transfers money from one database to another:

```java
// Assume utx is a UserTransaction object
utx.begin(); // begin the transaction
try {
  // obtain a connection object from the first data source
  Connection conn1 = ds1.getConnection();
  // obtain a connection object from the second data source
  Connection conn2 = ds2.getConnection();
  // create a statement object from the first connection object
  Statement stmt1 = conn1.createStatement();
  // create a statement object from the second connection object
  Statement stmt2 = conn2.createStatement();
  // subtract 100 from account A in the first database
  stmt1.executeUpdate("UPDATE accounts SET balance = balance - 100 WHERE name = 'A'");