### Queries and Sub Queries for the notes of the Unit 2 - Relational data Model and Language in the subject of Database Management System

- A query is a request for data or information from a database table or combination of tables. A query can be expressed in a high-level query language, such as SQL, or in a low-level programming language, such as C or Java.
- A subquery is a query that is nested inside another query, such as a SELECT, INSERT, UPDATE, or DELETE statement, or inside another subquery. A subquery can return a scalar value, a single row or column, or a table of rows and columns.
- Subqueries are often used to perform complex calculations, filter data, or join data from multiple tables. Subqueries can also be used to replace joins, aggregates, or expressions in some cases.
- There are three types of subqueries: scalar, multirow, and correlated.
  - A scalar subquery returns a single value and can be used anywhere a literal value can be used, such as in a SELECT clause, a WHERE clause, or a SET clause. For example:

    ```sql
    SELECT name, salary, (SELECT AVG(salary) FROM employees) AS avg_salary
    FROM employees;
    ```

    This query returns the name, salary, and average salary of all employees. The scalar subquery in the SELECT clause calculates the average salary from the employees table and returns a single value.

  - A multirow subquery returns one or more rows and can be used with operators such as IN, ANY, ALL, EXISTS, or NOT EXISTS. For example:

    ```sql
    SELECT name, department_id
    FROM employees
    WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');
    ```

    This query returns the name and department ID of employees who work in departments located in New York. The multirow subquery in the WHERE clause returns a list of department IDs that match the location criteria and is used with the IN operator to filter the employees table.

  - A correlated subquery is a subquery that depends on the outer query for its values. A correlated subquery is executed once for each row of the outer query. A correlated subquery can be used with operators such as =, <, >, <=, >=, <>, EXISTS, or NOT EXISTS. For example:

    ```sql
    SELECT name, salary
    FROM employees e
    WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);
    ```

    This query returns the name and salary of employees who earn more than the average salary of their department. The correlated subquery in the WHERE clause calculates the average salary for each department based on the department ID of the outer query and is used with the > operator to compare with the salary of the outer query.