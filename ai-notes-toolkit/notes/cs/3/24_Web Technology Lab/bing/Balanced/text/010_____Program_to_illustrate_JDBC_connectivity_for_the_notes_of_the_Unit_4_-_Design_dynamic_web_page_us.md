### Program to illustrate JDBC connectivity for the notes of the Unit 4 - Design dynamic web page using server site programming Ex. ASP/JSP/PHP in the subject of Web Technology Lab

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- JDBC provides a standard interface for connecting to different databases, executing SQL statements, and retrieving the results.
- JDBC consists of two components: a JDBC driver and a JDBC API.
- A JDBC driver is a software module that implements the JDBC interface for a specific database. It acts as a bridge between the Java program and the database.
- A JDBC API is a set of classes and interfaces that define the methods and constants for accessing the database. It is part of the Java standard library (java.sql and javax.sql packages).
- To use JDBC, a Java program needs to perform the following steps:
  - Load the JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method.
  - Create a statement object using the Connection.createStatement() method.
  - Execute a SQL query using the Statement.executeQuery() or Statement.executeUpdate() method.
  - Process the result set using the ResultSet.next() and ResultSet.getXXX() methods.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods.

- The following is an example of a Java program that illustrates JDBC connectivity with MySQL database:

```java
//import the required packages
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {
    //declare the JDBC objects
    Connection conn = null;
    Statement stmt = null;
    ResultSet rs = null;

    try {
      //load the JDBC driver class
      Class.forName("com.mysql.cj.jdbc.Driver");

      //establish a connection to the database
      conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");

      //create a statement object
      stmt = conn.createStatement();

      //execute a SQL query
      rs = stmt.executeQuery("SELECT * FROM students");

      //process the result set
      while (rs.next()) {
        //retrieve the data from each row
        int id = rs.getInt("id");
        String name = rs.getString("name");
        String course = rs.getString("course");
        double marks = rs.getDouble("marks");

        //display the data
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Course: " + course);
        System.out.println("Marks: " + marks);
        System.out.println();
      }
    } catch (Exception e) {
      //handle the exceptions
      e.printStackTrace();
    } finally {
      //close the resources
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