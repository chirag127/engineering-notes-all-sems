### Java Database Connectivity (JDBC)

JDBC is an API that allows Java programs to interact with various types of databases. To establish a JDBC connection, you need to do the following steps:

1. Load the JDBC driver class that corresponds to the database you want to connect to. You can use the `Class.forName()` method or the `DriverManager.registerDriver()` method to load the driver class. For example, to load the Oracle driver, you can use one of the following statements :

```java
Class.forName("oracle.jdbc.driver.OracleDriver");
// or
DriverManager.registerDriver(new oracle.jdbc.driver.OracleDriver());
```

2. Create a connection object that represents the connection to the database. You can use the `DriverManager.getConnection()` method to create a connection object. You need to pass a database URL, a username, and a password as parameters to this method. The database URL specifies the type of database, the host name, the port number, and the database name. For example, to connect to a MySQL database named testdb on localhost with port 3306, you can use the following statement :

```java
Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/testdb", "root", "password");
```

3. Create a statement object that allows you to execute SQL queries on the database. You can use the `Connection.createStatement()` method to create a statement object. For example, to create a statement object from the connection object con, you can use the following statement:

```java
Statement stmt = con.createStatement();
```

4. Execute the SQL query using the statement object and get the result set. You can use the `Statement.executeQuery()` method to execute a SQL query that returns a result set, such as a SELECT query. You can use the `Statement.executeUpdate()` method to execute a SQL query that does not return a result set, such as an INSERT, UPDATE, or DELETE query. For example, to execute a SELECT query that returns all the records from a table named employees, you can use the following statement:

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM employees");
```

5. Process the result set using the methods of the `ResultSet` class. You can use the `ResultSet.next()` method to move the cursor to the next row of the result set. You can use the `ResultSet.getXXX()` methods to get the values of the columns in the current row, where XXX is the data type of the column. For example, to print the values of the columns id, name, and salary from the result set rs, you can use the following loop:

```java
while (rs.next()) {
  int id = rs.getInt("id");
  String name = rs.getString("name");
  double salary = rs.getDouble("salary");
  System.out.println(id + " " + name + " " + salary);
}
```

6. Close the result set, the statement, and the connection objects using the `close()` method. This releases the resources and avoids memory leaks. For example, to close the result set rs, the statement stmt, and the connection con, you can use the following statements:

```java
rs.close();
stmt.close();
con.close();
```