### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregating data refers to the process of combining data from multiple rows into a single result.
- Group functions are used to perform calculations on a set of rows and return a single result.
- Some common group functions include `SUM`, `AVG`, `MIN`, `MAX`, and `COUNT`.
- Group functions can be used in the `SELECT`, `HAVING`, and `ORDER BY` clauses of a SQL statement.
- The `GROUP BY` clause is used to group rows based on one or more columns.
- The `HAVING` clause is used to filter groups based on a condition.
- When using group functions, it is important to consider the data type of the column being aggregated.
- Group functions can be used with the `DISTINCT` keyword to eliminate duplicate values before performing the calculation.
- Group functions can also be nested to perform more complex calculations.

For example, to calculate the average salary of employees grouped by department, the following SQL statement can be used:

```SQL
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id;
```

This statement calculates the average salary for each department and returns the results grouped by department. The `GROUP BY` clause specifies that the rows should be grouped by the `department_id` column. The `AVG` function calculates the average salary for each group of rows. The result is a table with two columns: `department_id` and `AVG(salary)`.