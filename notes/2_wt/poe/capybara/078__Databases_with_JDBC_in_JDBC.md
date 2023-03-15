#### Databases with JDBC in JDBC

- JDBC stands for Java Database Connectivity, a Java API that allows Java programs to interact with databases.
- JDBC provides a standard interface for accessing different types of databases, such as Oracle, MySQL, PostgreSQL, SQL Server, and more.
- To use JDBC, we need to download and install a JDBC driver for the specific database we want to connect to.
- JDBC drivers are usually provided by the database vendors and can be downloaded from their websites.
- To connect to a database using JDBC, we need to follow the following steps:
  1. Load the JDBC driver class using `Class.forName()` method.
  2. Create a connection object using `DriverManager.getConnection()` method.
  3. Create a statement object using the `connection.createStatement()` method.
  4. Execute SQL queries using the `statement.executeQuery()` or `statement.executeUpdate()` method.
  5. Process the result set returned by the SQL query using the `ResultSet` class.
  6. Close the connection and statement objects using the `close()` method.

- JDBC provides different types of statements for executing SQL queries:
  1. Statement: for executing static SQL queries, which do not contain any input parameters or variables.
  2. PreparedStatement: for executing dynamic SQL queries, which contain input parameters or variables. This type of statement is pre-compiled and can be reused multiple times with different input values.
  3. CallableStatement: for executing stored procedures, which are pre-defined database functions or procedures that can be called from Java programs.

- JDBC also provides support for transactions, which allow multiple SQL statements to be executed as a single unit of work. Transactions ensure data consistency and integrity by rolling back changes if any of the statements fail to execute.

- In addition to the basic JDBC API, there are also higher-level database access frameworks available for Java, such as Hibernate and Spring Data, which provide more advanced features and abstractions for working with databases.