## Unit 6 - Creating Procedures and Functions

Procedures and functions are subprograms that can be used to modularize and reuse code. They are similar in many ways, but there are some key differences between them.

### Procedures
- A procedure is a subprogram that performs a specific action.
- It does not return a value.
- It is called using a procedure call statement.
- It can have input parameters, which are passed by value or by reference.
- It can have output parameters, which are used to return values to the calling program.

### Functions
- A function is a subprogram that calculates and returns a value.
- It is called using a function call expression.
- It can have input parameters, which are passed by value or by reference.
- It cannot have output parameters.
- The value returned by the function is determined by the return statement.

### Creating Procedures and Functions
- Procedures and functions are created using the `CREATE PROCEDURE` and `CREATE FUNCTION` statements, respectively.
- The body of the procedure or function is defined using a `BEGIN ... END` block.
- Input parameters are defined using the `IN` keyword, and output parameters are defined using the `OUT` keyword.
- The data type of the parameters and the return value of a function must be specified.

### Example
Here is an example of a simple procedure that takes two input parameters and returns their sum as an output parameter:

```sql
CREATE PROCEDURE add_numbers(IN a INT, IN b INT, OUT sum INT)
BEGIN
    SET sum = a + b;
END
```

Here is an example of a simple function that takes two input parameters and returns their sum:

```sql
CREATE FUNCTION add_numbers(a INT, b INT) RETURNS INT
BEGIN
    RETURN a + b;
END
```

### Calling Procedures and Functions
- Procedures are called using the `CALL` statement.
- Functions are called using a function call expression, which can be used in a SELECT statement or an assignment statement.

### Example
Here is an example of calling the `add_numbers` procedure and function defined above:

```sql
-- calling the procedure
CALL add_numbers(1, 2, @sum);
SELECT @sum;

-- calling the function
SELECT add_numbers(1, 2);
SET @sum = add_numbers(1, 2);
```

In this example, the `add_numbers` procedure is called using the `CALL` statement, and the result is stored in the `@sum` user variable. The `add_numbers` function is called using a function call expression, and the result is returned directly or stored in the `@sum` user variable.