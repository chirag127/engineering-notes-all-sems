Transaction processing in JDBC is a way of ensuring the consistency and integrity of the data in a database by executing a set of SQL statements as a unit. A transaction is either committed (all changes are made permanent) or rolled back (all changes are undone) depending on the outcome of the execution. JDBC supports both local and distributed transactions, which can be managed by the application or by the Java EE application server.

A possible ASCII diagram for transaction processing in JDBC is:

```
+------------------+       +------------------+       +------------------+
|                  |       |                  |       |                  |
|  Application     |       |  JDBC Driver     |       |  Database Server |
|                  |       |                  |       |                  |
+------------------+       +------------------+       +------------------+
       |                         |                         |
       |  setAutoCommit(false)  |                         |
       |----------------------->|                         |
       |                         |                         |
       |  executeUpdate(...)    |                         |
       |----------------------->|                         |
       |                         |  executeUpdate(...)    |
       |                         |----------------------->|
       |                         |                         |
       |                         |  executeQuery(...)     |
       |                         |----------------------->|
       |                         |                         |
       |                         |  ResultSet             |
       |                         |<-----------------------|
       |  ResultSet             |                         |
       |<-----------------------|                         |
       |                         |                         |
       |  commit()              |                         |
       |----------------------->|                         |
       |                         |  commit()              |
       |                         |----------------------->|
       |                         |                         |
       |                         |  OK                    |
       |                         |<-----------------------|
       |  OK                    |                         |
       |<-----------------------|                         |
       |                         |                         |
```