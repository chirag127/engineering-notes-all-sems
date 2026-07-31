### Java Database Connectivity (JDBC) for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- JDBC is a Java API that allows Java applications to interact with various types of databases using a standard interface.
- JDBC provides methods for establishing a connection to a database, executing SQL statements, retrieving the results, and managing transactions.
- JDBC also defines a set of classes and interfaces that implement the common database functionality, such as ResultSet, Statement, PreparedStatement, CallableStatement, Connection, DriverManager, etc.
- JDBC supports four types of drivers that differ in how they communicate with the database server:
  - Type 1: JDBC-ODBC Bridge Driver - This driver uses the ODBC driver installed on the client machine to connect to the database. It is not recommended for production use as it is platform-dependent and has performance issues.
  - Type 2: Native Driver - This driver uses the native library of the database vendor to connect to the database. It is also platform-dependent and requires the installation of the native library on the client machine.
  - Type 3: Network Protocol Driver - This driver uses a middleware server that converts JDBC calls into the database-specific protocol. It is platform-independent and can connect to multiple databases, but it adds an extra layer of network communication and may have compatibility issues with some databases.
  - Type 4: Thin Driver - This driver uses the database-specific protocol to connect directly to the database server. It is platform-independent and does not require any additional software on the client machine. It is the most recommended driver for JDBC applications.
- To use JDBC, the following steps are required:
  - Load the JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method, which returns a Connection object.
  - Create a Statement object from the Connection object, which can be used to execute SQL statements.
  - Execute the SQL statement using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() methods, which return a boolean value, a ResultSet object, or an int value respectively.
  - Process the results using the ResultSet object, which contains the data returned by the query. The ResultSet object has methods to move the cursor, get the column values, and check the metadata of the result set.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods, which release the database resources and prevent memory leaks.