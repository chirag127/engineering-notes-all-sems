# Stored Procedures

- Stored procedures are Java methods that are published to SQL and stored in the database for general use.
- Stored procedures can perform complex tasks, improve performance, and enhance security.
- To create and use a stored procedure in Java DB, you need to follow these steps:
  - Create a public static Java method in a Java class that performs the required task of the stored procedure.
  - Create the stored procedure in the database that calls the Java method using the `CREATE PROCEDURE` statement.
  - Call the stored procedure from your Java application using the `CallableStatement` interface.
- To call a stored function or a stored procedure that returns a value, you need to use the `registerOutParameter` method to specify the type of the returned value and the `getXXX` method to retrieve it.
- To use stored procedures with JPA, you need to use the `@NamedStoredProcedureQuery` annotation to define the stored procedure name, parameters, and result classes, and the `createNamedStoredProcedureQuery` method to create and execute the query.