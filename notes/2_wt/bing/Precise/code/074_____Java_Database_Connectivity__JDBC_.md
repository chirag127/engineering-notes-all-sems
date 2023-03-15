### Java Database Connectivity (JDBC)
Java Database Connectivity (JDBC) is an application programming interface (API) for the programming language Java, which defines how a client may access a database. Here is an example of how to connect to a database using JDBC:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JdbcExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String username = "myusername";
        String password = "mypassword";

        System.out.println("Connecting to database...");

        try (Connection connection = DriverManager.getConnection(url, username, password)) {
            System.out.println("Database connected!");
        } catch (SQLException e) {
            throw new IllegalStateException("Cannot connect to the database!", e);
        }
    }
}
```
This code connects to a MySQL database running on the local machine on port 3306. The database name is `mydatabase`, the username is `myusername`, and the password is `mypassword`. The `try-with-resources` statement is used to automatically close the `Connection` object when it is no longer needed.