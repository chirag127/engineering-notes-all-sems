### Aggregate Functions

Aggregate functions are functions that take a collection of values as input and return a single value. They are commonly used in SQL to perform calculations on a set of values and return a single result. Some common aggregate functions include:

1. **COUNT:** Returns the number of rows in a table or the number of non-NULL values in a column.
2. **SUM:** Returns the sum of all the values in a column.
3. **AVG:** Returns the average of all the values in a column.
4. **MIN:** Returns the minimum value in a column.
5. **MAX:** Returns the maximum value in a column.

These functions can be used in the SELECT statement, along with the GROUP BY clause, to group the results by one or more columns and calculate aggregate values for each group. For example, to calculate the average salary of employees by department, the following SQL statement can be used:

```SQL
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

This statement groups the rows in the employees table by the department column and calculates the average salary for each department. The result is a table with two columns: department and average salary.

Aggregate functions can also be used in combination with other SQL clauses, such as WHERE and HAVING, to filter the results and perform more complex calculations. For example, to calculate the average salary of employees in the sales department who have been with the company for more than five years, the following SQL statement can be used:

```SQL
SELECT AVG(salary)
FROM employees
WHERE department = 'sales' AND years_of_service > 5;
```

This statement filters the rows in the employees table to include only those in the sales department who have been with the company for more than five years, and then calculates the average salary of the remaining rows.

In summary, aggregate functions are powerful tools for performing calculations on a set of values and returning a single result. They can be used in combination with other SQL clauses to perform complex calculations and data analysis.