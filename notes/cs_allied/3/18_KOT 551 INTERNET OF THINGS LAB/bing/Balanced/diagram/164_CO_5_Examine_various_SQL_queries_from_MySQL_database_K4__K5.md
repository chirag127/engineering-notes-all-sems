# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on data.

## SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you send to the database; after that, you expect the database will respond to the question by sending back the data.

There are different types of SQL queries, depending on the purpose and complexity of the query. Some of the common types are:

- Data Definition Language (DDL) queries: These are used to create, modify, or delete the structure of database objects, such as tables, views, indexes, etc. For example, `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, etc.
- Data Manipulation Language (DML) queries: These are used to insert, update, or delete data in the database tables. For example, `INSERT INTO`, `UPDATE`, `DELETE`, etc.
- Data Query Language (DQL) queries: These are used to select and retrieve data from the database tables. For example, `SELECT`, `WHERE`, `GROUP BY`, etc.
- Data Control Language (DCL) queries: These are used to grant or revoke permissions and access rights to users and roles on the database objects. For example, `GRANT`, `REVOKE`, etc.
- Transaction Control Language (TCL) queries: These are used to manage the transactions that affect the data in the database tables. For example, `COMMIT`, `ROLLBACK`, `SAVEPOINT`, etc.

## MySQL Database

MySQL is a widely used RDBMS that supports SQL queries and provides various features and tools for data management, security, performance, scalability, etc. MySQL generally follows the ANSI SQL standard, although there are a few cases where MySQL performs operations differently than the recognized standard.

To work with MySQL, you need to have a database management application, such as MySQL Workbench, Sequel Pro, etc. You can also use the command-line interface (CLI) to interact with MySQL.

To perform SQL queries on MySQL, you need to follow these steps:

1. Connect to the MySQL server using your username and password.
2. Select or create a database to work with. You can use the `SHOW DATABASES` query to list the available databases, and the `USE database_name` query to select a database.
3. Create or select a table to work with. You can use the `SHOW TABLES` query to list the tables in the current database, and the `DESCRIBE table_name` query to show the structure of a table.
4. Write and execute the SQL query to perform the desired operation on the table. You can use the `;` character to end a query, and the `\G` character to display the query result in a vertical format.
5. Close the connection to the MySQL server when you are done.

## Examples of SQL Queries from MySQL Database

Here are some examples of SQL queries from MySQL database, using the `employees` table as an example. The `employees` table has the following structure and data:

| id | name | department | salary |
|----|------|------------|--------|
| 1  | John | Sales      | 5000   |
| 2  | Mary | Marketing  | 6000   |
| 3  | Bob  | IT         | 7000   |
| 4  | Alice| HR         | 8000   |

- To create the `employees` table, you can use the following DDL query:

```sql
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  department VARCHAR(50) NOT NULL,
  salary INT NOT NULL
);
```

- To insert data into the `employees` table, you can use the following DML query:

```sql
INSERT INTO employees (id, name, department, salary) VALUES
(1, 'John', 'Sales', 5000),
(2, 'Mary', 'Marketing', 6000),
(3, 'Bob', 'IT', 7000),
(4, 'Alice', 'HR', 8000);
```

- To select all the data from the `employees` table, you can use the following DQL query:

```sql
SELECT * FROM