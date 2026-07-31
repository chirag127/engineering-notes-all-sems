# Unit 6 - Creating procedure and functions in the subject of Database Management Systems Lab

## Introduction

- A database management system (DBMS) is a software that allows users to create, manipulate, and manage data in a structured way.
- A DBMS consists of several components, such as data, database schema, database engine, database access language, and procedures.
- Procedures refer to general instructions to use a DBMS, such as how to install, login, logout, backup, restore, and generate reports.
- Procedures can also refer to specific instructions to perform certain operations on data, such as how to insert, update, delete, and select data.
- Procedures that perform operations on data are also called stored procedures, views, and functions.

## Stored procedures

- A stored procedure is a set of SQL statements that can be executed as a single unit.
- A stored procedure can accept input parameters and return output parameters or result sets.
- A stored procedure can be created using the CREATE PROCEDURE statement, and executed using the EXECUTE or EXEC statement.
- A stored procedure can improve the performance, security, and maintainability of a database application, by reducing the network traffic, enforcing access control, and encapsulating the business logic.
- A stored procedure can be modified using the ALTER PROCEDURE statement, and deleted using the DROP PROCEDURE statement.

## Views

- A view is a virtual table that contains the result of a SQL query.
- A view can be created using the CREATE VIEW statement, and queried using the SELECT statement.
- A view can simplify the access to complex or frequently used queries, by hiding the underlying tables and columns, and providing a meaningful name.
- A view can also provide a level of abstraction and security, by restricting the access to certain columns or rows of the underlying tables.
- A view can be modified using the ALTER VIEW statement, and deleted using the DROP VIEW statement.

## Functions

- A function is a named set of SQL statements that returns a single value or a table of values.
- A function can be created using the CREATE FUNCTION statement, and invoked using the SELECT statement or as part of an expression.
- A function can be used to perform calculations, validations, conversions, or manipulations on data, by encapsulating the logic and reusing the code.
- A function can be classified into two types: scalar functions and table-valued functions.
- A scalar function returns a single value of a specific data type, while a table-valued function returns a table of values.
- A function can be modified using the ALTER FUNCTION statement, and deleted using the DROP FUNCTION statement.