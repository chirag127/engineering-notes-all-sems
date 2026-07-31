# Aggregate Functions

Aggregate functions are special functions in SQL that perform calculations on a set of values and return a single value. They are often used with the GROUP BY clause to summarize data into groups, and with the HAVING clause to filter groups based on a condition.

Some of the common aggregate functions in SQL are:

- **AVG**: Returns the average of the values in a column.
- **COUNT**: Returns the number of rows in a table or the number of non-null values in a column.
- **MAX**: Returns the maximum value in a column.
- **MIN**: Returns the minimum value in a column.
- **SUM**: Returns the sum of the values in a column.

To use an aggregate function, you need to specify the column name as an argument inside parentheses. For example, to find the average salary of employees in a table called `employees`, you can write:

```sql
SELECT AVG(salary) FROM employees;
```

You can also use aggregate functions with the `DISTINCT` keyword to eliminate duplicate values before performing the calculation. For example, to find the number of distinct departments in the `employees` table, you can write:

```sql
SELECT COUNT(DISTINCT department) FROM employees;
```

You can also use aggregate functions with the `GROUP BY` clause to divide the rows into groups based on one or more columns, and then apply the aggregate function to each group. For example, to find the average salary of each department in the `employees` table, you can write:

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;
```

You can also use aggregate functions with the `HAVING` clause to filter the groups based on a condition that involves an aggregate function. For example, to find the departments that have more than 10 employees in the `employees` table, you can write:

```sql
SELECT department, COUNT(*) FROM employees GROUP BY department HAVING COUNT(*) > 10;
```

Some of the other aggregate functions in SQL are:

- **APPROX_COUNT_DISTINCT**: Returns an approximate count of the distinct values in a column.
- **CHECKSUM_AGG**: Returns the checksum of the values in a column.
- **COUNT_BIG**: Returns the number of rows in a table or the number of non-null values in a column as a bigint data type.
- **GROUPING**: Returns a 1 or 0 to indicate whether a row belongs to a subtotal or a grand total of a GROUP BY query.
- **GROUPING_ID**: Returns a bit vector that indicates the grouping level of a row in a GROUP BY query.
- **STDEV**: Returns the standard deviation of the values in a column.
- **STDEVP**: Returns the population standard deviation of the values in a column.
- **STRING_AGG**: Returns a string that concatenates the values in a column with a specified separator.
- **VAR**: Returns the variance of the values in a column.
- **VARP**: Returns the population variance of the values in a column.

For more details and examples of these aggregate functions, you can refer to the search results   .