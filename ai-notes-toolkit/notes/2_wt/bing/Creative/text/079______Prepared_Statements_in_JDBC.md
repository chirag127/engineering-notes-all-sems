#### Prepared Statements in JDBC

- A prepared statement is a precompiled SQL statement that can be executed multiple times with different parameters.
- A prepared statement improves the performance and security of the database operations, as it reduces the parsing, compiling, and planning overhead, and prevents SQL injection attacks.
- A prepared statement is created by using the `prepareStatement()` method of the `Connection` interface, which takes a SQL query as a parameter and returns a `PreparedStatement` object.
- A prepared statement can have one or more parameters, which are represented by question marks (?) in the SQL query. The parameters can be set by using the `setXXX()` methods of the `PreparedStatement` interface, where XXX is the data type of the parameter.
- A prepared statement can be executed by using the `executeQuery()` or `executeUpdate()` methods of the `PreparedStatement` interface, which return a `ResultSet` or an `int` value respectively.
- A prepared statement can be reused by changing the parameters and executing it again.
- A prepared statement can be closed by using the `close()` method of the `PreparedStatement` interface, which releases the database resources associated with it.