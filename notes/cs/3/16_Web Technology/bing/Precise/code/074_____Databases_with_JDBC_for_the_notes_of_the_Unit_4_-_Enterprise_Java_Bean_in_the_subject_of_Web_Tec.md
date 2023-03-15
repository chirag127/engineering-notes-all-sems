### Databases with JDBC for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

1. **JDBC (Java Database Connectivity)** is an API that allows Java programs to access and manipulate data stored in relational databases.
2. JDBC provides a standard interface for accessing databases, allowing developers to write database applications that are portable across different database management systems.
3. To use JDBC, a developer must first obtain a JDBC driver for the specific database management system they wish to use. The driver is responsible for translating the JDBC API calls into the specific commands understood by the database.
4. Once the driver is installed, a developer can use the JDBC API to establish a connection to the database, execute SQL statements, and retrieve results.
5. The JDBC API provides several classes and interfaces for working with databases, including the `Connection`, `Statement`, `PreparedStatement`, `CallableStatement`, and `ResultSet` classes.
6. The `Connection` class represents a connection to a database. It provides methods for creating `Statement` objects, which can be used to execute SQL statements.
7. The `Statement` class represents a SQL statement. It provides methods for executing SQL statements and retrieving results.
8. The `PreparedStatement` class is a subclass of `Statement` that represents a precompiled SQL statement. It can improve performance when executing the same statement multiple times with different parameters.
9. The `CallableStatement` class is a subclass of `PreparedStatement` that represents a call to a stored procedure in the database.
10. The `ResultSet` class represents the results of a database query. It provides methods for navigating the results and retrieving data.
