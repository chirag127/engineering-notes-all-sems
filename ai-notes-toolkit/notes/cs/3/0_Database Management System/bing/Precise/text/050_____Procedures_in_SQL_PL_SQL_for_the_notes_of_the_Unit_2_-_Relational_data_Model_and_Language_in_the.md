### Procedures in SQL/PL SQL

A procedure is a subprogram that performs a specific action. It is written in PL/SQL, which is a procedural language extension for SQL. Procedures are stored in the database and can be invoked by other programs or applications.

Here are some key points to remember about procedures in SQL/PL SQL:

1. Procedures are created using the `CREATE PROCEDURE` statement.
2. The procedure body is enclosed in the `IS` or `AS` keyword and the `BEGIN` and `END` keywords.
3. Procedures can have parameters, which are specified in the procedure header using the `IN`, `OUT`, or `IN OUT` keywords.
4. Procedures can contain SQL statements, PL/SQL statements, and control structures such as loops and conditional statements.
5. Procedures can be invoked using the `EXECUTE` or `CALL` statements, or by using the procedure name in an SQL statement.
6. Procedures can return values using the `RETURN` statement or through `OUT` parameters.
7. Procedures can be dropped using the `DROP PROCEDURE` statement.

Here is an example of a simple procedure that inserts a new record into a table:

```sql
CREATE PROCEDURE add_employee (p_name IN VARCHAR2, p_salary IN NUMBER)
IS
BEGIN
    INSERT INTO employees (name, salary)
    VALUES (p_name, p_salary);
END;
```

This procedure takes two parameters: `p_name` and `p_salary`, which are used to insert a new record into the `employees` table. To invoke this procedure, you can use the following statement:

```sql
EXECUTE add_employee('John Doe', 5000);
```

This will insert a new record into the `employees` table with the name 'John Doe' and a salary of 5000.