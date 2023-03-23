### Databases with JDBC

JDBC (Java Database Connectivity) is a standard API for connecting Java programs with databases. In this unit, we will learn about using JDBC to communicate with databases in Enterprise Java Beans.

Here are the key points to remember:

- JDBC is a Java API that allows Java programs to access and manipulate data stored in databases.
- JDBC provides a standard set of classes and interfaces for connecting to databases, executing SQL statements, and retrieving results.
- To use JDBC, you need to have a JDBC driver for your database. JDBC drivers are usually provided by the database vendor.
- The basic steps for using JDBC are: 
  1. Load the JDBC driver class using Class.forName()
  2. Open a connection to the database using DriverManager.getConnection()
  3. Create a statement object using the Connection.createStatement() method
  4. Execute SQL statements using the Statement.executeXXX() methods, such as executeQuery() for SELECT statements and executeUpdate() for INSERT, UPDATE, and DELETE statements.
  5. Process the results of the SQL query using ResultSet objects.
  6. Close the statement and connection using the close() method.
- JDBC supports transactions, which allow you to group multiple SQL statements into a single unit of work that can be either committed or rolled back as a whole.
- In Enterprise Java Beans, you can use JDBC to access databases from within the EJB container. To do this, you need to define a JDBC DataSource in the EJB container and use JNDI (Java Naming and Directory Interface) to look up the DataSource.
- When using JDBC in an EJB, it is important to be aware of the transactional context in which the JDBC operations are executed. If you are using container-managed transactions, the container will automatically handle transaction management for you. If you are using bean-managed transactions, you will need to manage the transactions yourself using the UserTransaction interface.

By mastering JDBC, you will be able to develop enterprise applications that can access and manipulate data stored in databases. Good luck with your studies!