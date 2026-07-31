### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

1. Load the JDBC driver class that corresponds to the type of database we want to connect to. For example, to connect to MySQL, we can use the `com.mysql.cj.jdbc.Driver` class, which is provided by the MySQL Connector/J library. We can load the driver class by using the `Class.forName()` method, passing the fully qualified name of the driver class as a parameter. This will register the driver with the `DriverManager` class, which is responsible for managing the available drivers and creating connections.
2. Create a connection object by using the `DriverManager.getConnection()` method, passing the connection URL, the user name, and the password as parameters. The connection URL specifies the protocol, the host name, the port number, and the database name of the server we want to connect to. For example, to connect to a MySQL database named `webtech` on the local host, we can use the following connection URL: `jdbc:mysql://localhost:3306/webtech`. The user name and password are the credentials for accessing the database server.
3. Create a statement object by using the `Connection.createStatement()` method, which returns an object that implements the `Statement` interface. A statement object allows us to execute SQL statements and retrieve the results. There are different types of statements, such as `Statement`, `PreparedStatement`, and `CallableStatement`, depending on the type and complexity of the SQL statements we want to execute.
4. Execute the SQL statement by using the `Statement.execute()` or `Statement.executeQuery()` methods, depending on whether the statement returns a result set or not. A result set is a collection of rows that match the query criteria. The `Statement.execute()` method returns a boolean value indicating whether the statement returns a result set or not. The `Statement.executeQuery()` method returns a `ResultSet` object that contains the result set. We can use the `ResultSet.next()` method to iterate over the rows of the result set, and the `ResultSet.getXXX()` methods to get the values of the columns by name or index.
5. Close the resources by using the `close()` methods of the `ResultSet`, `Statement`, and `Connection` objects, in the reverse order of their creation. This will release the resources and avoid memory leaks.

Here is an example of a Java program that illustrates JDBC connectivity to a MySQL database:

```java
import java.sql.*;

public class JDBCExample {

    public static void main(String[] args) {
        // Load the JDBC driver
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver loaded");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        // Create a connection
        Connection connection = null;
        try {
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/webtech", "root", "password");
            System.out.println("Connection established");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Create a statement
        Statement statement = null;
        try {
            statement = connection.createStatement();
            System.out.println("Statement created");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Execute a SQL statement
        ResultSet resultSet = null;
        try {
            resultSet = statement.executeQuery("SELECT * FROM students");
            System.out.println("Statement executed");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Process the result set
        try {
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                double gpa = resultSet.getDouble("gpa");
                System.out.println("Student: " + id + ", " + name + ", " + gpa);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Close the resources
        try {
            resultSet.close();
            statement.close();
            connection.close();
            System.out.println("Resources closed");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```