### Databases with JDBC for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

1. JDBC (Java Database Connectivity) is an API that allows Java programs to access and manipulate data stored in relational databases.
2. JDBC provides a standard interface for connecting to databases, executing SQL statements, and retrieving results.
3. To use JDBC, a JDBC driver for the specific database management system must be installed and configured.
4. JDBC drivers are available for most popular relational database management systems, including MySQL, Oracle, and Microsoft SQL Server.
5. The basic steps for using JDBC to access a database are:
    1. Load the JDBC driver.
    2. Establish a connection to the database.
    3. Create a statement object to execute SQL queries.
    4. Execute the SQL query and retrieve the results.
    5. Process the results.
    6. Close the connection to the database.
6. JDBC provides several classes and interfaces for working with databases, including:
    1. `DriverManager`: A class that manages the JDBC drivers installed on the system.
    2. `Connection`: An interface that represents a connection to a database.
    3. `Statement`: An interface that represents a SQL statement.
    4. `ResultSet`: An interface that represents the results of a SQL query.
    5. `SQLException`: An exception class for handling errors that occur when working with databases.
7. Enterprise Java Beans (EJB) is a server-side component architecture for building distributed, scalable, and secure enterprise applications.
8. EJBs can be used to access and manipulate data stored in databases using JDBC.
9. EJBs provide a higher level of abstraction for working with databases, allowing developers to focus on business logic rather than the details of database access.
10. EJBs can be used in conjunction with other Java EE technologies, such as JPA (Java Persistence API), to provide a complete solution for building enterprise applications that access and manipulate data stored in databases.