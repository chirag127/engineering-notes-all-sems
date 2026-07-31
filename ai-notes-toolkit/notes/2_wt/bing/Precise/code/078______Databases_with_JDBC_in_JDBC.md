#### Databases with JDBC in JDBC
Here is an example of how to connect to a database using JDBC:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseConnection {
    public static void main(String[] args) {
        // Replace with your database URL, username, and password
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String username = "myusername";
        String password = "mypassword";

        // Connect to the database
        try (Connection connection = DriverManager.getConnection(url, username, password)) {
            System.out.println("Connected to the database");
        } catch (SQLException e) {
            System.out.println("Error connecting to the database");
            e.printStackTrace();
        }
    }
}
```
This code connects to a MySQL database using the JDBC driver. The `url` variable should be updated with the URL of your database, and the `username` and `password` variables should be updated with your database username and password. The `try-with-resources` statement is used to automatically close the `Connection` object when it is no longer needed.
