# Stored Function in PL/SQL

- A stored function is a reusable program unit that can be invoked from SQL or PL/SQL code.
- A stored function returns a single value of a specified data type.
- A stored function can be created using the `CREATE FUNCTION` statement, which has the following syntax:

```
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
  [declarative section]
BEGIN
  [executable section]
  RETURN expression;
END [function_name];
```

- The `parameter_list` consists of zero or more parameters, each with a name, a mode (`IN`, `OUT`, or `IN OUT`), and a data type.
- The `return_type` specifies the data type of the value that the function returns.
- The `declarative section` is optional and contains the declarations of variables, constants, cursors, exceptions, and other local objects.
- The `executable section` is mandatory and contains the statements that perform the logic of the function.
- The `RETURN` statement specifies the expression that evaluates to the value that the function returns.
- The `function_name` at the end of the function is optional and can be used to improve readability.

- A stored function can be invoked from SQL statements, such as `SELECT`, `INSERT`, `UPDATE`, or `DELETE`, as long as the function does not modify any database tables or have any side effects.
- A stored function can also be invoked from PL/SQL blocks, procedures, packages, triggers, or other functions, using the syntax `function_name (argument_list)`, where the `argument_list` matches the `parameter_list` of the function.
- A stored function can be dropped using the `DROP FUNCTION` statement, which has the following syntax:

```
DROP FUNCTION function_name;
```

- A stored function can be modified using the `CREATE OR REPLACE FUNCTION` statement, which replaces the existing function definition with the new one.
- A stored function can be compiled using the `ALTER FUNCTION` statement, which has the following syntax:

```
ALTER FUNCTION function_name COMPILE;
```

- A stored function can be debugged using the `DBMS_DEBUG` package, which provides an API for debugging PL/SQL code.