#### CO 5 Examine various SQL queries from MySQL database K4, K5

1. **SELECT**: The SELECT statement is used to query a database and retrieve data from one or more tables. The basic syntax is `SELECT column1, column2, ... FROM table_name;`. The `*` wildcard can be used to select all columns from a table.
2. **INSERT**: The INSERT statement is used to add new records to a table. The basic syntax is `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`.
3. **UPDATE**: The UPDATE statement is used to modify existing records in a table. The basic syntax is `UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;`.
4. **DELETE**: The DELETE statement is used to delete existing records from a table. The basic syntax is `DELETE FROM table_name WHERE condition;`.
5. **CREATE**: The CREATE statement is used to create a new table in a database. The basic syntax is `CREATE TABLE table_name (column1 datatype, column2 datatype, ...);`.
6. **ALTER**: The ALTER statement is used to add, modify, or delete columns in an existing table. The basic syntax is `ALTER TABLE table_name ADD column_name datatype;` to add a new column, `ALTER TABLE table_name MODIFY COLUMN column_name datatype;` to modify an existing column, and `ALTER TABLE table_name DROP COLUMN column_name;` to delete a column.
7. **DROP**: The DROP statement is used to delete a table from a database. The basic syntax is `DROP TABLE table_name;`.
8. **INDEX**: The INDEX statement is used to create an index on one or more columns of a table to improve query performance. The basic syntax is `CREATE INDEX index_name ON table_name (column1, column2, ...);`.
9. **JOIN**: The JOIN statement is used to combine rows from two or more tables based on a related column between them. The basic syntax is `SELECT column1, column2, ... FROM table1 JOIN table2 ON table1.column_name = table2.column_name;`.

These are some of the basic SQL queries that can be used in a MySQL database. It is important to note that the syntax may vary slightly depending on the version of MySQL being used. It is recommended to consult the official MySQL documentation for the most up-to-date information.