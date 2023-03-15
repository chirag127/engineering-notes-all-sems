#### Prepared Statements in JDBC

A prepared statement is a precompiled SQL statement that can be executed multiple times with different parameters. It improves the performance and security of SQL queries.

To use a prepared statement in JDBC, follow these steps:

- Create a Connection object to connect to the database.
- Create a PreparedStatement object by calling the prepareStatement() method of the Connection object, passing the SQL query as a parameter. Use question marks (?) as placeholders for the parameters.
- Set the values of the parameters by calling the appropriate setXXX() methods of the PreparedStatement object, passing the index of the parameter (starting from 1) and the value as arguments.
- Execute the prepared statement by calling the executeQuery() or executeUpdate() method of the PreparedStatement object, depending on the type of the SQL query.
- Process the result set or the update count returned by the execute method.
- Close the PreparedStatement and Connection objects by calling their close() methods.

Here is an example of using a prepared statement to insert a record into a table named students:

```java
// import the required packages
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

// create a class
public class PreparedStatementExample {

  // define the database URL, username and password
  private static final String DB_URL = "jdbc:mysql://localhost:3306/school";
  private static final String DB_USER = "root";
  private static final String DB_PASS = "password";

  // define the SQL query
  private static final String SQL_INSERT = "INSERT INTO students (id, name, age) VALUES (?, ?, ?)";

  // create a main method
  public static void main(String[] args) {

    // declare the Connection and PreparedStatement objects
    Connection conn = null;
    PreparedStatement pstmt = null;

    try {
      // create a connection to the database
      conn = DriverManager.getConnection(DB_URL, DB_USER, DB_PASS);

      // create a prepared statement
      pstmt = conn.prepareStatement(SQL_INSERT);

      // set the values of the parameters
      pstmt.setInt(1, 101); // set the id to 101
      pstmt.setString(2, "Alice"); // set the name to Alice
      pstmt.setInt(3, 20); // set the age to 20

      // execute the prepared statement
      int rows = pstmt.executeUpdate();

      // print the number of rows affected
      System.out.println("Rows inserted: " + rows);

    } catch (SQLException e) {
      // handle the exception
      e.printStackTrace();
    } finally {
      // close the resources
      try {
        if (pstmt != null) {
          pstmt.close();
        }
        if (conn != null) {
          conn.close();
        }
      } catch (SQLException e) {
        // handle the exception
        e.printStackTrace();
      }
    }
  }
}
```