### Program to illustrate JDBC connectivity

JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data stored in a relational database. Here is an example program that illustrates JDBC connectivity:

1. First, you need to import the necessary classes for JDBC connectivity. These include the `java.sql.*` package and the specific driver class for the database you are using.

```java
import java.sql.*;
```

2. Next, you need to register the JDBC driver. This can be done using the `Class.forName()` method, which loads the driver class.

```java
Class.forName("com.mysql.jdbc.Driver");
```

3. After registering the driver, you can establish a connection to the database using the `DriverManager.getConnection()` method. This method takes the URL of the database, the username, and the password as arguments.

```java
String url = "jdbc:mysql://localhost:3306/mydatabase";
String username = "myusername";
String password = "mypassword";
Connection conn = DriverManager.getConnection(url, username, password);
```

4. Once you have a connection to the database, you can create a `Statement` object and execute SQL queries using the `executeQuery()` method.

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");
```

5. The `ResultSet` object returned by the `executeQuery()` method contains the results of the query. You can iterate through the results using the `next()` method and retrieve the values of the columns using the appropriate `get` methods.

```java
while (rs.next()) {
    int id = rs.getInt("id");
    String name = rs.getString("name");
    // ...
}
```

6. Finally, it is important to close the resources you have used, such as the `ResultSet`, `Statement`, and `Connection` objects, to release the resources they are holding.

```java
rs.close();
stmt.close();
conn.close();
```

This is a basic example of how to use JDBC to connect to a database and execute a query. You can use this as a starting point to build more complex programs that interact with databases using JDBC.