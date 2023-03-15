Hello, I am Sydney, your AI assistant. I can help you with your study material for the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System. Here is the content on aggregate functions:

### Aggregate functions
- Aggregate functions are functions that operate on a set of values and return a single value.
- Aggregate functions are often used with the `GROUP BY` clause to calculate summary statistics for each group of rows.
- Some common aggregate functions are:
  - `COUNT`: returns the number of values in a set or the number of rows that match a condition.
  - `SUM`: returns the sum of all values in a set.
  - `AVG`: returns the average of all values in a set.
  - `MIN`: returns the minimum value in a set.
  - `MAX`: returns the maximum value in a set.
- The syntax of using aggregate functions is:

```sql
SELECT aggregate_function(column_name)
FROM table_name
WHERE condition
GROUP BY column_name
HAVING condition
ORDER BY column_name;
```

- The `WHERE` clause is used to filter the rows before applying the aggregate function.
- The `GROUP BY` clause is used to divide the rows into groups based on the values of one or more columns.
- The `HAVING` clause is used to filter the groups after applying the aggregate function.
- The `ORDER BY` clause is used to sort the results based on the values of one or more columns.
- Example: To find the total sales and average sales of each product category from the `sales` table, we can use the following query:

```sql
SELECT category, SUM(amount) AS total_sales, AVG(amount) AS average_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;
```

- This query will return the following result:

| category | total_sales | average_sales |
|----------|-------------|---------------|
| Electronics | 12000 | 3000 |
| Furniture | 8000 | 2000 |
| Books | 6000 | 1500 |
| Clothing | 4000 | 1000 |