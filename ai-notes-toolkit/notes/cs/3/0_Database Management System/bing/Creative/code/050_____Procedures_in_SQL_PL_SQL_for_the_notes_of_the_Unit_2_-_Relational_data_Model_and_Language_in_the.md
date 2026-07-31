### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value like a function.
- A procedure can be invoked by other PL/SQL blocks, triggers, procedures, functions, or applications written in different languages.
- A procedure can be created using the CREATE PROCEDURE statement, which has the following syntax:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT expr],
  parameter2 [mode] datatype [DEFAULT expr],
  ...)]
IS | AS
  [local declarations]
BEGIN
  executable statements
[EXCEPTION
  exception handlers]
END [procedure_name];
```

- The procedure name must be unique within the same schema.
- The parameters can have three modes: IN, OUT, or IN OUT. IN parameters are read-only, OUT parameters are write-only, and IN OUT parameters are both readable and writable.
- The DEFAULT clause specifies a default value for an IN or IN OUT parameter if the caller does not provide one.
- The IS or AS keyword separates the parameter list from the procedure body.
- The local declarations section can declare variables, constants, cursors, or user-defined types that are local to the procedure.
- The executable statements section contains the PL/SQL code that performs the logic of the procedure.
- The EXCEPTION section handles any errors that may occur during the execution of the procedure.
- The optional procedure name at the end of the block must match the name at the beginning.
- A procedure can be modified using the ALTER PROCEDURE statement or replaced using the CREATE OR REPLACE PROCEDURE statement.
- A procedure can be deleted using the DROP PROCEDURE statement.
- A procedure can be executed using the EXECUTE statement or by using the procedure name as a statement by itself. For example:

```sql
EXECUTE adjust_salary(100, 10); -- using EXECUTE statement
adjust_salary(100, 10); -- using procedure name as a statement
```

- A procedure can also be executed from another PL/SQL block by using the procedure name with or without the schema name. For example:

```sql
BEGIN
  hr.adjust_salary(100, 10); -- using schema name and procedure name
  adjust_salary(100, 10); -- using procedure name only
END;
```

- A procedure can also be executed from an application written in a different language, such as Java, PHP, or C#, by using the appropriate API or library that supports calling PL/SQL procedures. For example, in Java, a procedure can be executed using the CallableStatement class.