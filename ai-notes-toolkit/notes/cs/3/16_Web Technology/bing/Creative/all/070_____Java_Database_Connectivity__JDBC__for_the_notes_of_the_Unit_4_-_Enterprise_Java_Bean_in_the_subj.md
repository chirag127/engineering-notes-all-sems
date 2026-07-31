# Java Database Connectivity (JDBC)

- JDBC is a Java API that allows Java applications to interact with various types of databases using a standard interface.
- JDBC provides methods for establishing a connection to a database, executing SQL statements, retrieving the results, and managing transactions.
- JDBC also defines a set of classes and interfaces that represent various database objects, such as Connection, Statement, ResultSet, PreparedStatement, CallableStatement, etc.
- JDBC supports different types of drivers that implement the JDBC interface and provide the connection to a specific database. The four types of drivers are:
  - JDBC-ODBC Bridge Driver: This driver uses the ODBC (Open Database Connectivity) driver to connect to the database. It is not recommended for production use as it is platform-dependent and has performance issues.
  - Native Driver: This driver uses the native library of the database to connect to the database. It is also platform-dependent and requires the installation of the native library on the client machine.
  - Network Protocol Driver: This driver uses a network protocol to communicate with the database server. It is platform-independent and does not require any native library on the client machine. However, it requires a middleware server that translates the JDBC calls into the database-specific protocol.
  - Thin Driver: This driver is a pure Java driver that directly communicates with the database server using the database-specific protocol. It is platform-independent and does not require any middleware server or native library on the client machine. It is the most preferred driver for JDBC applications.
- The steps to connect to a database using JDBC are:
  - Load the JDBC driver class using the Class.forName() method.
  - Obtain a Connection object using the DriverManager.getConnection() method with the appropriate JDBC URL, username, and password.
  - Create a Statement, PreparedStatement, or CallableStatement object using the Connection.createStatement(), Connection.prepareStatement(), or Connection.prepareCall() method respectively.
  - Execute the SQL statement using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() method depending on the type of statement.
  - Process the results using the ResultSet object if the statement returns a result set, or the Statement.getUpdateCount() method if the statement returns an update count.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods in the reverse order of their creation.
- The JDBC URL is a string that specifies the location and name of the database, and optionally some parameters for the connection. The format of the JDBC URL depends on the type of driver and database. For example, the JDBC URL for connecting to a Java DB database using the Embedded Driver is:

  `jdbc:derby:testdb;create=true`

  where testdb is the name of the database to connect to, and create=true instructs the DBMS to create the database if it does not exist.