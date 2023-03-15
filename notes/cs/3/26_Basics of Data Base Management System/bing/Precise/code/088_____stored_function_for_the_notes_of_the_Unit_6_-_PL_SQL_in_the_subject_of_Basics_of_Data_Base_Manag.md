### Stored Function

A stored function is a subprogram that is stored in the database and can be invoked by other programs. It is similar to a stored procedure, but with the following differences:

1. A stored function must return a value, while a stored procedure does not have to.
2. A stored function can be used in a SELECT statement, while a stored procedure cannot.
3. A stored function can be used in an expression, while a stored procedure cannot.

Here is an example of a stored function that calculates the factorial of a given number:

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
END;
```

This function can be invoked in a SELECT statement as follows:

```sql
SELECT factorial(5) FROM DUAL;
```

This will return the value 120, which is the factorial of 5.

Stored functions can be useful for encapsulating complex calculations or business logic that needs to be reused in multiple places. They can also help improve the performance of queries by reducing the amount of data that needs to be transferred between the database and the application.