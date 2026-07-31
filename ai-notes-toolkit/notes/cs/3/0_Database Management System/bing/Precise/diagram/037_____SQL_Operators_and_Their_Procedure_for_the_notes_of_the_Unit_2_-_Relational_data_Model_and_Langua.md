### SQL Operators and Their Procedure

SQL (Structured Query Language) is a standard language used to manage and manipulate relational databases. In the context of the Relational Data Model and Language, SQL operators are used to perform various operations on the data stored in the database.

Here are some common SQL operators and their procedures:

1. **SELECT**: The SELECT operator is used to retrieve data from one or more tables in a database. The basic syntax for the SELECT statement is as follows:
```
SELECT column1, column2, ...
FROM table_name;
```
2. **WHERE**: The WHERE operator is used to filter the records returned by the SELECT statement. The basic syntax for the WHERE clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
3. **AND, OR, NOT**: These logical operators are used in the WHERE clause to combine multiple conditions. The basic syntax for using these operators is as follows:
```
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND/OR/NOT condition2;
```
4. **ORDER BY**: The ORDER BY operator is used to sort the records returned by the SELECT statement. The basic syntax for the ORDER BY clause is as follows:
```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC/DESC], column2 [ASC/DESC], ...;
```
5. **INSERT**: The INSERT operator is used to add new records to a table. The basic syntax for the INSERT statement is as follows:
```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```
6. **UPDATE**: The UPDATE operator is used to modify existing records in a table. The basic syntax for the UPDATE statement is as follows:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
7. **DELETE**: The DELETE operator is used to delete existing records from a table. The basic syntax for the DELETE statement is as follows:
```
DELETE FROM table_name
WHERE condition;
```

These are some of the basic SQL operators and their procedures. It is important to note that the syntax and usage of these operators may vary slightly depending on the specific database management system being used. It is always a good idea to consult the documentation for the specific system to ensure proper usage.