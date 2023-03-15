### Aggregate Functions

Aggregate functions are used in SQL to perform calculations on a set of values and return a single value. They are commonly used with the `GROUP BY` clause to group the result set by one or more columns. Here are some commonly used aggregate functions:

1. `COUNT`: Returns the number of rows in a table.
2. `SUM`: Returns the sum of all values in a column.
3. `AVG`: Returns the average of all values in a column.
4. `MIN`: Returns the minimum value in a column.
5. `MAX`: Returns the maximum value in a column.

These functions can be used in the `SELECT` statement to perform calculations on the data in a table. For example, to find the average salary of employees in a company, you could use the following query:

```SQL
SELECT AVG(salary)
FROM employees;
```

This query calculates the average salary of all employees in the `employees` table and returns the result. You can also use the `GROUP BY` clause to group the result set by one or more columns. For example, to find the average salary of employees by department, you could use the following query:

```SQL
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

This query calculates the average salary of employees in each department and returns the result grouped by department. Aggregate functions can be very useful for performing calculations on large data sets and summarizing data in a meaningful way.