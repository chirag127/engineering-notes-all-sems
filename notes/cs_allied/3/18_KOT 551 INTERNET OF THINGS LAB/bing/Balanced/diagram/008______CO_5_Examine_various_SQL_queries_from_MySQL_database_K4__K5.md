#### CO 5 Examine various SQL queries from MySQL database K4, K5

SQL stands for Structured Query Language and is a standard language for accessing and manipulating data in relational databases. MySQL is one of the most popular open-source relational database management systems (RDBMS) that uses SQL to perform various operations on the data.

Some of the objectives of this topic are:

- To understand the basic syntax and structure of SQL queries.
- To learn how to create, use, and drop databases and tables in MySQL.
- To learn how to insert, update, delete, and select data from tables in MySQL.
- To learn how to use various clauses, operators, functions, and keywords in SQL queries to filter, sort, group, and aggregate data in MySQL.
- To learn how to join multiple tables and perform subqueries and nested queries in MySQL.

Some of the key points of this topic are:

- A SQL query is an expression that defines the set of data to be retrieved from the database. A SQL query consists of one or more statements that follow a specific syntax and order.
- A SQL statement can be classified into two categories: Data Definition Language (DDL) and Data Manipulation Language (DML). DDL statements are used to create, alter, rename, drop, and truncate databases and tables. DML statements are used to insert, update, delete, and select data from tables.
- A SQL query can also use various clauses, operators, functions, and keywords to modify the result set. Some of the common ones are:

  - WHERE clause: used to filter the rows based on a condition.
  - ORDER BY clause: used to sort the rows based on one or more columns.
  - GROUP BY clause: used to group the rows based on one or more columns and apply aggregate functions on them.
  - HAVING clause: used to filter the groups based on a condition.
  - LIMIT clause: used to limit the number of rows returned by the query.
  - DISTINCT keyword: used to eliminate duplicate rows from the result set.
  - AS keyword: used to assign aliases to columns or tables for readability or convenience.
  - AND, OR, and NOT operators: used to combine multiple conditions in the WHERE or HAVING clause.
  - LIKE, IN, BETWEEN, and NULL operators: used to perform pattern matching, set membership, range, and null value tests on the columns.
  - COUNT, SUM, AVG, MIN, MAX, and other aggregate functions: used to calculate summary statistics on the columns or groups.
  - CONCAT, SUBSTRING, UPPER, LOWER, and other string functions: used to manipulate string values in the columns.
  - NOW, DATE, TIME, and other date and time functions: used to manipulate date and time values in the columns.
  - IF, CASE, and other control flow functions: used to perform conditional logic on the columns.

- A SQL query can also join multiple tables to retrieve data from related tables. There are different types of joins, such as:

  - INNER JOIN: returns only the rows that match in both tables based on a join condition.
  - LEFT JOIN: returns all the rows from the left table and the matching rows from the right table, or NULL if no match is found.
  - RIGHT JOIN: returns all the rows from the right table and the matching rows from the left table, or NULL if no match is found.
  - FULL JOIN: returns all the rows from both tables, regardless of whether they match or not.
  - CROSS JOIN: returns the Cartesian product of both tables, i.e., every possible combination of rows from both tables.

- A SQL query can also perform subqueries and nested queries to use the result of one query as an input for another query. A subquery is a query that is nested inside another query, usually in the WHERE, HAVING, or SELECT clause. A nested query is a query that contains one or more subqueries.

Some of the examples of SQL queries from MySQL database are:

- To create a database named `db1`:

  ```sql
  CREATE DATABASE db1;
  ```

- To use the database `db1`:

  ```sql
  USE db1;
  ```

- To create a table named `students` with four columns: `id`, `name`, `age`, and `grade`:

  ```sql
  CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    grade CHAR(1)
  );
  ```

- To insert four records into the `students` table:

  ```sql