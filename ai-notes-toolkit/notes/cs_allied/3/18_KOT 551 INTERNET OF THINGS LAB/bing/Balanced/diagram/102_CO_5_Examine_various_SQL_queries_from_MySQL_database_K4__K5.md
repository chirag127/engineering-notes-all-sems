# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and it is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

## SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you sent to the database; after that, you expect the database will respond to the question by sending back the data.

There are different types of SQL queries, depending on the purpose and complexity of the query. Some of the common types are:

- Data Definition Language (DDL) queries: These are used to create, alter, or delete the structure of the database objects, such as tables, views, indexes, etc. For example, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
- Data Manipulation Language (DML) queries: These are used to insert, update, or delete the data in the database tables. For example, `INSERT INTO`, `UPDATE`, `DELETE`, etc.
- Data Query Language (DQL) queries: These are used to select and retrieve the data from the database tables. For example, `SELECT`, `WHERE`, `GROUP BY`, etc.
- Data Control Language (DCL) queries: These are used to grant or revoke the permissions and access rights to the database objects. For example, `GRANT`, `REVOKE`, etc.
- Transaction Control Language (TCL) queries: These are used to manage the transactions in the database, such as committing or rolling back the changes. For example, `COMMIT`, `ROLLBACK`, etc.

## MySQL Queries

MySQL is a RDBMS that supports SQL as the language for querying and manipulating the data. MySQL generally follows the ANSI SQL standard, although there are a few cases where MySQL performs operations differently than the recognized standard.

To execute MySQL queries, you need to have a database management application (such as MySQL Workbench, Sequel Pro, etc.) and a connection to the MySQL server. You can also use online MySQL editors, such as the one provided by W3Schools, to practice and run MySQL queries.

Some of the basic steps to query a MySQL database are:

- Understand your database and its hierarchy. A database consists of one or more tables, each table has one or more columns, and each column has a specific data type and constraints.
- Find out which fields are in your tables. You can use the `DESCRIBE` or `SHOW COLUMNS` commands to see the structure and attributes of a table.
- Begin writing a SQL query to pull your desired data. You can use various clauses, operators, functions, and keywords to specify the conditions and criteria for your query. You can also use subqueries, joins, unions, and other techniques to combine data from multiple tables or sources.
- Run your query and check the results. You can use the `;` symbol to end your query and execute it. You can also use the `LIMIT` clause to limit the number of rows returned by your query. You can also use the `EXPLAIN` command to see how MySQL executes your query and optimize it if needed.

## Examples of MySQL Queries

Here are some examples of MySQL queries for different purposes. Note that these queries are based on the sample database provided by W3Schools, which you can use to practice and run the queries.

- To create a new database named `mydb`, you can use the following DDL query:

```sql
CREATE DATABASE mydb;
```

- To use the database named `mydb`, you can use the following DQL query:

```sql
USE mydb;
```

- To create a new table named `customers` with four columns (`id`, `name`, `email`, and `country`), you can use the following DDL query:

```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE,
  country VARCHAR(50)
);
```

- To insert a new record into the `customers` table, you can use the following DML query:

```sql
INSERT INTO customers (id, name, email, country) VALUES (1, 'Alice', 'alice@example.com', 'USA');
```

- To update the `country` column