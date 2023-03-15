### Databases with JDBC

- JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases from Java applications.
- JDBC provides a common interface for sending SQL statements to any database that supports JDBC, such as MySQL, Oracle, SQL Server, etc.
- JDBC consists of two components: a JDBC driver and a JDBC API.
- A JDBC driver is a software component that implements the JDBC API for a specific database. It enables Java applications to communicate with the database using the native protocol of the database.
- A JDBC API is a set of classes and interfaces that define the methods and constants for accessing and manipulating data in a database. It includes classes such as `Connection`, `Statement`, `ResultSet`, etc.
- The steps for connecting to a database with JDBC are as follows:
  - Install or locate the database you want to access.
  - Include the JDBC library in your Java project.
  - Ensure the JDBC driver you need is on your classpath.
  - Use the JDBC library to obtain a connection to the database.
  - Create and execute SQL statements using the connection object.
  - Process the results returned by the statements using the result set object.
  - Close the connection and release the resources when done.
- The basic syntax for creating a connection to a database with JDBC is as follows:
  - Import the `java.sql` package in your Java class.
  - Load the JDBC driver class using the `Class.forName()` method.
  - Define the connection URL, which specifies the database name, host, port, and other parameters.
  - Define the username and password for accessing the database.
  - Call the `DriverManager.getConnection()` method with the connection URL, username, and password as arguments. This returns a `Connection` object that represents the database connection.
  - Use the `Connection` object to create and execute SQL statements using the `createStatement()`, `prepareStatement()`, or `prepareCall()` methods. These return `Statement`, `PreparedStatement`, or `CallableStatement` objects, respectively, that represent the SQL statements.
  - Use the `executeQuery()`, `executeUpdate()`, or `execute()` methods of the statement objects to execute the SQL statements. These return `ResultSet`, `int`, or `boolean` values, respectively, that represent the results of the statements.
  - Use the `ResultSet` object to iterate over the rows and columns of the data returned by the query statements. Use the `getXXX()` methods of the `ResultSet` object to retrieve the values of each column by name or index.
  - Use the `int` or `boolean` values returned by the update or execute statements to check the number of rows affected or the success of the statements.
  - Close the `ResultSet`, `Statement`, and `Connection` objects using the `close()` method when done. This releases the resources and prevents memory leaks.
- The following code snippet shows an example of connecting to a MySQL database and executing a simple query using JDBC:

```java
// Import the java.sql package
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {

    // Define the connection parameters
    String url = "jdbc:mysql://localhost:3306/testdb";
    String user = "root";
    String password = "root";

    // Declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.cj.jdbc.Driver");

      // Establish the connection
      conn = DriverManager.getConnection(url, user, password);

      // Create the statement
      stmt = conn.createStatement();

      // Execute the query
      rs = stmt.executeQuery("SELECT * FROM employees");

      // Process the result set
      while (rs.next()) {
        // Retrieve the values of each column by name or index
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String email = rs.getString(3);
        double salary = rs.getDouble("salary");

        // Print the values
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
        if