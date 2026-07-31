### Java Database Connectivity (JDBC)

- JDBC is the Java API that manages connecting to a database, issuing queries and commands, and handling result sets obtained from the database.
- JDBC is a Java-based data access technology used for Java database connectivity. It is part of the Java Standard Edition platform, from Oracle Corporation.
- JDBC allows multiple implementations to exist and be used by the same application. The API provides a mechanism for dynamically loading the correct Java packages and registering them with the JDBC Driver Manager. The Driver Manager is used as a connection factory for creating JDBC connections.
- JDBC provides a common base on which tools and alternate interfaces can be built. It also supports features such as transactions, stored procedures, and metadata access.
- JDBC uses JDBC drivers to connect with the database. There are four types of JDBC drivers: JDBC-ODBC Bridge Driver, Native Driver, Network Protocol Driver, and Thin Driver.
- JDBC-ODBC Bridge Driver uses the ODBC driver to connect to the database. It is not portable and not recommended for production use.
- Native Driver uses the native library of the database to connect to the database. It is platform-dependent and requires installation of the native library.
- Network Protocol Driver uses a middleware server to communicate with the database. It is platform-independent and can access multiple databases.
- Thin Driver is a pure Java driver that communicates directly with the database. It is platform-independent and does not require any native library or middleware server.
- To establish a connection with the database, JDBC requires a database connection URL, which is a string that specifies the location and name of the database, and configuration properties such as username and password. The exact syntax of a database connection URL is defined by the DBMS.
- A simple example of a database connection URL for Java DB is:

```
jdbc:derby://localhost:1527/myDB;create=true;user=me;password=mine
```

- The above URL indicates that the driver should connect to the database named myDB on the localhost at port 1527, create the database if it does not exist, and use the username me and password mine to authenticate.
- To connect to the database, the application needs to load the appropriate driver class, obtain a connection object from the driver manager, and use the connection object to execute SQL statements and retrieve results. For example:

```java
// Load the Java DB driver
Class.forName("org.apache.derby.jdbc.ClientDriver");

// Get a connection object
Connection conn = DriverManager.getConnection("jdbc:derby://localhost:1527/myDB;create=true;user=me;password=mine");

// Create a statement object
Statement stmt = conn.createStatement();

// Execute a SQL query
ResultSet rs = stmt.executeQuery("SELECT * FROM EMPLOYEE");

// Process the result set
while (rs.next()) {
  // Get the values from each column
  int id = rs.getInt("ID");
  String name = rs.getString("NAME");
  double salary = rs.getDouble("SALARY");

  // Print the values
  System.out.println("ID: " + id + ", Name: " + name + ", Salary: " + salary);
}

// Close the resources
rs.close();
stmt.close();
conn.close();
```

- A mnemonic to remember the steps for JDBC connection is:

```
Load, Get, Create, Execute, Process, Close
```

- JDBC is a powerful and flexible API that enables Java applications to interact with various types of databases and data sources. It is widely used for developing data-driven applications in Java.