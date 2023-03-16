#### CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

SQL queries are expressions that define the set of data to be retrieved from the database. They can be classified into different types based on their purpose and syntax. Some of the common types of SQL queries are:

- DDL (Data Definition Language): These queries are used to create, alter, rename, drop, or truncate the physical structure of the tables in the database. For example, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
- DML (Data Manipulation Language): These queries are used to insert, update, delete, or select the data in the tables. For example, `INSERT INTO`, `UPDATE`, `DELETE`, `SELECT`, etc.
- DCL (Data Control Language): These queries are used to grant or revoke permissions and access rights to the users or roles in the database. For example, `GRANT`, `REVOKE`, etc.
- TCL (Transaction Control Language): These queries are used to manage the transactions in the database, such as committing, rolling back, or saving the changes. For example, `COMMIT`, `ROLLBACK`, `SAVEPOINT`, etc.
- DQL (Data Query Language): These queries are used to query the data from the tables using various clauses, operators, functions, and keywords. For example, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `JOIN`, `UNION`, `DISTINCT`, `COUNT`, `SUM`, `AVG`, etc.

To write SQL queries in MySQL, one needs to follow these steps:

- Make sure that you have a database management application (such as MySQL Workbench, Sequel Pro, etc.) or a command-line interface (such as MySQL Shell, MySQL Client, etc.) to connect to the MySQL server and execute the queries.
- Understand the database and its hierarchy, such as the database name, the table names, the column names, the data types, the primary keys, the foreign keys, the indexes, the constraints, etc.
- Find out which fields are in the tables and what kind of data they store. For example, `name` is a `VARCHAR` field that stores the name of the customer, `price` is a `DECIMAL` field that stores the price of the product, etc.
- Begin writing a SQL query to pull your desired data from the tables using the appropriate syntax, keywords, clauses, operators, and functions. For example, `SELECT name, price FROM products WHERE price > 100;` will select the name and price of the products that have a price greater than 100.
- Run the query and check the result set. If the query is valid and successful, it will return the data that matches the query criteria. If the query is invalid or unsuccessful, it will return an error message that indicates the problem. For example, `ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'pric FROM products WHERE price > 100' at line 1` means that there is a typo in the query (`pric` instead of `price`).
- Modify the query if needed to refine the result set or perform additional operations on the data. For example, `SELECT name, price FROM products WHERE price > 100 ORDER BY price DESC;` will sort the result set by price in descending order.