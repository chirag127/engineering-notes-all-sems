### Program to illustrate JDBC connectivity

JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data stored in a relational database. Here is an example program that illustrates JDBC connectivity:

1. First, you need to import the necessary classes for JDBC connectivity. These include the `java.sql.*` package and the `javax.sql.*` package.

```java
import java.sql.*;
import javax.sql.*;
```

2. Next, you need to register the JDBC driver. This can be done using the `Class.forName()` method. For example, to register the MySQL JDBC driver, you would use the following code:

```java
Class.forName("com.mysql.jdbc.Driver");
```

3. After registering the driver, you need to establish a connection to the database. This can be done using the `DriverManager.getConnection()` method. You need to provide the URL of the database, the username, and the password as arguments.

```java
String url = "jdbc:mysql://localhost:3306/database_name";
String username = "username";
String password = "password";
Connection conn = DriverManager.getConnection(url, username, password);
```

4. Once you have a connection to the database, you can create a `Statement` object and execute SQL queries. For example, to execute a SELECT query and retrieve data from the database, you can use the following code:

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM table_name");
while (rs.next()) {
    // retrieve data from the result set
}
```

5. After you have finished working with the database, you should close the connection using the `Connection.close()` method.

```java
conn.close();
```

This is a basic example of how to use JDBC to connect to a database and execute SQL queries. You can use this as a starting point to build more complex programs that interact with databases using JDBC.