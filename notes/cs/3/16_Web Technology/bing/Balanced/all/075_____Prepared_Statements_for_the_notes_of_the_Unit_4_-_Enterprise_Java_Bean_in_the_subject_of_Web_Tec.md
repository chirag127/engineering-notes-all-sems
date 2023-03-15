# Prepared Statements

- A **prepared statement** is a subinterface of the **Statement** interface in Java that represents a precompiled SQL statement.
- A prepared statement can be used to execute the same SQL statement multiple times with different parameters, which improves the performance and security of the application  .
- A prepared statement can also handle complex data types such as BLOB, CLOB and Array, which are useful for storing and retrieving files and lists.
- To use a prepared statement, the following steps are required  :
  - Create a connection to the database using the `DriverManager.getConnection()` method.
  - Create a prepared statement object using the `Connection.prepareStatement()` method, passing the SQL query with placeholders (`?`) for the parameters.
  - Set the values for the parameters using the appropriate setter methods of the prepared statement object, such as `setInt()`, `setString()`, `setBlob()`, etc. The first argument of these methods specifies the position of the placeholder, starting from 1.
  - Execute the prepared statement using the `executeQuery()` or `executeUpdate()` methods, depending on the type of the SQL query (select or update/insert/delete).
  - Process the result set or the update count returned by the execution methods, if any.
  - Close the prepared statement and the connection objects using the `close()` methods.
- An example of using a prepared statement to insert a record into a table is given below:

```java
// import the required packages
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

// create a class
public class PreparedStatementExample {

  // define the database URL, username and password
  private static final String DB_URL = "jdbc:mysql://localhost:3306/mydb";
  private static final String DB_USER = "root";
  private static final String DB_PASS = "password";

  // define the SQL query with placeholders
  private static final String SQL_INSERT = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)";

  // create a main method
  public static void main(String[] args) {

    // declare the connection and prepared statement objects
    Connection conn = null;
    PreparedStatement pstmt = null;

    try {
      // create a connection to the database
      conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

      // create a prepared statement object
      pstmt = conn.prepareStatement(SQL_INSERT);

      // set the values for the parameters
      pstmt.setString(1, "Alice"); // name
      pstmt.setInt(2, 18); // age
      pstmt.setDouble(3, 9.5); // grade

      // execute the prepared statement
      int rowsAffected = pstmt.executeUpdate();

      // print the number of rows affected
      System.out.println("Rows affected: " + rowsAffected);

    } catch (Exception e) {
      // handle any exception
      e.printStackTrace();
    } finally {
      // close the prepared statement and connection objects
      try {
        if (pstmt != null) {
          pstmt.close();
        }
        if (conn != null) {
          conn.close();
        }
      } catch (Exception e) {
        // handle any exception
        e.printStackTrace();
      }
    }
  }
}
```