# Manipulating Data

In Unit 3 of the Database Management Systems Lab, we learn about writing SQL statements using ORACLE/MYSQL. Here are some key points to remember when manipulating data:

1. **Data Manipulation Language (DML)**: This is a subset of SQL used to retrieve, insert, update, and delete data in a database.

2. **SELECT statement**: This is used to retrieve data from one or more tables in a database. The basic syntax is `SELECT column1, column2, ... FROM table_name;`.

3. **INSERT statement**: This is used to add new rows of data to a table. The basic syntax is `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`.

4. **UPDATE statement**: This is used to modify existing data in a table. The basic syntax is `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`.

5. **DELETE statement**: This is used to delete existing data from a table. The basic syntax is `DELETE FROM table_name WHERE condition;`.

6. **WHERE clause**: This is used to filter the rows returned by a SELECT, UPDATE, or DELETE statement. The basic syntax is `SELECT column1, column2, ... FROM table_name WHERE condition;`.

7. **ORDER BY clause**: This is used to sort the rows returned by a SELECT statement. The basic syntax is `SELECT column1, column2, ... FROM table_name ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;`.

8. **GROUP BY clause**: This is used to group rows with the same values in one or more columns. The basic syntax is `SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ...;`.

9. **HAVING clause**: This is used to filter groups created by the GROUP BY clause. The basic syntax is `SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ... HAVING condition;`.

These are some of the key concepts to remember when manipulating data using SQL statements in ORACLE/MYSQL. It is important to practice writing and executing these statements to become proficient in data manipulation.