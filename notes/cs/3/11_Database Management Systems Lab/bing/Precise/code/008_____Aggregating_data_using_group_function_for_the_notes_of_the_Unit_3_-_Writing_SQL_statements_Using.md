### Aggregating data using group function

Group functions are used to perform calculations on a set of rows and return a single value. These functions are often used with the GROUP BY clause in the SELECT statement. The most commonly used group functions are:

1. **AVG**: Calculates the average value of a set of values.
2. **COUNT**: Counts the number of rows in a table.
3. **MAX**: Returns the maximum value of a set of values.
4. **MIN**: Returns the minimum value of a set of values.
5. **SUM**: Calculates the sum of a set of values.

Here is an example of using group functions with the GROUP BY clause in a SELECT statement:

```SQL
SELECT department_id, AVG(salary)
FROM employees
GROUP BY department_id;
```

This statement calculates the average salary for each department in the employees table. The GROUP BY clause groups the rows by department_id, and the AVG function calculates the average salary for each group.