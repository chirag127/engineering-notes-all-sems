#### Databases with JDBC in JDBC

- JDBC (Java Database Connectivity) is the Java API that manages connecting to a database, issuing queries and commands, and handling result sets obtained from the database.
- JDBC acts as a bridge from your code to the database, as shown in Figure 1.

![Figure 1. JDBC connects Java programs to databases.](https://images.idgesg.net/images/article/2019/05/jdbc-100796849-large.jpg)

- JDBC consists of two layers: the JDBC API and the JDBC driver.
- The JDBC API supports communication between the Java application and the JDBC manager, while the JDBC driver supports communication between the JDBC manager and the database driver.
- The JDBC URL is an important parameter to establish the connection between your Java application and the database.
- The JDBC URL format can be different for different database systems, but it usually follows this general structure:

```
jdbc:<driver_name>://<host_name>:<port>/<database_name>
```

- For example, the JDBC URL for MySQL is:

```
jdbc:mysql://localhost:3306/testdb
```

- To connect to a database using JDBC, you need to use the `java.sql.Connection` interface and the `java.sql.DriverManager` class.
- The `DriverManager` class provides methods to register and obtain a JDBC driver, while the `Connection` interface represents a connection to a specific database.
- To create a connection, you need to pass the JDBC URL, the username, and the password to the `DriverManager.getConnection()` method.
- For example, to connect to the MySQL database in the previous example, you can use the following code:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCExample {

    public static void main(String[] args) {
        // JDBC URL, username and password of MySQL server
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "root";

        // create a connection to the database
        try (Connection connection = DriverManager.getConnection(url, user, password)) {
            System.out.println("Connected to the database successfully.");
        } catch (SQLException e) {
            System.out.println("Error connecting to the database.");
            e.printStackTrace();
        }
    }
}
```

- To execute queries and commands on the database, you need to use the `java.sql.Statement` interface and its subclasses `java.sql.PreparedStatement` and `java.sql.CallableStatement`.
- The `Statement` interface provides methods to execute SQL statements and retrieve the results, while the `PreparedStatement` and `CallableStatement` interfaces provide methods to execute parameterized SQL statements and stored procedures, respectively.
- To create a statement, you need to use the `Connection.createStatement()`, `Connection.prepareStatement()`, or `Connection.prepareCall()` methods, depending on the type of statement you want to create.
- For example, to create and execute a simple SQL query using a `Statement` object, you can use the following code:

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCExample {

    public static void main(String[] args) {
        // JDBC URL, username and password of MySQL server
        String url = "jdbc:mysql://localhost:3306/testdb";
        String user = "root";
        String password = "root";

        // create a connection to the database
        try (Connection connection = DriverManager.getConnection(url, user, password);
             // create a statement object
             Statement statement = connection.createStatement()) {
            System.out.println("Connected to the database successfully.");

            // execute a SQL query and get the result set
            String query = "SELECT * FROM employees";
            ResultSet resultSet = statement.executeQuery(query);

            // iterate through the result set and print the data
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String name = resultSet.getString("name");
                double salary = resultSet.getDouble("salary");
                System.out.println(id + "\t" + name + "\t" + salary);
            }
        } catch (SQLException e) {
            System.out.println("Error connecting to the database or executing the query.");
            e.printStackTrace();
        }
    }
}
```

- To handle the result set obtained from the database, you need to use the `java.sql.ResultSet` interface[^5^