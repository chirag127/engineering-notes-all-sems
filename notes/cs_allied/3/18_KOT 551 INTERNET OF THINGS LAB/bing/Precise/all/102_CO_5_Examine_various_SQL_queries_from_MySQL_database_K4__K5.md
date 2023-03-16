# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL (Structured Query Language) is a standard language used to manage and manipulate data stored in relational databases. MySQL is one of the most popular open-source relational database management systems that use SQL.

Here are some common SQL queries used in MySQL:

1. **SELECT**: Used to retrieve data from one or more tables in a database. For example, to retrieve all data from a table named `customers`, the query would be `SELECT * FROM customers;`.

2. **INSERT**: Used to add new records to a table. For example, to insert a new customer record into the `customers` table, the query would be `INSERT INTO customers (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@email.com');`.

3. **UPDATE**: Used to modify existing records in a table. For example, to update the email address of a customer in the `customers` table, the query would be `UPDATE customers SET email = 'new.email@email.com' WHERE first_name = 'John' AND last_name = 'Doe';`.

4. **DELETE**: Used to delete records from a table. For example, to delete a customer record from the `customers` table, the query would be `DELETE FROM customers WHERE first_name = 'John' AND last_name = 'Doe';`.

5. **CREATE**: Used to create a new table in a database. For example, to create a new table named `orders` with columns `order_id`, `customer_id`, and `order_date`, the query would be `CREATE TABLE orders (order_id INT, customer_id INT, order_date DATE);`.

6. **ALTER**: Used to modify the structure of an existing table. For example, to add a new column named `order_total` to the `orders` table, the query would be `ALTER TABLE orders ADD COLUMN order_total DECIMAL(10,2);`.

7. **DROP**: Used to delete a table from a database. For example, to delete the `orders` table from the database, the query would be `DROP TABLE orders;`.

These are just a few examples of the many SQL queries that can be used in a MySQL database. It is important to have a good understanding of these queries and their syntax in order to effectively manage and manipulate data in a MySQL database.