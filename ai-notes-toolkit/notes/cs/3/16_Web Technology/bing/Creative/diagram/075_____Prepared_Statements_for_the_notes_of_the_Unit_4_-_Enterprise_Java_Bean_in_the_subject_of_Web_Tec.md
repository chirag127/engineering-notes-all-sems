### Prepared Statements

- A prepared statement is a subinterface of Statement that represents a precompiled SQL statement.
- A prepared statement can be used to efficiently execute the same SQL statement multiple times with different parameters.
- A prepared statement has the following advantages over a generic statement object :
  - It improves performance by reducing the parsing and compiling overhead of the SQL statement.
  - It prevents SQL injection attacks by escaping special characters in the parameters.
  - It provides an easy way to store and retrieve files by using BLOB and CLOB data types.
  - It helps to store lists by converting java.sql.Array to a SQL Array.
  - It implements methods like getMetaData() that contain information about the returned result.
- A prepared statement can be created by using the prepareStatement() method of the Connection interface.
- A prepared statement can have one or more question mark placeholders (?) that represent the parameters of the SQL statement.
- A prepared statement can set the values of the parameters by using the setter methods of the PreparedStatement interface, such as setInt(), setString(), setDate(), etc .
- A prepared statement can execute the SQL statement by using the executeQuery() or executeUpdate() methods of the PreparedStatement interface, depending on the type of the statement.
- A prepared statement can be closed by using the close() method of the PreparedStatement interface.