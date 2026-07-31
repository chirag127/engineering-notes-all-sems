# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and it is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

Some of the objectives of this topic are:

- To understand the basic syntax and structure of SQL queries.
- To learn how to create, select, use, and drop databases in MySQL.
- To learn how to create, alter, rename, drop, and truncate tables in MySQL.
- To learn how to insert, update, delete, and select records in MySQL tables.
- To learn how to use various clauses, operators, functions, and keywords in SQL queries to filter, sort, group, and manipulate data in MySQL tables.
- To learn how to use joins, subqueries, views, and indexes in SQL queries to combine and optimize data from multiple tables in MySQL.

## Basic Syntax and Structure of SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you send to the database; after that, you expect the database will respond to the question by sending back the data.

The basic syntax of a SQL query is:

```sql
SELECT column1, column2, ...
FROM table1, table2, ...
WHERE condition1, condition2, ...
GROUP BY column1, column2, ...
HAVING condition1, condition2, ...
ORDER BY column1, column2, ...
LIMIT number;
```

The basic structure of a SQL query consists of the following clauses:

- SELECT: specifies the columns or expressions to be returned in the result set.
- FROM: specifies the tables or views to be queried.
- WHERE: specifies the conditions to filter the rows from the tables or views.
- GROUP BY: specifies the columns or expressions to group the rows by.
- HAVING: specifies the conditions to filter the groups.
- ORDER BY: specifies the columns or expressions to sort the result set by.
- LIMIT: specifies the maximum number of rows to be returned in the result set.

Not all clauses are required in a SQL query. The only mandatory clause is the SELECT clause. The order of the clauses is also fixed and cannot be changed.

## Creating, Selecting, Using, and Dropping Databases in MySQL

A database is a collection of related tables, views, and other objects that store and organize data. MySQL allows you to create, select, use, and drop databases using the following commands:

- CREATE DATABASE: creates a new database with the given name. For example:

```sql
CREATE DATABASE db1;
```

- SHOW DATABASES: lists all the databases in the MySQL server. For example:

```sql
SHOW DATABASES;
```

- USE: selects a database to work with. For example:

```sql
USE db1;
```

- DROP DATABASE: deletes a database and all its objects. For example:

```sql
DROP DATABASE db1;
```

## Creating, Altering, Renaming, Dropping, and Truncating Tables in MySQL

A table is a structure that stores data in rows and columns. Each table has a name and a set of columns that define the attributes of the data. Each column has a name, a data type, and optionally some constraints. Each row has a unique identifier called a primary key. MySQL allows you to create, alter, rename, drop, and truncate tables using the following commands:

- CREATE TABLE: creates a new table with the given name and columns. For example:

```sql
CREATE TABLE student (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  gender CHAR(1)
);
```

- SHOW TABLES: lists all the tables in the current database. For example:

```sql
SHOW TABLES;
```

- DESCRIBE: shows the structure and details of a table. For example:

```sql
DESCRIBE student;
```

- ALTER TABLE: modifies the structure or properties of a table. For example:

```sql
ALTER TABLE student ADD COLUMN address VARCHAR(100);
```

- RENAME TABLE: changes the name of a table. For example:

```sql
RENAME TABLE student TO student_info;
```

- DROP TABLE: deletes a table and all its data. For example:

```sql
DROP TABLE student_info;
```

- TRUNCATE TABLE: deletes