#### Prepared Statements in JDBC

- Prepared Statements are a special type of statements that are derived from the Statement interface.
- They are used to execute parameterized queries against the database .
- A parameterized query is a SQL query that contains one or more placeholders (represented by ? symbol) for the values that will be supplied at runtime .
- Prepared Statements have the following advantages over regular statements:
  - They improve performance by precompiling the SQL query once and executing it multiple times with different values .
  - They prevent SQL injection attacks by escaping the values automatically .
  - They make the code more readable and maintainable by separating the SQL syntax from the values .
- To use Prepared Statements, we need to follow these steps:
  - Create a PreparedStatement object by calling the prepareStatement() method of the Connection object and passing the SQL query with placeholders as an argument  .
  - Set the values for the placeholders by calling the appropriate setter methods (such as setInt(), setString(), etc.) of the PreparedStatement object and passing the index of the placeholder and the value as arguments  .
  - Execute the PreparedStatement object by calling the executeQuery() or executeUpdate() method depending on the type of the query  .
  - Close the PreparedStatement object by calling the close() method  .
- An example of using Prepared Statements in JDBC is given below:

```java
// Assume conn is an active connection
String sql = "UPDATE EMPLOYEES SET SALARY = ? WHERE ID = ?"; // SQL query with placeholders
PreparedStatement pstmt = conn.prepareStatement(sql); // Creating a PreparedStatement object
pstmt.setDouble(1, 5000.0); // Setting the value for the first placeholder
pstmt.setInt(2, 101); // Setting the value for the second placeholder
int rows = pstmt.executeUpdate(); // Executing the PreparedStatement object
System.out.println("Rows affected: " + rows); // Printing the result
pstmt.close(); // Closing the PreparedStatement object
```