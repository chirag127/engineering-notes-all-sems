# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and it is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems that uses SQL as its query language.

## Types of SQL queries

There are five main types of SQL queries that can be used to perform different operations on the data in a MySQL database. They are:

- DDL (Data Definition Language): These queries are used to define the structure and schema of the database, such as creating, altering, renaming, dropping, or truncating tables and columns. For example, `CREATE TABLE students (id INT, name VARCHAR(50), age INT);` is a DDL query that creates a table called students with three columns: id, name, and age.

- DML (Data Manipulation Language): These queries are used to insert, update, delete, or modify the data in the database tables. For example, `INSERT INTO students VALUES (1, 'Alice', 20);` is a DML query that inserts a new record into the students table.

- DQL (Data Query Language): These queries are used to retrieve and display the data from the database tables. They usually start with the keyword `SELECT` and can use various clauses and functions to filter, sort, group, or aggregate the data. For example, `SELECT name, age FROM students WHERE age > 18 ORDER BY name;` is a DQL query that selects the name and age of the students who are older than 18 and sorts them by name.

- DCL (Data Control Language): These queries are used to control the access and permissions of the database users and roles. They include commands such as `GRANT`, `REVOKE`, `DENY`, or `ALTER USER`. For example, `GRANT SELECT, UPDATE ON students TO user1;` is a DCL query that grants the user1 the permission to select and update the data in the students table.

- TCL (Transaction Control Language): These queries are used to manage the transactions in the database, which are a set of logical operations that are executed as a unit. They include commands such as `BEGIN`, `COMMIT`, `ROLLBACK`, or `SAVEPOINT`. For example, `BEGIN; UPDATE students SET age = age + 1; COMMIT;` is a TCL query that starts a transaction, updates the age of all the students by adding one, and commits the changes to the database.

## How to write SQL queries in MySQL

To write and execute SQL queries in MySQL, you need to have a database management application (such as MySQL Workbench, Sequel Pro, or phpMyAdmin) that can connect to your MySQL server and provide a graphical or command-line interface for interacting with the database. Alternatively, you can use an online SQL editor (such as W3Schools or LearnSQL) that allows you to run SQL queries on a sample database.

The general steps for writing SQL queries in MySQL are:

- Understand your database and its hierarchy: A MySQL database consists of one or more tables that store the data in rows and columns. Each table has a name and a set of columns that define the attributes of the data. Each column has a name, a data type, and optionally some constraints (such as primary key, foreign key, unique, not null, etc.). Each row in a table represents a record or an entity that has a value for each column. A database can also have views, indexes, triggers, stored procedures, and functions that are derived from the tables and can perform some operations on the data.

- Find out which fields are in your tables: To write SQL queries, you need to know the names and data types of the columns in your tables, as well as the relationships between them. You can use the `SHOW` or `DESCRIBE` commands to display the information about the tables and columns in your database. For example, `SHOW TABLES;` will list all the tables in your database, and `DESCRIBE students;` will show the details of the columns in the students table.

- Begin writing a SQL query to pull your desired data: Depending on the type and purpose of your query, you need to use the appropriate keywords, clauses, operators, and functions to specify what data you want to retrieve, manipulate, or control from the database. You can use the online SQL reference or tutorials to learn the syntax and usage of the SQL commands and functions. You can also use the online SQL editors to practice and test your queries on a sample