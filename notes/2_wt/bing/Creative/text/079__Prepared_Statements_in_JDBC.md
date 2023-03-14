#### Prepared Statements in JDBC

- Prepared statements are a special type of statements that are derived from the Statement interface and are used to execute parameterized SQL queries against the database .
- A parameter is represented by a ? symbol in the SQL query and can be assigned a value at runtime .
- Prepared statements are created by passing a SQL query to the prepareStatement method of the Connection object .
- Prepared statements have the advantage of being precompiled by the database, which improves the performance and security of the queries .
- Prepared statements can prevent SQL injection attacks, which are a common technique to exploit applications that use client-supplied data in SQL statements .
- Prepared statements can be executed multiple times with different values for the parameters, which makes them reusable and efficient .
- Prepared statements have methods to set the values for the parameters, such as setInt, setString, setDouble, etc., depending on the data type of the parameter .
- Prepared statements also have methods to execute the queries, such as executeQuery, executeUpdate, executeBatch, etc., depending on the type of the query .
- Prepared statements are useful for SQL queries that are executed frequently or that involve user input .