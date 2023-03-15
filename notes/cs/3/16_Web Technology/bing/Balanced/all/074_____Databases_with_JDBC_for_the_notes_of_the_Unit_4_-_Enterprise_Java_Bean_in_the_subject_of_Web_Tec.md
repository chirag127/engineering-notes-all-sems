# Databases with JDBC

JDBC stands for Java Database Connectivity. It is an API that allows Java applications to interact with various types of databases using a standard interface. JDBC supports both relational and non-relational databases, such as MySQL, Oracle, SQL Server, MongoDB, etc.

Some of the benefits of using JDBC are:

- It provides a uniform and platform-independent way of accessing data from different sources.
- It simplifies the development and maintenance of database applications by hiding the low-level details of database communication.
- It enables the use of SQL, a powerful and widely used query language, to manipulate data in databases.
- It supports various features such as transactions, metadata, batch updates, stored procedures, etc.

The basic steps for connecting to a database with JDBC are as follows:

- Install or locate the database you want to access.
- Include the JDBC library in your Java project.
- Ensure the JDBC driver you need is on your classpath. A JDBC driver is a software component that implements the JDBC interface for a specific database.
- Use the JDBC library to obtain a connection to the database. A connection represents a session with the database and allows you to execute SQL statements.
- Create and execute SQL statements using the connection object. A statement is an object that represents a SQL command, such as a query, an update, or a call to a stored procedure. You can use different types of statements, such as Statement, PreparedStatement, or CallableStatement, depending on your needs.
- Process the results of the SQL statements. A result set is an object that contains the data returned by a query. You can iterate over the rows and columns of a result set using various methods and properties.
- Close the connection and release the resources. It is important to close the connection and any other objects that you have created, such as statements and result sets, when you are done with them. This will free up the resources and avoid memory leaks or connection errors.

Here is an example of a Java program that connects to a MySQL database and executes a simple query:

```java
// Import the JDBC library
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {

    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Connect to the database
      String url = "jdbc:mysql://localhost:3306/testdb";
      String user = "root";
      String password = "password";
      conn = DriverManager.getConnection(url, user, password);

      // Create and execute a SQL statement
      stmt = conn.createStatement();
      String sql = "SELECT * FROM employees";
      rs = stmt.executeQuery(sql);

      // Process the result set
      while (rs.next()) {
        // Retrieve the data from each row
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String department = rs.getString("department");
        double salary = rs.getDouble("salary");

        // Display the data
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
        System.out.println("Salary: " + salary);
        System.out.println();
      }
    } catch (Exception e) {
      // Handle any errors
      e.printStackTrace();
    } finally {
      // Close the connection and release the resources
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