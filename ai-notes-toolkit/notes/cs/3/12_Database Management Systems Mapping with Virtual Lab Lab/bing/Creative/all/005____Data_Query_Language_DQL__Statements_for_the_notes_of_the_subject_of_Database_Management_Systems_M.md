# Data Query Language (DQL) Statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Data Query Language (DQL) is a subset of SQL (Structured Query Language) that is used to retrieve data from a relational database.
- DQL statements are composed of clauses, expressions, predicates, and keywords that specify the criteria for the data to be returned.
- The most common DQL statement is the SELECT statement, which has the following syntax:

```sql
SELECT [DISTINCT] column_list
FROM table_list
[WHERE search_condition]
[GROUP BY group_by_list]
[HAVING search_condition]
[ORDER BY order_by_list]
[LIMIT row_limit]
[OFFSET row_offset];
```

- The SELECT clause specifies the columns or expressions to be returned in the result set. The DISTINCT keyword eliminates duplicate rows from the result set.
- The FROM clause specifies the tables or views to be queried. The tables or views can be joined using various join types, such as inner join, left join, right join, full join, cross join, natural join, etc.
- The WHERE clause specifies the filter condition for the rows to be returned. The condition can be a logical expression that combines multiple predicates using logical operators, such as AND, OR, NOT, etc.
- The GROUP BY clause specifies the grouping criteria for the rows to be aggregated. The grouping columns or expressions must be included in the SELECT clause. The GROUP BY clause is often used with aggregate functions, such as SUM, AVG, COUNT, MIN, MAX, etc.
- The HAVING clause specifies the filter condition for the groups to be returned. The condition can be a logical expression that involves aggregate functions or grouping columns or expressions.
- The ORDER BY clause specifies the sorting order for the rows or groups to be returned. The order can be ascending (ASC) or descending (DESC). The default order is ascending. The ORDER BY clause can also use column aliases or ordinal numbers to refer to the columns or expressions in the SELECT clause.
- The LIMIT clause specifies the maximum number of rows or groups to be returned. The LIMIT clause can be used for pagination or performance optimization.
- The OFFSET clause specifies the number of rows or groups to be skipped before returning the result set. The OFFSET clause can be used for pagination or performance optimization.

- Some examples of DQL statements are:

```sql
-- Select all columns from the customers table
SELECT * FROM customers;

-- Select the first name, last name, and email of the customers whose country is 'USA'
SELECT first_name, last_name, email
FROM customers
WHERE country = 'USA';

-- Select the total number of orders and the average order amount for each customer
SELECT customer_id, COUNT(*) AS total_orders, AVG(order_amount) AS avg_order_amount
FROM orders
GROUP BY customer_id;

-- Select the customer name and the total order amount for the customers who have placed more than 10 orders
SELECT c.first_name || ' ' || c.last_name AS customer_name, SUM(o.order_amount) AS total_order_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(*) > 10;

-- Select the top 5 products by sales amount in descending order
SELECT p.product_name, SUM(o.order_amount) AS sales_amount
FROM products p
JOIN order_details od ON p.product_id = od.product_id
JOIN orders o ON od.order_id = o.order_id
GROUP BY p.product_id, p.product_name
ORDER BY sales_amount DESC
LIMIT 5;
```

- DQL statements can be executed using various tools or applications, such as command-line interfaces, graphical user interfaces, web browsers, programming languages, etc.
- DQL statements can be tested and verified using virtual lab environments, such as SQL Fiddle, DB Fiddle, SQLZOO, etc. These environments allow users to create and populate tables, write and run queries, and see the results online.