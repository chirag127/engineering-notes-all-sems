### Aggregate Functions

Aggregate functions are used to perform calculations on a set of values and return a single value. They are often used in combination with the GROUP BY clause to group the results by one or more columns. Here are some common aggregate functions used in SQL:

1. **COUNT**: Returns the number of rows in a table or the number of non-NULL values in a column.
2. **SUM**: Returns the sum of all the values in a column.
3. **AVG**: Returns the average of all the values in a column.
4. **MIN**: Returns the minimum value in a column.
5. **MAX**: Returns the maximum value in a column.

These functions can be used in the SELECT, HAVING, and ORDER BY clauses of a query. For example, to find the average salary of employees in a company, you could use the following query:

```SQL
SELECT AVG(salary)
FROM employees;
```

This would return the average salary of all employees in the `employees` table. You can also use aggregate functions with the GROUP BY clause to group the results by one or more columns. For example, to find the average salary of employees by department, you could use the following query:

```SQL
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

This would return the average salary of employees for each department in the `employees` table. The GROUP BY clause groups the results by the `department` column, and the AVG function calculates the average salary for each group.