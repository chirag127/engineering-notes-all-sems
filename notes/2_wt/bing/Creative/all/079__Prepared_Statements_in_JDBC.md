#### Prepared Statements in JDBC

- A prepared statement is a special type of statement that is derived from the Statement interface and is used to execute parameterized SQL queries against the database .
- A parameter is represented by a ? symbol in the SQL query and can be assigned a value at runtime .
- A prepared statement is given a SQL query when it is created and is sent to the database for compilation. This means that the prepared statement contains a precompiled SQL query that can be executed faster and more efficiently than a regular statement.
- A prepared statement can be executed multiple times with different values for the parameters . This makes it convenient to reuse the same SQL query for different scenarios.
- A prepared statement also helps prevent SQL injection attacks, which are a technique to maliciously exploit applications that use client-supplied data in SQL statements. Prepared statements always treat client-supplied data as content of a parameter and never as a part of an SQL query.
- To create a prepared statement, you need to use the `prepareStatement` method of the Connection interface and pass the SQL query as a string argument . For example:

```java
// Create a SQL query with two parameters
String sql = "INSERT INTO EMPLOYEE (NAME, SALARY) VALUES (?, ?)";

// Create a prepared statement object from the connection
PreparedStatement pstmt = conn.prepareStatement(sql);

// Set the values for the parameters
pstmt.setString(1, "John"); // Set the first parameter to "John"
pstmt.setDouble(2, 5000.0); // Set the second parameter to 5000.0

// Execute the prepared statement
pstmt.executeUpdate();
```

- To supply values for the parameters, you need to use the `setXXX` methods of the PreparedStatement interface, where XXX is the data type of the parameter . For example, `setString` for string values, `setInt` for integer values, `setDate` for date values, etc .
- The `setXXX` methods take two arguments: the index of the parameter (starting from 1) and the value of the parameter . For example, `pstmt.setString(1, "John")` sets the first parameter to "John".
- To execute the prepared statement, you need to use the `executeUpdate` or `executeQuery` methods of the PreparedStatement interface, depending on the type of the SQL query . For example, `executeUpdate` for insert, update, or delete queries, and `executeQuery` for select queries .
- You can reuse the same prepared statement object with different values for the parameters by calling the `setXXX` methods again and then executing the prepared statement . For example:

```java
// Reuse the same prepared statement object with different values
pstmt.setString(1, "Mary"); // Set the first parameter to "Mary"
pstmt.setDouble(2, 6000.0); // Set the second parameter to 6000.0

// Execute the prepared statement again
pstmt.executeUpdate();
```

- Some of the advantages of using prepared statements are :

  - They improve the performance and efficiency of the database operations by reducing the compilation and parsing time of the SQL queries.
  - They enhance the readability and maintainability of the code by separating the SQL queries from the Java code.
  - They increase the security and reliability of the application by preventing SQL injection attacks and handling the data types of the parameters automatically.

- Some of the disadvantages of using prepared statements are:

  - They require more memory and resources than regular statements, as they need to store the precompiled SQL queries and the parameter values.
  - They are not suitable for dynamic SQL queries that change frequently or have a variable number of parameters, as they need to be created and compiled for each query.