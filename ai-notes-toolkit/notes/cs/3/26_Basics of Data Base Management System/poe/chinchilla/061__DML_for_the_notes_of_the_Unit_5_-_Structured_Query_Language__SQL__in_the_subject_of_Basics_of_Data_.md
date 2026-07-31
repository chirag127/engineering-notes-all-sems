### DML for the notes of the Unit 5 - Structured Query Language (SQL) in the subject of Basics of Data Base Management System

Data Manipulation Language (DML) is a subset of SQL used to manipulate data in a database. DML statements are used to add, delete, modify, and retrieve data from a database.

Here are some important points to remember about DML in SQL:

- DML commands are used to insert, update, and delete data in a database.
- The INSERT statement is used to add new data to a table. It is written in the following format: 

        INSERT INTO table_name (column1, column2, column3, ...)
        VALUES (value1, value2, value3, ...);

- The UPDATE statement is used to modify existing data in a table. It is written in the following format:

        UPDATE table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition;

- The DELETE statement is used to remove data from a table. It is written in the following format:

        DELETE FROM table_name
        WHERE condition;

- The SELECT statement is used to retrieve data from one or more tables in a database. It is written in the following format:

        SELECT column1, column2, ...
        FROM table_name
        WHERE condition;

- The VALUES keyword is used to specify the values to be inserted into a table. The values must be enclosed in parentheses and separated by commas.

- The WHERE clause is used to specify a condition that must be met in order for the statement to execute. It can be used with the UPDATE, DELETE, and SELECT statements.

- The SET keyword is used to specify the new values to be assigned to the columns in an UPDATE statement.

- The LIKE keyword is used to match patterns in string values. It is often used with the WHERE clause to filter results based on a specific pattern.

- The ORDER BY clause is used to sort the results of a SELECT statement in ascending or descending order based on one or more columns.

- The GROUP BY clause is used to group the results of a SELECT statement based on one or more columns.

- The HAVING clause is used to filter the results of a GROUP BY clause based on a condition.

- The JOIN keyword is used to combine data from two or more tables based on a common column.

- The INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, and FULL OUTER JOIN are different types of join operations that can be used to combine data from multiple tables.

- The UNION and UNION ALL operators are used to combine the results of two or more SELECT statements into a single result set.

- The subquery is a SELECT statement that is nested inside another SELECT statement. It is used to retrieve data that will be used in a WHERE or HAVING clause of another SELECT statement.

By understanding and applying these concepts, you will be able to effectively manipulate data in a database using DML commands in SQL.