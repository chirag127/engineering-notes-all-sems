# Merging Data from Multiple Tables

- In relational databases, data is often stored in multiple tables that are related by foreign keys.
- To query data from multiple tables, we can use SQL joins, which combine rows from two or more tables based on a common column value.
- There are different types of joins, such as inner join, left join, right join, and full join, that produce different results depending on how they match the rows from the tables.
- An inner join returns only the rows that have matching values in both tables.
- A left join returns all the rows from the left table, and the matching rows from the right table. If there is no match, the right side will be null.
- A right join returns all the rows from the right table, and the matching rows from the left table. If there is no match, the left side will be null.
- A full join returns all the rows from both tables, and fills the null values with the matching values if there is a match.
- To perform a join, we need to specify the join type, the tables to join, and the join condition, which is usually an equality operator (=) between the common columns.
- For example, to join the table `customers` with the table `orders` on the column `customer_id`, we can write:

```sql
SELECT customers.name, orders.order_id, orders.order_date
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;
```

- This query will return the name, order id, and order date of the customers who have placed orders.
- We can also use aliases to shorten the table names and make the query more readable, such as:

```sql
SELECT c.name, o.order_id, o.order_date
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;
```

- We can also join more than two tables by adding more join clauses, such as:

```sql
SELECT c.name, o.order_id, o.order_date, p.product_name, p.price
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN products p
ON o.product_id = p.product_id;
```

- This query will return the name, order id, order date, product name, and price of the customers who have ordered products.
- We can also use different join types to get different results, such as:

```sql
SELECT c.name, o.order_id, o.order_date
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;
```

- This query will return the name of all the customers, and the order id and order date of the customers who have placed orders. The customers who have not placed orders will have null values in the order columns.