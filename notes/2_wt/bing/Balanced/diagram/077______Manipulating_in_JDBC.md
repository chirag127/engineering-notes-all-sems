Manipulating in JDBC means using Java programs to communicate with a database and perform operations on its data, such as creating, inserting, updating, deleting, and querying tables. To manipulate a database with JDBC, the following steps are usually involved:

1. Load the JDBC driver class that corresponds to the database you want to connect to.
2. Establish a connection to the database using the DriverManager class and providing the URL, username, and password of the database.
3. Create a Statement object from the connection object to execute SQL queries.
4. Execute the SQL queries using the execute, executeQuery, or executeUpdate methods of the statement object and obtain the results as a ResultSet object or an int value.
5. Process the results of the queries by iterating over the result set object or checking the int value.
6. Close the resources such as the statement, result set, and connection objects to release the database resources.

A possible ASCII diagram for manipulating in JDBC is:

#### Manipulating in JDBC
```
+----------------+        +----------------+        +----------------+
| Java program   |        | JDBC driver    |        | Database       |
|                |        |                |        |                |
| +------------+ |        | +------------+ |        | +------------+ |
| | Statement  | |        | | Connection | |        | | Table      | |
| +------------+ |        | +------------+ |        | +------------+ |
| | execute    | |------->| | create     | |------->| | create     | |
| | execute    | |        | | execute    | |        | | insert     | |
| | execute    | |        | | execute    | |        | | update     | |
| | execute    | |        | | execute    | |        | | delete     | |
| | execute    | |        | | execute    | |        | | query      | |
| | execute    | |<-------| | get result | |<-------| | get result | |
| +------------+ |        | +------------+ |        | +------------+ |
| | process    | |        | | close      | |        | | close      | |
| +------------+ |        | +------------+ |        | +------------+ |
+----------------+        +----------------+        +----------------+
```