### Java Database Connectivity (JDBC)

Java Database Connectivity (JDBC) is a Java API that allows Java programs to access and manipulate data stored in a database. It provides a standard set of interfaces to connect to various relational databases and execute SQL statements.

#### Benefits of using JDBC

- JDBC provides a standard way to access databases from Java programs.
- It supports multiple database vendors, which makes it easy to switch between databases without changing the application code.
- JDBC provides a high-level abstraction layer over the underlying database, which makes it easy to write database-independent code.
- It allows Java programs to take full advantage of the features provided by the underlying database.

#### JDBC Components

- DriverManager: It manages a list of database drivers. It is responsible for establishing a connection to the database.
- Connection: It represents a connection to a database. It is responsible for creating Statement and PreparedStatement objects.
- Statement: It represents an SQL statement that is executed against a database. It is used to execute SQL queries and updates.
- ResultSet: It represents a set of rows retrieved from a database. It is used to retrieve data from the database.
- PreparedStatement: It represents a precompiled SQL statement. It is used to execute parameterized SQL statements.

#### JDBC Workflow

1. Load the JDBC driver class using Class.forName() method.
2. Establish a connection to the database using DriverManager.getConnection() method.
3. Create a Statement or PreparedStatement object.
4. Execute the SQL statement using the execute() or executeUpdate() method of the Statement or PreparedStatement object.
5. Retrieve the results using the ResultSet object.
6. Close the ResultSet, Statement, and Connection objects using the close() method.

#### Example

```java
import java.sql.*;

public class JDBCExample {
    public static void main(String[] args) throws SQLException {
        // Load the JDBC driver
        Class.forName("com.mysql.jdbc.Driver");

        // Establish a connection to the database
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "username", "password");

        // Create a PreparedStatement object
        PreparedStatement stmt = conn.prepareStatement("SELECT * FROM employees WHERE salary > ?");

        // Set the parameter value
        stmt.setInt(1, 50000);

        // Execute the SQL statement
        ResultSet rs = stmt.executeQuery();

        // Process the results
        while (rs.next()) {
            System.out.println(rs.getString("name") + " " + rs.getInt("salary"));
        }

        // Close the ResultSet, Statement, and Connection objects
        rs.close();
        stmt.close();
        conn.close();
    }
}
```

In the above example, we load the JDBC driver class for MySQL, establish a connection to the database, create a PreparedStatement object with a parameterized SQL statement, set the parameter value, execute the statement, and process the results using a ResultSet object.

#### Conclusion

Java Database Connectivity (JDBC) is a powerful API that provides a standard way to access and manipulate data stored in a database. It provides a high-level abstraction layer over the underlying database, which makes it easy to write database-independent code. By following the JDBC workflow and using the JDBC components, Java programs can interact with various relational databases and take full advantage of their features.