### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java application to execute SQL statements and retrieve the results from a database server.

To use JDBC, we need to follow these steps:

1. Load the JDBC driver class that corresponds to the type of database we want to connect to. For example, to connect to MySQL, we can use `Class.forName("com.mysql.jdbc.Driver");`.
2. Create a connection object that represents the database connection. We need to provide a connection URL that specifies the database server address, the database name, and the user credentials. For example, to connect to MySQL, we can use `Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");`.
3. Create a statement object that allows us to execute SQL queries. We can use `Statement stmt = con.createStatement();` to create a simple statement, or `PreparedStatement pstmt = con.prepareStatement(sql);` to create a prepared statement that can accept parameters.
4. Execute the SQL query and obtain the result set object that contains the data returned by the query. We can use `ResultSet rs = stmt.executeQuery(sql);` to execute a query that returns data, or `int rows = stmt.executeUpdate(sql);` to execute a query that modifies data.
5. Process the result set by using methods such as `rs.next()`, `rs.getInt()`, `rs.getString()`, etc. to iterate over the rows and columns of the data.
6. Close the resources such as statement, result set, and connection when they are no longer needed. We can use `rs.close()`, `stmt.close()`, and `con.close()` to close them respectively.

Here is an example of a Java program that connects to a MySQL database and executes a simple query:

```java
import java.sql.*;

public class JDBCExample {

    public static void main(String[] args) {

        // Load the JDBC driver
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        // Create the connection object
        Connection con = null;
        try {
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","password");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Create the statement object
        Statement stmt = null;
        try {
            stmt = con.createStatement();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Execute the query and get the result set
        ResultSet rs = null;
        try {
            rs = stmt.executeQuery("SELECT * FROM students");
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Process the result set
        try {
            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
                int age = rs.getInt("age");
                System.out.println(id + " " + name + " " + age);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        // Close the resources
        try {
            rs.close();
            stmt.close();
            con.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

This program assumes that there is a table called `students` in the database `test` with the following schema:

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```

And some sample data:

```sql
INSERT INTO students VALUES (1, 'Alice', 20);
INSERT INTO students VALUES (2, 'Bob', 21);
INSERT INTO students VALUES (3, 'Charlie', 19);
```

The output of the program should be:

```
1 Alice 20
2 Bob 21
3 Charlie 19
```