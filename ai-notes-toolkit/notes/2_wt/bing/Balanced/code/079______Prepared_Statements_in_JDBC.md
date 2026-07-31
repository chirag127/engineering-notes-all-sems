#### Prepared Statements in JDBC

A prepared statement is a precompiled SQL statement that can be executed multiple times with different parameters. It is useful for improving the performance and security of SQL queries. A prepared statement is created by using the `prepareStatement` method of the `Connection` interface. The SQL query passed to this method can have one or more placeholders (`?`) for the parameters. The parameters can be set by using the setter methods of the `PreparedStatement` interface, such as `setInt`, `setString`, `setDate`, etc. The index of the parameter starts from 1. The prepared statement can be executed by using the `executeQuery` or `executeUpdate` methods of the `PreparedStatement` interface.

Here is an example of creating and executing a prepared statement in JDBC:

```java
// Assume conn is an already created JDBC connection
// Create a SQL query with two parameters
String sql = "SELECT * FROM employees WHERE name = ? AND salary > ?";
// Create a prepared statement
PreparedStatement pstmt = conn.prepareStatement(sql);
// Set the values for the parameters
pstmt.setString(1, "John"); // name
pstmt.setInt(2, 5000); // salary
// Execute the query and get the result set
ResultSet rs = pstmt.executeQuery();
// Process the result set
while (rs.next()) {
  // Get the values from each column
  int id = rs.getInt("id");
  String name = rs.getString("name");
  int salary = rs.getInt("salary");
  // Print the values
  System.out.println(id + " " + name + " " + salary);
}
// Close the resources
rs.close();
pstmt.close();
conn.close();
```