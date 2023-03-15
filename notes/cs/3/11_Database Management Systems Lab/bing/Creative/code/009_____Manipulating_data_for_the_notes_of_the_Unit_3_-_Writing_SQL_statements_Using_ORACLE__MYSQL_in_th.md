# Manipulating data using SQL statements in Oracle or MySQL

- SQL stands for Structured Query Language, which is a standard language for accessing and manipulating data in relational database management systems (RDBMS) such as Oracle or MySQL.
- SQL has several sub-languages, such as Data Definition Language (DDL), Data Manipulation Language (DML), Data Control Language (DCL), and Data Query Language (DQL).
- Data Manipulation Language (DML) comprises the SQL statements that modify stored data but not the schema or database objects. The main DML statements are INSERT, UPDATE, DELETE, and SELECT.
- INSERT statement is used to add new rows of data to a table. The syntax is:

```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
```

- UPDATE statement is used to modify existing rows of data in a table. The syntax is:

```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

- DELETE statement is used to remove existing rows of data from a table. The syntax is:

```sql
DELETE FROM table_name WHERE condition;
```

- SELECT statement is used to query data from one or more tables. The syntax is:

```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
```

- Oracle and MySQL are two popular RDBMS that support SQL and DML statements. However, they may have some differences in syntax, data types, functions, operators, and features. Therefore, it is important to check the documentation of each RDBMS before writing SQL statements for them.