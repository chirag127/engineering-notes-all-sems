### Stored Function in PL/SQL

- A stored function is a reusable program unit that can be defined and stored in the database as a schema object .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement, another PL/SQL block, or a PL/SQL expression .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must not have any side effects such as committing or rolling back transactions .
- The syntax for creating a stored function is as follows :

```sql
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
END [function_name];
```

- The `CREATE OR REPLACE` option allows to overwrite an existing function with the same name .
- The `parameter_list` consists of zero or more parameters, each with a name, a data type, and an optional mode (IN, OUT, or IN OUT) .
- The `return_type` specifies the data type of the value that the function returns .
- The `declarative section` is optional and can contain declarations of variables, constants, cursors, or exceptions that are used in the function .
- The `executable section` is mandatory and contains the PL/SQL statements that implement the function logic .
- The `END` clause marks the end of the function body and can optionally include the function name for clarity .

- An example of a stored function that calculates the factorial of a given number is as follows:

```sql
CREATE OR REPLACE FUNCTION factorial (n IN NUMBER)
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

- The output of the above statement is 120.