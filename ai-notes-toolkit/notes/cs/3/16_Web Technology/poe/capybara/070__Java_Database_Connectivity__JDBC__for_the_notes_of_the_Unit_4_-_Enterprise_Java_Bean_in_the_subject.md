### Java Database Connectivity (JDBC)
#### Introduction
- JDBC stands for Java Database Connectivity. It is a Java API that enables Java programs to interact with a database.
- JDBC provides a standard interface for accessing relational databases, such as Oracle, MySQL, SQL Server, etc.
- JDBC allows the developer to write Java programs that can send SQL or PL/SQL commands to the database and receive results back from the database.

#### Architecture of JDBC
- JDBC architecture consists of two layers: the JDBC API layer and the JDBC driver layer.
- The JDBC API layer provides a set of interfaces and classes for the developer to interact with the database.
- The JDBC driver layer translates the JDBC API calls into database-specific calls, which will be executed by the database.
- There are four types of JDBC drivers: 
  - Type 1 driver (JDBC-ODBC bridge driver)
  - Type 2 driver (Native API driver)
  - Type 3 driver (Network Protocol driver)
  - Type 4 driver (Thin driver)

#### Steps to use JDBC
- Import the JDBC classes.
- Load the JDBC driver.
- Establish a connection to the database using the DriverManager class.
- Create a Statement object to send SQL commands to the database.
- Execute the SQL command using the Statement object.
- Retrieve the results using the ResultSet object.
- Close the database connection, statement, and result set.

#### JDBC API
- The JDBC API consists of several interfaces and classes, such as:
  - DriverManager: for managing JDBC drivers.
  - Connection: for establishing a connection to the database.
  - Statement: for executing SQL commands.
  - ResultSet: for retrieving the results of an SQL query.
  - PreparedStatement: for executing parameterized SQL commands.
  - CallableStatement: for executing stored procedures.
  - ResultSetMetaData: for retrieving metadata about a ResultSet.
  - SQLException: for handling exceptions.

#### Advantages of JDBC
- JDBC provides a standard API for accessing relational databases, which allows for platform independence.
- JDBC provides a simple and easy-to-use API for accessing databases.
- JDBC provides good performance by allowing the use of database-specific features, such as stored procedures and triggers.
- JDBC provides support for transaction management.

#### Disadvantages of JDBC
- JDBC code can be verbose and repetitive.
- JDBC requires the developer to write SQL commands, which can be error-prone.
- JDBC requires the developer to handle exceptions, which can be tedious.
- JDBC does not provide support for non-relational databases, such as NoSQL databases.