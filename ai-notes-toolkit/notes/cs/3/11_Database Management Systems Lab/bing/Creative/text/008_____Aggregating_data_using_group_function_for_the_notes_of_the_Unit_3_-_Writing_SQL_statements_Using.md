### Aggregating data using group function for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

- Aggregate functions are functions that operate on a set of values and return a single value. They are commonly used to perform calculations or summaries on groups of rows in a table or view. Examples of aggregate functions are `SUM`, `MAX`, `MIN`, `COUNT`, `AVG`, etc.  
- Group functions are aggregate functions that can be used with the `GROUP BY` clause in a `SELECT` statement. The `GROUP BY` clause divides the rows of a table or view into groups based on the values of one or more columns. The aggregate functions are then applied to each group and return a single result row for each group.  
- The syntax of using group functions with the `GROUP BY` clause is:

```sql
SELECT column1, column2, ..., group_function(column)
FROM table
[WHERE condition]
GROUP BY column1, column2, ...
[HAVING group_condition]
[ORDER BY column1, column2, ...];
```

- The `WHERE` clause is used to filter the rows before grouping them. The `HAVING` clause is used to filter the groups after applying the aggregate functions. The `ORDER BY` clause is used to sort the result rows by one or more columns. 
- The columns in the `SELECT` list must be either the columns used in the `GROUP BY` clause or the columns used in the aggregate functions. Otherwise, the query will return an error. 
- The columns used in the `GROUP BY` clause can be either the column names or the column aliases. They can also be expressions or functions, as long as they are not aggregate functions. 
- The `GROUP BY` clause can be omitted if the query does not need to group the rows. In this case, the aggregate functions will be applied to all the rows in the table or view and return a single result row. 
- Oracle and MySQL support some different aggregate functions. For example, Oracle has the `LISTAGG` function that concatenates the values of a column into a string, while MySQL has the `GROUP_CONCAT` function that does the same thing. MySQL also has some JSON aggregation functions, such as `JSON_ARRAYAGG` and `JSON_OBJECTAGG`, that return JSON arrays or objects from the values of a column.  
- Here are some examples of using group functions with the `GROUP BY` clause in Oracle and MySQL:

```sql
-- Oracle example: Find the total sales and average sales of each product category
SELECT category, SUM(sales) AS total_sales, AVG(sales) AS average_sales
FROM products
GROUP BY category
ORDER BY total_sales DESC;

-- MySQL example: Find the number of customers and the list of customer names in each country
SELECT country, COUNT(*) AS customer_count, GROUP_CONCAT(name) AS customer_list
FROM customers
GROUP BY country
HAVING customer_count > 10
ORDER BY customer_count DESC;
```