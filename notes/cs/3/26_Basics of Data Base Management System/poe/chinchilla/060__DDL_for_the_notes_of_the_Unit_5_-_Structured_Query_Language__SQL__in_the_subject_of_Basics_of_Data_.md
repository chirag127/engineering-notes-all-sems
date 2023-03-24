### DDL for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

In the world of database management, Structured Query Language (SQL) is a widely used language for managing and manipulating databases. SQL allows users to create, modify, and delete database objects using Data Definition Language (DDL) statements.

In this unit, we will learn about DDL statements and how they are used to create and modify database objects. Here are some important points to keep in mind:

- DDL statements are used to create, modify, and delete database objects such as tables, views, indexes, and constraints.
- The CREATE statement is used to create new database objects. For example, the CREATE TABLE statement is used to create a new table.
- The ALTER statement is used to modify existing database objects. For example, the ALTER TABLE statement is used to add or remove columns from a table.
- The DROP statement is used to delete database objects. For example, the DROP TABLE statement is used to delete a table.
- Constraints are used to enforce rules on the data in a table. The CREATE TABLE statement can be used to add constraints to a table.
- Views are virtual tables that are created from one or more tables. The CREATE VIEW statement is used to create a view.

Here are some examples of DDL statements:

- CREATE TABLE customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(50), customer_email VARCHAR(50));
- ALTER TABLE customers ADD customer_phone VARCHAR(20);
- DROP TABLE customers;
- CREATE TABLE orders (order_id INT PRIMARY KEY, customer_id INT, order_date DATE, total_amount DECIMAL(10,2), FOREIGN KEY (customer_id) REFERENCES customers(customer_id));
- CREATE VIEW order_details AS SELECT order_id, customer_name, order_date, total_amount FROM orders JOIN customers ON orders.customer_id = customers.customer_id;

By understanding DDL statements and how they are used, you will be able to create, modify, and delete database objects with ease. Remember to always use caution when making changes to your database and to test your statements thoroughly before implementing them in a production environment.