Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of creating procedures and functions in the subject of Database Management Systems Lab. Here is the content in markdown format:

# Unit 6 - Creating procedures and functions

## Procedures

- A procedure is a named block of SQL statements that performs a specific task or operation.
- A procedure can be invoked by other procedures, functions, triggers, or applications.
- A procedure can have parameters that are passed by value or by reference.
- A procedure can return a value to the caller using the `RETURN` statement or an `OUT` parameter.
- A procedure can be created using the `CREATE PROCEDURE` statement, with the following syntax:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode1] datatype1 [DEFAULT default_value1],
  parameter2 [mode2] datatype2 [DEFAULT default_value2],
  ...)]
[IS | AS]
  [local_variable_declarations]
BEGIN
  executable_statements
[EXCEPTION
  exception_handlers]
END [procedure_name];
```

- The `OR REPLACE` option allows to modify an existing procedure.
- The `parameter` can have one of the following modes:
  - `IN`: The parameter value is passed from the caller to the procedure. It is the default mode.
  - `OUT`: The parameter value is passed from the procedure to the caller. The parameter must be a variable.
  - `IN OUT`: The parameter value is passed both ways, from the caller to the procedure and vice versa. The parameter must be a variable.
- The `local_variable_declarations` section allows to declare and initialize local variables that are visible only within the procedure.
- The `executable_statements` section contains the SQL statements that perform the task of the procedure.
- The `EXCEPTION` section allows to handle any errors or exceptions that may occur during the execution of the procedure.
- The `procedure_name` at the end of the block is optional and can be used to improve readability.

## Functions

- A function is a named block of SQL statements that returns a single value or a table of values.
- A function can be invoked by other procedures, functions, triggers, or applications, or used as an expression in a SQL statement.
- A function can have parameters that are passed by value only.
- A function must return a value to the caller using the `RETURN` statement.
- A function can be created using the `CREATE FUNCTION` statement, with the following syntax:

```sql
CREATE [OR REPLACE] FUNCTION function_name
[(parameter1 datatype1 [DEFAULT default_value1],
  parameter2 datatype2 [DEFAULT default_value2],
  ...)]
RETURN return_datatype
[IS | AS]
  [local_variable_declarations]
BEGIN
  executable_statements
[EXCEPTION
  exception_handlers]
END [function_name];
```

- The `OR REPLACE` option allows to modify an existing function.
- The `parameter` can have only the `IN` mode, which is implicit and can be omitted.
- The `return_datatype` specifies the data type of the value or the table that the function returns.
- The `local_variable_declarations` section allows to declare and initialize local variables that are visible only within the function.
- The `executable_statements` section contains the SQL statements that perform the task of the function and return a value using the `RETURN` statement.
- The `EXCEPTION` section allows to handle any errors or exceptions that may occur during the execution of the function.
- The `function_name` at the end of the block is optional and can be used to improve readability.

## Examples

- The following example shows how to create a procedure that accepts two numbers as input parameters and returns their sum as an output parameter:

```sql
CREATE PROCEDURE add_numbers (num1 IN NUMBER, num2 IN NUMBER, result OUT NUMBER)
IS
BEGIN
  result := num1 + num2;
END add_numbers;
```

- The following example shows how to create a function that accepts a string as an input parameter and returns its length as an output value:

```sql
CREATE FUNCTION get_length (str IN VARCHAR2) RETURN NUMBER
IS
  len NUMBER;
BEGIN
  len := LENGTH(str);
  RETURN len;
END get_length;
```

- The following example shows how to invoke the procedure and the function created above:

```sql
DECLARE
  x NUMBER := 10;
  y NUMBER := 20;
  z NUMBER;
  n NUMBER;
BEGIN
  -- Call the procedure
  add_numbers(x, y, z);
  DBMS_OUTPUT.PUT_LINE('The sum of ' || x || ' and ' || y || ' is

```
