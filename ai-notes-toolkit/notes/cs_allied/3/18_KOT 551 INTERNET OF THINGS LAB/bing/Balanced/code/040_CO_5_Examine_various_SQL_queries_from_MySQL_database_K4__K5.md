# CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on data.

Some of the objectives of this topic are:

- To understand the basic syntax and structure of SQL queries.
- To learn how to create, use, and drop databases and tables in MySQL.
- To learn how to insert, update, delete, and select data from tables in MySQL.
- To learn how to use various clauses, operators, functions, and keywords in SQL queries to filter, sort, group, and aggregate data in MySQL.
- To learn how to use joins, subqueries, and views to combine data from multiple tables in MySQL.

## Basic Syntax and Structure of SQL Queries

A SQL query is an expression, similar to an English sentence, that defines the set of data to be retrieved from the database. You can think of a SQL query as a question you sent to the database; after that, you expect the database will respond to the question by sending back the data.

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

The keywords in the syntax are:

- SELECT: specifies the columns or expressions to be returned in the result set.
- FROM: specifies the tables or views to be queried.
- WHERE: specifies the conditions to filter the rows from the tables or views.
- GROUP BY: specifies the columns or expressions to group the rows by.
- HAVING: specifies the conditions to filter the groups.
- ORDER BY: specifies the columns or expressions to sort the result set by.
- LIMIT: specifies the maximum number of rows to be returned in the result set.

Not all the keywords are mandatory in a SQL query. The only required keyword is SELECT, followed by at least one column or expression. The other keywords are optional and can be used depending on the requirement of the query.

## Creating, Using, and Dropping Databases and Tables in MySQL

A database is a collection of related data organized in a logical way. A table is a structure that stores data in rows and columns. Each column has a name and a data type, and each row has a unique identifier called a primary key.

To create a database in MySQL, you can use the CREATE DATABASE statement. For example:

```sql
CREATE DATABASE db1;
```

This statement creates a database named db1. To use a database in MySQL, you can use the USE statement. For example:

```sql
USE db1;
```

This statement sets the current database to db1. To drop a database in MySQL, you can use the DROP DATABASE statement. For example:

```sql
DROP DATABASE db1;
```

This statement deletes the database db1 and all its tables and data.

To create a table in MySQL, you can use the CREATE TABLE statement. For example:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  grade CHAR(1)
);
```

This statement creates a table named students with four columns: id, name, age, and grade. The data types of the columns are INT, VARCHAR, INT, and CHAR, respectively. The id column is also defined as the primary key of the table, which means it cannot have duplicate or null values.

To drop a table in MySQL, you can use the DROP TABLE statement. For example:

```sql
DROP TABLE students;
```

This statement deletes the table students and all its data.