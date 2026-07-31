#### Databases with JDBC

JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases. JDBC provides a standard set of interfaces and classes that enable database operations such as creating, updating, deleting, and querying data.

To use JDBC, you need to follow these steps:

1. Load the JDBC driver class that corresponds to the database you want to connect to. For example, if you want to connect to MySQL, you need to load the `com.mysql.cj.jdbc.Driver` class. You can do this by calling the `Class.forName()` method with the driver class name as a parameter.
2. Establish a connection to the database using the `DriverManager.getConnection()` method. This method takes a connection URL, a username, and a password as parameters. The connection URL specifies the protocol, host, port, and database name of the database server. For example, a connection URL for MySQL might look like this: `jdbc:mysql://localhost:3306/testdb`.
3. Create a `Statement` object from the connection object. A `Statement` object allows you to execute SQL statements against the database. You can create a `Statement` object by calling the `Connection.createStatement()` method.
4. Execute the SQL statement using the `Statement` object. Depending on the type of SQL statement, you can use different methods of the `Statement` object. For example, if you want to execute a query that returns a result set, you can use the `Statement.executeQuery()` method. If you want to execute an update statement that modifies the data, you can use the `Statement.executeUpdate()` method.
5. Process the result set or the update count returned by the `Statement` object. A result set is a collection of rows that match the query criteria. You can access the result set using a `ResultSet` object, which provides methods to move the cursor and get the values of each column. An update count is an integer that indicates how many rows were affected by the update statement. You can get the update count using the `Statement.getUpdateCount()` method.
6. Close the result set, the statement, and the connection objects. This is important to release the resources and avoid memory leaks. You can close these objects by calling their `close()` methods.

Here is an example of a JDBC program that creates a table in a MySQL database and inserts some data into it:

```java
// Load the MySQL JDBC driver
Class.forName("com.mysql.cj.jdbc.Driver");

// Establish a connection to the database
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");

// Create a statement object
Statement stmt = conn.createStatement();

// Execute a SQL statement to create a table
String sql = "CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(50), age INT)";
stmt.executeUpdate(sql);

// Execute a SQL statement to insert some data
sql = "INSERT INTO students VALUES (1, 'Alice', 20), (2, 'Bob', 21), (3, 'Charlie', 19)";
stmt.executeUpdate(sql);

// Close the statement and the connection
stmt.close();
conn.close();
```