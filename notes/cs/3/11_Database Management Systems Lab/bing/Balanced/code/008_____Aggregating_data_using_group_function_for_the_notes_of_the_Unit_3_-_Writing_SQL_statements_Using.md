### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of rows and return a single value for each group of rows. They are commonly used to perform calculations, such as sum, count, average, minimum, and maximum, on numeric or date values in a table or view. 
- Aggregate functions can appear in the select list and in the order by and having clauses of a select statement. They can also be used as window functions, which apply to a partition of rows defined by the over clause.  
- To use aggregate functions with a group by clause, the following syntax is used:

```sql
SELECT column1, column2, ..., aggregate_function(column)
FROM table
WHERE condition
GROUP BY column1, column2, ...
HAVING condition
ORDER BY column;
```

- The group by clause divides the rows of the table or view into groups based on the values of the specified columns. The aggregate function is then applied to each group and returns a single result row for each group. If the group by clause is omitted, the aggregate function is applied to all the rows in the table or view and returns a single result row.  
- The having clause is used to filter the groups based on a condition. It is similar to the where clause, but it operates on the groups rather than the individual rows. The having clause can only refer to the columns that are in the group by clause or are arguments of aggregate functions.  
- The order by clause is used to sort the result rows based on the values of the specified columns or expressions. It can also refer to the columns that are in the group by clause or are arguments of aggregate functions.  
- Some examples of aggregate functions are:

  - SUM(column): returns the sum of the values in the column.  
  - COUNT(column): returns the number of rows that have a non-null value in the column.  
  - AVG(column): returns the average of the values in the column.  
  - MIN(column): returns the minimum value in the column.  
  - MAX(column): returns the maximum value in the column.  
  - LISTAGG(column, delimiter): returns a string that concatenates the values in the column separated by the delimiter. This function is available in Oracle but not in MySQL. 
  - JSON_ARRAYAGG(column): returns a JSON array that contains the values in the column. This function is available in MySQL but not in Oracle.  
  - JSON_OBJECTAGG(key, value): returns a JSON object that contains the key-value pairs from the columns. This function is available in MySQL but not in Oracle.  

- Some examples of using aggregate functions with group by clause are:

  - To find the total sales amount for each product category in a sales table:

  ```sql
  SELECT category, SUM(amount) AS total_sales
  FROM sales
  GROUP BY category
  ORDER BY total_sales DESC;
  ```

  - To find the number of employees in each department in an employees table:

  ```sql
  SELECT department, COUNT(*) AS employee_count
  FROM employees
  GROUP BY department
  HAVING employee_count > 10;
  ```

  - To find the average salary of each job title in an employees table:

  ```sql
  SELECT job_title, AVG(salary) AS average_salary
  FROM employees
  GROUP BY job_title
  ORDER BY average_salary DESC;
  ```

  - To find the names of the customers who have bought more than one product in a orders table:

  ```sql
  SELECT customer_name, LISTAGG(product_name, ', ') AS products
  FROM orders
  GROUP BY customer_name
  HAVING COUNT(DISTINCT product_name) > 1;
  ```

  - To find the JSON array of the product names and prices in a products table:

  ```sql
  SELECT JSON_ARRAYAGG(JSON_OBJECT('name', product_name, 'price', product_price