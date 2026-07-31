### Procedures in SQL/PL SQL

- A procedure is a named block of PL/SQL code that can be stored in the database and executed by name.
- A procedure can perform a specific task or a set of related tasks, such as validating data, performing calculations, or manipulating database objects.
- A procedure can accept input parameters and return output parameters, but it cannot return a value like a function.
- A procedure can be invoked by other PL/SQL blocks, triggers, procedures, functions, or applications written in different languages such as Java, PHP, etc.
- A procedure has a header and a body. The header contains the keyword PROCEDURE, the name of the procedure, and the list of parameters in parentheses. The body contains the keyword IS (or AS), the declaration section, the keyword BEGIN, the executable section, and the keyword END.
- A procedure can be created using the CREATE PROCEDURE statement, or using a PL/SQL block with the keyword CREATE OR REPLACE PROCEDURE.
- A procedure can be executed using the EXECUTE statement, or by using the procedure name followed by the list of arguments in parentheses.
- A procedure can be modified using the ALTER PROCEDURE statement, or by using a PL/SQL block with the keyword CREATE OR REPLACE PROCEDURE.
- A procedure can be deleted using the DROP PROCEDURE statement.

Some examples of procedures in SQL/PL SQL are:

- A procedure to increase the salary of an employee by a given percentage:

```sql
CREATE OR REPLACE PROCEDURE adjust_salary (p_emp_id IN NUMBER, p_percent IN NUMBER)
IS
  v_salary NUMBER;
BEGIN
  SELECT salary INTO v_salary FROM employees WHERE employee_id = p_emp_id;
  UPDATE employees SET salary = v_salary * (1 + p_percent/100) WHERE employee_id = p_emp_id;
  COMMIT;
END;
```

- A procedure to display the details of an employee:

```sql
CREATE OR REPLACE PROCEDURE show_employee (p_emp_id IN NUMBER)
IS
  v_first_name VARCHAR2(20);
  v_last_name VARCHAR2(20);
  v_email VARCHAR2(25);
  v_salary NUMBER;
BEGIN
  SELECT first_name, last_name, email, salary INTO v_first_name, v_last_name, v_email, v_salary FROM employees WHERE employee_id = p_emp_id;
  DBMS_OUTPUT.PUT_LINE('Employee ID: ' || p_emp_id);
  DBMS_OUTPUT.PUT_LINE('First Name: ' || v_first_name);
  DBMS_OUTPUT.PUT_LINE('Last Name: ' || v_last_name);
  DBMS_OUTPUT.PUT_LINE('Email: ' || v_email);
  DBMS_OUTPUT.PUT_LINE('Salary: ' || v_salary);
END;
```

- A procedure to insert a new employee into the database:

```sql
CREATE OR REPLACE PROCEDURE add_employee (p_first_name IN VARCHAR2, p_last_name IN VARCHAR2, p_email IN VARCHAR2, p_salary IN NUMBER)
IS
  v_emp_id NUMBER;
BEGIN
  SELECT MAX(employee_id) + 1 INTO v_emp_id FROM employees;
  INSERT INTO employees (employee_id, first_name, last_name, email, salary) VALUES (v_emp_id, p_first_name, p_last_name, p_email, p_salary);
  COMMIT;
END;
```