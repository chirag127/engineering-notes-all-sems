#### Stored Procedures in JDBC

- Stored procedures are a group of SQL statements that form a logical unit and perform a particular task, and they are used to encapsulate a set of operations or queries to execute on a database server.
- Stored procedures can be compiled and executed with different parameters and results, and they can have any combination of input, output, and input/output parameters.
- Stored procedures are supported by most DBMSs, but there is a fair amount of variation in their syntax and capabilities.
- Stored procedures have the following advantages:
  - They are stored in the database and can be called as and when required.
  - They can store business and database logic in the database itself which can be used by multiple applications.
  - They reduce network traffic as they do not need to send the set of queries over the network, but only a call to the stored procedure.
  - They lead to fast execution as they are compiled once and used multiple times.
- To call a stored procedure using a JDBC program, you need to :
  - Register the driver class using the `registerDriver()` method of the `DriverManager` class.
  - Establish a connection to the database using the `getConnection()` method of the `DriverManager` class.
  - Create a `CallableStatement` object using the `prepareCall()` method of the `Connection` object. The `prepareCall()` method takes a string argument that specifies the SQL escape syntax for calling the stored procedure.
  - Set the values for the input parameters using the `setXXX()` methods of the `CallableStatement` object, where `XXX` is the data type of the parameter.
  - Register the output parameters using the `registerOutParameter()` method of the `CallableStatement` object, specifying the parameter index and the data type.
  - Execute the stored procedure using the `execute()` or `executeUpdate()` method of the `CallableStatement` object.
  - Retrieve the values of the output parameters using the `getXXX()` methods of the `CallableStatement` object, where `XXX` is the data type of the parameter.
  - Close the `CallableStatement` and `Connection` objects using the `close()` method.
- The SQL escape syntax for calling a stored procedure is:
  - `{call procedure_name[(?, ?, ...)]}` for procedures that do not return result sets.
  - `{? = call function_name[(?, ?, ...)]}` for functions that return a single value.
  - `{call procedure_name[(?, ?, ...)]}` for procedures that return one or more result sets. The result sets can be retrieved using the `getResultSet()` method of the `CallableStatement` object.
- The following is an example of calling a stored procedure named `SHOW_SUPPLIERS` that prints a result set containing the names of coffee suppliers and the coffees they supply:

```java
import java.sql.*;

public class StoredProcedureExample {

   public static void main(String[] args) {
      //Register the driver
      try {
         DriverManager.registerDriver(new com.mysql.jdbc.Driver());
      } catch (SQLException ex) {
         System.out.println("Error: unable to load driver class!");
         System.exit(1);
      }
      
      //Establish the connection
      String URL = "jdbc:mysql://localhost:3306/CoffeeDB";
      String USER = "root";
      String PASS = "password";
      Connection conn = null;
      try {
         conn = DriverManager.getConnection(URL, USER, PASS);
      } catch (SQLException e) {
         e.printStackTrace();
      }
      
      //Create the CallableStatement
      CallableStatement cs = null;
      try {
         cs = conn.prepareCall("{call SHOW_SUPPLIERS}");
      } catch (SQLException e) {
         e.printStackTrace();
      }
      
      //Execute the stored procedure
      ResultSet rs = null;
      try {
         boolean hasResults = cs.execute();
         if (hasResults) {
            rs = cs.getResultSet();
         }
      } catch (SQLException e) {
         e.printStackTrace();
      }
      
      //Process the result set
      try {
         while (rs.next()) {
            String supplier = rs.getString("SUP_NAME");
            String coffee = rs.getString("COF_NAME");
            System.out.println(supplier + ": " + coffee);
         }
      } catch (SQLException e) {
         e.printStackTrace();
      }
      
      //Close the resources
      try {
         rs.close();
         cs.close();
         conn.close();
      } catch (SQLException e) {