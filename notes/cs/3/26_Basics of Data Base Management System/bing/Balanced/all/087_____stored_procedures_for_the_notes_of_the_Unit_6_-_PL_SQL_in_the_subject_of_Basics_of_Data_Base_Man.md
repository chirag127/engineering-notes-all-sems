# Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database for reuse .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to it. The body contains the declarative, executable, and exception-handling parts of the code .
- A stored procedure can be created using the CREATE PROCEDURE statement, which has the following syntax :

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
  (parameter1 [IN|OUT|IN OUT] datatype1 [DEFAULT value1],
   parameter2 [IN|OUT|IN OUT] datatype2 [DEFAULT value2],
   ...
   parameterN [IN|OUT|IN OUT] datatypeN [DEFAULT valueN])
IS
  -- declarative part
  variable1 datatype1;
  variable2 datatype2;
  ...
  variableN datatypeN;
BEGIN
  -- executable part
  statement1;
  statement2;
  ...
  statementN;
EXCEPTION
  -- exception-handling part
  WHEN exception1 THEN
    statement1;
    statement2;
    ...
    statementN;
  WHEN exception2 THEN
    statement1;
    statement2;
    ...
    statementN;
  ...
  WHEN exceptionN THEN
    statement1;
    statement2;
    ...
    statementN;
END procedure_name;
```

- A stored procedure can be executed using the EXECUTE or EXEC command, which has the following syntax :

```sql
EXECUTE schema.procedure_name(parameter1, parameter2, ..., parameterN);
```

- A stored procedure can be dropped using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE schema.procedure_name;
```

- A stored procedure can be modified using the ALTER PROCEDURE statement, which has the following syntax:

```sql
ALTER PROCEDURE schema.procedure_name COMPILE;
```

- A stored procedure can have advantages such as modularity, reusability, maintainability, security, and performance .