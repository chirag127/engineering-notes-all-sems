#### Prepared Statements in JDBC

- Prepared statements are a special type of statements that are derived from the Statement interface.
- Prepared statements are used to execute parameterized queries against the database .
- Parameterized queries are SQL queries that contain placeholders (represented by ? symbol) for the values that will be supplied at runtime   .
- Prepared statements are precompiled by the database and can be executed multiple times with different values  .
- Prepared statements have several advantages over regular statements, such as:
  - Improved performance: The database only needs to compile the query once and can reuse the same execution plan for subsequent executions .
  - Enhanced security: The values are passed as parameters and not as part of the SQL query, which prevents SQL injection attacks .
  - Increased readability: The SQL query is more concise and clear, as it does not contain the actual values .
- To use prepared statements, the following steps are required:
  - Create a PreparedStatement object by calling the prepareStatement() method of the Connection object and passing the SQL query with placeholders as an argument   .
  - Set the values for the placeholders by calling the appropriate setter methods of the PreparedStatement object, such as setInt(), setString(), setDouble(), etc. The first argument of these methods specifies the index of the placeholder (starting from 1), and the second argument specifies the value   .
  - Execute the query by calling the executeQuery() or executeUpdate() method of the PreparedStatement object, depending on the type of the query (select or update/insert/delete)   .
  - Process the result set (if any) by using the ResultSet object returned by the executeQuery() method   .
  - Close the PreparedStatement and ResultSet objects by calling their close() methods   .
- An example of using prepared statements in JDBC is given below:

```java
// Assume conn is an already created Connection object
// Create a SQL query with two placeholders
String sql = "SELECT * FROM employees WHERE name = ? AND salary > ?";
// Create a PreparedStatement object
PreparedStatement pstmt = conn.prepareStatement(sql);
// Set the values for the placeholders
pstmt.setString(1, "John"); // name
pstmt.setDouble(2, 5000.0); // salary
// Execute the query
ResultSet rs = pstmt.executeQuery();
// Process the result set
while (rs.next()) {
  // Retrieve the data from each row
  int id = rs.getInt("id");
  String name = rs.getString("name");
  double salary = rs.getDouble("salary");
  // Print the data
  System.out.println(id + " " + name + " " + salary);
}
// Close the resources
rs.close();
pstmt.close();
```