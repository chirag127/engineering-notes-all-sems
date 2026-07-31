# Stored function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement or another PL/SQL block .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must not have any side effects such as committing or rolling back transactions .

## Syntax of creating a stored function

The following is the general syntax for creating a stored function in PL/SQL :

```sql
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
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

- The `CREATE [OR REPLACE]` clause specifies whether to create a new function or replace an existing one with the same name .
- The `function_name` is the name of the function that must be unique within the same schema .
- The `parameter_list` is a comma-separated list of parameters that the function can accept as input. Each parameter has a name, a mode (`IN`, `OUT`, or `IN OUT`), and a data type .
- The `RETURN return_type` clause specifies the data type of the value that the function returns .
- The `IS` keyword marks the beginning of the function body .
- The `declarative section` is an optional section where variables, constants, cursors, or exceptions that are used by the function can be declared .
- The `BEGIN` keyword marks the beginning of the executable section where the main logic of the function is written .
- The `RETURN expression` statement returns a value to the caller of the function. The expression must have the same data type as the return type of the function .
- The `EXCEPTION` keyword marks the beginning of the exception handling section where errors or exceptions that occur during the execution of the function can be handled .
- The `END [function_name]` clause marks the end of the function body. The optional function name can be used to improve the readability of the code .

## Example of creating and invoking a stored function

The following example creates a stored function named `get_full_name` that takes two parameters (`first_name` and `last_name`) and returns a concatenated string as the full name:

```sql
CREATE OR REPLACE FUNCTION get_full_name (first_name VARCHAR2, last_name VARCHAR2)
RETURN VARCHAR2
IS
BEGIN
  RETURN first_name || ' ' || last_name;
END get_full_name;
```

The following example invokes the stored function `get_full_name` from a SQL statement:

```sql
SELECT get_full_name('John', 'Doe') AS full_name FROM dual;
```

The output is:

```
FULL_NAME
---------
John Doe
```

The following example invokes the stored function `get_full_name` from another PL/SQL block:

```sql
DECLARE
  v_full_name VARCHAR2(50);
BEGIN
  v_full_name := get_full_name('Jane', 'Doe');
  DBMS_OUTPUT.PUT_LINE('Full name: ' || v_full_name);
END;
```

The output is:

```
Full name: Jane Doe
```