Hello, I am Sydney, your AI assistant. I can help you with writing SQL statements using Oracle or MySQL. Here is some content that you can use for studying or reference.

## Unit 3 - Writing SQL statements Using ORACLE /MYSQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- Oracle and MySQL are two popular relational database management systems (RDBMS) that support SQL.
- To write SQL statements using Oracle or MySQL, you need to follow some basic steps:
  - Connect to the database server using a client application or a command-line interface.
  - Specify the database and the schema (or user) that you want to work with.
  - Write SQL statements that follow the syntax and rules of the SQL language and the specific RDBMS.
  - Execute the SQL statements and view the results or messages returned by the database server.
  - Close the connection when you are done.

- Some common types of SQL statements are:
  - Data Definition Language (DDL) statements, which are used to create, modify, or delete database objects such as tables, views, indexes, constraints, etc.
  - Data Manipulation Language (DML) statements, which are used to insert, update, delete, or query data in database tables or views.
  - Data Control Language (DCL) statements, which are used to grant or revoke permissions or roles to users or groups on database objects or operations.
  - Transaction Control Language (TCL) statements, which are used to manage transactions, which are logical units of work that ensure data consistency and integrity.
  - Session Control Language (SCL) statements, which are used to alter the properties or behavior of the current session or connection.

- Some examples of SQL statements using Oracle or MySQL are:

  - To create a table named `employees` with four columns: `emp_id`, `name`, `salary`, and `dept_id`:

    ```sql
    -- Oracle syntax
    CREATE TABLE employees (
      emp_id NUMBER(10) PRIMARY KEY,
      name VARCHAR2(50) NOT NULL,
      salary NUMBER(10,2) CHECK (salary > 0),
      dept_id NUMBER(10) REFERENCES departments(dept_id)
    );

    -- MySQL syntax
    CREATE TABLE employees (
      emp_id INT(10) PRIMARY KEY,
      name VARCHAR(50) NOT NULL,
      salary DECIMAL(10,2) CHECK (salary > 0),
      dept_id INT(10) REFERENCES departments(dept_id)
    );
    ```

  - To insert a new row into the `employees` table with the values `1001`, `Alice`, `5000`, and `1`:

    ```sql
    -- Oracle and MySQL syntax
    INSERT INTO employees (emp_id, name, salary, dept_id)
    VALUES (1001, 'Alice', 5000, 1);
    ```

  - To update the salary of the employee with the `emp_id` of `1001` to `6000`:

    ```sql
    -- Oracle and MySQL syntax
    UPDATE employees
    SET salary = 6000
    WHERE emp_id = 1001;
    ```

  - To delete the employee with the `emp_id` of `1001` from the `employees` table:

    ```sql
    -- Oracle and MySQL syntax
    DELETE FROM employees
    WHERE emp_id = 1001;
    ```

  - To query the name and salary of all employees who work in the department with the `dept_id` of `1`:

    ```sql
    -- Oracle and MySQL syntax
    SELECT name, salary
    FROM employees
    WHERE dept_id = 1;
    ```

  - To grant the `SELECT` privilege on the `employees` table to the user `bob`:

    ```sql
    -- Oracle syntax
    GRANT SELECT ON employees TO bob;

    -- MySQL syntax
    GRANT SELECT ON employees TO 'bob'@'localhost';
    ```

  - To revoke the `SELECT` privilege on the `employees` table from the user `bob`:

    ```sql
    -- Oracle syntax
    REVOKE SELECT ON employees FROM bob;

    -- MySQL syntax
    REVOKE SELECT ON employees FROM 'bob'@'localhost';
    ```

  - To commit the current transaction:

    ```sql
    -- Oracle and MySQL syntax
    COMMIT;
    ```

  - To rollback the current transaction:

    ```sql
    -- Oracle and MySQL syntax
    ROLLBACK;
    ```

  - To change the session time zone to `UTC`:

    ```sql
    -- Oracle syntax