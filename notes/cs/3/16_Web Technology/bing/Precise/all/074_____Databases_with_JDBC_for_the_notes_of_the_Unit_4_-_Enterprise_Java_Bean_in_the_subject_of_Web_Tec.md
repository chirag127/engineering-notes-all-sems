# Databases with JDBC

JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data stored in relational databases. It is part of the Java Standard Edition platform and provides a standard interface for connecting to databases, executing SQL statements, and retrieving results.

Here are some key points to remember when working with databases and JDBC:

1. JDBC drivers: To connect to a database, you need a JDBC driver that is specific to the database management system you are using. The driver acts as a bridge between the Java program and the database, translating JDBC calls into database-specific commands.

2. Connection: To access a database, you need to establish a connection to it using the `DriverManager` class. You provide the database URL, username, and password, and the `DriverManager` returns a `Connection` object that represents the connection to the database.

3. Statements: Once you have a connection to the database, you can create `Statement` objects to execute SQL commands. There are three types of statements: `Statement`, `PreparedStatement`, and `CallableStatement`. Each has its own methods for executing SQL commands and retrieving results.

4. ResultSets: When you execute a query, the results are returned in a `ResultSet` object. You can iterate through the rows of the `ResultSet` and retrieve the values of each column using the appropriate `get` method.

5. Transactions: By default, JDBC automatically commits each SQL statement as soon as it is executed. However, you can disable this behavior and manage transactions manually using the `setAutoCommit` method of the `Connection` object. This allows you to group multiple statements into a single transaction and either commit or rollback the entire transaction.

6. Exception handling: When working with JDBC, it is important to handle exceptions properly. SQLException is the base class for all exceptions thrown by JDBC. You can catch this exception and use its methods to get more information about the error that occurred.
