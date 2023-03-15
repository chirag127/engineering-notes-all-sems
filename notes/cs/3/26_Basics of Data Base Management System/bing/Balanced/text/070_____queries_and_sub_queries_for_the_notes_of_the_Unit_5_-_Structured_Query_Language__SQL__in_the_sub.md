### Queries and Subqueries

- A query is a request for data from a database that follows the syntax and rules of a query language, such as SQL (Structured Query Language).
- A subquery, also known as a nested query or an inner query, is a query within another query that is embedded in a clause such as WHERE, HAVING, or FROM.
- A subquery is used to return data that will be used in the main query as a condition, a source, or a value to further restrict or manipulate the data to be retrieved.
- A subquery can return a single value, a single row, a single column, or a table of values or rows.
- A subquery can be correlated or uncorrelated. A correlated subquery depends on the outer query for its values, while an uncorrelated subquery can be executed independently of the outer query.
- A subquery can be placed in various clauses of the main query, such as:

  - SELECT: A subquery in the SELECT clause returns a single value or a single column that can be used as an expression or an alias in the main query.
  - FROM: A subquery in the FROM clause returns a table of values or rows that can be used as a source or a join partner in the main query. The subquery must have an alias in this case.
  - WHERE: A subquery in the WHERE clause returns a single value, a single row, a single column, or a table of values or rows that can be used as a condition or a comparison operator in the main query.
  - HAVING: A subquery in the HAVING clause returns a single value, a single row, a single column, or a table of values or rows that can be used as a condition or a comparison operator in the main query after the GROUP BY clause.
  - IN: A subquery in the IN operator returns a single column or a table of values that can be used to check if a value exists in the subquery result set.
  - EXISTS: A subquery in the EXISTS operator returns a boolean value that indicates whether the subquery has any rows or not.
  - ANY, ALL: A subquery in the ANY or ALL operator returns a single column or a table of values that can be used to compare with a value in the main query using a comparison operator such as =, <, >, etc. The ANY operator returns true if any value in the subquery satisfies the comparison, while the ALL operator returns true if all values in the subquery satisfy the comparison.

- Some examples of subqueries are:

  - SELECT name, salary FROM employees WHERE salary > (SELECT AVG(salary) FROM employees); -- This query returns the name and salary of employees who earn more than the average salary of all employees. The subquery in the WHERE clause returns a single value, the average salary, that is used as a condition in the main query.
  - SELECT * FROM (SELECT name, department, salary FROM employees) AS emp_dept; -- This query returns all the columns from a subquery that returns the name, department, and salary of employees. The subquery in the FROM clause returns a table of values that is used as a source in the main query. The subquery must have an alias, emp_dept, in this case.
  - SELECT name, department FROM employees WHERE department IN (SELECT department FROM departments WHERE location = 'New York'); -- This query returns the name and department of employees who work in departments that are located in New York. The subquery in the IN operator returns a single column, the department, that is used to check if the department of the employee exists in the subquery result set.
  - SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department HAVING SUM(salary) > (SELECT MAX(total_salary) FROM (SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department) AS dept_sal); -- This query returns the department and the total salary of employees who have the highest total salary among all departments. The subquery in the HAVING clause returns a single value, the maximum total salary, that is used as a condition in the main query after the GROUP BY clause. The subquery in the MAX function returns a table of values, the department and the total salary, that is used as a source in the subquery. The subquery must have an alias, dept_sal, in this case.
  - SELECT name, salary FROM employees WHERE salary > ANY (SELECT salary FROM employees WHERE department = 'Sales'); -- This query returns the name and salary of employees who