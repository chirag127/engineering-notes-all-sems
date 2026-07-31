### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value directly like a function.
- A procedure can be invoked by other PL/SQL blocks, procedures, functions, triggers, or applications written in different languages.
- A procedure has a header and a body. The header specifies the name and the parameters of the procedure. The body contains the executable statements and optional exception handlers.
- The syntax of a procedure is as follows:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT expr],
  parameter2 [mode] datatype [DEFAULT expr],
  ...)]
IS
  [declaration_section]
BEGIN
  executable_section
[EXCEPTION
  exception_section]
END [procedure_name];
```

- The `CREATE OR REPLACE` option allows you to modify an existing procedure without dropping and recreating it.
- The parameters can have three modes: `IN`, `OUT`, or `IN OUT`. The `IN` mode is the default and means that the parameter is read-only. The `OUT` mode means that the parameter is write-only and will return a value to the caller. The `IN OUT` mode means that the parameter is both read and write and will pass a value to the procedure and return a modified value to the caller.
- The `DEFAULT` option allows you to specify a default value for an `IN` or `IN OUT` parameter. If the caller does not pass a value for that parameter, the default value will be used.
- The `IS` keyword separates the header and the body of the procedure.
- The `declaration_section` is optional and allows you to declare local variables, constants, cursors, and user-defined exceptions that are only visible within the procedure.
- The `executable_section` is mandatory and contains the PL/SQL statements that perform the logic of the procedure. It must have at least one executable statement.
- The `EXCEPTION` keyword introduces the `exception_section`, which is optional and allows you to handle any errors or exceptions that may occur during the execution of the procedure. You can use predefined or user-defined exceptions and associate them with appropriate actions using the `WHEN` clause.
- The `END` keyword terminates the procedure. You can optionally repeat the procedure name after the `END` keyword for clarity.
- To execute a procedure, you can use the `EXECUTE` or `EXEC` command, or call it from another PL/SQL block. You can pass the parameters by position or by name, and use the `=>` operator to assign values to `OUT` or `IN OUT` parameters. For example:

```sql
EXECUTE procedure_name(parameter1, parameter2, ...);

EXEC procedure_name(parameter1 => value1, parameter2 => value2, ...);

BEGIN
  procedure_name(parameter1, parameter2, ...);
END;
/
```