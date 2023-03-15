#### Manipulating in JDBC
Here is an example of how to manipulate data in a database using JDBC:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class JdbcExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String user = "username";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            Statement stmt = conn.createStatement();
            String sql = "INSERT INTO mytable (column1, column2) VALUES ('value1', 'value2')";
            stmt.executeUpdate(sql);
            System.out.println("Data inserted successfully.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
This code connects to a MySQL database, creates a `Statement` object, and executes an `INSERT` statement to add a new row to the `mytable` table. The `executeUpdate` method is used to execute statements that manipulate data in the database, such as `INSERT`, `UPDATE`, and `DELETE` statements.
