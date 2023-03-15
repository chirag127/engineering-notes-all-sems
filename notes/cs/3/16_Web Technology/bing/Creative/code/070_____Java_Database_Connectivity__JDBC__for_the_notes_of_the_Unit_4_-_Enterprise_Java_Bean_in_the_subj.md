# Java Database Connectivity (JDBC)

- JDBC is a Java API that allows Java applications to interact with various types of databases using a standard interface.
- JDBC provides methods for establishing a connection to a database, executing SQL statements, retrieving the results, and managing transactions.
- JDBC also defines a set of classes and interfaces that represent different data types, exceptions, and metadata objects.
- JDBC supports four types of drivers that differ in how they communicate with the database server:
  - JDBC-ODBC Bridge Driver: This driver uses the ODBC (Open Database Connectivity) API to connect to any database that has an ODBC driver. This driver is platform-dependent and requires an ODBC installation on the client machine.
  - Native Driver: This driver uses the native library of the database vendor to connect to the database. This driver is also platform-dependent and requires the native library to be installed on the client machine.
  - Network Protocol Driver: This driver uses a network protocol (such as TCP/IP) to communicate with a middleware server that in turn communicates with the database server. This driver is platform-independent but requires the middleware server to be installed and configured.
  - Thin Driver: This driver uses a network protocol (such as HTTP) to communicate directly with the database server. This driver is platform-independent and does not require any additional software on the client machine.
- The basic steps to use JDBC in a Java application are:
  - Load the JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method. This method returns a Connection object that represents the database connection.
  - Create a Statement object using the Connection.createStatement() method. This object is used to execute SQL statements.
  - Execute the SQL statement using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() methods. These methods return different types of objects depending on the type of SQL statement.
  - Process the results using the ResultSet object for queries, or the int value for updates. The ResultSet object provides methods to access the data in each row and column of the result set.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods. This releases the resources and avoids memory leaks.
- The following code snippet shows an example of using JDBC to connect to a MySQL database and execute a simple query:

```java
// Load the JDBC driver
Class.forName("com.mysql.jdbc.Driver");

// Establish a connection
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

// Create a statement
Statement stmt = conn.createStatement();

// Execute a query
ResultSet rs = stmt.executeQuery("SELECT * FROM employees");

// Process the result set
while (rs.next()) {
  // Get the data from each column using the column name or index
  int id = rs.getInt("id");
  String name = rs.getString("name");
  double salary = rs.getDouble(3);
  // Print the data
  System.out.println(id + "\t" + name + "\t" + salary);
}

// Close the resources
rs.close();
stmt.close();
conn.close();
```