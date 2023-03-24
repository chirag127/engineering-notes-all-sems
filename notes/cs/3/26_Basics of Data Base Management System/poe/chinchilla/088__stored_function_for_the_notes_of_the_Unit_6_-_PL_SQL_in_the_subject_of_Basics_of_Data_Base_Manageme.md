### Stored Function

A stored function is a named PL/SQL block that returns a single value or a collection of values. It can be used in SQL statements or other PL/SQL blocks.

#### Creating a Stored Function

To create a stored function, the following syntax can be used:

```sql
CREATE [OR REPLACE] FUNCTION function_name
    [(parameter1 [IN | OUT | IN OUT] datatype [, parameter2 ...])]
RETURN return_datatype
IS
    [local_variable_declarations]
BEGIN
    executable_statements
    [EXCEPTION
        exception_handlers]
END [function_name];
```

- The `CREATE FUNCTION` statement is used to create a new stored function.
- The `OR REPLACE` keyword is optional and can be used to modify an existing function.
- `function_name` is the name of the function.
- `parameter1, parameter2` are the input parameters of the function. They can be of type `IN`, `OUT`, or `IN OUT`.
- `datatype` is the data type of the parameter.
- `return_datatype` is the data type of the value returned by the function.
- `local_variable_declarations` are the variables declared within the function.
- `executable_statements` are the actual PL/SQL code that performs the desired operations.
- `EXCEPTION` is an optional block that handles exceptions that may occur within the function.

#### Invoking a Stored Function

To call a stored function, the following syntax can be used:

```sql
SELECT function_name(parameter1, parameter2, ...);
```

- `function_name` is the name of the function.
- `parameter1, parameter2` are the input parameters of the function.

#### Example

Here is an example of a stored function that returns the average salary of all employees in a given department:

```sql
CREATE OR REPLACE FUNCTION avg_salary(department_id IN NUMBER)
RETURN NUMBER
IS
    total_salary NUMBER := 0;
    employee_count NUMBER := 0;
BEGIN
    FOR emp IN (SELECT * FROM employees WHERE department_id = department_id) LOOP
        total_salary := total_salary + emp.salary;
        employee_count := employee_count + 1;
    END LOOP;
    RETURN total_salary / employee_count;
END avg_salary;
```

To call this function and get the average salary for department 10, the following SQL statement can be used:

```sql
SELECT avg_salary(10) FROM dual;
```

This will return the average salary for department 10.