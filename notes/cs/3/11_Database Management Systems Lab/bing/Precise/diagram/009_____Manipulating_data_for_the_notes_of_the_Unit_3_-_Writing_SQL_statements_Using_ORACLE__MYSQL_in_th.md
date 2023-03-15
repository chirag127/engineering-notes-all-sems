### Manipulating data for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. **Data Manipulation Language (DML)** is a subset of SQL used to manipulate data in a database. It includes commands such as `INSERT`, `UPDATE`, `DELETE`, and `SELECT`.
2. `INSERT` is used to add new rows of data to a table. The basic syntax is `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...)`.
3. `UPDATE` is used to modify existing data in a table. The basic syntax is `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition`.
4. `DELETE` is used to remove rows from a table. The basic syntax is `DELETE FROM table_name WHERE condition`.
5. `SELECT` is used to retrieve data from a table. The basic syntax is `SELECT column1, column2, ... FROM table_name WHERE condition`.
6. These commands can be used in both ORACLE and MYSQL databases, with some minor differences in syntax and functionality.
7. It is important to carefully construct the `WHERE` condition in `UPDATE` and `DELETE` statements to ensure that only the intended rows are affected.
8. It is also important to properly sanitize user input to prevent SQL injection attacks.