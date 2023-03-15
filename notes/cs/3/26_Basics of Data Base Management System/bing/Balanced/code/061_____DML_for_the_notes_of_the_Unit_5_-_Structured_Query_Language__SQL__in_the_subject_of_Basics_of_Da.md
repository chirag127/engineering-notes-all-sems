### DML

Data Manipulation Language (DML) is a class of SQL statements that are used to query, edit, add and delete row-level data from database tables or views  . The main DML statements are:

- **SELECT**: retrieve data from one or more tables or views .
- **INSERT**: add new rows of data to a table or view  .
- **UPDATE**: modify existing rows of data in a table or view  .
- **DELETE**: remove existing rows of data from a table or view  .

DML statements can be used with various clauses, such as WHERE, GROUP BY, HAVING, ORDER BY, etc., to filter, aggregate, sort, or limit the data that is returned or affected.

DML statements can also be used with subqueries, joins, functions, expressions, and operators to perform complex operations on the data.

DML statements are executed by the database engine, which checks the syntax, semantics, and permissions of the statements, and then performs the requested actions on the data.

DML statements can be used in various contexts, such as interactive SQL sessions, stored procedures, triggers, functions, or applications that connect to the database.

DML statements can be classified into two types: read-only and write-only.

- Read-only DML statements are those that only retrieve data from the database, such as SELECT.
- Write-only DML statements are those that modify the data in the database, such as INSERT, UPDATE, and DELETE.

Write-only DML statements can affect the integrity, consistency, and concurrency of the data, and therefore they are subject to various constraints, rules, and mechanisms, such as primary keys, foreign keys, check constraints, default values, triggers, transactions, locks, etc., to ensure the data quality and prevent data anomalies.