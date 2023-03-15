### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can have parameters that allow passing values to and from the procedure.
- A procedure can be invoked by other PL/SQL blocks, such as triggers, functions, or other procedures, or by external applications, such as Java, PHP, or .NET.
- A procedure can return a value to the caller using the RETURN statement, or by using an OUT or IN OUT parameter.
- A procedure can also raise exceptions to handle errors or abnormal situations.

#### Syntax of a procedure

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT value],
  parameter2 [mode] datatype [DEFAULT value],
  ...)]
IS
  [declaration_section]
BEGIN
  [executable_section]
[EXCEPTION
  [exception_section]]
END [procedure_name];
```

- The CREATE OR REPLACE clause allows replacing an existing procedure with a new one.
- The parameter list contains the names, modes, and data types of the parameters. The mode can be IN, OUT, or IN OUT, indicating the direction of the parameter. The default mode is IN. The DEFAULT value specifies a default value for the parameter if none is passed by the caller.
- The IS keyword separates the header and the body of the procedure.
- The declaration section contains the declarations of local variables, constants, cursors, and other items that are used in the procedure.
- The executable section contains the PL/SQL statements that perform the logic of the procedure.
- The EXCEPTION keyword introduces the exception section, which handles the errors or exceptions that may occur during the execution of the procedure.
- The END keyword marks the end of the procedure. Optionally, the procedure name can be repeated after the END keyword for clarity.

#### Example of a procedure

The following example creates a procedure named adjust_salary that increases the salary of an employee by a given percentage.

```sql
CREATE OR REPLACE PROCEDURE adjust_salary
(p_emp_id IN employees.employee_id%TYPE,
 p_percent IN NUMBER)
IS
  v_salary employees.salary%TYPE;
BEGIN
  SELECT salary INTO v_salary
  FROM employees
  WHERE employee_id = p_emp_id;
  
  UPDATE employees
  SET salary = v_salary * (1 + p_percent/100)
  WHERE employee_id = p_emp_id;
  
  COMMIT;
  
  DBMS_OUTPUT.PUT_LINE('Salary adjusted for employee ' || p_emp_id);
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    DBMS_OUTPUT.PUT_LINE('Employee not found');
  WHEN OTHERS THEN
    DBMS_OUTPUT.PUT_LINE('Error occurred: ' || SQLERRM);
    ROLLBACK;
END adjust_salary;
```

#### Calling a procedure

A procedure can be called by using the EXECUTE or EXEC command, or by using the procedure name in a PL/SQL block.

For example, to call the adjust_salary procedure, we can use the following commands:

```sql
EXECUTE adjust_salary(100, 10); -- increase salary of employee 100 by 10%
EXEC adjust_salary(101, 15); -- increase salary of employee 101 by 15%
```

Or, we can use the following PL/SQL block:

```sql
BEGIN
  adjust_salary(102, 20); -- increase salary of employee 102 by 20%
END;
/
```