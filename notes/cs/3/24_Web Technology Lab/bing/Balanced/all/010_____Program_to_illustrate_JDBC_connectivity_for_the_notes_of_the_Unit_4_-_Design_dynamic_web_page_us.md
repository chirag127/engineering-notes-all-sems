### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases. JDBC provides a standard set of interfaces and classes that define how to connect to a database, execute queries and updates, and retrieve the results.

To illustrate JDBC connectivity, we will use a simple example of a Java program that connects to a MySQL database and performs some basic operations. The steps involved are:

- Import the required packages, such as `java.sql.*` and `com.mysql.cj.jdbc.*`.
- Register the JDBC driver for MySQL using the `Class.forName()` method.
- Establish a connection to the database using the `DriverManager.getConnection()` method, which takes the URL, username, and password of the database as parameters.
- Create a `Statement` object using the `Connection.createStatement()` method, which allows us to execute SQL queries and updates.
- Execute a query using the `Statement.executeQuery()` method, which returns a `ResultSet` object that contains the data returned by the query.
- Iterate over the `ResultSet` using the `next()` method, and access the values of each column using the `getXXX()` methods, where XXX is the data type of the column.
- Close the `ResultSet`, `Statement`, and `Connection` objects using the `close()` method, to release the resources and avoid memory leaks.

The following code snippet shows the Java program that illustrates JDBC connectivity:

```java
// Import the required packages
import java.sql.*;
import com.mysql.cj.jdbc.*;

public class JDBCExample {

    public static void main(String[] args) {
        // Declare the variables for the database connection
        String url = "jdbc:mysql://localhost:3306/webtech"; // The URL of the database
        String user = "root"; // The username of the database
        String password = "root"; // The password of the database
        Connection conn = null; // The connection object
        Statement stmt = null; // The statement object
        ResultSet rs = null; // The result set object

        try {
            // Register the JDBC driver for MySQL
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Establish a connection to the database
            conn = DriverManager.getConnection(url, user, password);

            // Create a statement object
            stmt = conn.createStatement();

            // Execute a query
            String sql = "SELECT * FROM student"; // The SQL query to execute
            rs = stmt.executeQuery(sql); // The result set object that contains the data returned by the query

            // Iterate over the result set
            while (rs.next()) {
                // Access the values of each column using the getXXX() methods
                int id = rs.getInt("id"); // The id column
                String name = rs.getString("name"); // The name column
                int age = rs.getInt("age"); // The age column
                String course = rs.getString("course"); // The course column

                // Print the values of each row
                System.out.println("ID: " + id + ", Name: " + name + ", Age: " + age + ", Course: " + course);
            }
        } catch (Exception e) {
            // Handle any exceptions
            e.printStackTrace();
        } finally {
            // Close the result set, statement, and connection objects
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
                // Handle any SQL exceptions
                se.printStackTrace();
            }
        }
    }
}
```

The output of the program will depend on the data stored in the `student` table of the `webtech` database. For example, if the table contains the following data:

| id | name  | age | course |
|----|-------|-----|--------|
| 1  | Alice | 20  | Java   |
| 2  | Bob   | 21  | PHP    |
| 3  | Carol | 19  | ASP    |

The output of the program will be:

```
ID: 1, Name: Alice, Age: 20, Course: Java
ID: 2, Name: Bob, Age: 21, Course: PHP
ID: 3, Name: Carol, Age: 19, Course: ASP
```