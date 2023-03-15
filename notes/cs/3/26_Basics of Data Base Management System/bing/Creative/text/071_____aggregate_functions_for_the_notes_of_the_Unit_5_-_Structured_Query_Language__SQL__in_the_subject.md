### Aggregate Functions
- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used with the GROUP BY clause to calculate summary statistics for each group of rows.
- Some common aggregate functions are:
  - COUNT: returns the number of values in a set or the number of rows that satisfy a condition.
  - SUM: returns the sum of all values in a set.
  - AVG: returns the average of all values in a set.
  - MIN: returns the minimum value in a set.
  - MAX: returns the maximum value in a set.
- Aggregate functions can be used in the SELECT, HAVING, and ORDER BY clauses of a SQL query.
- Aggregate functions ignore NULL values in the set, except for COUNT(*), which counts all rows regardless of NULL values.
- Example: The following query calculates the total number of employees, the average salary, the minimum salary, and the maximum salary for each department in the employees table.

```sql
SELECT department, COUNT(*), AVG(salary), MIN(salary), MAX(salary)
FROM employees
GROUP BY department;
```