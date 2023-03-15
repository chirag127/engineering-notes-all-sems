# Aggregate Functions in SQL

Aggregate functions in SQL are used to perform calculations on a set of values and return a single value. They are often used with the GROUP BY clause to group the result set by one or more columns. Here are some commonly used aggregate functions in SQL:

1. **COUNT**: Returns the number of rows in a table or the number of non-NULL values in a column.
2. **SUM**: Returns the sum of all the values in a column.
3. **AVG**: Returns the average of all the values in a column.
4. **MIN**: Returns the minimum value in a column.
5. **MAX**: Returns the maximum value in a column.

These functions can be used in the SELECT, HAVING, and ORDER BY clauses of a query. They can also be used with the DISTINCT keyword to eliminate duplicate values before performing the calculation.

For example, to find the average salary of employees in a company, you could use the following query:

```SQL
SELECT AVG(salary)
FROM employees;
```

To find the number of employees in each department, you could use the following query:

```SQL
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

These are just a few examples of how aggregate functions can be used in SQL. They are powerful tools for summarizing and analyzing data in a database.