

### Prepared Statements in JDBC

- Prepared statements are pre-compiled SQL statements that are used to execute parameterized queries.
- They are used to increase performance by reusing the same statement multiple times with different parameters.
- Prepared statements are created using the `Connection.prepareStatement()` method and can be executed using the `PreparedStatement.executeQuery()` or `PreparedStatement.executeUpdate()` methods.
- Prepared statements are more secure than ordinary statements, as they prevent SQL injection attacks by using parameterized queries.
- Prepared statements can also be used to execute batch updates, which can be used to execute multiple SQL statements in one operation.
- Prepared statements can also be used to execute stored procedures, which are stored in the database and can be used to perform complex operations.
- Prepared statements can also be used to retrieve result sets, which can be used to retrieve data from the database.
- Prepared statements can also be used to execute stored functions, which are stored in the database and can be used to perform calculations or other operations.
- Prepared statements can also be used to execute dynamic queries, which can be used to execute queries with unknown parameters at runtime.
- Prepared statements can also be used to create temporary tables, which can be used to store data temporarily in the database.