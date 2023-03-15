### Program to illustrate JDBC connectivity

JDBC stands for Java Database Connectivity, which is a standard Java API for connecting to relational databases. JDBC allows a Java program to execute SQL statements and retrieve the results from a database server.

To use JDBC, a Java program needs to do the following steps:

1. Load the JDBC driver class that corresponds to the type of database server. For example, to connect to a MySQL database, the driver class is `com.mysql.jdbc.Driver`. The driver class can be loaded by using the `Class.forName()` method, which registers the driver with the `DriverManager` class.
2. Obtain a connection object from the `DriverManager` class by passing the connection URL, the user name and the password. The connection URL specifies the protocol, the host name, the port number, the database name and other parameters for connecting to the database server. For example, the connection URL for a MySQL database is `jdbc:mysql://localhost:3306/test`, where `localhost` is the host name, `3306` is the port number and `test` is the database name.
3. Create a statement object from the connection object by using the `createStatement()` method. A statement object allows the Java program to execute SQL statements on the database server.
4. Execute the SQL statement by using the `executeQuery()` method for queries that return a result set, or the `executeUpdate()` method for queries that modify the database. The result set object contains the data returned by the query, and can be accessed by using the `next()` and the `getXXX()` methods, where `XXX` is the data type of the column. The execute update method returns an integer value indicating the number of rows affected by the query.
5. Close the statement object and the connection object by using the `close()` method. This releases the resources used by the JDBC objects and closes the connection to the database server.

The following code snippet shows an example of a Java program that connects to a MySQL database and executes a simple query:

```java
// Load the JDBC driver
Class.forName("com.mysql.jdbc.Driver");

// Obtain a connection
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "password");

// Create a statement
Statement stmt = con.createStatement();

// Execute a query
ResultSet rs = stmt.executeQuery("SELECT * FROM students");

// Process the result set
while (rs.next()) {
  // Get the data from each column
  int id = rs.getInt("id");
  String name = rs.getString("name");
  int age = rs.getInt("age");
  // Print the data
  System.out.println(id + " " + name + " " + age);
}

// Close the statement and the connection
stmt.close();
con.close();
```