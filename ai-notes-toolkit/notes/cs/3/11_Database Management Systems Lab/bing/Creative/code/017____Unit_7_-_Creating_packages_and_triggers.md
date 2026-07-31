## Unit 7 - Creating packages and triggers

In this unit, you will learn how to create packages and triggers in Oracle Database.

### Packages

- A package is a collection of related procedures, functions, variables, constants, cursors, and types that are stored together in the database.
- A package has two parts: a specification and a body. The specification declares the public elements of the package that can be accessed by other programs. The body defines the implementation of the package elements and can also contain private elements that are only visible within the package.
- A package can provide several benefits, such as:
  - Modularity: A package can group related functionality into a single unit, making it easier to maintain and reuse.
  - Performance: A package can reduce the overhead of parsing and loading subprograms, as they are loaded into memory once when the package is first referenced.
  - Information hiding: A package can hide the implementation details of its elements from other programs, allowing for better security and flexibility.
  - Overloading: A package can contain subprograms with the same name but different parameters, allowing for different versions of the same functionality.
- To create a package, you use the CREATE PACKAGE and CREATE PACKAGE BODY statements. For example:

```sql
-- Create the package specification
CREATE PACKAGE math_pkg AS
  -- Declare a constant
  pi CONSTANT NUMBER := 3.14159;
  -- Declare a function
  FUNCTION square (x NUMBER) RETURN NUMBER;
  -- Declare a procedure
  PROCEDURE swap (x IN OUT NUMBER, y IN OUT NUMBER);
END math_pkg;
/

-- Create the package body
CREATE PACKAGE BODY math_pkg AS
  -- Define the function
  FUNCTION square (x NUMBER) RETURN NUMBER IS
  BEGIN
    RETURN x * x;
  END square;
  -- Define the procedure
  PROCEDURE swap (x IN OUT NUMBER, y IN OUT NUMBER) IS
    temp NUMBER;
  BEGIN
    temp := x;
    x := y;
    y := temp;
  END swap;
END math_pkg;
/
```

- To use a package element, you prefix it with the package name. For example:

```sql
-- Use the constant
DECLARE
  area NUMBER;
BEGIN
  area := math_pkg.pi * math_pkg.square(10);
  DBMS_OUTPUT.PUT_LINE('Area = ' || area);
END;
/

-- Use the procedure
DECLARE
  a NUMBER := 1;
  b NUMBER := 2;
BEGIN
  DBMS_OUTPUT.PUT_LINE('Before swap: a = ' || a || ', b = ' || b);
  math_pkg.swap(a, b);
  DBMS_OUTPUT.PUT_LINE('After swap: a = ' || a || ', b = ' || b);
END;
/
```

### Triggers

- A trigger is a named PL/SQL block that is stored in the database and executed automatically when a certain event occurs, such as inserting, updating, or deleting a row in a table.
- A trigger can perform various actions, such as:
  - Enforcing complex business rules or data integrity constraints that cannot be expressed by declarative constraints.
  - Auditing or logging changes to the data or the database.
  - Generating derived column values or sequence numbers.
  - Implementing complex security or access control policies.
  - Sending alerts or notifications to other applications or users.
- To create a trigger, you use the CREATE TRIGGER statement. For example:

```sql
-- Create a trigger that logs changes to the employees table
CREATE TRIGGER emp_audit_trg
  AFTER INSERT OR UPDATE OR DELETE ON employees
  FOR EACH ROW
BEGIN
  -- Insert a record into the audit table
  INSERT INTO emp_audit (emp_id, action, old_sal, new_sal, audit_date)
  VALUES (:OLD.employee_id, -- The old value of the employee_id column
          CASE WHEN INSERTING THEN 'INSERT'
               WHEN UPDATING THEN 'UPDATE'
               WHEN DELETING THEN 'DELETE'
          END, -- The type of action
          :OLD.salary, -- The old value of the salary column
          :NEW.salary, -- The new value of the salary column
          SYSDATE); -- The current date and time
END;
/
```

- To use a trigger, you simply perform the triggering event. For example:

```sql
-- Insert a new employee
INSERT INTO employees (employee_id, first_name, last_name, email, hire_date, job_id, salary)
VALUES (999, 'Sydney', 'AI', 'sydney@ai.com', SYSDATE, 'IT_PROG', 10000);

-- Update the salary of an existing employee
UPDATE employees
SET salary = salary * 1.1

```
