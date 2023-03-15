#### Joining in JDBC

- Joining in JDBC is a technique to combine data from two or more tables based on a common column or condition.
- Joining in JDBC can be done by using the SQL JOIN clause in the query statement and executing it with a JDBC statement object.
- There are different types of SQL JOINs, such as INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN, and CROSS JOIN, each with different rules and results.
- To perform a join operation in JDBC, the following steps are required:

  1. Import the JDBC packages, such as `java.sql.*` and `javax.sql.*`.
  2. Register and load the JDBC driver, such as `Class.forName("com.mysql.cj.jdbc.Driver")`.
  3. Set a connection to the database, such as `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "password")`.
  4. Create a statement object to execute the query, such as `Statement stmt = con.createStatement()`.
  5. Write the SQL query with the JOIN clause, such as `String query = "SELECT e.name, d.dept_name FROM employee e INNER JOIN department d ON e.dept_id = d.dept_id"`.
  6. Execute the query and obtain the result set, such as `ResultSet rs = stmt.executeQuery(query)`.
  7. Process the result set by iterating over the rows and columns, such as `while (rs.next()) { System.out.println(rs.getString("name") + " works in " + rs.getString("dept_name")); }`.
  8. Close the statement, result set, and connection objects, such as `stmt.close()`, `rs.close()`, and `con.close()`.

- A mnemonic to remember the steps of joining in JDBC is **I RACE WEP** (Import, Register, Connect, Create, Execute, Process, Close).
- An example of joining in JDBC is shown below:

```java
import java.sql.*;

public class JoinExample {

  public static void main(String[] args) {
    try {
      // Import JDBC packages
      // Register and load the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");
      // Set a connection to the database
      Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "password");
      // Create a statement object to execute the query
      Statement stmt = con.createStatement();
      // Write the SQL query with the JOIN clause
      String query = "SELECT e.name, d.dept_name FROM employee e INNER JOIN department d ON e.dept_id = d.dept_id";
      // Execute the query and obtain the result set
      ResultSet rs = stmt.executeQuery(query);
      // Process the result set by iterating over the rows and columns
      while (rs.next()) {
        System.out.println(rs.getString("name") + " works in " + rs.getString("dept_name"));
      }
      // Close the statement, result set, and connection objects
      stmt.close();
      rs.close();
      con.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```