Transaction processing in JDBC is a way of ensuring the consistency and integrity of the data in a database by executing a set of SQL statements as a unit. A transaction is either committed or rolled back, meaning that all the changes made by the statements are either saved or discarded. JDBC supports both local and distributed transactions, depending on the driver and the database.

The following diagram illustrates the basic architecture of a local transaction in JDBC:

```
+------------------+        +-----------------+        +-----------------+
| Application code |        | JDBC driver     |        | Database server |
+------------------+        +-----------------+        +-----------------+
|                  |        |                 |        |                 |
| 1. Create        |        |                 |        |                 |
| connection       |------->|                 |------->|                 |
|                  |        |                 |        |                 |
| 2. Disable       |        |                 |        |                 |
| auto-commit      |------->|                 |------->|                 |
|                  |        |                 |        |                 |
| 3. Execute       |        |                 |        |                 |
| SQL statements   |------->|                 |------->|                 |
|                  |        |                 |        |                 |
| 4. Commit or     |        |                 |        |                 |
| rollback         |------->|                 |------->|                 |
| transaction      |        |                 |        |                 |
|                  |        |                 |        |                 |
| 5. Close         |        |                 |        |                 |
| connection       |------->|                 |------->|                 |
+------------------+        +-----------------+        +-----------------+
```

The steps are as follows:

1. The application code creates a connection object by using the JDBC driver.
2. The application code disables the auto-commit mode of the connection, which means that the SQL statements will not be committed automatically after execution.
3. The application code executes one or more SQL statements using the connection object. The statements are sent to the database server by the JDBC driver.
4. The application code decides whether to commit or rollback the transaction, based on the results of the SQL statements. The commit or rollback operation is performed by the JDBC driver on the database server.
5. The application code closes the connection object, which releases the resources used by the transaction.