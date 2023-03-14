### Java Database Connectivity (JDBC)

- JDBC is a Java API that provides universal data access from the Java programming language to various types of data sources, such as relational databases, spreadsheets, and flat files.
- JDBC is part of the Java Standard Edition (Java SE) platform and consists of two packages: `java.sql` and `javax.sql`.
- JDBC uses JDBC drivers to communicate with different data sources. Each data source requires a specific JDBC driver that implements the JDBC interfaces and classes.
- There are four types of JDBC drivers: JDBC-ODBC Bridge Driver, Native Driver, Network Protocol Driver, and Thin Driver. Each type has its own advantages and disadvantages in terms of performance, portability, and security.
- To use JDBC, a Java application needs to perform the following steps:
  - Load the JDBC driver class using the `Class.forName()` method or the `DriverManager.registerDriver()` method.
  - Establish a connection to the data source using the `DriverManager.getConnection()` method or the `DataSource.getConnection()` method.
  - Create a statement object using the `Connection.createStatement()`, `Connection.prepareStatement()`, or `Connection.prepareCall()` method.
  - Execute a query or an update using the `Statement.executeQuery()`, `Statement.executeUpdate()`, or `Statement.execute()` method.
  - Process the result set (if any) using the `ResultSet` object and its methods, such as `ResultSet.next()`, `ResultSet.getInt()`, `ResultSet.getString()`, etc.
  - Close the resources (result set, statement, and connection) using the `close()` method.
- JDBC provides various interfaces and classes to handle different types of data and operations, such as `SQLType`, `JDBCType`, `Blob`, `Clob`, `Array`, `Ref`, `RowId`, `NClob`, `SQLXML`, `Struct`, `BatchUpdateException`, `SQLWarning`, etc.
- JDBC also supports advanced features, such as transactions, metadata, row sets, connection pooling, distributed transactions, savepoints, scrollable and updatable result sets, etc.
- JDBC is based on the X/Open SQL Call Level Interface and follows the SQL standard for data manipulation and query syntax.
- JDBC is a widely used technology for Java database connectivity and provides a common base for developing database applications and tools in Java.