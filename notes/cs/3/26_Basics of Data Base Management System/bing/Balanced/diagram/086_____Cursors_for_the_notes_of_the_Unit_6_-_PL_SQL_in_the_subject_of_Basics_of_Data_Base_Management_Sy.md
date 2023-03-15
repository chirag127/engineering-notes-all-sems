### Cursors

A cursor is a pointer to a result set, or the data that results from a query. Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.

There are two types of cursors in PL/SQL: implicit and explicit.

- Implicit cursors are automatically created by Oracle whenever an SQL statement is executed. You can refer to the most recent implicit cursor as the SQL cursor, which has attributes such as %FOUND, %ISOPEN, %NOTFOUND, and %ROWCOUNT.
- Explicit cursors are user-defined cursors that allow you to name, open, fetch, and close them. You can use explicit cursors to perform complex queries that return more than one row, or to process each row individually.

To declare an explicit cursor, you use the CURSOR keyword followed by the cursor name and the query. For example:

```sql
CURSOR c_emp IS
  SELECT * FROM employees;
```

To open an explicit cursor, you use the OPEN statement followed by the cursor name. For example:

```sql
OPEN c_emp;
```

To fetch data from an explicit cursor, you use the FETCH statement followed by the cursor name and the INTO clause. For example:

```sql
FETCH c_emp INTO emp_rec;
```

To close an explicit cursor, you use the CLOSE statement followed by the cursor name. For example:

```sql
CLOSE c_emp;
```

You can also use a cursor FOR loop to simplify the process of opening, fetching, and closing an explicit cursor. For example:

```sql
FOR emp_rec IN c_emp LOOP
  -- do something with emp_rec
END LOOP;
```

You can also use dynamic SQL to create and execute SQL statements at run time. Dynamic SQL allows you to use variables, parameters, or user input to construct SQL statements. You can use the EXECUTE IMMEDIATE statement to execute a dynamic SQL statement, or use the DBMS_SQL package to create and manipulate cursors dynamically. For example:

```sql
-- using EXECUTE IMMEDIATE
sql_stmt := 'UPDATE employees SET salary = salary * 1.1 WHERE employee_id = :id';
EXECUTE IMMEDIATE sql_stmt USING emp_id;

-- using DBMS_SQL
sql_stmt := 'SELECT * FROM employees';
c := DBMS_SQL.OPEN_CURSOR;
DBMS_SQL.PARSE(c, sql_stmt, DBMS_SQL.NATIVE);
DBMS_SQL.DEFINE_COLUMN(c, 1, emp_id);
DBMS_SQL.DEFINE_COLUMN(c, 2, emp_name);
DBMS_SQL.DEFINE_COLUMN(c, 3, emp_salary);
rows := DBMS_SQL.EXECUTE(c);
LOOP
  IF DBMS_SQL.FETCH_ROWS(c) > 0 THEN
    DBMS_SQL.COLUMN_VALUE(c, 1, emp_id);
    DBMS_SQL.COLUMN_VALUE(c, 2, emp_name);
    DBMS_SQL.COLUMN_VALUE(c, 3, emp_salary);
    -- do something with emp_id, emp_name, and emp_salary
  ELSE
    EXIT;
  END IF;
END LOOP;
DBMS_SQL.CLOSE_CURSOR(c);
```