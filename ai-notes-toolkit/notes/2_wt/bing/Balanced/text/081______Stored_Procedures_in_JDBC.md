#### Stored Procedures in JDBC

- A stored procedure is a precompiled SQL statement that can be executed by a database server.
- A stored procedure can have input and output parameters, and can return a result set or a single value.
- A stored procedure can improve the performance and security of a database application, as it reduces the network traffic and the risk of SQL injection attacks.
- To call a stored procedure from a JDBC program, the following steps are required:

  1. Create a `CallableStatement` object using the `prepareCall()` method of the `Connection` object, and pass the SQL call statement as a parameter. The SQL call statement has the following syntax: `{call procedure_name[(?, ?, ...)]}`
  2. Set the values of the input parameters using the appropriate `setXXX()` methods of the `CallableStatement` object, and register the output parameters using the `registerOutParameter()` method. The parameters are identified by their position (starting from 1) or by their name (if supported by the database).
  3. Execute the `CallableStatement` object using the `execute()` or `executeUpdate()` method, depending on whether the stored procedure returns a result set or not.
  4. Retrieve the values of the output parameters using the appropriate `getXXX()` methods of the `CallableStatement` object, and process the result set (if any) using the `ResultSet` object returned by the `getResultSet()` method.
  5. Close the `CallableStatement` and the `ResultSet` objects using the `close()` method.