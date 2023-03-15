### Aggregate Functions

Aggregate functions are used to perform calculations on a set of values and return a single value. They are often used in conjunction with the GROUP BY clause in a SELECT statement to group rows into sets and perform calculations on each set.

Some common aggregate functions include:

1. COUNT: Returns the number of rows in a table or the number of non-NULL values in a column.
2. SUM: Returns the sum of all values in a column.
3. AVG: Returns the average of all values in a column.
4. MIN: Returns the minimum value in a column.
5. MAX: Returns the maximum value in a column.

These functions can be used in a SELECT statement to perform calculations on a single column or multiple columns. For example, to find the average salary of all employees in a company, you could use the following query:

```
SELECT AVG(salary) FROM employees;
```

This query calculates the average of all values in the salary column of the employees table and returns the result.

Aggregate functions can also be used with the GROUP BY clause to perform calculations on groups of rows. For example, to find the average salary of employees in each department, you could use the following query:

```
SELECT department, AVG(salary) FROM employees GROUP BY department;
```

This query groups the rows in the employees table by department and calculates the average salary for each group. The result is a table with one row for each department, showing the department name and the average salary of employees in that department.