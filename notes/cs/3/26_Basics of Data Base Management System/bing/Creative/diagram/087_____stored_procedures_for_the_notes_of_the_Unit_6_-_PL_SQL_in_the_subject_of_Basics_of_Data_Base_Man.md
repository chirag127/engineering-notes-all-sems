### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database for reuse .
- A stored procedure can be invoked by other procedures, triggers, or applications written in Java, PHP, etc .
- A stored procedure has a header and a body .
- The header contains the name of the procedure and the parameters passed to it .
- The body contains the declarative, executable, and exception-handling parts of the procedure .
- The syntax of a stored procedure is as follows :

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype1, parameter2 [mode] datatype2, ...)]
IS
  --declarative part
  --variables, constants, cursors, etc.
BEGIN
  --executable part
  --SQL and PL/SQL statements
EXCEPTION
  --exception-handling part
  --error handling logic
END procedure_name;
```

- The mode of a parameter can be IN, OUT, or IN OUT, depending on whether the parameter is used to pass a value to the procedure, return a value from the procedure, or both .
- To execute a stored procedure, use the EXECUTE or EXEC command, followed by the procedure name and the arguments (if any) .
- To drop a stored procedure, use the DROP PROCEDURE command, followed by the procedure name.
- Stored procedures can improve the performance, modularity, and maintainability of the database applications .