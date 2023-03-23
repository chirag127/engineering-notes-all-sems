### Queries and Subqueries for the Notes of Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Database Management System

SQL is a standard language used to manage and manipulate databases. Queries and subqueries are essential components of SQL that allow users to retrieve and manipulate data from the database. Here are the queries and subqueries you need to know for the Unit 5 of the Basics of Database Management System:

#### Queries

1. Select query: 
    - Used to retrieve data from the database.
    - Syntax: `SELECT column_name FROM table_name WHERE condition;`
    - Example: `SELECT * FROM employees WHERE salary > 50000;`

2. Insert query:
    - Used to insert data into the database.
    - Syntax: `INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);`
    - Example: `INSERT INTO employees (name, age, salary) VALUES ('John Doe', 30, 60000);`

3. Update query:
    - Used to modify or update data in the database.
    - Syntax: `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`
    - Example: `UPDATE employees SET salary = 65000 WHERE name = 'John Doe';`

4. Delete query:
    - Used to delete data from the database.
    - Syntax: `DELETE FROM table_name WHERE condition;`
    - Example: `DELETE FROM employees WHERE age > 40;`

#### Subqueries

1. Single-row subquery:
    - Used to return a single value from a subquery.
    - Syntax: `SELECT column_name FROM table_name WHERE column_name = (SELECT column_name FROM table_name WHERE condition);`
    - Example: `SELECT name FROM employees WHERE age = (SELECT MAX(age) FROM employees);`

2. Multiple-row subquery:
    - Used to return multiple values from a subquery.
    - Syntax: `SELECT column_name FROM table_name WHERE column_name IN (SELECT column_name FROM table_name WHERE condition);`
    - Example: `SELECT name FROM employees WHERE salary IN (SELECT salary FROM employees WHERE age > 30);`

3. Correlated subquery:
    - Used to reference a column from the outer query in the subquery.
    - Syntax: `SELECT column_name FROM table_name t1 WHERE condition = (SELECT MAX(column_name) FROM table_name t2 WHERE t1.column_name = t2.column_name);`
    - Example: `SELECT name FROM employees t1 WHERE salary = (SELECT MAX(salary) FROM employees t2 WHERE t1.department = t2.department);`

SQL queries and subqueries are powerful tools for managing and manipulating data in a database. With a good understanding of these components, you can easily retrieve, insert, update, and delete data from your database.