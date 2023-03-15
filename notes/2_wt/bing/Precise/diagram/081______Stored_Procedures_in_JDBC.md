#### Stored Procedures in JDBC

Here is an ASCII diagram that illustrates the process of calling a stored procedure in JDBC:

```
+----------------+       +----------------+
| Java Program   |       | Database       |
|                |       |                |
| +------------+ |       | +------------+ |
| | Connection | |       | | Stored     | |
| +------+-----+ |       | | Procedure  | |
|        |       |       | +------+-----+ |
|        |       |       |        |       |
|        v       |       |        v       |
| +------+-----+ |       | +------+-----+ |
| | Callable   | |       | | Result Set | |
| | Statement  | |       | +------------+ |
| +------+-----+ |       |                |
|        |       |       |                |
|        v       |       |                |
| +------+-----+ |       |                |
| | Result Set | |       |                |
| +------------+ |       |                |
+----------------+       +----------------+
```

A Java program uses a `Connection` object to establish a connection to the database. Once the connection is established, the program creates a `CallableStatement` object to call the stored procedure. The `CallableStatement` object is used to execute the stored procedure and retrieve the result set. The result set is then processed by the Java program.
