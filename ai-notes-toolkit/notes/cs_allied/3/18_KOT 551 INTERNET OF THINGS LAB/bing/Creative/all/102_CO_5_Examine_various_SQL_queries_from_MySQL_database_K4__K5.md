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

The `SELECT` clause specifies the columns or expressions to be returned in the result set. The `FROM` clause specifies the table or tables to be queried. The `WHERE` clause specifies the conditions or filters to be applied to the rows in the table. The `GROUP BY` clause specifies the columns or expressions to be used for grouping the rows. The `HAVING` clause specifies the conditions or filters to be applied to the groups. The `ORDER BY` clause specifies the columns or expressions to be used for sorting the result set. The `LIMIT` clause specifies the maximum number of rows to be returned in the result set.

Not all of these clauses are mandatory in a SQL query. The only required clause is the `SELECT` clause. The other clauses are optional and can be used depending on the requirements of the query.

## Creating, Using, and Dropping Databases and Tables in MySQL

A database is a collection of related tables that store data. A table is a structure that organizes data into rows and columns. Each row represents a record or an entity, and each column represents an attribute or a field of the entity.

To create a database in MySQL, you can use the `CREATE DATABASE` statement. For example, to create a database named `db1`, you can use the following statement:

```sql
CREATE DATABASE db1;
```

To use a database in MySQL, you can use the `USE` statement. For example, to use the database `db1`, you can use the following statement:

```sql
USE db1;
```

To drop a database in MySQL, you can use the `DROP DATABASE` statement. For example, to drop the database `db1`, you can use the following statement:

```sql
DROP DATABASE db1;
```

To create a table in MySQL, you can use the `CREATE TABLE` statement. For example, to create a table named `students` with four columns: `id`, `name`, `age`, and `grade`, you can use the following statement:

```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT,
  grade CHAR(1)
);
```

The `CREATE TABLE` statement defines the name of the table and the columns with their data types, constraints, and default values. The `PRIMARY KEY` constraint specifies that the `id` column is the unique identifier of each row in the table. The `NOT NULL` constraint specifies that the `name` column cannot have null values. The `VARCHAR` data type specifies a variable-length string with a maximum length of 50 characters. The `CHAR` data type specifies a fixed-length string with a length of 1 character.

To drop a table in MySQL, you can use the `DROP TABLE` statement. For example, to drop the table `students`, you can use the following statement:

```sql
DROP TABLE students;
```

## Inserting, Updating, Deleting, and Selecting Data from Tables in MySQL

To insert data into a table in MySQL, you can use the `INSERT INTO` statement. For example, to insert a row into