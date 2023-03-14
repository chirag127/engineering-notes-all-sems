Transaction processing in JDBC is a way of ensuring that a set of SQL statements are executed as a unit, so that either all of them are committed or none of them are committed. Transaction processing can be performed locally or distributed, depending on the application requirements. Transactions are atomic, consistent, isolated, and durable (ACID) modules of execution .

The following diagram illustrates the basic architecture of a transaction processing in JDBC:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Application     |    |  JDBC Driver     |    |  Database Server |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Begin           |    |                  |    |                  |
|  Transaction     |    |                  |    |                  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Execute         |    |  Execute         |    |  Execute         |
|  SQL Statement 1 |    |  SQL Statement 1 |    |  SQL Statement 1 |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Execute         |    |  Execute         |    |  Execute         |
|  SQL Statement 2 |    |  SQL Statement 2 |    |  SQL Statement 2 |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  ...             |    |  ...             |    |  ...             |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Commit or       |    |  Commit or       |    |  Commit or       |
|  Rollback        |    |  Rollback        |    |  Rollback        |
|  Transaction     |    |  Transaction     |    |  Transaction     |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```