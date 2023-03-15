### Stored function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement or another PL/SQL block .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function has the following syntax :

```sql
CREATE [ OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
[declarative section]
BEGIN
[executable section]
RETURN expression;
END [function_name];
```

- The parameter_list consists of zero or more parameters, each with a name, a data type, and an optional mode (IN, OUT, or IN OUT) .
- The return_type specifies the data type of the value that the function returns .
- The declarative section declares the variables, constants, cursors, or exceptions that are used by the function .
- The executable section contains the statements that define the logic of the function .
- The RETURN statement specifies the expression that evaluates to the value that the function returns .
- The function_name at the end of the block is optional and can be used to improve readability .
- A stored function can be executed by using the function name followed by the argument list in parentheses .
- A stored function can be used in a SQL statement wherever an expression of the same data type is allowed .
- A stored function can also be used in another PL/SQL block by assigning its return value to a variable or using it in an expression .