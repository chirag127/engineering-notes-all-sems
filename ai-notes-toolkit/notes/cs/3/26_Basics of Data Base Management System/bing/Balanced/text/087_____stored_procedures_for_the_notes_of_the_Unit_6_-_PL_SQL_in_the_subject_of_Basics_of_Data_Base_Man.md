### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database catalog .
- A stored procedure can be thought of as a function or a method that can be invoked by triggers, other procedures, or applications on Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to the procedure. The body contains the declarative, executable, and exception-handling parts of the procedure .
- A stored procedure can be created using the CREATE PROCEDURE statement, which has the following syntax :

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
  (parameter1 [IN|OUT|IN OUT] parameter_type1,
   parameter2 [IN|OUT|IN OUT] parameter_type2,
   ...
   parameterN [IN|OUT|IN OUT] parameter_typeN)
IS
  -- declarative part
  -- variables, constants, cursors, exceptions, etc.
BEGIN
  -- executable part
  -- SQL statements and PL/SQL code
EXCEPTION
  -- exception-handling part
  -- actions to handle errors
END;
```

- A stored procedure can be executed using the EXECUTE or EXEC command, which has the following syntax :

```sql
EXECUTE schema.procedure_name(parameter1, parameter2, ..., parameterN);
```

- A stored procedure can be dropped using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE schema.procedure_name;
```