### Queries and Subqueries

- A query is a request for data from a database that follows the syntax and rules of a query language, such as SQL (Structured Query Language).
- A subquery, also known as a nested query or an inner query, is a query within another query that is embedded in a clause such as WHERE, HAVING, or FROM.
- A subquery is used to return data that will be used in the main query as a condition to further restrict the data to be retrieved or to perform calculations on the data.
- A subquery can return a single value, a single row, a single column, or a table of values or rows.
- A subquery can be correlated or uncorrelated. A correlated subquery depends on the outer query for its values, while an uncorrelated subquery can be executed independently of the outer query.
- A subquery can be placed in various clauses of a SQL statement, such as:

  - SELECT: A subquery in the SELECT clause returns a single value that is used as a column in the result set of the main query.
  - FROM: A subquery in the FROM clause returns a table that is used as a source of data for the main query. The subquery must have an alias to be referenced in the main query.
  - WHERE: A subquery in the WHERE clause returns a value, a row, a column, or a table that is used as a condition to filter the data in the main query. The subquery can use comparison operators, such as =, <, >, IN, EXISTS, etc.
  - HAVING: A subquery in the HAVING clause returns a value, a row, a column, or a table that is used as a condition to filter the groups in the main query. The subquery can use comparison operators, such as =, <, >, IN, EXISTS, etc.
  - INSERT: A subquery in the INSERT statement returns a table that is used as the source of data to be inserted into another table.
  - UPDATE: A subquery in the UPDATE statement returns a value, a row, or a column that is used to update the data in another table.
  - DELETE: A subquery in the DELETE statement returns a value, a row, a column, or a table that is used as a condition to delete the data from another table.

- Some examples of subqueries are:

  - A subquery in the SELECT clause:

    ```sql
    SELECT name, (SELECT MAX(salary) FROM employees) AS max_salary
    FROM employees;
    ```

    This query returns the name and the maximum salary of all employees.

  - A subquery in the FROM clause:

    ```sql
    SELECT name, salary
    FROM (SELECT * FROM employees WHERE department = 'Sales') AS sales_employees;
    ```

    This query returns the name and salary of all employees who work in the sales department.

  - A subquery in the WHERE clause:

    ```sql
    SELECT name, salary
    FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees);
    ```

    This query returns the name and salary of all employees who earn more than the average salary of all employees.

  - A subquery in the HAVING clause:

    ```sql
    SELECT department, SUM(salary) AS total_salary
    FROM employees
    GROUP BY department
    HAVING SUM(salary) > (SELECT AVG(salary) * COUNT(*) FROM employees);
    ```

    This query returns the department and the total salary of each department that pays more than the average salary of all employees.

  - A subquery in the INSERT statement:

    ```sql
    INSERT INTO bonuses (employee_id, bonus_amount)
    SELECT employee_id, salary * 0.1
    FROM employees
    WHERE department = 'Sales';
    ```

    This query inserts a record into the bonuses table for each employee who works in the sales department, with a bonus amount equal to 10% of their salary.

  - A subquery in the UPDATE statement:

    ```sql
    UPDATE employees
    SET salary = salary * 1.1
    WHERE department = (SELECT department FROM employees WHERE name = 'John Smith');
    ```

    This query updates the salary of all employees who work in the same department as John Smith, by increasing it by 10%.

  - A subquery in the DELETE statement:

    ```sql
    DELETE FROM employees
    WHERE salary < (SELECT MIN(salary) FROM employees WHERE department = '

```
