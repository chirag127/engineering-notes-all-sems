Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 6 - Creating procedure and functions.

## Unit 6 - Creating procedure and functions

- A procedure is a set of statements that performs a specific task or action. A function is a set of statements that returns a value or a result.
- Procedures and functions are useful for modularizing and reusing code, improving readability and maintainability, and reducing complexity and errors.
- In SQL, procedures and functions are stored in the database as objects that can be invoked by other SQL statements or applications.
- The syntax for creating a procedure in SQL is:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name (parameter_list)
[ AUTHID { DEFINER | CURRENT_USER } ]
[ { IS | AS } ]
BEGIN
  -- procedure body
END [ procedure_name ];
```

- The syntax for creating a function in SQL is:

```sql
CREATE [OR REPLACE] FUNCTION function_name (parameter_list)
RETURN return_datatype
[ AUTHID { DEFINER | CURRENT_USER } ]
[ { IS | AS } ]
BEGIN
  -- function body
  RETURN return_value;
END [ function_name ];
```

- The parameter_list consists of zero or more parameters, each with a name, a data type, and an optional mode (IN, OUT, or IN OUT). The default mode is IN, which means the parameter can only be used as an input value. The OUT mode means the parameter can only be used as an output value. The IN OUT mode means the parameter can be used as both input and output value.
- The return_datatype specifies the data type of the value that the function returns. The return_value is an expression that evaluates to the return_datatype.
- The AUTHID clause determines whether the procedure or function executes with the privileges of the owner (DEFINER) or the caller (CURRENT_USER). The default is DEFINER.
- The IS or AS keyword separates the header and the body of the procedure or function. The body consists of a BEGIN-END block that contains the executable statements of the procedure or function.
- To invoke a procedure, use the EXECUTE or CALL statement, followed by the procedure name and the argument list. To invoke a function, use the function name and the argument list as part of an expression in a SQL statement. For example:

```sql
-- invoke a procedure
EXECUTE add_employee(101, 'John', 'Smith', 5000);

-- invoke a function
SELECT get_salary(101) FROM dual;
```

- To drop a procedure or a function, use the DROP statement, followed by the object type and the name. For example:

```sql
-- drop a procedure
DROP PROCEDURE add_employee;

-- drop a function
DROP FUNCTION get_salary;
```