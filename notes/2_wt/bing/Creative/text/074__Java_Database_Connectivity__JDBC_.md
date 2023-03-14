### Java Database Connectivity (JDBC)

- JDBC is a Java API that provides universal data access from the Java programming language to various types of data sources, such as relational databases, spreadsheets, and flat files.
- JDBC also provides a common base for building tools and alternate interfaces for data access in Java.
- JDBC is part of the Java SE platform and consists of two packages: java.sql and javax.sql.
- To use JDBC with a specific database system, a JDBC driver is required. A JDBC driver is a software component that enables a Java application to interact with a database. There are four types of JDBC drivers: JDBC-ODBC bridge driver, native driver, network protocol driver, and thin driver.
- JDBC supports the following features :
  - Connecting to any data source that can be accessed by SQL queries.
  - Executing SQL statements and stored procedures on the data source.
  - Retrieving and updating data from the data source using ResultSet and PreparedStatement objects.
  - Performing transactions and managing concurrency on the data source using Connection and Statement objects.
  - Obtaining metadata information about the data source, such as tables, columns, indexes, etc. using DatabaseMetaData and ResultSetMetaData objects.
  - Using RowSet objects to manipulate data in a tabular format that is disconnected from the data source.
  - Using JDBC 4.2 features, such as REF_CURSOR support, large update counts, and SQLType interface.
- JDBC is based on the X/Open SQL Call Level Interface and follows a standard specification. The current version of JDBC is 4.3, which is the stable release since September 2017.