### Aggregate Functions for the Notes of the Unit 5 - Structured Query Language (SQL) in the Subject of Basics of Data Base Management System

- Aggregate functions are SQL functions that perform calculations on a set of values and return a single value  .
- Aggregate functions can be used in the select list of a SELECT statement, or in a HAVING clause to filter the grouped rows.
- Some of the common aggregate functions are:
  - AVG: returns the average of the values in a column   .
  - COUNT: returns the number of rows in a table or the number of non-null values in a column   .
  - MAX: returns the maximum value in a column   .
  - MIN: returns the minimum value in a column   .
  - SUM: returns the sum of the values in a column   .
- Aggregate functions can be combined with the GROUP BY clause to calculate the aggregate values for each group of rows that share the same values in the specified columns   .
- Aggregate functions can also be combined with the HAVING clause to filter the groups based on a condition that involves the aggregate values  .
- Aggregate functions ignore null values in the columns, except for the COUNT function, which counts null values as well   .
- Aggregate functions can be nested inside other aggregate functions, as long as they operate on different columns.
- Some examples of using aggregate functions are:

```sql
-- Find the average salary of all employees
SELECT AVG(salary) FROM employees;

-- Find the number of employees in each department
SELECT department_id, COUNT(*) FROM employees GROUP BY department_id;

-- Find the highest salary in each department
SELECT department_id, MAX(salary) FROM employees GROUP BY department_id;

-- Find the total salary of each department that is more than 100000
SELECT department_id, SUM(salary) FROM employees GROUP BY department_id HAVING SUM(salary) > 100000;

-- Find the number of distinct job titles in the company
SELECT COUNT(DISTINCT job_title) FROM employees;
```