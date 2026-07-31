### Prepared Statements

- A prepared statement is a subinterface of the Statement interface in Java that represents a precompiled SQL statement.
- A prepared statement can be used to execute the same SQL statement multiple times with different parameters, which improves the performance and security of the application .
- A prepared statement can also handle complex data types such as BLOB, CLOB, and Array, which are useful for storing and retrieving files and lists.
- To use a prepared statement, the following steps are required :
  - Create a connection to the database using the DriverManager class.
  - Prepare the SQL statement with placeholders (?) for the parameters.
  - Create a PreparedStatement object by passing the SQL statement to the connection's prepareStatement method.
  - Set the values for the parameters using the appropriate setter methods of the PreparedStatement object, such as setInt, setString, setBlob, etc.
  - Execute the prepared statement using the executeQuery or executeUpdate method, depending on the type of the SQL statement.
  - Process the result set or the update count returned by the execution.
  - Close the prepared statement and the connection objects.
- An example of using a prepared statement to insert a record into a table is given below:

```java
//Create a connection to the database
Connection myCon = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "user", "password");

//Prepare the SQL statement with a placeholder for the name parameter
String sql = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";

//Create a PreparedStatement object
PreparedStatement myStmt = myCon.prepareStatement(sql);

//Set the values for the parameters
myStmt.setString(1, "Alice"); //set the name to Alice
myStmt.setInt(2, 12); //set the age to 12
myStmt.setInt(3, 7); //set the grade to 7

//Execute the prepared statement
int rowsAffected = myStmt.executeUpdate();

//Print the number of rows affected
System.out.println("Rows affected: " + rowsAffected);

//Close the prepared statement and the connection
myStmt.close();
myCon.close();
```