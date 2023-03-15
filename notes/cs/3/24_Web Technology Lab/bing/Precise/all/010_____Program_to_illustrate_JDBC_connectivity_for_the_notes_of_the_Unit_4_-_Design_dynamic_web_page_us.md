### Program to illustrate JDBC connectivity

JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data stored in a relational database. Here is an example program that illustrates JDBC connectivity:

1. First, you need to import the necessary packages. These include `java.sql.*` for JDBC classes and interfaces, and `java.util.*` for the `Scanner` class, which is used to take input from the user.

```java
import java.sql.*;
import java.util.*;
```

2. Next, you need to load the JDBC driver. This is done using the `Class.forName()` method, which takes the name of the driver class as a parameter. The driver class for MySQL, for example, is `com.mysql.jdbc.Driver`.

```java
Class.forName("com.mysql.jdbc.Driver");
```

3. Once the driver is loaded, you can establish a connection to the database using the `DriverManager.getConnection()` method. This method takes three parameters: the URL of the database, the username, and the password.

```java
String url = "jdbc:mysql://localhost:3306/mydatabase";
String username = "myusername";
String password = "mypassword";
Connection con = DriverManager.getConnection(url, username, password);
```

4. After establishing a connection, you can create a `Statement` object using the `createStatement()` method of the `Connection` object. This object is used to execute SQL statements.

```java
Statement stmt = con.createStatement();
```

5. You can then execute an SQL query using the `executeQuery()` method of the `Statement` object. This method takes an SQL query as a parameter and returns a `ResultSet` object, which contains the results of the query.

```java
String query = "SELECT * FROM mytable";
ResultSet rs = stmt.executeQuery(query);
```

6. You can iterate through the `ResultSet` object using the `next()` method, which returns `true` if there is another row in the result set and `false` otherwise. You can retrieve the values of the columns in the current row using the `getString()` method, which takes the name of the column as a parameter.

```java
while (rs.next()) {
    String column1 = rs.getString("column1");
    String column2 = rs.getString("column2");
    // ...
}
```

7. Finally, you should close the resources that you have used, including the `ResultSet`, `Statement`, and `Connection` objects. This is done using the `close()` method of each object.

```java
rs.close();
stmt.close();
con.close();
```

This is a basic example of how to use JDBC to connect to a database and execute an SQL query. You can use this as a starting point to build more complex programs that interact with databases using JDBC.