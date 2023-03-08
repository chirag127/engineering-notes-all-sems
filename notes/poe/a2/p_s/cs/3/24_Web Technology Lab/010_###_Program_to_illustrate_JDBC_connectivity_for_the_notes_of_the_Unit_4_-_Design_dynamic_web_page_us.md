 Here is the content in markdown format for the given topic:

### Program to illustrate JDBC connectivity

JDBC (Java Database Connectivity) is an API that allows Java programs to interact with a relational database. A JDBC program requires a JDBC driver to connect to a database. Here are the steps to connect to a database:

1. Import the java.sql package. This package contains the required classes and interfaces to connect to a database.
2. Load the JDBC driver. This is done by calling Class.forName() and passing it the driver class name. This loads the driver so that it can establish a connection with the database.
3. Get a database connection. This is done by calling DriverManager.getConnection() and passing it the database URL, username, and password.
4. Create a Statement object. This is done by calling the createStatement() method on the Connection object. The Statement object is used to execute SQL queries.
5. Execute the SQL query. This is done by calling the executeQuery() method on the Statement object and passing it the SQL query string.
6. Process the results. This is done by calling methods on the ResultSet object such as next() to iterate through rows and getString() to retrieve column values.
7. Close the connection. This is done by calling the close() method on the Connection object.

Advantages:
- It is independent of the database software. The same JDBC code can work with different databases by just changing the JDBC driver.
- It moves the database connectivity code out of the application code into the JDBC driver. This makes the application code database agnostic and more portable.
- It defines a standard API for SQL-based relational databases.

Disadvantages:
- There is a performance overhead due to the additional JDBC layer.
- Difficulty in handling database-specific features since JDBC aims to provide a common interface for all databases. Database-specific features may not have direct mappings to the JDBC API.

[Include diagrams and code snippets here if required]

Applications: JDBC is used to connect to databases from Java applications to execute SQL queries and process results. It allows Java programs to be database agnostic and more portable. Many other APIs are built on top of JDBC such as JPA and Hibernate which provide an object-relational mapping facility.