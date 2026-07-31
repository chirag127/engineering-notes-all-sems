A stored procedure is a segment of SQL statements that is stored in the database and can be executed by applications. Stored procedures can have input and output parameters, and can return values to the caller. JDBC provides a standard way to call stored procedures using the CallableStatement interface. A CallableStatement object can be created by using the prepareCall() method of the Connection interface, and can execute the stored procedure by using the execute() or executeUpdate() methods. The following is a possible ASCII diagram for stored procedures in JDBC:

#### Stored Procedures in JDBC

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Application  |       |   JDBC Driver  |       |   Database     |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
       |                       |                       |
       | prepareCall()         |                       |
       |---------------------> |                       |
       |                       |                       |
       |                       | create CallableStatement
       |                       |---------------------> |
       |                       |                       |
       |                       |                       |
       | set input parameters  |                       |
       |---------------------> |                       |
       |                       |                       |
       |                       | set input parameters  |
       |                       |---------------------> |
       |                       |                       |
       | execute()             |                       |
       |---------------------> |                       |
       |                       |                       |
       |                       | execute stored procedure
       |                       |---------------------> |
       |                       |                       |
       |                       | get output parameters |
       |                       |<--------------------- |
       |                       |                       |
       | get output parameters |                       |
       |<--------------------- |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       | close()               |                       |
       |---------------------> |                       |
       |                       |                       |
       |                       | close CallableStatement
       |                       |---------------------> |
       |                       |                       |
       |                       |                       |
       V                       V                       V
```