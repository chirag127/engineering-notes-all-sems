# Procedures in SQL/PL SQL

- A procedure is a named PL/SQL block that can be stored in the database and can be invoked by name  .
- A procedure can perform a specific task or a series of tasks, such as inserting, updating, deleting, or querying data .
- A procedure can have parameters that can be passed by the caller or the invoker  .
- A procedure can return values to the caller through output parameters or variables  .
- A procedure can be invoked by other procedures, functions, triggers, or applications  .

## Syntax of a procedure

- A procedure has a header and a body  .
- The header consists of the keyword PROCEDURE, followed by the procedure name, followed by a list of parameters in parentheses  .
- The body consists of the keyword IS or AS, followed by the declaration section, the executable section, and the optional exception-handling section  .
- The declaration section declares the variables, constants, cursors, and user-defined exceptions that are used in the procedure  .
- The executable section contains the PL/SQL statements that perform the logic of the procedure  .
- The exception-handling section handles the errors that may occur during the execution of the procedure  .

## Example of a procedure

- The following example shows a procedure named adjust_salary that accepts an employee ID and a percentage as input parameters and updates the salary of the employee by the given percentage .

```sql
CREATE OR REPLACE PROCEDURE adjust_salary (
  p_emp_id IN employees.employee_id%TYPE,
  p_percentage IN NUMBER
) IS
BEGIN
  UPDATE employees
  SET salary = salary * (1 + p_percentage/100)
  WHERE employee_id = p_emp_id;
END adjust_salary;
/
```

## Calling a procedure

- A procedure can be called by using the keyword EXECUTE or EXEC, followed by the procedure name and the arguments in parentheses .
- The arguments can be literals, variables, expressions, or placeholders .
- The arguments must match the number, order, and data type of the parameters in the procedure .

## Example of calling a procedure

- The following example shows how to call the adjust_salary procedure with different arguments .

```sql
-- Call the procedure with literals
EXECUTE adjust_salary(100, 10);

-- Call the procedure with variables
DECLARE
  v_emp_id employees.employee_id%TYPE := 101;
  v_percentage NUMBER := 15;
BEGIN
  adjust_salary(v_emp_id, v_percentage);
END;
/

-- Call the procedure with expressions
EXECUTE adjust_salary(102, 5 + 2);

-- Call the procedure with placeholders
EXECUTE adjust_salary(:emp_id, :percentage);
```