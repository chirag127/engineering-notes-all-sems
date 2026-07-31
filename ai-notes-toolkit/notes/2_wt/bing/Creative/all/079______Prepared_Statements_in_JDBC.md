#### Prepared Statements in JDBC

- Prepared Statements are a special type of statements that are derived from the Statement interface.
- They are used to execute parameterized queries against the database  .
- A parameterized query is a query that contains placeholders (represented by ? symbol) for the values that will be supplied at runtime  .
- Prepared Statements are precompiled by the database and can be executed multiple times with different values for the parameters  .
- Prepared Statements provide several advantages over regular statements, such as:
  - Improved performance: Since the query is precompiled, the database does not need to parse and optimize it every time it is executed  .
  - Enhanced security: Since the values for the parameters are supplied separately, the query is less vulnerable to SQL injection attacks  .
  - Increased readability: Since the query does not contain the actual values, it is easier to read and maintain  .
- To use Prepared Statements, the following steps are required:
  - Create a PreparedStatement object by calling the prepareStatement() method of the Connection object and passing the parameterized query as an argument   .
  - Set the values for the parameters by calling the appropriate setter methods of the PreparedStatement object, such as setInt(), setString(), setDouble(), etc. The first argument for each setter method specifies the index of the placeholder (starting from 1), and the second argument specifies the value   .
  - Execute the query by calling the executeQuery() or executeUpdate() method of the PreparedStatement object, depending on the type of the query   .
  - Process the result set (if any) by using the ResultSet object returned by the executeQuery() method   .
  - Close the PreparedStatement and ResultSet objects by calling their close() methods   .
- An example of using Prepared Statements in JDBC is given below:

```java
// Assume conn is an active connection
String sql = "SELECT * FROM EMPLOYEE WHERE SALARY > ?"; // Parameterized query
PreparedStatement pstmt = conn.prepareStatement(sql); // Create PreparedStatement object
pstmt.setDouble(1, 50000.00); // Set the value for the first parameter
ResultSet rs = pstmt.executeQuery(); // Execute the query and get the result set
while (rs.next()) { // Loop through the result set
  System.out.println(rs.getString("NAME") + " " + rs.getDouble("SALARY")); // Print the name and salary of each employee
}
rs.close(); // Close the result set
pstmt.close(); // Close the prepared statement
```