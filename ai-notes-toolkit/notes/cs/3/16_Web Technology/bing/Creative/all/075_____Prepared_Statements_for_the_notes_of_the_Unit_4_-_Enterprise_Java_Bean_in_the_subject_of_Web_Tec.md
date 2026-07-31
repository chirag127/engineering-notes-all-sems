# Prepared Statements

- A prepared statement is a subinterface of the Statement interface in Java that represents a precompiled SQL statement.
- A prepared statement can be used to execute the same SQL statement multiple times with different parameters, which improves the performance and security of the application .
- A prepared statement can also handle complex data types such as BLOB, CLOB, and Array, which are useful for storing and retrieving files and lists.
- To use a prepared statement, the following steps are required :
  - Create a connection to the database using the DriverManager class.
  - Prepare the SQL statement with placeholders (?) for the parameters.
  - Create a PreparedStatement object by passing the SQL statement to the connection's prepareStatement method.
  - Set the values for the parameters using the appropriate setter methods of the PreparedStatement object, such as setInt, setString, setBlob, etc.
  - Execute the prepared statement using the executeQuery or executeUpdate method of the PreparedStatement object.
  - Close the prepared statement and the connection after use.

- An example of using a prepared statement to insert a record into a table is given below:

```java
// create a connection to the database
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");

// prepare the SQL statement with placeholders
String sql = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";

// create a PreparedStatement object
PreparedStatement ps = con.prepareStatement(sql);

// set the values for the parameters
ps.setString(1, "Alice"); // name
ps.setInt(2, 12); // age
ps.setDouble(3, 9.5); // grade

// execute the prepared statement
int rows = ps.executeUpdate();

// display the number of rows affected
System.out.println("Rows inserted: " + rows);

// close the prepared statement and the connection
ps.close();
con.close();
```