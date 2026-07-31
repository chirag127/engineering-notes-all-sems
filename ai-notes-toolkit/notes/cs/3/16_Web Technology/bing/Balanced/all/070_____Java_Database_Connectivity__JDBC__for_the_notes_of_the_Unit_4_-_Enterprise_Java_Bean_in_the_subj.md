# Java Database Connectivity (JDBC)

- JDBC is a Java API that allows Java applications to interact with various types of databases using a standard interface.
- JDBC provides methods for establishing a connection to a database, executing SQL statements, retrieving the results, and managing transactions.
- JDBC also defines a set of classes and interfaces that represent various database objects, such as Connection, Statement, ResultSet, PreparedStatement, CallableStatement, etc.
- JDBC supports different types of drivers that implement the JDBC interface and communicate with different databases using different protocols.
- The four types of JDBC drivers are:
  - JDBC-ODBC Bridge Driver: This driver uses the ODBC driver installed on the client machine to connect to the database. It is not recommended for production use as it is platform-dependent and has performance issues.
  - Native Driver: This driver uses the native library of the database to connect to the database. It is also platform-dependent and requires the installation of the native library on the client machine.
  - Network Protocol Driver: This driver uses a network protocol to communicate with a middleware server that connects to the database. It is platform-independent but requires the installation and maintenance of the middleware server.
  - Thin Driver: This driver uses a network protocol to communicate directly with the database server. It is platform-independent and does not require any additional software on the client machine. It is the most widely used driver type.
- To use JDBC in a Java application, the following steps are required:
  - Load the JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method. This method returns a Connection object that represents the database connection.
  - Create a Statement object using the Connection.createStatement() method. This object is used to execute SQL statements.
  - Execute the SQL statement using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() methods. These methods return a boolean value, a ResultSet object, or an int value respectively, depending on the type of the SQL statement.
  - Process the results using the ResultSet object if the SQL statement is a query. The ResultSet object provides methods to access the data in each row and column of the result set.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods. This releases the resources and avoids memory leaks.