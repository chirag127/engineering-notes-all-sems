Stored procedures are subroutines, segments of SQL statements that are stored in the SQL catalog. They can be accessed by applications that can access relational databases, such as Java, Python, PHP, etc. Stored procedures can improve performance, security, and modularity of database applications.

To call a stored procedure using JDBC, you need to:

- Register the driver class using the registerDriver() method of the DriverManager class.
- Establish a connection to the database using the getConnection() method of the DriverManager class.
- Create a CallableStatement object using the prepareCall() method of the Connection object. The prepareCall() method takes a string argument that specifies the SQL escape syntax for calling the stored procedure. The syntax is: {call procedure_name[(?, ?, ...)]}
- If the stored procedure has input parameters, use the setXXX() methods of the CallableStatement object to bind values to the parameters. The setXXX() methods take two arguments: the parameter index and the parameter value.
- If the stored procedure has output parameters, use the registerOutParameter() method of the CallableStatement object to bind the JDBC data type to the data type the stored procedure expects for the output values. The registerOutParameter() method takes two arguments: the parameter index and the JDBC data type.
- Execute the stored procedure using the execute() method of the CallableStatement object.
- If the stored procedure returns output values, use the getXXX() methods of the CallableStatement object to retrieve them. The getXXX() methods take one argument: the parameter index.

The following diagram illustrates the basic architecture of a stored procedure in JDBC using ASCII art:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Application   |        |  JDBC Driver   |        |  Database      |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
       |                        |                        |
       |                        |                        |
       | registerDriver()      |                        |
       |----------------------->|                        |
       |                        |                        |
       | getConnection()       |                        |
       |----------------------->|                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       | prepareCall()         |                        |
       |----------------------->|                        |
       |                        |                        |
       | setXXX()              |                        |
       |----------------------->|                        |
       |                        |                        |
       | registerOutParameter()|                        |
       |----------------------->|                        |
       |                        |                        |
       | execute()             |                        |
       |----------------------->|                        |
       |                        |                        |
       |                        | call procedure_name()  |
       |                        |----------------------->|
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        | return output values   |
       |                        |<-----------------------|
       |                        |                        |
       | getXXX()              |                        |
       |<-----------------------|                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       | close()               |                        |
       |----------------------->|                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
       |                        |                        |
```