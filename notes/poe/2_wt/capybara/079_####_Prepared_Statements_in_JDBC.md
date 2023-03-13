#### Prepared Statements in JDBC

Prepared Statements in JDBC are a way of executing SQL queries that have placeholders for input values. The placeholders are replaced with actual values at runtime, which makes the query execution more efficient and secure.

Here are some key points to remember about Prepared Statements in JDBC:

- Prepared Statements are created using the `prepareStatement()` method of the `Connection` interface.
- The SQL query is passed as a parameter to the `prepareStatement()` method.
- Placeholders are represented by question marks (`?`) in the SQL query. 
- The `setXXX()` methods of the `PreparedStatement` interface are used to set input values for the placeholders. The `XXX` in the method name represents the data type of the input value.
- The input values are set in the order in which the placeholders appear in the SQL query.
- The `executeQuery()` method is used to execute a Prepared Statement that returns a result set, while the `executeUpdate()` method is used to execute a Prepared Statement that modifies the database.
- Prepared Statements can be reused with different input values, which makes them more efficient than regular SQL queries. 

Mnemonic/learning trick:

- One possible mnemonic to remember the order of setting input values for placeholders is to think of it as a countdown. For example, if there are three placeholders in the SQL query, you would set the input values in the following order: `set3()`, `set2()`, `set1()`.

Here are some advantages of using Prepared Statements in JDBC:

- Prepared Statements can improve performance by reducing the number of times a query needs to be parsed and compiled by the database server.
- Prepared Statements are more secure than regular SQL queries because they prevent SQL injection attacks.
- Prepared Statements can be used to execute parameterized queries, which makes the application more flexible and reusable.

However, there are also some disadvantages to using Prepared Statements:

- Prepared Statements can be more complex to write than regular SQL queries, especially for complex queries with multiple input values.
- Prepared Statements may not be as flexible as regular SQL queries, since the query structure is fixed at runtime.

Here is an example of using a Prepared Statement in JDBC to retrieve data from a database:

```
String query = "SELECT * FROM customers WHERE city = ?";
PreparedStatement stmt = conn.prepareStatement(query);
stmt.setString(1, "London");
ResultSet rs = stmt.executeQuery();
while (rs.next()) {
    // process the result set
}
```

In this example, the `query` string contains a placeholder for the city input value. The `prepareStatement()` method creates a Prepared Statement for this query, and the `setString()` method sets the value of the placeholder to "London". Finally, the `executeQuery()` method is called to execute the Prepared Statement and retrieve the result set.

Overall, Prepared Statements are a powerful tool for executing SQL queries in JDBC. By using Prepared Statements, you can improve performance, enhance security, and make your application more flexible and reusable.