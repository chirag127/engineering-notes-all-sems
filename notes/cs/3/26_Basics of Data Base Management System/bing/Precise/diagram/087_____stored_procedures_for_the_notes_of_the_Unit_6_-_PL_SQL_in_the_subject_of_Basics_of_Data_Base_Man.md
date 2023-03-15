### Stored Procedures

A stored procedure is a pre-compiled, reusable routine that is stored in a database. It is a group of SQL statements that perform a specific task. Stored procedures can be used to improve the performance and security of a database application.

Here are some key points to remember about stored procedures:

1. Stored procedures are pre-compiled and stored in the database, which can improve the performance of the database application.
2. Stored procedures can help to improve the security of a database application by restricting access to the underlying data.
3. Stored procedures can be used to encapsulate complex business logic, making it easier to maintain and update.
4. Stored procedures can help to reduce network traffic between the application and the database by reducing the number of round trips required to perform a task.
5. Stored procedures can be used to enforce data integrity by implementing complex validation rules.

In PL/SQL, stored procedures can be created using the `CREATE PROCEDURE` statement. The syntax for creating a stored procedure is as follows:

```
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype, parameter2 [mode] datatype, ...)]
IS
    [local_variable_declarations]
BEGIN
    executable_statements
[EXCEPTION
    exception_handlers]
END [procedure_name];
```

The `mode` for a parameter can be `IN`, `OUT`, or `IN OUT`. `IN` parameters are used to pass values into the stored procedure, `OUT` parameters are used to return values from the stored procedure, and `IN OUT` parameters can be used for both.

Once a stored procedure has been created, it can be executed using the `EXECUTE` statement or by calling it from another PL/SQL block or program.