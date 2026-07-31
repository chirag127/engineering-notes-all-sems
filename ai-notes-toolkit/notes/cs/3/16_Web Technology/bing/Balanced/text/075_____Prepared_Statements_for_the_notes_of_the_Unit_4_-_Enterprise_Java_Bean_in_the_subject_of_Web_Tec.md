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
  - Process the result set or the update count returned by the execute method.
  - Close the prepared statement and the connection objects.
- An example of using a prepared statement to insert a record into a table is given below:

```java
// Step 1: Create a connection to the database
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

// Step 2: Prepare the SQL statement with a placeholder for the parameter
String sql = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";

// Step 3: Create a PreparedStatement object by passing the SQL statement to the connection
PreparedStatement ps = con.prepareStatement(sql);

// Step 4: Set the values for the parameters using the setter methods
ps.setString(1, "Alice"); // set the first parameter to "Alice"
ps.setInt(2, 12); // set the second parameter to 12
ps.setDouble(3, 9.5); // set the third parameter to 9.5

// Step 5: Execute the prepared statement using the executeUpdate method
int rows = ps.executeUpdate();

// Step 6: Process the update count returned by the executeUpdate method
System.out.println("Rows affected: " + rows);

// Step 7: Close the prepared statement and the connection objects
ps.close();
con.close();
```