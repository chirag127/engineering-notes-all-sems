#### Stored Procedures in JDBC

- Stored procedures are subroutines, segments of SQL statements that are stored in the SQL catalog of a database    .
- Stored procedures can be accessed by any application that can access relational databases, such as Java, Python, PHP, etc  .
- Stored procedures can improve the performance and security of database applications by reducing the network traffic, validating the input parameters, and encapsulating the business logic  .
- Stored procedures can also return output parameters and result sets to the calling application   .
- To call a stored procedure using JDBC, you need to follow these steps   :
  - Register the driver class using the `registerDriver()` method of the `DriverManager` class or the `Class.forName()` method.
  - Establish a connection to the database using the `getConnection()` method of the `DriverManager` class.
  - Create a `CallableStatement` object using the `prepareCall()` method of the `Connection` object. The `prepareCall()` method takes a SQL escape syntax that specifies the name and parameters of the stored procedure.
  - Register the output parameters using the `registerOutParameter()` method of the `CallableStatement` object. The `registerOutParameter()` method binds the JDBC data type to the data type of the stored procedure parameter.
  - Set the input parameters using the `setXXX()` methods of the `CallableStatement` object, where `XXX` is the JDBC data type of the parameter.
  - Execute the stored procedure using the `execute()` or `executeUpdate()` method of the `CallableStatement` object.
  - Retrieve the output parameters and result sets using the `getXXX()` methods of the `CallableStatement` object, where `XXX` is the JDBC data type of the parameter or column.
  - Close the `CallableStatement` and `Connection` objects using the `close()` method.

- Here is an example of calling a stored procedure that takes two input parameters and returns one output parameter using JDBC:

```java
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class StoredProcExample {

   public static void main(String[] args) {
      //Register the driver
      try {
         Class.forName("com.mysql.jdbc.Driver");
      } catch (ClassNotFoundException e) {
         System.out.println("Driver not found");
         e.printStackTrace();
         return;
      }
      
      Connection connection = null;
      CallableStatement callableStatement = null;
      
      try {
         //Establish a connection
         connection = DriverManager
            .getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
         
         //Create a CallableStatement object
         callableStatement = connection.prepareCall("{call addNumbers(?,?,?)}");
         
         //Register the output parameter
         callableStatement.registerOutParameter(3, java.sql.Types.INTEGER);
         
         //Set the input parameters
         callableStatement.setInt(1, 10);
         callableStatement.setInt(2, 20);
         
         //Execute the stored procedure
         callableStatement.executeUpdate();
         
         //Retrieve the output parameter
         int result = callableStatement.getInt(3);
         
         //Print the result
         System.out.println("The sum is: " + result);
         
      } catch (SQLException e) {
         System.out.println("SQL exception occurred");
         e.printStackTrace();
      } finally {
         //Close the resources
         try {
            if (callableStatement != null) {
               callableStatement.close();
            }
            if (connection != null) {
               connection.close();
            }
         } catch (SQLException e) {
            e.printStackTrace();
         }
      }
   }
}
```

- The output of the above program is:

```
The sum is: 30
```

- The stored procedure `addNumbers` is defined as follows in the MySQL database:

```sql
DELIMITER //
CREATE PROCEDURE addNumbers(IN a INT, IN b INT, OUT c INT)
BEGIN
   SET c = a + b;
END //
DELIMITER ;
```

- Some mnemonics and learning tricks for stored procedures in JDBC are:
  - Remember the acronym **CRSER** for the steps of calling a stored procedure: **C**reate, **