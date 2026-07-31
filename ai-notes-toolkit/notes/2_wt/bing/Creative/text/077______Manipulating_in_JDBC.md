#### Manipulating in JDBC

- JDBC stands for Java Database Connectivity, which is an API for connecting and executing queries on databases from Java applications.
- JDBC uses drivers to communicate with different types of databases, such as Oracle, MySQL, PostgreSQL, etc.
- JDBC allows Java applications to manipulate data in databases using SQL statements, such as SELECT, INSERT, UPDATE, DELETE, etc.
- JDBC provides classes and interfaces to perform various operations on databases, such as:
  - Establishing a connection to a database using the DriverManager or DataSource classes.
  - Creating and executing statements using the Statement, PreparedStatement, or CallableStatement classes.
  - Retrieving and processing the results of executed queries using the ResultSet class.
  - Handling exceptions and errors using the SQLException class.
  - Managing transactions and isolation levels using the Connection class.
  - Using batch updates and stored procedures for improved performance and functionality.
  - Using metadata to obtain information about the database structure and capabilities using the DatabaseMetaData and ResultSetMetaData classes.
  - Using advanced features such as scrollable and updatable result sets, rowsets, blobs, clobs, etc. using the JDBC 2.0 and JDBC 3.0 APIs.