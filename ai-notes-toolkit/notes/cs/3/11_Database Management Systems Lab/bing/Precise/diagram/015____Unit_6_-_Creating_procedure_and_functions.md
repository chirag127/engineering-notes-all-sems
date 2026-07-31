## Unit 6 - Creating Procedures and Functions

Procedures and functions are subprograms that can be used to modularize and reuse code. They are both named PL/SQL blocks that can accept parameters and be invoked. However, there are some differences between them:

1. **Procedures** are subprograms that perform a specific action. They can return values to the calling program through output parameters, but they do not have a return value.

2. **Functions** are subprograms that compute and return a value. They must have a return statement that specifies the value to be returned.

Here are some key points to remember when creating procedures and functions:

- The `CREATE PROCEDURE` or `CREATE FUNCTION` statement is used to create a procedure or function.
- The `IS` or `AS` keyword is used to begin the declarative section of the subprogram.
- The `BEGIN` keyword is used to begin the executable section of the subprogram.
- The `END` keyword is used to end the subprogram.
- Parameters can be passed to the subprogram using the `IN`, `OUT`, or `IN OUT` mode.
- The `RETURN` statement is used to return a value from a function.

Example of creating a procedure:

```sql
CREATE PROCEDURE my_procedure (p_param1 IN NUMBER, p_param2 OUT NUMBER)
IS
    v_local_variable NUMBER;
BEGIN
    v_local_variable := p_param1 * 2;
    p_param2 := v_local_variable;
END;
```

Example of creating a function:

```sql
CREATE FUNCTION my_function (p_param1 IN NUMBER) RETURN NUMBER
IS
    v_local_variable NUMBER;
BEGIN
    v_local_variable := p_param1 * 2;
    RETURN v_local_variable;
END;
```