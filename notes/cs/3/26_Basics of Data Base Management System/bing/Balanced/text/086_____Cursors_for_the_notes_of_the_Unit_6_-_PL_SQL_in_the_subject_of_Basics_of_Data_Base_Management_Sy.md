### Cursors

A cursor is a pointer to a result set, or the data that results from a query. Cursors let you fetch one or more rows from the database into memory, process them, and then either commit or roll back those changes.

There are two types of cursors in PL/SQL: implicit and explicit.

- Implicit cursors are automatically created by Oracle whenever an SQL statement is executed. You can access the attributes of an implicit cursor using the SQL prefix. For example, SQL%ROWCOUNT returns the number of rows affected by the last SQL statement.
- Explicit cursors are user-defined cursors that allow you to name and control the result set of a query. You can declare, open, fetch, and close an explicit cursor using PL/SQL statements. You can also define parameters for an explicit cursor and use them in the query.

Some advantages of using explicit cursors are:

- You can fetch the rows of the result set one by one or in bulk.
- You can perform complex logic on each row of the result set.
- You can use the same query with different parameters to get different result sets.
- You can handle exceptions that may occur during the execution of the query.

Some examples of explicit cursor declarations are:

- `DECLARE CURSOR c_emp IS SELECT * FROM employees;` -- This declares a cursor named c_emp that selects all rows from the employees table.
- `DECLARE CURSOR c_dept (p_deptno NUMBER) IS SELECT * FROM departments WHERE department_id = p_deptno;` -- This declares a cursor named c_dept that takes a parameter p_deptno and selects all rows from the departments table where the department_id matches the parameter value.
- `DECLARE CURSOR c_sal IS SELECT last_name, salary FROM employees FOR UPDATE;` -- This declares a cursor named c_sal that selects the last_name and salary columns from the employees table and locks the rows for update.