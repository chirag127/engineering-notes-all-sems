## Unit 7 - Creating packages and triggers

In this unit, you will learn how to create packages and triggers in Oracle Database. Packages and triggers are two types of PL/SQL program units that can enhance the functionality and performance of your database applications.

### Packages

A package is a collection of related PL/SQL objects, such as procedures, functions, variables, constants, cursors, and types, that are stored together in the database. A package has two parts: a specification and a body. The specification declares the public objects that can be accessed by other program units, while the body defines the private objects and the implementation of the public objects.

Some benefits of using packages are:

- Modularity: You can organize your PL/SQL code into logical groups of related objects that are easier to maintain and reuse.
- Performance: You can improve the execution speed of your PL/SQL code by loading the entire package into memory once, rather than loading each object separately.
- Information hiding: You can hide the implementation details of your PL/SQL objects from other program units by declaring them as private in the package body.
- Overloading: You can define multiple procedures or functions with the same name but different parameters in the same package, which allows you to use the same name for different operations.
- Persistent state: You can declare variables and cursors in the package specification that retain their values across multiple calls to the package objects, which allows you to share data among different program units.

To create a package, you use the CREATE PACKAGE and CREATE PACKAGE BODY statements. For example, the following code creates a package named EMP_PKG that contains a procedure to insert a new employee record and a function to calculate the salary of an employee:

```sql
-- Create the package specification
CREATE PACKAGE emp_pkg AS
  -- Declare the public objects
  PROCEDURE insert_emp (p_empno NUMBER, p_ename VARCHAR2, p_job VARCHAR2, p_mgr NUMBER, p_hiredate DATE, p_sal NUMBER, p_comm NUMBER, p_deptno NUMBER);
  FUNCTION calc_sal (p_empno NUMBER) RETURN NUMBER;
END emp_pkg;
/

-- Create the package body
CREATE PACKAGE BODY emp_pkg AS
  -- Declare the private objects
  CURSOR emp_cur IS SELECT * FROM emp;
  v_raise CONSTANT NUMBER := 1.1;
  
  -- Define the public objects
  PROCEDURE insert_emp (p_empno NUMBER, p_ename VARCHAR2, p_job VARCHAR2, p_mgr NUMBER, p_hiredate DATE, p_sal NUMBER, p_comm NUMBER, p_deptno NUMBER) IS
  BEGIN
    INSERT INTO emp VALUES (p_empno, p_ename, p_job, p_mgr, p_hiredate, p_sal, p_comm, p_deptno);
  END insert_emp;
  
  FUNCTION calc_sal (p_empno NUMBER) RETURN NUMBER IS
    v_sal NUMBER;
  BEGIN
    SELECT sal INTO v_sal FROM emp WHERE empno = p_empno;
    RETURN v_sal * v_raise;
  END calc_sal;
END emp_pkg;
/
```

To call the package objects, you use the dot notation with the package name and the object name. For example, the following code calls the insert_emp procedure and the calc_sal function from the EMP_PKG package:

```sql
-- Call the insert_emp procedure
BEGIN
  emp_pkg.insert_emp(8000, 'SCOTT', 'ANALYST', 7566, SYSDATE, 3000, NULL, 20);
END;
/

-- Call the calc_sal function
DECLARE
  v_new_sal NUMBER;
BEGIN
  v_new_sal := emp_pkg.calc_sal(8000);
  DBMS_OUTPUT.PUT_LINE('New salary of SCOTT is ' || v_new_sal);
END;
/
```

### Triggers

A trigger is a PL/SQL block or a stored procedure that is automatically executed by the database in response to certain events, such as DML statements, DDL statements, database errors, or user-defined events. A trigger can be used to enforce business rules, audit data changes, maintain derived values, or perform complex validations.

Some characteristics of triggers are:

- A trigger is associated with a specific table, view, schema, or database.
- A trigger can be fired either before or after the triggering event, or instead of the triggering event for DML statements on views.
- A trigger can be fired either for each row affected by the triggering event, or once for the entire statement.
- A trigger can access the old and new values of the columns involved in the triggering event by using the :OLD and :NEW qualifiers.
- A trigger can use the SQL%ROWCOUNT, SQL%FOUND, SQL%NOTFOUND, and SQL%ISOPEN attributes to check