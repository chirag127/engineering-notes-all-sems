# Stored Function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement or another PL/SQL block .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must not have any side effects such as committing or rolling back transactions .

## Syntax of a Stored Function

The syntax for creating a stored function is as follows :

```sql
CREATE [ OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
RETURN expression;
EXCEPTION
[exception handling section]
END [function_name];
```

- The `CREATE OR REPLACE` clause allows you to modify an existing function or create a new one if it does not exist .
- The `function_name` is the name of the function that must be unique within the schema .
- The `parameter_list` is a comma-separated list of parameters that can have different modes: `IN`, `OUT`, or `IN OUT` .
- The `return_type` is the data type of the value that the function returns .
- The `IS` keyword marks the beginning of the function body .
- The `declarative section` is optional and can contain declarations of variables, constants, cursors, or exceptions that are used in the function .
- The `BEGIN` keyword marks the beginning of the executable section that contains the logic of the function .
- The `RETURN` statement specifies the expression that evaluates to the value that the function returns .
- The `EXCEPTION` keyword marks the beginning of the exception handling section that can handle any errors or exceptions that occur in the function .
- The `END` keyword marks the end of the function body and can optionally include the function name for clarity .

## Example of a Stored Function

The following example shows how to create a stored function that calculates the factorial of a given number:

```sql
CREATE OR REPLACE FUNCTION factorial (n IN NUMBER)
RETURN NUMBER
IS
  result NUMBER := 1;
BEGIN
  IF n < 0 THEN
    RAISE VALUE_ERROR;
  END IF;
  FOR i IN 1..n LOOP
    result := result * i;
  END LOOP;
  RETURN result;
EXCEPTION
  WHEN VALUE_ERROR THEN
    DBMS_OUTPUT.PUT_LINE('Invalid input');
    RETURN NULL;
END factorial;
```

The function takes a parameter `n` of type `NUMBER` and returns a `NUMBER` as well. It declares a local variable `result` to store the intermediate values. It checks if the input is negative and raises a `VALUE_ERROR` exception if so. It uses a `FOR` loop to iterate from 1 to n and multiply the result by each value. It returns the final result or `NULL` if an exception occurs.

To invoke the function, you can use a `SELECT` statement or a PL/SQL block, for example:

```sql
SELECT factorial(5) FROM dual;
```

The output is:

```sql
FACTORIAL(5)
------------
120
```