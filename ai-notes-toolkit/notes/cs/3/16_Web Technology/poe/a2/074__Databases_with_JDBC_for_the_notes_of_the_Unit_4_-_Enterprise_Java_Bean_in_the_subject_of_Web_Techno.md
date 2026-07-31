 Here is the content in markdown format without any emojis or external links and in formal tone:

### Databases with JDBC for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

1. JDBC (Java Database Connectivity) is an API that allows Java programs to interact with a relational database.
2. JDBC provides a standard interface for SQL-based databases. It defines a set of classes and interfaces that can be used to query and update data in a database.
3. The steps to connect to a database and execute queries are:

- Load the database driver: First, we need to load the driver for the specific database we want to connect to. Each database has its own driver.
- Establish the connection: Next, we need to establish a connection to the database using the DriverManager class. We pass in the database URL, username and password to get the connection object.
- Create a statement: We then create a Statement or PreparedStatement object. The Statement is used to execute static SQL statements and retrieve results. The PreparedStatement is used to execute precompiled statements with variable parameters.
- Execute queries and retrieve results: Finally, we execute the query on the statement and retrieve the results. We can get the results as a ResultSet, which represents the table of data produced by the query.

4. Some advantages of JDBC are:
- It is database independent and can connect to various databases with little or no change in application code.
- It supports various SQL features like stored procedures, transactions, etc.
- It is a standard API with multiple implementations from database vendors.
- It leverages the Java security model and other Java features.