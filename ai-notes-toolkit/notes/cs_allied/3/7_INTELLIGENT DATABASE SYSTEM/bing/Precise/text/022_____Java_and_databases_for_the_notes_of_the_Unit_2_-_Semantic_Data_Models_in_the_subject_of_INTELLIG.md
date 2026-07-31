### Unit 2 - Semantic Data Models: Java and Databases

1. **Java Database Connectivity (JDBC)**: JDBC is an API for the Java programming language that defines how a client may access a database. It provides methods for querying and updating data in a database.

2. **JDBC Drivers**: JDBC drivers are used to connect to different types of databases. There are four types of JDBC drivers: Type 1 (JDBC-ODBC bridge), Type 2 (Native-API), Type 3 (Network-Protocol), and Type 4 (Thin).

3. **Connecting to a Database**: To connect to a database using JDBC, you need to first load the appropriate driver, then establish a connection using the `DriverManager.getConnection()` method.

4. **Executing SQL Statements**: Once a connection to the database has been established, you can execute SQL statements using the `Statement` or `PreparedStatement` objects.

5. **Retrieving Results**: After executing an SQL statement, you can retrieve the results using the `ResultSet` object.

6. **Closing Resources**: It is important to close all resources such as `Connection`, `Statement`, and `ResultSet` objects when you are finished using them to free up resources and prevent memory leaks.

7. **Transactions**: JDBC allows you to group a set of related database operations into a single transaction. This ensures that either all the operations are completed successfully, or none of them are applied.

8. **Error Handling**: When working with databases, it is important to handle errors and exceptions appropriately. JDBC provides several classes for handling SQL exceptions, including `SQLException` and `SQLWarning`.

9. **Java Persistence API (JPA)**: JPA is a specification for accessing, persisting, and managing data between Java objects and a relational database. It provides an object-relational mapping (ORM) approach to data management.

10. **Hibernate**: Hibernate is an ORM framework that implements the JPA specification. It provides a way to map Java objects to database tables and simplifies the development of Java applications that access relational databases.