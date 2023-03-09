 Here is the content in markdown format for the given topic:

### Stored Functions

- A stored function is a named PL/SQL block that performs a task and returns a single value.
- It is similar to a procedure, but it must return a value.
- The return type can be any PL/SQL data type or a record.
- Stored functions can be used in SQL statements, allowing you to extend the functionality of SQL.
- Syntax:

```
CREATE [OR REPLACE] FUNCTION function_name
(parameter_name [IN | OUT | IN OUT] parameter_type,...)
RETURN return_type
IS
/* function body */
BEGIN
   /* function logic */
   RETURN return_value;
END;
```

- Example: A function to calculate the area of a circle based on the radius:

```
CREATE OR REPLACE FUNCTION circle_area (radius IN NUMBER)
RETURN NUMBER
IS
BEGIN
   RETURN pi * radius * radius;
END;
```

- We can then use this function in a SQL statement:

```
SELECT circle_area(5) FROM DUAL;
```

- Advantages:
   - Reusability - can be used multiple times.
   - Modularization - isolates logic.
   - Naming - can be given meaningful names.
   - Information hiding - hides implementation details.
- Disadvantages:
   - Overhead of calling the function.
   - Complexity if many parameters are used.

- Applications:
   - Perform complex calculations.
   - Encapsulate business logic.
   - Format output (e.g. convert number to string).
   - Validate input data.