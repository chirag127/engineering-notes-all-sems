### Aggregate Functions

Aggregate functions are used to perform calculations on a set of values and return a single value. They are often used in conjunction with the GROUP BY clause in a SELECT statement to group rows into sets and perform calculations on each set.

Some common aggregate functions include:

- **COUNT**: Returns the number of rows in a table or the number of non-NULL values in a column.
- **SUM**: Returns the sum of all values in a column.
- **AVG**: Returns the average of all values in a column.
- **MIN**: Returns the minimum value in a column.
- **MAX**: Returns the maximum value in a column.

These functions can be used in a SELECT statement to perform calculations on a single column or multiple columns. For example, to find the average salary of all employees in a company, the following query can be used:

```
SELECT AVG(salary) FROM employees;
```

To find the total salary paid to employees in each department, the following query can be used:

```
SELECT department, SUM(salary) FROM employees GROUP BY department;
```

In this query, the GROUP BY clause groups the rows by department and the SUM function calculates the total salary for each department.