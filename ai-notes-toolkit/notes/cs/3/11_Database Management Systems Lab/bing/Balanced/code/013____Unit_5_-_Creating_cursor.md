## Unit 5 - Creating cursor

- A cursor is a temporary work area created in the system memory when a SQL statement is executed.
- A cursor contains information on a select statement and the rows of data accessed by it.
- A cursor can be used to retrieve one or more rows of data and perform operations on them.
- A cursor can be either implicit or explicit.
- An implicit cursor is automatically created by Oracle whenever a SQL statement is executed, when there is no explicit cursor for the statement.
- An explicit cursor is created by the programmer to gain more control over the query execution and result handling.
- An explicit cursor has four attributes: `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN` that can be used to check the status of the cursor execution.
- An explicit cursor is defined using the `CURSOR` keyword, followed by a name, a parameter list (optional), and a query.
- An explicit cursor is opened using the `OPEN` statement, which allocates memory for the cursor and executes the query.
- An explicit cursor is fetched using the `FETCH` statement, which retrieves the next row of data from the cursor into a record or a list of variables.
- An explicit cursor is closed using the `CLOSE` statement, which releases the memory allocated for the cursor and marks it as invalid.
- An example of creating and using an explicit cursor is shown below:

```sql
-- Declare a cursor named c_emp to retrieve the employee details
CURSOR c_emp IS
  SELECT empno, ename, sal, deptno
  FROM emp
  WHERE deptno = 10;

-- Declare a record type to store the fetched data
emp_rec c_emp%ROWTYPE;

-- Open the cursor
OPEN c_emp;

-- Fetch the first row of data from the cursor into the record
FETCH c_emp INTO emp_rec;

-- Loop through the remaining rows of data until no more rows are found
WHILE c_emp%FOUND LOOP
  -- Display the employee details
  DBMS_OUTPUT.PUT_LINE(emp_rec.empno || ' ' || emp_rec.ename || ' ' || emp_rec.sal || ' ' || emp_rec.deptno);
  -- Fetch the next row of data from the cursor into the record
  FETCH c_emp INTO emp_rec;
END LOOP;

-- Close the cursor
CLOSE c_emp;
```