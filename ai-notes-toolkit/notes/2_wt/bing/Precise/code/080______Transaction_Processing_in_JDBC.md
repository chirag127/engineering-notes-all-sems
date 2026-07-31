#### Transaction Processing in JDBC
```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class TransactionProcessing {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            // Step 1: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            // Step 2: Open a connection
            conn = DriverManager.getConnection("jdbc:mysql://localhost/EMP", "username", "password");

            // Step 3: Disable auto-commit mode
            conn.setAutoCommit(false);

            // Step 4: Create a statement object
            stmt = conn.createStatement();

            // Step 5: Execute a series of SQL statements
            String sql1 = "INSERT INTO Employees VALUES (106, 20, 'Rita', 'Tez')";
            stmt.executeUpdate(sql1);

            String sql2 = "UPDATE Employees SET age=30 WHERE id=106";
            stmt.executeUpdate(sql2);

            // Step 6: Commit the transaction
            conn.commit();

            System.out.println("Transaction committed successfully.");
        } catch (SQLException se) {
            // Handle errors for JDBC
            try {
                // Rollback the transaction in case of errors
                if (conn != null) {
                    conn.rollback();
                }
                System.out.println("Transaction rolled back.");
            } catch (SQLException se2) {
                se2.printStackTrace();
            }
            se.printStackTrace();
        } catch (Exception e) {
            // Handle errors for Class.forName
            e.printStackTrace();
        } finally {
            // Step 7: Clean-up environment
            try {
                if (stmt != null) {
                    stmt.close();
                }
            } catch (SQLException se2) {
                se2.printStackTrace();
            }
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException se) {
                se.printStackTrace();
            }
        }
    }
}
```