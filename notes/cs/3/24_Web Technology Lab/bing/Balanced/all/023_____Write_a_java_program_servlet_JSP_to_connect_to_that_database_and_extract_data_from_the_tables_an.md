# Write a java program/servlet/JSP to connect to that database and extract data from the tables and display them for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- To write a java program/servlet/JSP to connect to a database and extract data from the tables and display them, you need to follow these steps:

  - Import the required packages for JDBC (Java Database Connectivity), such as `java.sql.*` and `javax.sql.*` .
  - Load and register the JDBC driver for the database you want to connect to, such as MySQL, Oracle, PostgreSQL, etc. You can use the `Class.forName()` method to load the driver class and the `DriverManager.registerDriver()` method to register it  .
  - Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the URL, username and password of the database as parameters. You can store the connection object in a `Connection` variable  .
  - Create a statement object using the `Connection.createStatement()` method, which allows you to execute SQL queries on the database. You can store the statement object in a `Statement` variable  .
  - Execute the SQL query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data retrieved from the database. You can store the result set object in a `ResultSet` variable  .
  - Iterate over the result set using the `ResultSet.next()` method, which moves the cursor to the next row of data. You can access the data in each column using the `ResultSet.getXXX()` methods, where XXX is the data type of the column, such as `getString()`, `getInt()`, `getDouble()`, etc. You can display the data using the `System.out.println()` method or any other output method   .
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
      String url = "jdbc:mysql://localhost:3306/mydb"; // Change the URL, database name, username and password as per your configuration
      String username = "root";
      String password = "root";
      conn = DriverManager.getConnection(url, username, password);

      // Create a statement object
      stmt = conn.createStatement();

      // Execute a SQL query
      String sql = "SELECT * FROM employees"; // Change the query as per your table name and columns
      rs = stmt.executeQuery(sql);

      // Iterate over the result set and display the data
      while (rs.next()) {
        // Retrieve the data from each column using the column name or index
        int id = rs.getInt("id"); // or rs.getInt(1);
        String name = rs.getString("name"); // or rs.getString(2);
        String department = rs.getString("department"); // or rs.getString(3);
        double salary = rs.getDouble("salary"); // or rs.getDouble(4);

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
        if (rs != null)

```
