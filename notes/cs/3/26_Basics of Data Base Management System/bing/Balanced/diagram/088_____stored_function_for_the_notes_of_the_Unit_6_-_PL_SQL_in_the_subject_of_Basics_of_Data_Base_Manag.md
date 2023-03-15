### Stored function in PL/SQL

- A stored function is a reusable program unit that can be called from other PL/SQL blocks or SQL statements.
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

- The `parameter_list` consists of zero or more parameters, each with a name, a data type, and an optional mode (`IN`, `OUT`, or `IN OUT`).
- The `return_type` specifies the data type of the value that the function returns.
- The `declarative section` is optional and can contain declarations of variables, constants, cursors, exceptions, etc.
- The `executable section` contains the logic of the function and must end with a `RETURN` statement that specifies the expression to be returned.
- The `function_name` at the end of the block is optional and can be used to improve readability.

- A stored function can be invoked from a PL/SQL block using the syntax:

```
variable := function_name (argument_list);
```

- A stored function can also be invoked from a SQL statement using the syntax:

```
SELECT function_name (argument_list) FROM table_name;
```

- A stored function can be modified using the `CREATE OR REPLACE FUNCTION` statement, which replaces the existing definition of the function with the new one.
- A stored function can be deleted using the `DROP FUNCTION` statement, which removes the function and its definition from the database.

- Some advantages of using stored functions are:

  - They improve code reusability and modularity.
  - They reduce network traffic and improve performance by executing on the server side.
  - They can be used in SQL statements to manipulate data or perform calculations.
  - They can be used in check constraints, default values, or triggers to enforce business rules or data integrity.