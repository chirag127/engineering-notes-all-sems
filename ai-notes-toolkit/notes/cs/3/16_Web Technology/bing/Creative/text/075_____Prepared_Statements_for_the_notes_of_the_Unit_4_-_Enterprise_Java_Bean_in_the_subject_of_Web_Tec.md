### Prepared Statements

- A prepared statement is a subinterface of the Statement interface in Java that represents a precompiled SQL statement.
- A prepared statement can be used to execute the same SQL statement multiple times with different parameters, which improves the performance and security of the application .
- A prepared statement can also handle complex data types such as BLOB, CLOB, and Array, which are useful for storing and retrieving files and lists.
- To use a prepared statement, the following steps are required  :
  - Create a connection to the database using the DriverManager class.
  - Prepare the SQL statement with placeholders (?) for the parameters.
  - Create a PreparedStatement object by passing the SQL statement to the connection's prepareStatement method.
  - Set the values for the parameters using the appropriate setter methods of the PreparedStatement object, such as setInt, setString, setBlob, etc.
  - Execute the prepared statement using the executeQuery or executeUpdate method of the PreparedStatement object.
  - Retrieve the results using the ResultSet object if the statement is a query, or the number of affected rows if the statement is an update.
  - Close the resources such as the PreparedStatement, ResultSet, and Connection objects.
- An example of using a prepared statement to insert a record into a table is given below:

```java
// Step 1: Create a connection to the database
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

// Step 2: Prepare the SQL statement with placeholders
String sql = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";

// Step 3: Create a PreparedStatement object
PreparedStatement ps = con.prepareStatement(sql);

// Step 4: Set the values for the parameters
ps.setString(1, "Alice"); // name
ps.setInt(2, 12); // age
ps.setDouble(3, 9.5); // grade

// Step 5: Execute the prepared statement
int rows = ps.executeUpdate();

// Step 6: Retrieve the results
System.out.println("Rows affected: " + rows);

// Step 7: Close the resources
ps.close();
con.close();
```