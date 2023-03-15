# Unit 5 - Structured Query Language (SQL)

## Introduction

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational databases.
- SQL can perform various tasks, such as creating, querying, updating, deleting, and modifying data and database objects.
- SQL is divided into several sublanguages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- SQL follows a set of rules and syntax, which may vary slightly depending on the database management system (DBMS) used, such as Oracle, MySQL, SQL Server, etc.

## Data Definition Language (DDL)

- DDL is used to define and modify the structure of database objects, such as tables, views, indexes, constraints, etc.
- DDL commands include CREATE, ALTER, DROP, RENAME, and TRUNCATE.
- CREATE is used to create a new database object, such as a table or a view.
- ALTER is used to modify the structure or attributes of an existing database object, such as adding, deleting, or renaming columns or constraints in a table.
- DROP is used to delete an existing database object, such as a table or a view, and all its data and dependencies.
- RENAME is used to change the name of an existing database object, such as a table or a view.
- TRUNCATE is used to delete all the data from an existing table, but not the table structure or its dependencies.

## Data Manipulation Language (DML)

- DML is used to insert, update, delete, and retrieve data from database tables.
- DML commands include INSERT, UPDATE, DELETE, and SELECT.
- INSERT is used to add one or more rows of data to a table.
- UPDATE is used to modify one or more rows of data in a table based on a condition.
- DELETE is used to remove one or more rows of data from a table based on a condition.
- SELECT is used to query data from one or more tables based on a condition, and optionally sort, group, or aggregate the results.

## Data Control Language (DCL)

- DCL is used to control the access and permissions of users and roles on database objects and data.
- DCL commands include GRANT, REVOKE, and DENY.
- GRANT is used to give a user or a role a specific privilege or permission on a database object or data, such as SELECT, INSERT, UPDATE, DELETE, etc.
- REVOKE is used to take back a previously granted privilege or permission from a user or a role on a database object or data.
- DENY is used to explicitly prevent a user or a role from having a specific privilege or permission on a database object or data.

## Data Query Language (DQL)

- DQL is a subset of DML that is used to query data from database tables using the SELECT command.
- DQL can use various clauses, operators, functions, and keywords to specify the data to be retrieved, such as WHERE, ORDER BY, GROUP BY, HAVING, JOIN, UNION, DISTINCT, etc.
- WHERE is used to filter the rows of data based on a condition.
- ORDER BY is used to sort the rows of data based on one or more columns in ascending or descending order.
- GROUP BY is used to group the rows of data based on one or more columns and apply an aggregate function, such as SUM, AVG, COUNT, MIN, MAX, etc.
- HAVING is used to filter the groups of data based on a condition involving an aggregate function.
- JOIN is used to combine the data from two or more tables based on a common column or condition, such as INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN, CROSS JOIN, etc.
- UNION is used to combine the results of two or more SELECT queries into a single result set, eliminating any duplicate rows.
- DISTINCT is used to eliminate any duplicate rows from the result set of a SELECT query.