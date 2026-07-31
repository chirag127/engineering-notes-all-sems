# Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them

- To write a java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

  - Import the required packages for JDBC (Java Database Connectivity), such as `java.sql.*` and `javax.sql.*`.
  - Load and register the JDBC driver for the database you want to connect to, such as `com.mysql.cj.jdbc.Driver` for MySQL.
  - Establish a connection to the database using the `DriverManager.getConnection()` method, passing the URL, username and password of the database as parameters.
  - Create a `Statement` or `PreparedStatement` object to execute SQL queries on the database.
  - Execute the query using the `executeQuery()` method, which returns a `ResultSet` object that contains the data from the tables.
  - Iterate over the `ResultSet` object using the `next()` method, and access the data using the `getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, `getDouble()`, etc.
  - Display the data using `System.out.println()` or any other output method, such as `JOptionPane.showMessageDialog()` for GUI applications.
  - Close the `ResultSet`, `Statement` and `Connection` objects using the `close()` method to release the resources.

- Here is an example of a java program that connects to a MySQL database and displays the data from a table called `employees`:

```java
// Import the required packages
import java.sql.*;

public class DatabaseConnection {

  public static void main(String[] args) {
    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load and register the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish the connection to the database
      String url = "jdbc:mysql://localhost:3306/testdb";
      String user = "root";
      String password = "root";
      conn = DriverManager.getConnection(url, user, password);

      // Create a statement object to execute the query
      stmt = conn.createStatement();

      // Execute the query and get the result set
      String sql = "SELECT * FROM employees";
      rs = stmt.executeQuery(sql);

      // Display the data from the result set
      while (rs.next()) {
        // Retrieve the data by column name
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String email = rs.getString("email");
        double salary = rs.getDouble("salary");

        // Print the data
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Email: " + email);
        System.out.println("Salary: " + salary);
        System.out.println();
      }
    } catch (Exception e) {
      // Handle any errors
      e.printStackTrace();
    } finally {
      // Close the JDBC objects
      try {
        if (rs != null) {
          rs.close();
        }
        if (stmt != null) {
          stmt.close();
        }
        if (conn != null) {
          conn.close();
        }
      } catch (SQLException se) {
        se.printStackTrace();
      }
    }
  }
}
```

- Here is an example of a servlet that connects to a MySQL database and displays the data from a table called `employees` in an HTML table:

```java
// Import the required packages
import java.io.*;
import java.sql.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class DatabaseConnectionServlet extends HttpServlet {

  public void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    // Set the content type and character encoding of the response
    response.setContentType("text/html");
    response.setCharacterEncoding("UTF-8");

    // Get the output stream to write the response
    PrintWriter out = response.getWriter();

    try {
      // Load and register the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish the connection to the database
      String url = "jdbc:mysql://localhost:3306/testdb";
      String user = "root";
      String password = "root";
      conn = DriverManager.getConnection(url, user, password);

      // Create a statement object to execute the query
      stmt =

```
