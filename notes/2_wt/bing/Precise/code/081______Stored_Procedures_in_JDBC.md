#### Stored Procedures in JDBC

A stored procedure is a precompiled set of SQL statements that are stored in a database. They can be called from a Java program using JDBC. Here is an example of how to call a stored procedure using JDBC:

```java
import java.sql.*;

public class StoredProcedureExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String user = "username";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password);
             CallableStatement stmt = conn.prepareCall("{call my_stored_procedure(?, ?)}")) {

            // Set input parameters
            stmt.setInt(1, 123);
            stmt.setString(2, "example");

            // Register output parameters
            stmt.registerOutParameter(3, Types.INTEGER);
            stmt.registerOutParameter(4, Types.VARCHAR);

            // Execute stored procedure
            stmt.execute();

            // Get output parameters
            int output1 = stmt.getInt(3);
            String output2 = stmt.getString(4);

            // Process results
            System.out.println("Output 1: " + output1);
            System.out.println("Output 2: " + output2);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```
This code calls a stored procedure named `my_stored_procedure` with two input parameters and two output parameters. The input parameters are set using the `setInt` and `setString` methods, and the output parameters are registered using the `registerOutParameter` method. The stored procedure is executed using the `execute` method, and the output parameters are retrieved using the `getInt` and `getString` methods. The results are then processed as needed.