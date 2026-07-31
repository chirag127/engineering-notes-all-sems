Manipulating in JDBC means using Java programs to communicate with a database and perform operations on its data, such as creating, inserting, updating, deleting, and querying tables. To manipulate a database with JDBC, the following steps are usually involved:

1. Load the JDBC driver class that corresponds to the database you want to connect to.
2. Establish a connection to the database using the DriverManager class and providing the URL, username, and password of the database.
3. Create a Statement object from the connection object to execute SQL queries.
4. Execute the SQL queries using the execute, executeQuery, or executeUpdate methods of the statement object and obtain the results as a ResultSet object or an int value.
5. Process the results by iterating over the result set object or checking the int value for the number of rows affected.
6. Close the resources such as the statement, result set, and connection objects to release the database resources.

A possible ASCII diagram for manipulating in JDBC is:

#### Manipulating in JDBC
```
+----------------+       +----------------+       +----------------+
| Java Program   |       | JDBC Driver    |       | Database       |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
| 1. Load driver | ----> |                |       |                |
|                |       |                |       |                |
| 2. Get         | ----> | 2. Create      | ----> | 2. Establish   |
|    connection  |       |    connection  |       |    connection  |
|                |       |                |       |                |
| 3. Create      | <---- | 3. Return      |       |                |
|    statement   |       |    statement   |       |                |
|                |       |                |       |                |
| 4. Execute     | ----> | 4. Execute     | ----> | 4. Execute     |
|    query       |       |    query       |       |    query       |
|                |       |                |       |                |
| 5. Process     | <---- | 5. Return      | <---- | 5. Return      |
|    results     |       |    results     |       |    results     |
|                |       |                |       |                |
| 6. Close       | ----> | 6. Close       | ----> | 6. Close       |
|    resources   |       |    resources   |       |    resources   |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```