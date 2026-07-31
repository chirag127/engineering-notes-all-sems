#### Manipulating in JDBC

To manipulate data in a database using JDBC, you need to follow these steps:

- Load the JDBC driver class using the `Class.forName()` method.
- Establish a connection to the database using the `DriverManager.getConnection()` method.
- Create a `Statement` object using the `Connection.createStatement()` method.
- Execute a SQL query or update using the `Statement.executeQuery()` or `Statement.executeUpdate()` method.
- Process the results using the `ResultSet` object returned by the `Statement.executeQuery()` method, or get the number of affected rows using the `Statement.executeUpdate()` method.
- Close the `ResultSet`, `Statement`, and `Connection` objects using the `close()` method.

For example, the following code snippet shows how to insert a new record into a table called `employees` using JDBC:

```java
// Load the JDBC driver class
Class.forName("com.mysql.jdbc.Driver");

// Establish a connection to the database
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "password");

// Create a statement object
Statement stmt = conn.createStatement();

// Execute a SQL update
int rows = stmt.executeUpdate("INSERT INTO employees (name, salary, department) VALUES ('Alice', 5000, 'IT')");

// Print the number of affected rows
System.out.println("Inserted " + rows + " row(s) into the table");

// Close the statement and connection objects
stmt.close();
conn.close();
```