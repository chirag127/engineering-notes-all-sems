# Queries and Subqueries in SQL

## What is a query?

- A query is a request for data or information from a database table or combination of tables.
- A query can be written in SQL (Structured Query Language), which is a standard language for accessing and manipulating databases.
- A query can perform various operations on the data, such as selecting, inserting, updating, deleting, sorting, filtering, grouping, aggregating, joining, etc.
- A query can return a result set, which is a collection of rows that match the criteria specified in the query.
- A query can be executed by a database management system (DBMS), which is a software that manages the storage and retrieval of data in a database.

## What is a subquery?

- A subquery is a query that is nested inside another query, also known as the outer query or the main query.
- A subquery can be used to return data that will be used in the outer query as a condition, a value, or a table.
- A subquery can be placed in various clauses of the outer query, such as the WHERE clause, the HAVING clause, the FROM clause, or the SELECT clause.
- A subquery can be classified into two types: correlated and non-correlated.
- A correlated subquery is a subquery that depends on the outer query for its values. It is executed once for each row of the outer query.
- A non-correlated subquery is a subquery that does not depend on the outer query for its values. It is executed only once and returns a single value or a set of values.

## Examples of subqueries

- A subquery in the WHERE clause can be used to filter the rows of the outer query based on the result of the subquery. For example, the following query returns the customers who have ordered more than the average order amount:

```sql
SELECT customer_id, customer_name, order_amount
FROM customers
WHERE order_amount > (SELECT AVG(order_amount) FROM customers);
```

- A subquery in the HAVING clause can be used to filter the groups of the outer query based on the result of the subquery. For example, the following query returns the products that have been ordered more than 10 times in the last month:

```sql
SELECT product_id, product_name, COUNT(order_id) AS order_count
FROM products
JOIN orders ON products.product_id = orders.product_id
WHERE order_date BETWEEN '2023-02-01' AND '2023-02-28'
GROUP BY product_id, product_name
HAVING COUNT(order_id) > (SELECT 10);
```

- A subquery in the FROM clause can be used to create a temporary table that can be joined with other tables in the outer query. For example, the following query returns the products that have the highest price in each category:

```sql
SELECT p.product_id, p.product_name, p.product_price, p.category_id, c.category_name
FROM products p
JOIN (SELECT category_id, MAX(product_price) AS max_price
      FROM products
      GROUP BY category_id) m
ON p.category_id = m.category_id AND p.product_price = m.max_price
JOIN categories c
ON p.category_id = c.category_id;
```

- A subquery in the SELECT clause can be used to return a single value or a set of values as a column in the outer query. For example, the following query returns the total number of orders and the average order amount for each customer:

```sql
SELECT customer_id, customer_name, 
       (SELECT COUNT(order_id) FROM orders WHERE customer_id = c.customer_id) AS order_count,
       (SELECT AVG(order_amount) FROM orders WHERE customer_id = c.customer_id) AS order_average
FROM customers c;
```