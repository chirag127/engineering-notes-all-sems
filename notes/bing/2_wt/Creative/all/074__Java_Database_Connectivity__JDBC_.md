### Java Database Connectivity (JDBC)

- JDBC is an API (Application Programming Interface) that allows Java applications to interact with various types of databases, such as relational, hierarchical, or object-oriented.
- JDBC provides a standard way of accessing data from different sources, such as Oracle, MySQL, SQL Server, etc., using a common set of methods and classes.
- JDBC consists of two main components: the JDBC API and the JDBC driver.
- The JDBC API defines the interfaces and classes that Java applications use to connect to a database, execute queries and commands, and process the results.
- The JDBC driver is a software component that implements the JDBC API for a specific database. It acts as a bridge between the Java application and the database, translating the JDBC calls into the native protocol of the database.
- There are four types of JDBC drivers, each with different advantages and disadvantages:
  - Type 1: JDBC-ODBC Bridge Driver. This driver uses the ODBC (Open Database Connectivity) driver of the database to connect to it. It is the simplest and most portable driver, but it has performance and security issues, and it requires the ODBC driver to be installed on the client machine.
  - Type 2: Native Driver. This driver uses the native library of the database to connect to it. It is faster and more secure than the Type 1 driver, but it is platform-dependent and requires the native library to be installed on the client machine.
  - Type 3: Network Protocol Driver. This driver uses a middleware server to connect to the database. The middleware server converts the JDBC calls into the protocol of the database and forwards them to the database server. This driver is platform-independent and scalable, but it adds an extra layer of complexity and network overhead.
  - Type 4: Thin Driver. This driver uses the network protocol of the database to connect to it directly. It is the most efficient and flexible driver, as it does not require any additional software or configuration on the client or the server side. However, it may not support all the features of the database.
- To use JDBC in a Java application, the following steps are required:
  - Load the JDBC driver class using the `Class.forName()` method. This registers the driver with the `DriverManager` class, which manages the available drivers.
  - Create a connection object using the `DriverManager.getConnection()` method. This method takes a database connection URL, which specifies the location and name of the database, and optionally a username and password for authentication. The connection object represents a physical connection to the database.
  - Create a statement object using the `Connection.createStatement()` method. This object is used to execute SQL queries and commands on the database.
  - Execute the query or command using the `Statement.executeQuery()` or `Statement.executeUpdate()` method. The former returns a `ResultSet` object, which contains the data returned by the query. The latter returns an `int` value, which indicates the number of rows affected by the command.
  - Process the results using the `ResultSet` methods, such as `next()`, `getString()`, `getInt()`, etc. These methods allow accessing the data in each row and column of the result set.
  - Close the resources using the `close()` method of the `ResultSet`, `Statement`, and `Connection` objects. This releases the resources and prevents memory leaks and database locks.

- A simple example of using JDBC to connect to a MySQL database and execute a query is shown below:

```java
// Load the JDBC driver class
Class.forName("com.mysql.cj.jdbc.Driver");

// Create a connection object
String url = "jdbc:mysql://localhost:3306/testdb";
String user = "root";
String password = "root";
Connection con = DriverManager.getConnection(url, user, password);

// Create a statement object
Statement stmt = con.createStatement();

// Execute a query
String sql = "SELECT * FROM employees";
ResultSet rs = stmt.executeQuery(sql);

// Process the results
while (rs.next()) {
  int id = rs.getInt("id");
  String name = rs.getString("name");
  double salary = rs.getDouble("salary");
  System.out.println(id + "\t" + name + "\t" + salary);
}

// Close the resources
rs.close();
stmt.close();
con.close();
```

- Some mnemonics and learning tricks for JDBC are:

  - JDBC stands for Java Database Connectivity, which reminds us that it is a Java API for connecting to databases.
  - The four types of JDBC drivers can be remembered by the acronym BNNP, which stands for Bridge, Native, Network, and Protocol. Alternatively