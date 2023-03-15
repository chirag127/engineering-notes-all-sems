### Java Database Connectivity (JDBC)

Java Database Connectivity (JDBC) is an application programming interface (API) for the programming language Java, which defines how a client may access a database. It is a Java-based data access technology used for Java database connectivity. It is part of the Java Standard Edition platform, from Oracle Corporation.

- **JDBC Architecture**: JDBC architecture consists of two layers: the JDBC API, which provides the application-to-JDBC Manager connection, and the JDBC Driver API, which supports the JDBC Manager-to-Driver Connection.
- **JDBC Drivers**: There are four types of JDBC drivers: JDBC-ODBC bridge driver, Native-API driver, Network Protocol driver, and Thin driver.
- **JDBC API**: The JDBC API provides a set of interfaces and classes for writing database applications in Java by making database connections. Some of the important interfaces and classes in JDBC API are: `DriverManager`, `Connection`, `Statement`, `PreparedStatement`, `CallableStatement`, `ResultSet`, and `SQLException`.
- **JDBC Connections**: To connect to a database using JDBC, you need to first register the appropriate JDBC driver, then create a connection object by calling the `DriverManager.getConnection()` method with the appropriate connection parameters (URL, username, password).
- **JDBC Statements**: JDBC provides three types of statements: `Statement`, `PreparedStatement`, and `CallableStatement`. `Statement` is used for general-purpose access to the database, `PreparedStatement` is used for executing precompiled SQL statements, and `CallableStatement` is used for executing stored procedures.
- **JDBC Transactions**: JDBC supports transactions, which allow multiple SQL statements to be executed as a single atomic unit. Transactions are managed using the `Connection` object's `setAutoCommit()`, `commit()`, and `rollback()` methods.
