### Stored function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement, another PL/SQL block, or a Java program .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must do so in a read-only manner .
- A stored function can be created using the following syntax :

```sql
CREATE [ OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
END [function_name];
```

- The `CREATE OR REPLACE` option allows to modify an existing function without dropping and recreating it .
- The `parameter_list` consists of zero or more parameters, each with a name, a data type, and an optional mode (IN, OUT, or IN OUT) .
- The `return_type` specifies the data type of the value that the function returns .
- The `declarative section` contains the declarations of variables, constants, cursors, or exceptions that are used by the function .
- The `executable section` contains the statements that define the logic of the function .
- The `END` clause marks the end of the function body and optionally repeats the function name for clarity .

- Here is an example of a stored function that calculates the factorial of a given number:

```sql
CREATE OR REPLACE FUNCTION factorial (n NUMBER)
RETURN NUMBER
IS
  result NUMBER := 1;
BEGIN
  FOR i IN 1..n LOOP
    result := result * i;
  END LOOP;
  RETURN result;
END factorial;
```

- To invoke a stored function, use the function name followed by the argument list in parentheses .
- For example, to call the factorial function from a SQL statement, use the following syntax:

```sql
SELECT factorial(5) FROM dual;
```

- The output is:

```sql
FACTORIAL(5)
------------
        120
```