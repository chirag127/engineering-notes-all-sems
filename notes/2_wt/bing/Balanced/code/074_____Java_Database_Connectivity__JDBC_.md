### Java Database Connectivity (JDBC)

JDBC is an API that allows Java programs to interact with databases. To use JDBC, you need to have a JDBC driver that supports the database you want to connect to. You can find the JDBC drivers for various databases on their official websites or online repositories.

To connect to a database using JDBC, you need to follow these steps:

1. Load the JDBC driver class using the Class.forName() method. For example, to load the MySQL driver, you can use: `Class.forName("com.mysql.jdbc.Driver");`
2. Create a connection object using the DriverManager.getConnection() method. You need to pass a database URL, a username, and a password as parameters. The database URL specifies the protocol, the server name, the port number, and the database name. For example, to connect to a MySQL database named testdb on localhost with username root and password root, you can use: `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "root");`
3. Create a statement object using the connection.createStatement() method. A statement object allows you to execute SQL queries on the database. For example, to create a statement object, you can use: `Statement stmt = con.createStatement();`
4. Execute the SQL query using the statement.executeQuery() method for SELECT queries, or the statement.executeUpdate() method for INSERT, UPDATE, or DELETE queries. You need to pass the SQL query as a string parameter. For example, to execute a SELECT query, you can use: `ResultSet rs = stmt.executeQuery("SELECT * FROM employees");`
5. Process the result set object using the methods of the ResultSet interface. A result set object contains the data returned by the query. You can use methods like next(), getString(), getInt(), getDouble(), etc. to access the data in each row and column. For example, to print the data in the result set, you can use: `while (rs.next()) { System.out.println(rs.getInt(1) + " " + rs.getString(2) + " " + rs.getDouble(3)); }`
6. Close the resources using the close() method. You should close the result set, the statement, and the connection objects in the reverse order of their creation. This will release the resources and avoid memory leaks. For example, to close the resources, you can use: `rs.close(); stmt.close(); con.close();`

Here is a complete example of connecting to a MySQL database and executing a SELECT query using JDBC:

```java
import java.sql.*;

public class JDBCExample {

  public static void main(String[] args) {
    try {
      // Load the MySQL driver
      Class.forName("com.mysql.jdbc.Driver");
      
      // Create a connection object
      Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "root");
      
      // Create a statement object
      Statement stmt = con.createStatement();
      
      // Execute a SQL query
      ResultSet rs = stmt.executeQuery("SELECT * FROM employees");
      
      // Process the result set
      while (rs.next()) {
        System.out.println(rs.getInt(1) + " " + rs.getString(2) + " " + rs.getDouble(3));
      }
      
      // Close the resources
      rs.close();
      stmt.close();
      con.close();
      
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```