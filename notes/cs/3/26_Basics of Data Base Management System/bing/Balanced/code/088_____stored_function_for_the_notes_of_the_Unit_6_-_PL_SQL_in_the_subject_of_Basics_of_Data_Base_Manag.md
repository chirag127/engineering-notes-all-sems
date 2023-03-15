### Stored function in PL/SQL

- A stored function is a reusable program unit that can be stored as a schema object in the Oracle Database .
- A stored function can take zero or more parameters as input and return a single value as output .
- A stored function can be invoked from a SQL statement, another PL/SQL block, or a Java program .
- A stored function can be used to perform calculations, validations, transformations, or other business logic .
- A stored function can also be used to access or modify database data, but it must do so in a read-only manner .
- A stored function cannot contain DML statements that modify database data, such as INSERT, UPDATE, or DELETE .
- A stored function cannot contain transaction control statements, such as COMMIT or ROLLBACK .
- A stored function cannot return a result set, such as a cursor or a collection .

The syntax for creating a stored function is as follows :

```sql
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_type
IS
-- declarative section
BEGIN
-- executable section
END;
```

- The CREATE OR REPLACE clause allows you to modify an existing function or create a new one if it does not exist .
- The function_name is the name of the function that must be unique within the schema .
- The parameter_list is a comma-separated list of parameters that can be of three modes: IN, OUT, or IN OUT .
- The IN mode indicates that the parameter is an input value that cannot be modified by the function .
- The OUT mode indicates that the parameter is an output value that can be modified by the function .
- The IN OUT mode indicates that the parameter is both an input and an output value that can be modified by the function .
- The return_type is the data type of the value that the function returns .
- The IS keyword marks the beginning of the function body .
- The declarative section is optional and can contain declarations of variables, constants, cursors, exceptions, or other local objects that are used by the function .
- The BEGIN keyword marks the beginning of the executable section that contains the logic of the function .
- The END keyword marks the end of the function body .

An example of a stored function that calculates the factorial of a given number is as follows:

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
END;
```

To execute a stored function, you can use one of the following methods:

- Use the function in a SQL statement, such as SELECT, INSERT, UPDATE, or DELETE.
- Use the function in a PL/SQL expression, such as an assignment, a conditional, or a loop.
- Use the function in a PL/SQL procedure or another function.
- Use the function in a Java program by using the CallableStatement interface.

An example of using the factorial function in a SQL statement is as follows:

```sql
SELECT factorial(5) FROM dual;
```

The output is:

```sql
FACTORIAL(5)
------------
120
```