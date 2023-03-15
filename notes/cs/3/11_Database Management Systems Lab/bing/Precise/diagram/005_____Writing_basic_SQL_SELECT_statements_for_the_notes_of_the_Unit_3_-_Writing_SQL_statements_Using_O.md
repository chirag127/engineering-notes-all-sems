### Writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. The SELECT statement is used to retrieve data from a database table.
2. The basic syntax of the SELECT statement is as follows: `SELECT column1, column2, ... FROM table_name;`
3. The `*` wildcard character can be used to select all columns from a table: `SELECT * FROM table_name;`
4. The `WHERE` clause can be used to filter the rows returned by the SELECT statement: `SELECT column1, column2, ... FROM table_name WHERE condition;`
5. The `AND` and `OR` operators can be used to combine multiple conditions in the WHERE clause: `SELECT column1, column2, ... FROM table_name WHERE condition1 AND/OR condition2;`
6. The `ORDER BY` clause can be used to sort the rows returned by the SELECT statement: `SELECT column1, column2, ... FROM table_name ORDER BY column1 [ASC/DESC];`
7. The `LIMIT` clause can be used to limit the number of rows returned by the SELECT statement: `SELECT column1, column2, ... FROM table_name LIMIT number_of_rows;`
8. The `DISTINCT` keyword can be used to return only distinct (unique) values: `SELECT DISTINCT column1, column2, ... FROM table_name;`
9. The `COUNT` function can be used to count the number of rows returned by the SELECT statement: `SELECT COUNT(column_name) FROM table_name;`
10. The `GROUP BY` clause can be used to group the rows returned by the SELECT statement: `SELECT column1, COUNT(column2) FROM table_name GROUP BY column1;`
11. The `HAVING` clause can be used to filter the groups returned by the GROUP BY clause: `SELECT column1, COUNT(column2) FROM table_name GROUP BY column1 HAVING condition;`