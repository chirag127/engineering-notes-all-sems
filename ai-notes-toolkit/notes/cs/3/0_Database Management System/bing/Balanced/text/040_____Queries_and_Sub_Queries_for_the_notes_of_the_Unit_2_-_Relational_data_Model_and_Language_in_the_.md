### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be written in a declarative query language such as SQL, which specifies what data is needed, not how to get it.
- A subquery is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used when you need to process data in several steps, or when you want to use the result of one query as an input for another query. Subqueries can also be used to compare values, test for existence, or perform aggregations.
- There are three types of subqueries: scalar, multirow, and correlated.
  - A scalar subquery returns a single value and can be used anywhere a literal value can be used, such as in a WHERE clause, a SELECT clause, or an assignment statement. For example:

    ```sql
    SELECT name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees);
    ```

    This query returns the name and salary of employees who earn more than the average salary of all employees. The scalar subquery `(SELECT AVG(salary) FROM employees)` returns the average salary as a single value.

  - A multirow subquery returns one or more rows and can be used with operators such as IN, ANY, ALL, EXISTS, or NOT EXISTS. For example:

    ```sql
    SELECT name, department_id
    FROM employees
    WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
    ```

    This query returns the name and department ID of employees who work in departments located in New York. The multirow subquery `(SELECT department_id FROM departments WHERE location = 'New York')` returns a set of department IDs that match the condition.

  - A correlated subquery is a subquery that depends on the outer query for its values. A correlated subquery is executed once for each row of the outer query, and the result of the subquery is compared with the value of the outer query row. For example:

    ```sql
    SELECT name, salary
    FROM employees e
    WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);
    ```

    This query returns the name and salary of employees who earn more than the average salary of their department. The correlated subquery `(SELECT AVG(salary) FROM employees WHERE department_id = e.department_id)` returns the average salary for each department, using the department ID from the outer query row.

- Relational data model and language is a way of representing and manipulating data in a database using tables, columns, rows, and keys. A relational database is a collection of tables, each with a unique name and a set of columns. A row in a table is a record of data, and a column is an attribute of data. A key is a column or a combination of columns that uniquely identifies a row in a table.
- A relational query language is a language that allows users to access and manipulate data in a relational database. The most widely used relational query language is SQL, which stands for Structured Query Language. SQL has commands for creating, modifying, querying, and deleting data and tables in a database. SQL also has features for defining views, functions, procedures, triggers, and constraints. SQL is a standard language, but different database systems may have different extensions or variations of SQL.