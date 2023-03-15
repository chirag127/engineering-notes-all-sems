# Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value directly like a function.
- A procedure can be invoked by other PL/SQL blocks, procedures, functions, triggers, or applications written in different languages such as Java, PHP, etc.
- A procedure can be created using the CREATE PROCEDURE statement, which has the following syntax:

```sql
CREATE [OR REPLACE] PROCEDURE procedure_name
[(parameter1 [mode] datatype [DEFAULT expr],
  parameter2 [mode] datatype [DEFAULT expr],
  ...)]
IS | AS
  [local declarations]
BEGIN
  [executable statements]
[EXCEPTION
  [exception handlers]]
END [procedure_name];
```

- The CREATE OR REPLACE option allows to modify an existing procedure without dropping it.
- The procedure name must be unique within the schema and follow the naming rules of SQL identifiers.
- The parameters can be of three modes: IN, OUT, or IN OUT. The IN parameters are used to pass values to the procedure, the OUT parameters are used to return values from the procedure, and the IN OUT parameters are used to do both. The mode defaults to IN if not specified.
- The datatype of the parameters can be any valid PL/SQL datatype, such as NUMBER, VARCHAR2, DATE, BOOLEAN, etc. The DEFAULT option allows to assign a default value to the parameter if it is not passed by the caller.
- The IS or AS keyword marks the beginning of the procedure body, which consists of three optional sections: local declarations, executable statements, and exception handlers.
- The local declarations section is used to declare and initialize local variables, constants, cursors, and other PL/SQL constructs that are only visible within the procedure.
- The executable statements section is used to write the PL/SQL logic that performs the task of the procedure. It can include SQL statements, control structures, loops, assignments, calls to other subprograms, etc.
- The exception handlers section is used to handle any errors or exceptions that may occur during the execution of the procedure. It can include predefined or user-defined exceptions, and use the RAISE, RAISE_APPLICATION_ERROR, or PRAGMA EXCEPTION_INIT statements to raise or handle them.
- The END keyword marks the end of the procedure body, which can be optionally followed by the procedure name for clarity.

- To execute a procedure, it can be called by using the EXECUTE or EXEC command, or by using the procedure name followed by parentheses and the actual parameters, if any. For example:

```sql
EXECUTE adjust_salary(100, 10); -- using EXECUTE command
adjust_salary(100, 10); -- using procedure name
```

- To view the source code of a procedure, it can be queried from the USER_SOURCE, ALL_SOURCE, or DBA_SOURCE data dictionary views, depending on the privileges of the user. For example:

```sql
SELECT text FROM user_source
WHERE name = 'ADJUST_SALARY'
ORDER BY line;
```

- To drop a procedure, it can be deleted by using the DROP PROCEDURE statement, which has the following syntax:

```sql
DROP PROCEDURE procedure_name;
```

- To modify a procedure, it can be altered by using the CREATE OR REPLACE PROCEDURE statement, which will replace the existing procedure with the new one. Alternatively, it can be dropped and recreated with the new code. For example:

```sql
CREATE OR REPLACE PROCEDURE adjust_salary
(emp_id IN NUMBER, percentage IN NUMBER)
IS
  new_salary NUMBER;
BEGIN
  SELECT salary * (1 + percentage/100) INTO new_salary
  FROM employees
  WHERE employee_id = emp_id;
  
  UPDATE employees
  SET salary = new_salary
  WHERE employee_id = emp_id;
  
  DBMS_OUTPUT.PUT_LINE('Salary adjusted for employee ' || emp_id);
EXCEPTION
  WHEN NO_DATA_FOUND THEN
    RAISE_APPLICATION_ERROR(-20001, 'Invalid employee id');
END adjust_salary;
```