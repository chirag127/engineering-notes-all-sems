A stored procedure is a segment of SQL statements that is stored in the database and can be invoked by applications. Stored procedures can improve the performance and security of database applications. JDBC provides a standard way to call stored procedures using the CallableStatement interface. A CallableStatement object can execute a stored procedure with input and output parameters. The following is a possible diagram for stored procedures in JDBC:

#### Stored Procedures in JDBC

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Application    |        |  JDBC Driver    |        |  Database       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Create         |        |                 |        |                 |
|  CallableStatement|----->|  Send SQL       |------->|  Execute        |
|                 |        |  escape syntax  |        |  stored procedure|
|                 |        |                 |        |                 |
|  Set input      |        |                 |        |                 |
|  parameters     |------->|  Send input     |------->|  Use input      |
|                 |        |  parameters     |        |  parameters     |
|                 |        |                 |        |                 |
|  Register output|        |                 |        |                 |
|  parameters     |------->|  Receive output |<-------|  Return output  |
|                 |        |  parameters     |        |  parameters     |
|                 |        |                 |        |                 |
|  Get output     |<-------|  Return output  |        |                 |
|  parameters     |        |  parameters     |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```