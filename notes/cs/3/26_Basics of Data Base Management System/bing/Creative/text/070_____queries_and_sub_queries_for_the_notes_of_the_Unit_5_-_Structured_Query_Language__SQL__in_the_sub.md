### Queries and Subqueries in SQL

- A query is a request for data from a database that follows the syntax and rules of the Structured Query Language (SQL).
- A subquery, also known as a nested query or an inner query, is a query within another query that provides data for the outer query.
- A subquery can be used in different clauses of an SQL statement, such as the SELECT, FROM, WHERE, HAVING, or JOIN clause.
- A subquery can return a single value, a single row, a single column, or a table of values or rows.
- A subquery can be correlated or uncorrelated. A correlated subquery depends on the outer query for its values, while an uncorrelated subquery can be executed independently of the outer query.
- A subquery can be used for various purposes, such as filtering, aggregation, comparison, or existence testing.

Some examples of subqueries are:

- A subquery in the SELECT clause that returns a single value:

```sql
SELECT name, salary, (SELECT AVG(salary) FROM employees) AS average_salary
FROM employees;
```

- A subquery in the FROM clause that returns a table:

```sql
SELECT name, department, salary
FROM (SELECT * FROM employees WHERE salary > 5000) AS high_paid;
```

- A subquery in the WHERE clause that returns a single row:

```sql
SELECT name, address, phone
FROM customers
WHERE customer_id = (SELECT customer_id FROM orders WHERE order_id = 1001);
```

- A subquery in the WHERE clause that returns a single column:

```sql
SELECT name, product, quantity, price
FROM orders
WHERE product IN (SELECT product FROM products WHERE category = 'Electronics');
```

- A subquery in the WHERE clause that returns a table:

```sql
SELECT name, product, quantity, price
FROM orders
WHERE (product, quantity) IN (SELECT product, MAX(quantity) FROM orders GROUP BY product);
```

- A subquery in the HAVING clause that returns a single value:

```sql
SELECT product, SUM(quantity) AS total_quantity
FROM orders
GROUP BY product
HAVING SUM(quantity) > (SELECT AVG(quantity) FROM orders);
```

- A subquery in the JOIN clause that returns a table:

```sql
SELECT e.name, e.department, m.name AS manager
FROM employees e
JOIN (SELECT name, employee_id FROM employees WHERE position = 'Manager') m
ON e.manager_id = m.employee_id;
```

- A correlated subquery in the WHERE clause that returns a single value:

```sql
SELECT name, salary
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department = e.department);
```

- A subquery with the EXISTS operator that returns a boolean value:

```sql
SELECT name, address, phone
FROM customers c
WHERE EXISTS (SELECT * FROM orders WHERE customer_id = c.customer_id);
```