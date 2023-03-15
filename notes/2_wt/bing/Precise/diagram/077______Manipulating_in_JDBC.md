#### Manipulating in JDBC
Here is an ASCII diagram that shows the process of manipulating data in a database using JDBC:

```
+----------------+       +------------+       +------------+
| Java Program   |       | JDBC Driver|       |  Database  |
|                |       |            |       |            |
| +------------+ |       |            |       |            |
| | Connection | |       |            |       |            |
| +------+-----+ |       |            |       |            |
|        |       |       |            |       |            |
| +------+-----+ |       |            |       |            |
| | Statement  | |       |            |       |            |
| +------+-----+ |       |            |       |            |
|        |       |       |            |       |            |
| +------+-----+ |       |            |       |            |
| | ResultSet  | |       |            |       |            |
| +------+-----+ |       |            |       |            |
|        |       |       |            |       |            |
+--------+-------+       +------+-----+       +------+-----+
         |                      |                    |
         +----------------------+--------------------+
```

In this diagram, a Java program uses a JDBC driver to connect to a database. The program creates a `Connection` object, which is used to create a `Statement` object. The `Statement` object is used to execute SQL commands on the database, and the results are returned in a `ResultSet` object. The program can then manipulate the data in the `ResultSet` as needed.
