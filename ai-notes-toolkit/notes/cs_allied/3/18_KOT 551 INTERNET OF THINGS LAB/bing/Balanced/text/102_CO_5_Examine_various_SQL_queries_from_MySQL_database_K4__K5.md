# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and it is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

Some of the objectives of this topic are:

- To understand the basic syntax and structure of SQL queries.
- To learn how to create, use, and drop databases and tables in MySQL.
- To learn how to insert, update, delete, and select data from tables in MySQL.
- To learn how to use various clauses, operators, functions, and keywords in SQL queries to filter, sort, group, and aggregate data in MySQL.
- To learn how to join multiple tables and perform subqueries and nested queries in MySQL.

## Basic Syntax and Structure of SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you sent to the database; after that, you expect the database will respond to the question by sending back the data.

The basic syntax of a SQL query is:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column1, column2, ...
HAVING condition
ORDER BY column1, column2, ...
LIMIT number;
```

The `SELECT` clause specifies the columns or expressions to be returned in the result set. You can use `*` to select all columns from the table.

The `FROM` clause specifies the table or tables from which to retrieve the data. You can use aliases to give a table or a column a different name.

The `WHERE` clause specifies the conditions that must be met for the rows to be selected. You can use various operators and logical expressions to combine multiple conditions.

The `GROUP BY` clause groups the rows that have the same values in the specified columns. You can use aggregate functions such as `SUM`, `COUNT`, `AVG`, `MIN`, and `MAX` to perform calculations on each group.

The `HAVING` clause specifies the conditions that must be met for the groups to be selected. It is similar to the `WHERE` clause but it is applied after the `GROUP BY` clause.

The `ORDER BY` clause sorts the rows in the result set by one or more columns. You can use `ASC` or `DESC` to specify the ascending or descending order.

The `LIMIT` clause limits the number of rows returned in the result set. You can use an offset to specify the starting point of the result set.

Not all clauses are required in a SQL query. The minimum requirement is the `SELECT` and `FROM` clauses. The order of the clauses is fixed and cannot be changed.

## Creating, Using, and Dropping Databases and Tables in MySQL

A database is a collection of related data organized in a logical way. A table is a structure that stores data in rows and columns. Each column has a name and a data type. Each row has a unique identifier called a primary key.

To create a database in MySQL, you can use the `CREATE DATABASE` command. For example:

```sql
CREATE DATABASE db1;
```

This command creates a database named `db1`. You can use the `SHOW DATABASES` command to list all the databases in MySQL.

To use a database in MySQL, you can use the `USE` command. For example:

```sql
USE db1;
```

This command sets the current database to `db1`. You can use the `SELECT DATABASE()` function to check the current database.

To drop a database in MySQL, you can use the `DROP DATABASE` command. For example:

```sql
DROP DATABASE db1;
```

This command deletes the database named `db1` and all its tables and data. You should be careful when using this command as it cannot be undone.

To create a table in MySQL, you can use the `CREATE TABLE` command. For example:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  gender CHAR(1)
);
```

This command creates a table named `students` with four columns: `id`, `name`, `age`, and `gender`. The `id` column is the primary key and it cannot be null or duplicated. The `name` column is a variable-length string and it cannot be null. The `age` column