### Program to illustrate JDBC connectivity

JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data stored in a relational database. Here is an example program that illustrates JDBC connectivity:

1. **Import necessary packages**: The first step is to import the necessary packages, such as `java.sql.*` which contains classes and interfaces for JDBC.

```java
import java.sql.*;
```

2. **Load and register the driver**: The next step is to load and register the JDBC driver. This can be done using the `Class.forName()` method.

```java
Class.forName("com.mysql.jdbc.Driver");
```

3. **Establish a connection**: After the driver is loaded and registered, a connection to the database can be established using the `DriverManager.getConnection()` method.

```java
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "username", "password");
```

4. **Create a statement**: Once a connection is established, a `Statement` object can be created using the `createStatement()` method of the `Connection` object.

```java
Statement stmt = con.createStatement();
```

5. **Execute a query**: A query can be executed using the `executeQuery()` method of the `Statement` object. The result of the query is returned as a `ResultSet` object.

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");
```

6. **Process the result**: The result of the query can be processed using the methods of the `ResultSet` object, such as `next()` and `getString()`.

```java
while (rs.next()) {
    System.out.println(rs.getString(1) + " " + rs.getString(2));
}
```

7. **Close the resources**: Finally, it is important to close the resources such as the `ResultSet`, `Statement`, and `Connection` objects to release the resources held by them.

```java
rs.close();
stmt.close();
con.close();
```

This is an example of how JDBC connectivity can be achieved in a Java program. It is important to note that the specific details, such as the driver class name and the connection URL, may vary depending on the specific database and JDBC driver being used.