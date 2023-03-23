### Aggregating data using group function

In SQL, the GROUP BY clause is used to group together rows that have the same values in one or more columns. Grouping data allows us to perform aggregate functions on sets of data instead of individual rows. 

Some of the commonly used aggregate functions are:

- COUNT(): This function is used to count the number of rows in a group. It can be used with the * wildcard character to count all rows in a table or with a specific column to count the number of non-null values in that column.

- SUM(): This function is used to calculate the sum of values in a group. It can only be used with numeric data types.

- AVG(): This function is used to calculate the average value of a column in a group. It can only be used with numeric data types.

- MAX(): This function is used to find the maximum value in a group. It can be used with any data type.

- MIN(): This function is used to find the minimum value in a group. It can be used with any data type.

Here's an example of how to use the GROUP BY clause and aggregate functions:

```sql
SELECT department, COUNT(*) as total_employees, AVG(salary) as avg_salary
FROM employees
GROUP BY department;
```

This query will group employees by department and calculate the total number of employees and the average salary for each department.

It's important to note that when using the GROUP BY clause, all columns in the SELECT statement that are not part of an aggregate function must be included in the GROUP BY clause. 

```sql
SELECT department, salary, COUNT(*) as total_employees
FROM employees
GROUP BY department, salary;
```

This query will group employees by department and salary, and count the total number of employees for each department and salary combination.

In conclusion, the GROUP BY clause and aggregate functions in SQL allow us to group together data and perform calculations on sets of data instead of individual rows. These functions are essential for data analysis and reporting in SQL.