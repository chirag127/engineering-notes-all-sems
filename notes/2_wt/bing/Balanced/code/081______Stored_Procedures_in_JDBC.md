#### Stored Procedures in JDBC

Stored procedures are subroutines, segments of SQL statements that are stored in the SQL catalog of a database. They can be accessed by applications that can access relational databases, such as Java, Python, PHP, etc. Stored procedures can improve the performance and security of database applications, as well as simplify the code and reduce network traffic.

To call a stored procedure using a JDBC program, you need to:

- Register the driver class using the `registerDriver()` method of the `DriverManager` class.
- Establish a connection to the database using the `getConnection()` method of the `DriverManager` class.
- Create a `CallableStatement` object using the `prepareCall()` method of the `Connection` object. The `prepareCall()` method takes a SQL escape syntax that specifies the name and parameters of the stored procedure.
- Set the input parameters (if any) using the `setXXX()` methods of the `CallableStatement` object, where `XXX` is the data type of the parameter.
- Register the output parameters (if any) using the `registerOutParameter()` method of the `CallableStatement` object. This method binds the JDBC data type to the data type the stored procedure returns.
- Execute the stored procedure using the `execute()` or `executeUpdate()` method of the `CallableStatement` object.
- Retrieve the output parameters (if any) using the `getXXX()` methods of the `CallableStatement` object, where `XXX` is the data type of the parameter.
- Close the `CallableStatement` and `Connection` objects using the `close()` method.

Here is an example of calling a stored procedure that takes two input parameters and returns one output parameter:

```java
import java.sql.*;

public class CallStoredProc {

  public static void main(String[] args) {
    try {
      // Register the driver class
      DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());
      
      // Establish a connection
      Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
      
      // Create a CallableStatement object
      CallableStatement stmt = con.prepareCall("{call addNumbers(?, ?, ?)}");
      
      // Set the input parameters
      stmt.setInt(1, 10); // First input parameter
      stmt.setInt(2, 20); // Second input parameter
      
      // Register the output parameter
      stmt.registerOutParameter(3, Types.INTEGER); // Third parameter is output
      
      // Execute the stored procedure
      stmt.execute();
      
      // Retrieve the output parameter
      int result = stmt.getInt(3); // Get the output parameter
      
      // Print the result
      System.out.println("The sum is: " + result);
      
      // Close the objects
      stmt.close();
      con.close();
      
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

The above code assumes that there is a stored procedure named `addNumbers` in the `testdb` database, which takes two integers as input and returns their sum as output. The SQL script to create the stored procedure is:

```sql
DELIMITER //
CREATE PROCEDURE addNumbers(IN a INT, IN b INT, OUT c INT)
BEGIN
  SET c = a + b;
END //
DELIMITER ;
```