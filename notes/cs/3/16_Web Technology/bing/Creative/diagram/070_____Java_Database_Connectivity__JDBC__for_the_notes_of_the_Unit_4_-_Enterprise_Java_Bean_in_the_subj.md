### Java Database Connectivity (JDBC)

- JDBC is a Java API that allows Java applications to interact with various types of databases using a standard interface.
- JDBC provides methods for establishing a connection to a database, executing SQL statements, retrieving the results, and managing transactions.
- JDBC also defines a set of classes and interfaces that represent different data types, exceptions, and metadata objects.
- JDBC supports four types of drivers that differ in how they communicate with the database server:
  - JDBC-ODBC Bridge Driver: This driver uses the ODBC (Open Database Connectivity) API to connect to any database that supports ODBC. This driver is platform-dependent and requires an ODBC driver to be installed on the client machine.
  - Native Driver: This driver uses the native library of the database to connect to the database. This driver is also platform-dependent and requires the native library to be available on the client machine.
  - Network Protocol Driver: This driver uses a network protocol (such as TCP/IP) to communicate with the database server. This driver is platform-independent but requires a server-side component to translate the network protocol to the database protocol.
  - Thin Driver: This driver is a pure Java driver that uses the database protocol directly to communicate with the database server. This driver is platform-independent and does not require any additional software on the client or server side.
- To use JDBC, the following steps are required:
  - Load the JDBC driver class using the Class.forName() method.
  - Create a Connection object using the DriverManager.getConnection() method with the appropriate JDBC URL, username, and password.
  - Create a Statement, PreparedStatement, or CallableStatement object using the Connection.createStatement(), Connection.prepareStatement(), or Connection.prepareCall() method respectively.
  - Execute the SQL statement using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() method depending on the type of statement.
  - Process the results using the ResultSet object returned by the Statement.executeQuery() method or the update count returned by the Statement.executeUpdate() method.
  - Close the resources using the ResultSet.close(), Statement.close(), and Connection.close() methods.