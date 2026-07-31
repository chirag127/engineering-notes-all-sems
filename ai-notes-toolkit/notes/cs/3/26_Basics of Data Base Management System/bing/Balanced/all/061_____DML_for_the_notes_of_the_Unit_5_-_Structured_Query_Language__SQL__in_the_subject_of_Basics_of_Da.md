# DML

DML stands for Data Manipulation Language. It is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views   . The main DML statements are:

- SELECT: retrieve data from one or more tables or views .
- INSERT: add new rows to a table or view   .
- UPDATE: modify existing rows in a table or view   .
- DELETE: remove existing rows from a table or view   .

DML statements can be used to store, modify, retrieve, delete and update data in a database. They can also be used with other SQL clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, and LIMIT, to filter, aggregate, sort, and limit the data returned by the query.

Some examples of DML statements are:

- SELECT * FROM customers; -- returns all the rows and columns from the customers table
- INSERT INTO orders (order_id, customer_id, order_date) VALUES (1, 101, '2022-01-01'); -- adds a new row to the orders table with the specified values
- UPDATE products SET price = price * 1.1 WHERE category = 'Electronics'; -- increases the price of all the products in the Electronics category by 10%
- DELETE FROM employees WHERE department = 'Sales'; -- removes all the employees who work in the Sales department

DML statements are different from DDL (Data Definition Language) statements, which are used to create, alter, or drop database objects and their structure, such as tables, views, indexes, constraints, etc. DML statements are also different from DCL (Data Control Language) statements, which are used to grant or revoke permissions and roles to users and groups in a database.