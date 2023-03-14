Stored procedures are a group of SQL statements that form a logical unit and perform a particular task on a database server. They can have input, output, or input/output parameters and can return zero or more values. They are stored in the database and can be called by applications using the CALL SQL statement. JDBC provides a standard stored procedure SQL escape syntax using which you can call procedures in all RDBMSs.

#### Stored Procedures in JDBC

The following diagram illustrates the basic architecture of a stored procedure in JDBC:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  JDBC Program   |     |  JDBC Driver    |     |  Database       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  1. Register    |     |                 |     |                 |
|     driver      |     |                 |     |                 |
|                 |     |                 |     |                 |
|  2. Establish   |---->|                 |     |                 |
|     connection  |     |                 |     |                 |
|                 |     |                 |     |                 |
|  3. Create      |     |                 |     |                 |
|     statement   |     |                 |     |                 |
|                 |     |                 |     |                 |
|  4. Execute     |     |  5. Send        |---->|  6. Execute     |
|     statement   |     |     statement   |     |     statement   |
|                 |     |                 |     |                 |
|  7. Process     |<----|  8. Return      |<----|  9. Return      |
|     results     |     |     results     |     |     results     |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The steps involved in calling a stored procedure in JDBC are:

1. Register the driver class using the registerDriver() method of the DriverManager class.
2. Establish a connection to the database using the getConnection() method of the DriverManager class.
3. Create a statement object using the prepareCall() method of the Connection object. The prepareCall() method takes a string argument that specifies the SQL escape syntax for calling the stored procedure. For example, "{call SHOW_SUPPLIERS()}" or "{? = call GET_SUPPLIER_OF_COFFEE(?)}".
4. Execute the statement using the execute() or executeUpdate() method of the CallableStatement object. The execute() method returns a boolean value indicating whether the statement produced a result set or not. The executeUpdate() method returns an int value indicating the number of rows affected by the statement.
5. Process the results using the getResultSet() method of the CallableStatement object to obtain a ResultSet object if the statement produced a result set, or using the getXXX() methods of the CallableStatement object to obtain the output parameters if the statement returned any. For example, getString(2) or getInt(1).
6. Close the statement and connection objects using the close() method of the respective objects.