JDBC stands for Java Database Connectivity, which is an API that allows Java programs to communicate with various types of databases. JDBC provides a set of classes and interfaces that can be used to execute SQL statements, manipulate data, and handle errors.

One of the main components of JDBC is the DriverManager class, which manages the loading and registering of different JDBC drivers. A JDBC driver is a software component that enables a Java application to interact with a specific database. There are four types of JDBC drivers: JDBC-ODBC bridge driver, native-API driver, network protocol driver, and pure Java driver.

To manipulate data in a database using JDBC, a Java application typically follows these steps:

1. Load and register the JDBC driver for the database.
2. Establish a connection to the database using the DriverManager class.
3. Create a Statement object from the connection object.
4. Execute a SQL statement using the statement object, and obtain a ResultSet object if the statement is a query.
5. Process the result set object, and retrieve the data from each row and column.
6. Close the result set, statement, and connection objects.

The following diagram illustrates the basic architecture of JDBC:

```
+---------------------+      +---------------------+
|      Java App       |      |      Database       |
+---------------------+      +---------------------+
|                     |      |                     |
|  +--------------+   |      |  +--------------+   |
|  | DriverManager|<--+----->|  |   JDBC Driver |<--+
|  +--------------+   |      |  +--------------+   |
|                     |      |                     |
|  +--------------+   |      |  +--------------+   |
|  |  Connection  |<--+----->|  |    Database   |   |
|  +--------------+   |      |  +--------------+   |
|                     |      |                     |
|  +--------------+   |      |  +--------------+   |
|  |   Statement  |<--+----->|  |    SQL Engine |   |
|  +--------------+   |      |  +--------------+   |
|                     |      |                     |
|  +--------------+   |      |  +--------------+   |
|  |  ResultSet   |<--+----->|  |    Data       |   |
|  +--------------+   |      |  +--------------+   |
|                     |      |                     |
+---------------------+      +---------------------+
```