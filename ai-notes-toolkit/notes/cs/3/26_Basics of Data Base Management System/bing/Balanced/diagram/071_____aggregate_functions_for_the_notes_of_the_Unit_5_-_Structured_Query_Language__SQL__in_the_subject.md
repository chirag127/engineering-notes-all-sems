### Aggregate Functions

- Aggregate functions are SQL functions that perform calculations on a set of values and return a single value.
- Aggregate functions can be used in the select list or the having clause of a select statement.
- Aggregate functions ignore null values in the input set, except for the count function, which counts all rows.
- Some of the common aggregate functions are:

  - **AVG**: Returns the average of the values in a column.
  - **COUNT**: Returns the number of rows in a table or the number of non-null values in a column.
  - **MAX**: Returns the maximum value in a column.
  - **MIN**: Returns the minimum value in a column.
  - **SUM**: Returns the sum of the values in a column.
  - **STDEV**: Returns the standard deviation of the values in a column.
  - **VAR**: Returns the variance of the values in a column.

- Aggregate functions can be used with the group by clause to group the input set by one or more columns and calculate the aggregate value for each group.
- Aggregate functions can also be used with the having clause to filter the groups based on a condition.
- Example: To find the average salary of each department in a company, we can use the following query:

```sql
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 5000;
```

- This query will return the department name and the average salary of each department, where the average salary is greater than 5000.