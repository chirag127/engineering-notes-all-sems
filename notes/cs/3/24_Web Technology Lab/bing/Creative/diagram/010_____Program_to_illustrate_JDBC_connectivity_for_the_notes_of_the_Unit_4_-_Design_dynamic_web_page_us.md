### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

- Load the JDBC driver class that implements the `java.sql.Driver` interface. This can be done by using the `Class.forName()` method with the fully qualified name of the driver class as a parameter. For example, to load the JDBC driver for MySQL, we can use:

```java
Class.forName("com.mysql.jdbc.Driver");
```

- Establish a connection to the database server by using the `DriverManager.getConnection()` method with a connection URL, a user name and a password as parameters. The connection URL specifies the protocol, the host name, the port number, the database name and other connection properties of the database server. For example, to connect to a MySQL database named `webtech` on the local host with the user name `root` and the password `admin`, we can use:

```java
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "admin");
```

- Create a statement object by using the `Connection.createStatement()` method. A statement object is used to execute SQL queries and update statements on the database. For example, to create a statement object, we can use:

```java
Statement stmt = con.createStatement();
```

- Execute the SQL statement by using the `Statement.executeQuery()` method for queries or the `Statement.executeUpdate()` method for updates. The `executeQuery()` method returns a `ResultSet` object that contains the rows and columns of the query result. The `executeUpdate()` method returns an `int` value that indicates the number of rows affected by the update. For example, to execute a query that selects all the records from a table named `students`, we can use:

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM students");
```

- Process the result set by using the `ResultSet.next()` method to move the cursor to the next row and the `ResultSet.getXXX()` methods to retrieve the values of the columns. The `getXXX()` methods take the column name or the column index as a parameter and return the value of the column as a Java data type. For example, to print the name and the age of each student in the result set, we can use:

```java
while (rs.next()) {
  String name = rs.getString("name");
  int age = rs.getInt("age");
  System.out.println(name + " is " + age + " years old.");
}
```

- Close the resources by using the `ResultSet.close()`, `Statement.close()` and `Connection.close()` methods. This releases the memory and the database connections used by the JDBC objects. For example, to close the resources, we can use:

```java
rs.close();
stmt.close();
con.close();
```

- Handle any exceptions that may occur during the JDBC operations by using the `try-catch-finally` blocks. The JDBC methods may throw a `SQLException` or a `ClassNotFoundException` that need to be caught and handled appropriately. For example, to handle the exceptions, we can use:

```java
try {
  // JDBC code
} catch (SQLException e) {
  // Handle SQL exception
} catch (ClassNotFoundException e) {
  // Handle class not found exception
} finally {
  // Close resources
}
```

The following is a complete Java program that illustrates the JDBC connectivity to a MySQL database:

```java
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {

    // Declare JDBC objects
    Connection con = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      // Load the JDBC driver
      Class.forName("com.mysql.jdbc.Driver");

      // Establish the connection
      con = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "admin");

      // Create the statement
      stmt = con.createStatement();

      // Execute the query
      rs = stmt.executeQuery("SELECT * FROM students");

      // Process the result set
      while (rs.next()) {
        String name = rs.getString("name");
        int age = rs.getInt("age");
        System.out.println(name + " is " + age + " years old.");
      }
    } catch (SQLException e) {
      // Handle SQL exception
      e.printStackTrace();
    } catch (ClassNotFoundException e) {
      // Handle class not found exception
      e.printStackTrace();
    } finally {
      //