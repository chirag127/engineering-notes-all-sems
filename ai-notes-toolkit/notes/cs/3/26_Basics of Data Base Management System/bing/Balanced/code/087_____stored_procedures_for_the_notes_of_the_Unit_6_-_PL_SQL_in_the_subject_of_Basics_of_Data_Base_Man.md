### Stored Procedures in PL/SQL

- A stored procedure in PL/SQL is a named block of code that performs one or more specific tasks and can be stored in the database for reuse .
- A stored procedure can be invoked by other procedures, triggers, or applications written in Java, PHP, etc .
- A stored procedure has a header and a body. The header contains the name of the procedure and the parameters passed to it. The body contains the executable statements and optional exception handlers .
- A stored procedure can have three types of parameters: IN, OUT, and IN OUT. IN parameters are used to pass values to the procedure. OUT parameters are used to return values from the procedure. IN OUT parameters are used to do both .
- A stored procedure can be created using the CREATE PROCEDURE statement. The syntax is as follows:

```sql
CREATE [OR REPLACE] PROCEDURE schema.procedure_name
[(parameter_name [IN | OUT | IN OUT] parameter_type, ...)]
IS
  -- declare local variables
BEGIN
  -- executable statements
EXCEPTION
  -- exception handlers
END [procedure_name];
```

- A stored procedure can be executed using the EXECUTE or EXEC statement, or by calling it from another block of code. The syntax is as follows:

```sql
EXECUTE schema.procedure_name[(parameter_value, ...)];
EXEC schema.procedure_name[(parameter_value, ...)];
BEGIN
  schema.procedure_name[(parameter_value, ...)];
END;
```

- A stored procedure can be dropped using the DROP PROCEDURE statement. The syntax is as follows:

```sql
DROP PROCEDURE schema.procedure_name;
```

- A stored procedure can be modified using the CREATE OR REPLACE PROCEDURE statement, which replaces the existing procedure with the new one.
- A stored procedure can be viewed using the USER_PROCEDURES, ALL_PROCEDURES, or DBA_PROCEDURES data dictionary views.