### Prepared Statements

- A prepared statement is a subinterface of the Statement interface in Java that represents a precompiled SQL statement.
- A prepared statement can be used to execute the same SQL statement multiple times with different parameters, which improves the performance and security of the application .
- A prepared statement can also handle complex data types such as BLOB, CLOB, and Array, which are useful for storing and retrieving files and lists.
- To use a prepared statement, the following steps are required  :
  - Create a connection to the database using the DriverManager class.
  - Prepare the SQL statement with placeholders (?) for the parameters.
  - Create a PreparedStatement object by passing the SQL statement to the connection's prepareStatement method.
  - Set the values for the parameters using the appropriate setter methods of the PreparedStatement object, such as setInt, setString, setBlob, etc.
  - Execute the prepared statement using the executeQuery or executeUpdate method, depending on the type of the SQL statement.
  - Retrieve the results using the ResultSet object if the SQL statement is a query.
  - Close the resources such as the PreparedStatement, ResultSet, and Connection objects.