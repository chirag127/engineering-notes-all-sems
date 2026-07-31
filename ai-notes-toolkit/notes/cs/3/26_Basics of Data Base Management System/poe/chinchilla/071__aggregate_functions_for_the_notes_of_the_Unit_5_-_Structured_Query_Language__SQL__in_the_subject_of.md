### Aggregate Functions in SQL

Aggregate functions are used to perform calculations on a set of values and return a single value as the result. These functions are often used in SQL queries to summarize data in a table. Here are some of the most commonly used aggregate functions in SQL:

1. COUNT(): This function returns the number of rows in a table that meet a specified condition. For example, to count the number of records in a table called "employees" where the salary is greater than 50000, you would use the following SQL statement:

```
SELECT COUNT(*) FROM employees WHERE salary > 50000;
```

2. SUM(): This function returns the sum of all values in a particular column. For example, to calculate the total salary of all employees in the "employees" table, you would use the following SQL statement:

```
SELECT SUM(salary) FROM employees;
```

3. AVG(): This function returns the average of all values in a particular column. For example, to calculate the average salary of all employees in the "employees" table, you would use the following SQL statement:

```
SELECT AVG(salary) FROM employees;
```

4. MAX(): This function returns the maximum value in a particular column. For example, to find the highest salary among all employees in the "employees" table, you would use the following SQL statement:

```
SELECT MAX(salary) FROM employees;
```

5. MIN(): This function returns the minimum value in a particular column. For example, to find the lowest salary among all employees in the "employees" table, you would use the following SQL statement:

```
SELECT MIN(salary) FROM employees;
```

6. GROUP BY: This function is used to group rows in a table based on the values in one or more columns. It is often used with aggregate functions to summarize data in a table. For example, to calculate the total salary for each department in the "employees" table, you would use the following SQL statement:

```
SELECT department, SUM(salary) FROM employees GROUP BY department;
```

In conclusion, aggregate functions are an important part of SQL and are used to summarize data in a table. By using these functions in your SQL queries, you can quickly calculate sums, averages, and other statistics on your data.