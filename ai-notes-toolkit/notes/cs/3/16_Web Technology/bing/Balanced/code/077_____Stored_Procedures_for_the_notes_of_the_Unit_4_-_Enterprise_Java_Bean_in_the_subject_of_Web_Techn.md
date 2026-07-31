# Stored Procedures

- Stored procedures are Java methods that are published to SQL and stored in the database for general use.
- Stored procedures can perform complex tasks, improve performance, and enhance security.
- To publish Java methods as stored procedures, you write call specifications, which map Java method names, parameter types, and return types to their SQL counterparts.
- To call a Java stored procedure, you use the SQL CALL statement or a PL/SQL block.
- You can also use the JDBC API to call stored procedures from Java applications.
- To use JDBC to call stored procedures, you need to create a CallableStatement object, register the output parameters, set the input parameters, execute the statement, and retrieve the results.
- You can also use the JPA API to call stored procedures from Java applications.
- To use JPA to call stored procedures, you need to annotate your entity class with @NamedStoredProcedureQuery, specify the name, parameters, and result class of the stored procedure, and use the EntityManager to create and execute a StoredProcedureQuery object.