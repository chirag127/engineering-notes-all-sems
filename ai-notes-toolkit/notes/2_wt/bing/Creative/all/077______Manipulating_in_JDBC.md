#### Manipulating in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- JDBC provides a set of classes and interfaces that define how a Java program can access and manipulate data stored in a database.
- JDBC supports both SQL and non-SQL databases, but most commonly it is used with relational databases that use SQL as the query language.
- To manipulate data in a database using JDBC, a Java program typically follows these steps:
  1. Load the JDBC driver class that corresponds to the type of database being used. For example, to use MySQL database, the driver class is `com.mysql.cj.jdbc.Driver`.
  2. Establish a connection to the database using the `DriverManager` class, which requires the database URL, username and password. For example, to connect to a MySQL database named `test` on the local host, the URL is `jdbc:mysql://localhost:3306/test`.
  3. Create a `Statement` object from the connection object, which represents a SQL statement that can be executed on the database. There are three types of statements: `Statement`, `PreparedStatement` and `CallableStatement`.
  4. Execute the statement on the database using one of the methods: `execute()`, `executeQuery()` or `executeUpdate()`. The method to use depends on the type of statement and the type of result expected. For example, to execute a query that returns a `ResultSet` object, use `executeQuery()`.
  5. Process the result of the statement execution, which can be a `ResultSet` object, an `int` value or a `boolean` value. For example, to iterate over the rows of a `ResultSet` object, use a `while` loop and the `next()` method.
  6. Close the resources used, such as the statement object, the result set object and the connection object, using the `close()` method. This is important to avoid memory leaks and database locks.

- Here is an example of a Java program that manipulates data in a MySQL database using JDBC:

```java
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {
    // Load the JDBC driver class
    try {
      Class.forName("com.mysql.cj.jdbc.Driver");
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
    }

    // Declare the connection, statement and result set objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    // Establish a connection to the database
    try {
      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "password");
    } catch (SQLException e) {
      e.printStackTrace();
    }

    // Create a statement object
    try {
      stmt = conn.createStatement();
    } catch (SQLException e) {
      e.printStackTrace();
    }

    // Execute a query that returns a result set
    try {
      rs = stmt.executeQuery("SELECT * FROM employees");
    } catch (SQLException e) {
      e.printStackTrace();
    }

    // Process the result set
    try {
      while (rs.next()) {
        // Get the values of each column using the column name or index
        int id = rs.getInt("id");
        String name = rs.getString("name");
        double salary = rs.getDouble(3);

        // Print the values
        System.out.println("ID: " + id + ", Name: " + name + ", Salary: " + salary);
      }
    } catch (SQLException e) {
      e.printStackTrace();
    }

    // Close the resources
    try {
      rs.close();
      stmt.close();
      conn.close();
    } catch (SQLException e) {
      e.printStackTrace();
    }
  }
}
```

- Some advantages of using JDBC are:
  - It is platform-independent, meaning it can run on any operating system that supports Java.
  - It is database-independent, meaning it can work with any database that has a JDBC driver.
  - It is easy to use, as it follows a simple and consistent API.
  - It is flexible, as it supports different types of statements and results.

- Some disadvantages of using JDBC are:
  - It is low-level, meaning it requires writing a lot of code to perform simple tasks.
  - It is verbose, meaning it requires handling a lot of exceptions and closing a lot of resources.
  - It is not object-oriented, meaning it does not map the database entities to Java objects.
  - It is not secure, meaning it exposes the database credentials in plain text.

- Some mnemonics and learning tricks for manipulating in JDBC are:
  - Remember the acronym JDBC: Java Database Connectivity.