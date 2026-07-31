# Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

- Load the JDBC driver class that corresponds to the type of database we want to connect to. For example, for MySQL, we can use `Class.forName("com.mysql.jdbc.Driver");`
- Create a connection object that represents a physical connection to the database server. We need to provide a connection URL that specifies the database name, host, port, and other parameters. We also need to provide a user name and password for authentication. For example, for MySQL, we can use `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");`
- Create a statement object that allows us to execute SQL queries and commands. We can use different types of statements, such as `Statement`, `PreparedStatement`, or `CallableStatement`, depending on our needs. For example, we can use `Statement stmt = con.createStatement();`
- Execute the statement and obtain the result set object that contains the data returned by the query. We can use different methods, such as `executeQuery`, `executeUpdate`, or `execute`, depending on the type of statement. For example, we can use `ResultSet rs = stmt.executeQuery("SELECT * FROM students");`
- Process the result set by iterating over the rows and columns and extracting the values. We can use different methods, such as `next`, `getString`, `getInt`, or `getBoolean`, depending on the data type. For example, we can use `while(rs.next()){System.out.println(rs.getString("name") + " " + rs.getInt("age"));}`
- Close the result set, statement, and connection objects to release the resources and avoid memory leaks. We can use the `close` method for each object. For example, we can use `rs.close(); stmt.close(); con.close();`

Here is a complete example of a Java program that connects to a MySQL database and prints the data from a table:

```java
import java.sql.*;

public class JDBCExample {

    public static void main(String[] args) {
        try {
            // Load the JDBC driver
            Class.forName("com.mysql.jdbc.Driver");
            
            // Create a connection object
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");
            
            // Create a statement object
            Statement stmt = con.createStatement();
            
            // Execute a query and obtain a result set
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            
            // Process the result set
            while(rs.next()){
                System.out.println(rs.getString("name") + " " + rs.getInt("age"));
            }
            
            // Close the result set, statement, and connection objects
            rs.close();
            stmt.close();
            con.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```