### Stored Function

Stored Function is a subprogram that is stored in a database and can be called by a program. It is a reusable unit of code that performs a specific task and returns a single value. Stored functions are used to encapsulate complex business logic and perform calculations within a database.

#### Syntax

```
CREATE OR REPLACE FUNCTION function_name
(parameter_name datatype [, parameter_name datatype...])
RETURN return_datatype
IS
    variable_declaration
BEGIN
    statement(s);
    RETURN expression;
END;
```

#### Explanation

- `CREATE OR REPLACE FUNCTION` is used to create or replace a stored function.
- `function_name` is the name of the function.
- `parameter_name` is the name of the input parameter.
- `datatype` is the data type of the parameter.
- `RETURN` is used to specify the data type of the function return value.
- `IS` is used to begin the function block.
- `variable_declaration` is used to declare local variables.
- `BEGIN` is used to begin the executable section of the function.
- `statement(s)` is used to define the logic of the function.
- `RETURN` is used to return a single value from the function.
- `expression` is the value returned by the function.

#### Example

```
CREATE OR REPLACE FUNCTION calculate_salary
(salary NUMBER, bonus NUMBER)
RETURN NUMBER
IS
    total_salary NUMBER;
BEGIN
    total_salary := salary + bonus;
    RETURN total_salary;
END;
```

#### Advantages

- Reusability: Stored functions are reusable modules of code that can be used in multiple applications.
- Encapsulation: Stored functions encapsulate complex business logic and hide it from the user.
- Performance: Stored functions can improve performance by reducing the number of calls to the database.

#### Disadvantages

- Complexity: Stored functions can be complex and difficult to debug.
- Limited functionality: Stored functions can only return a single value, which limits their functionality.

#### Applications

Stored functions are commonly used in database applications to perform various tasks, such as:

- Data validation
- Data transformation
- Data aggregation
- Calculation of complex business logic

#### Conclusion

Stored functions are a powerful feature of PL/SQL that can be used to encapsulate complex business logic and improve performance. By using stored functions, developers can create reusable modules of code that can be used in multiple applications.