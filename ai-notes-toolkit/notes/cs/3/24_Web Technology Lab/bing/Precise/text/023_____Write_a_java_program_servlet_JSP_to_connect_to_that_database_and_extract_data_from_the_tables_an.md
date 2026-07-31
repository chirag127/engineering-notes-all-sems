### Java Program to Connect to Database and Extract Data

Here is an example of a Java program that connects to a database and extracts data from tables to display:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DatabaseConnection {
    public static void main(String[] args) {
        // Replace with your database URL, username, and password
        String url = "jdbc:mysql://localhost:3306/databaseName";
        String username = "username";
        String password = "password";

        try {
            // Load the JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            // Establish a connection to the database
            Connection conn = DriverManager.getConnection(url, username, password);

            // Create a statement object to execute SQL queries
            Statement stmt = conn.createStatement();

            // Execute a SELECT query and store the result in a ResultSet
            ResultSet rs = stmt.executeQuery("SELECT * FROM tableName");

            // Iterate through the ResultSet and print the data
            while (rs.next()) {
                System.out.println(rs.getString("columnName1") + " " + rs.getString("columnName2"));
            }

            // Close the ResultSet and Statement
            rs.close();
            stmt.close();

            // Close the connection to the database
            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

This program uses the JDBC API to connect to a MySQL database. The JDBC driver for MySQL is loaded using the `Class.forName()` method. A connection to the database is established using the `DriverManager.getConnection()` method, which takes the database URL, username, and password as arguments.

A `Statement` object is created using the `conn.createStatement()` method, which is used to execute a SQL `SELECT` query. The result of the query is stored in a `ResultSet` object, which is iterated through to print the data from the table.

After the data has been extracted and displayed, the `ResultSet`, `Statement`, and `Connection` objects are closed using their respective `close()` methods.

This is a basic example of how to connect to a database and extract data from tables using Java. More advanced features, such as prepared statements and transaction management, can be implemented as needed.