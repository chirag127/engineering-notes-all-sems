### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of rows and return a single value for each group of rows. They are commonly used to perform calculations, such as sum, count, average, minimum, and maximum, on numeric or date values. 
- Aggregate functions can be used in the select list and in the order by and having clauses of a select statement. They can also be used as window functions, which apply to a subset of rows defined by a window specification.
- To use aggregate functions with a group by clause, the following syntax is used:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
HAVING condition
ORDER BY column;
```

- The group by clause divides the rows of the queried table or view into groups based on the values of the specified columns. Oracle or MySQL applies the aggregate function to each group of rows and returns a single result row for each group. 
- The having clause is used to filter the groups based on a condition. It is similar to the where clause, but it operates on the grouped rows, not on the individual rows. 
- The order by clause is used to sort the result set based on the values of the specified columns or expressions. 
- Some examples of aggregate functions are:

  - SUM(column): returns the sum of the values in the column.
  - MAX(column): returns the maximum value in the column.
  - MIN(column): returns the minimum value in the column.
  - COUNT(column): returns the number of rows that have a non-null value in the column.
  - AVG(column): returns the average of the values in the column.
  - JSON_ARRAYAGG(column): returns a JSON array containing the values in the column.
  - JSON_OBJECTAGG(key, value): returns a JSON object containing the key-value pairs in the columns.

- Some examples of using aggregate functions with group by are:

  - To calculate the total sales amount for each product category:

  ```sql
  SELECT category, SUM(amount) AS total_sales
  FROM sales
  GROUP BY category;
  ```

  - To find the highest and lowest salary for each department:

  ```sql
  SELECT department, MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary
  FROM employees
  GROUP BY department;
  ```

  - To count the number of employees in each department who have a salary above 5000:

  ```sql
  SELECT department, COUNT(*) AS num_employees
  FROM employees
  WHERE salary > 5000
  GROUP BY department;
  ```

  - To find the average salary for each job title, sorted by descending order:

  ```sql
  SELECT job_title, AVG(salary) AS average_salary
  FROM employees
  GROUP BY job_title
  ORDER BY average_salary DESC;
  ```