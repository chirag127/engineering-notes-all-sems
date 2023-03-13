#### Manipulating in JDBC

JDBC stands for Java Database Connectivity, which is an API that allows Java programs to communicate with databases and manipulate their data. JDBC supports various types of databases, but it is mainly used with relational databases.

To manipulate data in a database using JDBC, you need to follow these steps:

- Load the JDBC driver class that corresponds to the database you want to use. For example, for Oracle database, you need to load the oracle.jdbc.driver.OracleDriver class. You can use the Class.forName() method to load the driver class.
- Establish a connection to the database using the DriverManager.getConnection() method. You need to provide the URL, username and password of the database as parameters. For example, for Oracle database, the URL format is jdbc:oracle:thin:@host:port:SID.
- Create a Statement object using the Connection.createStatement() method. A Statement object allows you to execute SQL statements against the database.
- Execute the SQL statement using the Statement.execute(), Statement.executeQuery() or Statement.executeUpdate() methods. The execute() method returns a boolean value indicating whether the statement returns a ResultSet object or not. The executeQuery() method returns a ResultSet object that contains the data retrieved from the database. The executeUpdate() method returns an int value indicating the number of rows affected by the statement.
- Process the ResultSet object if the statement returns one. A ResultSet object represents a table of data that can be accessed by column name or index. You can use the ResultSet.next() method to move the cursor to the next row and the ResultSet.getXXX() methods to retrieve the values of the columns. For example, ResultSet.getString(1) returns the value of the first column as a String.
- Close the ResultSet, Statement and Connection objects using the close() methods. This releases the resources and prevents memory leaks.

Here is an example of manipulating data in an Oracle database using JDBC:

```java
// Load the Oracle JDBC driver
Class.forName("oracle.jdbc.driver.OracleDriver");

// Connect to the database
Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "scott", "tiger");

// Create a statement
Statement stmt = conn.createStatement();

// Execute a query
ResultSet rs = stmt.executeQuery("SELECT * FROM emp");

// Process the result set
while (rs.next()) {
  // Print the employee name and salary
  System.out.println(rs.getString("ename") + " " + rs.getInt("sal"));
}

// Close the result set, statement and connection
rs.close();
stmt.close();
conn.close();
```