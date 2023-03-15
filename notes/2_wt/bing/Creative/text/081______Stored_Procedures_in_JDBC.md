#### Stored Procedures in JDBC

- A stored procedure is a precompiled SQL statement that can be executed by the database server.
- A stored procedure can have input parameters, output parameters, or both.
- A stored procedure can perform complex operations, such as looping, conditional logic, or error handling, that are not possible with a single SQL statement.
- A stored procedure can improve the performance and security of the database application, by reducing the network traffic and enforcing the access control.
- To execute a stored procedure from a JDBC program, the following steps are required:

  1. Create a CallableStatement object using the Connection.prepareCall() method, passing the SQL call statement as a parameter. The SQL call statement has the following syntax: `{call procedure_name [(?, ?, ...)]}`
  2. Set the values of the input parameters using the appropriate setXXX() methods of the CallableStatement object, where XXX is the data type of the parameter. The parameters are referenced by their ordinal position, starting from 1.
  3. Register the output parameters using the CallableStatement.registerOutParameter() method, specifying the parameter index, the SQL type, and optionally the scale or type name.
  4. Execute the stored procedure using the CallableStatement.execute() method.
  5. Retrieve the values of the output parameters using the appropriate getXXX() methods of the CallableStatement object, where XXX is the data type of the parameter. The parameters are referenced by their ordinal position, starting from 1.
  6. Close the CallableStatement object using the CallableStatement.close() method.