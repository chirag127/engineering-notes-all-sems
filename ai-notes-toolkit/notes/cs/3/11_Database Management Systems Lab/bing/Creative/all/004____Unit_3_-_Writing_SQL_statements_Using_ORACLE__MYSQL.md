## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- ORACLE and MYSQL are two popular relational database management systems (RDBMS) that use SQL as their query language.
- To write SQL statements using ORACLE or MYSQL, one needs to follow some basic steps:
  - Connect to the database server using a client application, such as SQL*Plus for ORACLE or MySQL Workbench for MYSQL.
  - Specify the database name and the user credentials to access the data.
  - Write SQL statements in the query editor or the command-line interface, following the syntax and rules of SQL.
  - Execute the SQL statements by pressing a button or hitting the enter key, and view the results in the output window or the console.
  - Save, edit, or delete the SQL statements as needed.
- Some common types of SQL statements are:
  - Data Definition Language (DDL) statements, which are used to create, alter, or drop database objects, such as tables, views, indexes, etc.
  - Data Manipulation Language (DML) statements, which are used to insert, update, delete, or select data from database tables or views.
  - Data Control Language (DCL) statements, which are used to grant or revoke permissions or roles to users or groups on database objects or data.
  - Transaction Control Language (TCL) statements, which are used to control the transactions, such as commit, rollback, savepoint, etc.
- Some examples of SQL statements using ORACLE or MYSQL are:

  - To create a table named `employees` with four columns: `emp_id`, `emp_name`, `emp_salary`, and `emp_dept`, one can write:

    ```sql
    -- ORACLE syntax
    CREATE TABLE employees (
      emp_id NUMBER(10) PRIMARY KEY,
      emp_name VARCHAR2(50) NOT NULL,
      emp_salary NUMBER(10,2) CHECK (emp_salary > 0),
      emp_dept VARCHAR2(20)
    );

    -- MYSQL syntax
    CREATE TABLE employees (
      emp_id INT(10) PRIMARY KEY,
      emp_name VARCHAR(50) NOT NULL,
      emp_salary DECIMAL(10,2) CHECK (emp_salary > 0),
      emp_dept VARCHAR(20)
    );
    ```

  - To insert a row into the `employees` table with the values `101`, `Alice`, `5000`, and `Sales`, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    INSERT INTO employees (emp_id, emp_name, emp_salary, emp_dept)
    VALUES (101, 'Alice', 5000, 'Sales');
    ```

  - To update the salary of the employee with the id `101` to `6000`, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    UPDATE employees
    SET emp_salary = 6000
    WHERE emp_id = 101;
    ```

  - To delete the employee with the id `101` from the `employees` table, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    DELETE FROM employees
    WHERE emp_id = 101;
    ```

  - To select all the columns and rows from the `employees` table, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    SELECT * FROM employees;
    ```

  - To select only the name and salary of the employees who work in the `Sales` department, one can write:

    ```sql
    -- ORACLE and MYSQL syntax
    SELECT emp_name, emp_salary FROM employees
    WHERE emp_dept = 'Sales';
    ```