### Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To write a java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

  - Import the required packages for JDBC (Java Database Connectivity), such as `java.sql.*` and `javax.servlet.*` .
  - Load and register the JDBC driver for the database you want to connect to, such as MySQL, Oracle, etc. You can use the `Class.forName()` method to load the driver class and the `DriverManager.registerDriver()` method to register it  .
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the URL, username and password of the database as parameters. You can store the connection object in a `Connection` variable  .
  - Create a statement object using the `Connection.createStatement()` method, which allows you to execute SQL queries on the database. You can store the statement object in a `Statement` variable  .
  - Execute the SQL query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data retrieved from the database. You can store the result set object in a `ResultSet` variable  .
  - Iterate over the result set using the `ResultSet.next()` method, which moves the cursor to the next row of data. You can access the data in each column using the `ResultSet.getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, etc. You can display the data using the `System.out.println()` method or the `out.println()` method if you are using a servlet or JSP  .
  - Close the result set, statement and connection objects using the `ResultSet.close()`, `Statement.close()` and `Connection.close()` methods, respectively. This releases the resources and avoids memory leaks  .

- Here is an example of a java program that connects to a MySQL database and displays the data from a table called `employees`:

  ```java
  // Import the required packages
  import java.sql.*;

  public class DatabaseConnection {

    public static void main(String[] args) {

      // Declare the connection, statement and result set variables
      Connection conn = null;
      Statement stmt = null;
      ResultSet rs = null;

      try {
        // Load and register the MySQL driver
        Class.forName("com.mysql.cj.jdbc.Driver");
        DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());

        // Establish a connection to the database
        String url = "jdbc:mysql://localhost:3306/mydb";
        String user = "root";
        String password = "root";
        conn = DriverManager.getConnection(url, user, password);

        // Create a statement object
        stmt = conn.createStatement();

        // Execute a SQL query
        String sql = "SELECT * FROM employees";
        rs = stmt.executeQuery(sql);

        // Iterate over the result set and display the data
        while (rs.next()) {
          // Get the data from each column
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
        // Handle any exceptions
        e.printStackTrace();
      } finally {
        // Close the result set, statement and connection objects
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
        } catch (SQLException e) {
          e.printStackTrace();
        }
      }
    }
  }
  ```
[assistant