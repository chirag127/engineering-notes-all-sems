### Prepared Statements

A prepared statement is a special kind of statement object that allows you to execute parameterized SQL queries efficiently and securely. A parameterized SQL query is one that contains placeholders (usually question marks) for the values that will be supplied at runtime. For example:

```sql
SELECT * FROM employees WHERE salary > ? AND department = ?
```

The advantages of using prepared statements are:

- **Performance**: A prepared statement is compiled only once by the database server and can be executed multiple times with different values. This reduces the overhead of parsing and optimizing the query for each execution.
- **Security**: A prepared statement prevents SQL injection attacks by escaping the values that are supplied at runtime. SQL injection is a technique where malicious users can inject arbitrary SQL commands into a query by manipulating the input values. For example, if the input value for the department is `'Sales' OR 1 = 1`, the query will return all the records from the employees table. A prepared statement will treat the input value as a literal string and not as part of the SQL command.
- **Convenience**: A prepared statement simplifies the code by avoiding the need to concatenate strings and escape special characters. It also provides methods to set and get values of different data types, such as int, String, Date, etc.

To use a prepared statement in Java, you need to follow these steps:

1. Create a connection to the database using the `DriverManager.getConnection()` method.
2. Create a prepared statement object using the `Connection.prepareStatement()` method and pass the SQL query with placeholders as an argument.
3. Set the values for the placeholders using the appropriate setter methods of the `PreparedStatement` interface, such as `setInt()`, `setString()`, `setDate()`, etc. The first argument of these methods is the index of the placeholder (starting from 1), and the second argument is the value to be set.
4. Execute the prepared statement using the `executeQuery()` method for SELECT queries or the `executeUpdate()` method for INSERT, UPDATE, or DELETE queries. These methods return a `ResultSet` object or an int value respectively.
5. Process the results using the `ResultSet` methods, such as `next()`, `getInt()`, `getString()`, `getDate()`, etc.
6. Close the prepared statement and the connection objects using the `close()` method.

Here is an example of using a prepared statement to query the employees table:

```java
import java.sql.*;

public class PreparedStatementExample {

    public static void main(String[] args) {

        // Database connection parameters
        String url = "jdbc:mysql://localhost:3306/mydb";
        String user = "root";
        String password = "root";

        // SQL query with placeholders
        String sql = "SELECT * FROM employees WHERE salary > ? AND department = ?";

        try {
            // Create a connection to the database
            Connection conn = DriverManager.getConnection(url, user, password);

            // Create a prepared statement object
            PreparedStatement pstmt = conn.prepareStatement(sql);

            // Set the values for the placeholders
            pstmt.setInt(1, 5000); // salary > 5000
            pstmt.setString(2, "IT"); // department = 'IT'

            // Execute the query and get the result set
            ResultSet rs = pstmt.executeQuery();

            // Print the result set
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " | " + rs.getString("name") + " | " + rs.getInt("salary") + " | " + rs.getString("department"));
            }

            // Close the result set, the prepared statement, and the connection
            rs.close();
            pstmt.close();
            conn.close();

        } catch (SQLException e) {
            // Handle any SQL exceptions
            e.printStackTrace();
        }
    }
}
```