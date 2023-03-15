# Aggregate Functions

- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used in conjunction with the `GROUP BY` clause to perform calculations on groups of rows that share some common attribute.
- Some common aggregate functions are:

  - `COUNT`: returns the number of values in a set or the number of rows that satisfy a condition.
  - `SUM`: returns the sum of all values in a set or the sum of values that satisfy a condition.
  - `AVG`: returns the average of all values in a set or the average of values that satisfy a condition.
  - `MIN`: returns the minimum value in a set or the minimum value that satisfies a condition.
  - `MAX`: returns the maximum value in a set or the maximum value that satisfies a condition.

- Aggregate functions can be used in the `SELECT` clause, the `HAVING` clause, or the `ORDER BY` clause of a query.
- Aggregate functions ignore `NULL` values in the set of values they operate on, unless otherwise specified by the function.
- Aggregate functions can be combined with other expressions or functions using arithmetic operators or nested function calls.
- Aggregate functions can also be applied to distinct values in a set by using the keyword `DISTINCT` before the function name.

- Example: The following query returns the total number of employees, the average salary, the minimum salary, and the maximum salary in each department of a company.

  ```sql
  SELECT dept_id, COUNT(*), AVG(salary), MIN(salary), MAX(salary)
  FROM employee
  GROUP BY dept_id;
  ```