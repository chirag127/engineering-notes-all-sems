### Aggregate Functions

Aggregate functions are special functions in SQL that perform calculations on a set of values and return a single value. They are often used with the `GROUP BY` clause to summarize data into groups, and with the `HAVING` clause to filter groups based on a condition.

Some of the common aggregate functions in SQL are:

- `AVG`: Returns the average of the values in a column.
- `COUNT`: Returns the number of rows or non-null values in a column.
- `MAX`: Returns the maximum value in a column.
- `MIN`: Returns the minimum value in a column.
- `SUM`: Returns the sum of the values in a column.
- `STDEV`: Returns the standard deviation of the values in a column.
- `VAR`: Returns the variance of the values in a column.

To use an aggregate function, you need to specify the column name or expression as an argument inside parentheses. For example:

```sql
-- Find the average salary of employees
SELECT AVG(salary) FROM employees;

-- Find the number of products in each category
SELECT category, COUNT(*) FROM products GROUP BY category;

-- Find the highest price of products in each category
SELECT category, MAX(price) FROM products GROUP BY category;
```

You can also use aggregate functions with other clauses, such as `WHERE`, `ORDER BY`, and `LIMIT`. For example:

```sql
-- Find the total sales of products in 2022
SELECT SUM(sales) FROM products WHERE year = 2022;

-- Find the top 5 categories with the most products
SELECT category, COUNT(*) FROM products GROUP BY category ORDER BY COUNT(*) DESC LIMIT 5;

-- Find the categories with an average price above 100
SELECT category, AVG(price) FROM products GROUP BY category HAVING AVG(price) > 100;
```

Aggregate functions are useful for analyzing and summarizing data in SQL. They can help you find patterns, trends, and statistics from your data. You can also combine multiple aggregate functions using commas or nested queries. For example:

```sql
-- Find the category with the highest average price
SELECT category, AVG(price) FROM products GROUP BY category ORDER BY AVG(price) DESC LIMIT 1;

-- Find the average number of products per category
SELECT AVG(count) FROM (SELECT category, COUNT(*) AS count FROM products GROUP BY category) AS subquery;
```