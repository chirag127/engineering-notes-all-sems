#### Databases with JDBC in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to interact with various types of databases.
- JDBC provides a standard interface for connecting to different databases, executing SQL statements, retrieving results, and handling errors.
- JDBC consists of two main components: the JDBC driver and the JDBC API.
- The JDBC driver is a software module that implements the JDBC interface for a specific database. It acts as a bridge between the Java program and the database server. Different databases require different drivers, which can be downloaded from the database vendor's website or included in the Java Development Kit (JDK).
- The JDBC API is a set of classes and interfaces that define the methods and constants for accessing and manipulating data using JDBC. The JDBC API is part of the java.sql and javax.sql packages in the JDK.
- To use JDBC, a Java program needs to perform the following steps:
  - Load the JDBC driver class using the Class.forName() method.
  - Establish a connection to the database using the DriverManager.getConnection() method, which returns a Connection object.
  - Create a Statement object from the Connection object, which can be used to execute SQL queries or updates.
  - Execute the SQL statement using the Statement.execute(), Statement.executeQuery(), or Statement.executeUpdate() methods, which return a boolean value, a ResultSet object, or an int value, respectively.
  - Process the results using the ResultSet object, which contains the data returned by the query. The ResultSet object has methods to move the cursor, get the column values, and check the metadata of the result set.
  - Close the resources using the Statement.close(), ResultSet.close(), and Connection.close() methods, which release the memory and database resources associated with them.