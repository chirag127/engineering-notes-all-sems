# Databases with JDBC

JDBC (Java Database Connectivity) is an API (Application Programming Interface) that allows Java programs to interact with databases. JDBC provides classes and interfaces to establish connections, execute queries, manipulate data, and handle errors. JDBC can be used with any relational database management system (RDBMS) that has a JDBC driver. A JDBC driver is a software component that enables the communication between the Java application and the database.

Some of the main concepts and steps involved in using JDBC are:

- **Connection**: A connection represents a session with a specific database. To establish a connection, the application needs to provide the JDBC driver name, the database URL, and the user name and password if required. A connection object can be obtained by calling the `DriverManager.getConnection()` method with the appropriate parameters.
- **Statement**: A statement is an object that represents a SQL command that can be executed on the database. There are three types of statements: `Statement`, `PreparedStatement`, and `CallableStatement`. A statement object can be created by calling the `Connection.createStatement()` method or its variants.
- **ResultSet**: A result set is an object that holds the data returned by a query. A result set object can be obtained by calling the `Statement.executeQuery()` method or its variants. A result set has a cursor that points to the current row of data. The cursor can be moved by calling methods such as `ResultSet.next()`, `ResultSet.previous()`, or `ResultSet.absolute()`. The data in the current row can be accessed by calling methods such as `ResultSet.getString()`, `ResultSet.getInt()`, or `ResultSet.getObject()`.
- **Exception**: An exception is an object that represents an error or a warning that occurs during the execution of a JDBC operation. JDBC defines a hierarchy of exception classes that inherit from the `SQLException` class. An exception object contains information such as the error code, the SQL state, and the error message. An exception object can be caught by using a `try-catch` block or a `try-with-resources` statement.

A simple example of using JDBC to query a database is:

```java
// Load the JDBC driver
Class.forName("org.sqlite.JDBC");

// Establish a connection
Connection conn = DriverManager.getConnection("jdbc:sqlite:sample.db");

// Create a statement
Statement stmt = conn.createStatement();

// Execute a query
ResultSet rs = stmt.executeQuery("SELECT * FROM employees");

// Process the result set
while (rs.next()) {
  // Get the data from the current row
  int id = rs.getInt("id");
  String name = rs.getString("name");
  double salary = rs.getDouble("salary");

  // Print the data
  System.out.println(id + "\t" + name + "\t" + salary);
}

// Close the resources
rs.close();
stmt.close();
conn.close();
```