# Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of values and return a single value. They are commonly used to perform calculations or summaries on groups of rows in a table or view. Some examples of aggregate functions are `SUM`, `MAX`, `MIN`, `COUNT`, `AVG`, `LISTAGG`, `JSON_ARRAYAGG`, etc.    
- Group functions are aggregate functions that can be used with the `GROUP BY` clause in a `SELECT` statement. The `GROUP BY` clause divides the rows of a table or view into groups based on the values of one or more columns. The aggregate functions are then applied to each group and return a single result row for each group.    
- The syntax of using group functions with the `GROUP BY` clause is as follows:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
ORDER BY column1, column2, ...
```

- The columns in the `SELECT` list must be either the columns used in the `GROUP BY` clause or the aggregate functions. The columns in the `ORDER BY` clause must be the same as the columns in the `SELECT` list. The `WHERE` clause can be used to filter the rows before grouping them.    
- The `HAVING` clause can be used to filter the groups after applying the aggregate functions. The `HAVING` clause can only contain aggregate functions or columns used in the `GROUP BY` clause. The syntax of using the `HAVING` clause is as follows:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
HAVING aggregate_function(column) condition
ORDER BY column1, column2, ...
```

- The `HAVING` clause is similar to the `WHERE` clause, but it operates on groups rather than rows. The `HAVING` clause can be used to eliminate groups that do not satisfy the condition.    
- Some examples of using group functions with the `GROUP BY` and `HAVING` clauses are as follows:

```sql
-- Find the total sales amount for each product category
SELECT category, SUM(amount) AS total_sales
FROM sales
GROUP BY category
ORDER BY category;

-- Find the average salary for each department that has more than 10 employees
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 10
ORDER BY department;

-- Find the name and email of the customers who have placed more than 5 orders
SELECT name, email
FROM customers
JOIN orders ON customers.id = orders.customer_id
GROUP BY customers.id, name, email
HAVING COUNT(orders.id) > 5
ORDER BY name, email;

-- Find the name and price of the most expensive product in each category
SELECT category, name, MAX(price) AS max_price
FROM products
GROUP BY category
ORDER BY category;
```

- Oracle and MySQL support different aggregate functions and have some differences in how they handle the `GROUP BY` clause. For example, Oracle supports the `LISTAGG` function to concatenate values from a group into a single string, while MySQL supports the `JSON_ARRAYAGG` and `JSON_OBJECTAGG` functions to aggregate values from a group into a JSON array or object.   
- Another difference is that Oracle requires that all columns in the `SELECT` list must be either the columns used in the `GROUP BY` clause or the aggregate functions, while MySQL allows columns that are not in the `GROUP BY` clause or the aggregate functions, but the values of those columns are indeterminate and may vary for each execution of the query.   
- Therefore, it is important to check the documentation of the specific database system before using the group functions and the `GROUP BY` clause.