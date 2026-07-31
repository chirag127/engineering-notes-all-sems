#### Manipulating in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to communicate with databases and manipulate their data.
- JDBC is mainly used with relational databases, but it can also work with any other data sources that have a tabular structure, such as spreadsheets or flat files.
- To manipulate data in a database using JDBC, you need to follow these steps:
  1. Load the JDBC driver class that corresponds to the database you want to connect to. For example, if you want to connect to an Oracle database, you need to load the `oracle.jdbc.driver.OracleDriver` class. You can do this by using the `Class.forName()` method or by using the `DriverManager.registerDriver()` method.
  2. Establish a connection to the database by using the `DriverManager.getConnection()` method. You need to provide the URL of the database, the username and the password as parameters. For example, if you want to connect to an Oracle database with the username `scott` and the password `tiger`, you can use the following URL: `jdbc:oracle:thin:@localhost:1521:orcl`.
  3. Create a statement object by using the `Connection.createStatement()` method. A statement object is used to execute SQL queries or commands on the database. There are three types of statements: `Statement`, `PreparedStatement` and `CallableStatement`. The `Statement` object is used for simple SQL statements that do not have parameters. The `PreparedStatement` object is used for SQL statements that have parameters, which can be set by using the `setXXX()` methods. The `CallableStatement` object is used for calling stored procedures or functions in the database.
  4. Execute the statement by using the `Statement.execute()`, `Statement.executeQuery()` or `Statement.executeUpdate()` methods. The `execute()` method returns a boolean value indicating whether the statement returns a result set or not. The `executeQuery()` method returns a `ResultSet` object, which contains the data returned by the query. The `executeUpdate()` method returns an int value, which indicates the number of rows affected by the update, insert or delete statement.
  5. Process the result set by using the `ResultSet` methods. A result set is a cursor that points to the current row of data. You can move the cursor by using the `next()`, `previous()`, `first()`, `last()`, `absolute()` or `relative()` methods. You can retrieve the data from the current row by using the `getXXX()` methods, where XXX is the data type of the column. For example, if you want to get the value of the first column as a string, you can use the `getString(1)` method.
  6. Close the statement and the connection by using the `Statement.close()` and `Connection.close()` methods. This will release the resources and prevent memory leaks.

- Here is an example of manipulating data in an Oracle database using JDBC:

```java
// Load the Oracle JDBC driver
Class.forName("oracle.jdbc.driver.OracleDriver");

// Establish a connection to the database
Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl", "scott", "tiger");

// Create a statement object
Statement stmt = conn.createStatement();

// Execute a query to get all the employees from the EMP table
ResultSet rs = stmt.executeQuery("SELECT * FROM EMP");

// Print the result set
while (rs.next()) {
  System.out.println(rs.getInt("EMPNO") + " " + rs.getString("ENAME") + " " + rs.getDouble("SAL"));
}

// Execute an update statement to increase the salary of employee 7369 by 10%
int rows = stmt.executeUpdate("UPDATE EMP SET SAL = SAL * 1.1 WHERE EMPNO = 7369");

// Print the number of rows affected
System.out.println("Rows updated: " + rows);

// Close the statement and the connection
stmt.close();
conn.close();
```

- Some mnemonics and learning tricks for manipulating data in JDBC are:

  - **L.E.C.S.E.P.C.**: Load driver, Establish connection, Create statement, Execute statement, Process result set, Close statement, Close connection.
  - **S.P.C.**: Statement, PreparedStatement, CallableStatement.
  - **E.E.E.**: Execute, ExecuteQuery, ExecuteUpdate.
  - **N.P.F.L.A.R.**: Next, Previous, First, Last, Absolute, Relative.
  - **G.S.I.D.B.F.C.**: GetString