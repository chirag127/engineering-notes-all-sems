## Unit 5 - Creating cursor

- A cursor is a temporary work area created in the system memory when a SQL statement is executed.
- A cursor contains information on a select statement and the rows of data accessed by it.
- A cursor can be used to manipulate data in a row-by-row manner.
- There are two types of cursors: implicit and explicit.
- An implicit cursor is automatically created by Oracle whenever a SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is a cursor that is defined by the programmer in the declaration section of a PL/SQL block.
- An explicit cursor can be used to process multiple rows returned by a select statement.
- An explicit cursor has four attributes: %FOUND, %NOTFOUND, %ISOPEN, and %ROWCOUNT.
- An explicit cursor can be created using the following steps:
  - Declare the cursor in the declaration section of the PL/SQL block using the CURSOR keyword and a select statement.
  - Open the cursor in the executable section of the PL/SQL block using the OPEN statement.
  - Fetch the data from the cursor into variables or records using the FETCH statement.
  - Close the cursor in the executable section of the PL/SQL block using the CLOSE statement.
- An example of creating an explicit cursor is:

```sql
DECLARE
  CURSOR c_emp IS
    SELECT empno, ename, sal FROM emp;
  v_empno NUMBER(4);
  v_ename VARCHAR2(10);
  v_sal NUMBER(7,2);
BEGIN
  OPEN c_emp;
  LOOP
    FETCH c_emp INTO v_empno, v_ename, v_sal;
    EXIT WHEN c_emp%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_empno || ' ' || v_ename || ' ' || v_sal);
  END LOOP;
  CLOSE c_emp;
END;
```