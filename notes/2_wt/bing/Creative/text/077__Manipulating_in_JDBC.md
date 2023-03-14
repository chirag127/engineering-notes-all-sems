#### Manipulating in JDBC

- JDBC stands for Java Database Connectivity, which is an API that allows Java programs to communicate with databases and manipulate their data.
- JDBC uses drivers that enable the Java application to connect to a specific database. There are different types of drivers for different databases, such as Oracle, MySQL, PostgreSQL, etc.
- JDBC provides classes and interfaces that represent the components of a database connection, such as Connection, Statement, ResultSet, PreparedStatement, CallableStatement, etc.
- JDBC also provides methods for executing SQL statements, retrieving and updating data, handling transactions, and managing metadata.
- JDBC supports different types of ResultSet objects, which are tables of data that represent the results of executed queries. ResultSet objects have different characteristics, such as type, concurrency, and cursor holdability, that determine their functionality and behavior.
- JDBC allows the manipulation of data in a database through various methods, such as:
  - Inserting rows in a ResultSet object or directly in the database using the executeUpdate method of a Statement object.
  - Updating rows in a ResultSet object using the updateXXX methods and the updateRow method, or directly in the database using the executeUpdate method of a Statement object.
  - Deleting rows in a ResultSet object using the deleteRow method, or directly in the database using the executeUpdate method of a Statement object.
  - Batch updating, which is the process of sending multiple SQL statements to the database as a single unit, using the addBatch and executeBatch methods of a Statement object.
- JDBC also provides methods for retrieving data from a database, such as:
  - Retrieving column values from rows in a ResultSet object using the getXXX methods, where XXX corresponds to the data type of the column.
  - Retrieving metadata from a ResultSet object using the getMetaData method, which returns a ResultSetMetaData object that contains information about the columns, such as name, type, size, etc.
  - Retrieving metadata from a database using the getMetaData method of a Connection object, which returns a DatabaseMetaData object that contains information about the database, such as name, version, supported features, etc.