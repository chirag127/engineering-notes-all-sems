### Java Database Connectivity (JDBC)

- JDBC is an API (Application Programming Interface) that allows Java programs to interact with databases .
- JDBC provides a common interface for different types of databases, such as relational, spreadsheet, or flat file .
- JDBC consists of two components: a JDBC driver and a JDBC API.
- A JDBC driver is a software module that implements the JDBC interface for a specific database. It enables the Java program to communicate with the database using the native protocol of the database .
- A JDBC API is a set of classes and interfaces that define the methods and constants for accessing and manipulating data in a database. It includes classes such as Connection, Statement, ResultSet, PreparedStatement, CallableStatement, etc .
- To use JDBC, a Java program needs to perform the following steps  :
  - Load the JDBC driver class using the Class.forName() method or the DriverManager.registerDriver() method.
  - Establish a connection to the database using the DriverManager.getConnection() method or the DataSource.getConnection() method. A connection object represents a session with the database.
  - Create a statement object using the Connection.createStatement() method or the Connection.prepareStatement() method or the Connection.prepareCall() method. A statement object represents a SQL query or command to be executed on the database.
  - Execute the statement using the Statement.execute() method or the Statement.executeQuery() method or the Statement.executeUpdate() method. A result set object represents the data returned by the query. An update count represents the number of rows affected by the command.
  - Process the result set or the update count using the ResultSet methods or the Statement.getUpdateCount() method. A result set cursor points to the current row of data in the result set.
  - Close the result set, the statement, and the connection using the ResultSet.close() method, the Statement.close() method, and the Connection.close() method. This releases the resources associated with them.