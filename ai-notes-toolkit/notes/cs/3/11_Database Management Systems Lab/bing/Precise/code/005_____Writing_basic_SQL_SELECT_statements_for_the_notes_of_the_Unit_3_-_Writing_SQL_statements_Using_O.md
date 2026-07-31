### Writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. The SELECT statement is used to retrieve data from a database table.
2. The basic syntax of the SELECT statement is as follows: `SELECT column1, column2, ... FROM table_name;`
3. To retrieve all columns from a table, the `*` wildcard character can be used in place of the column names: `SELECT * FROM table_name;`
4. The SELECT statement can include a WHERE clause to filter the rows returned by the query: `SELECT column1, column2, ... FROM table_name WHERE condition;`
5. Multiple conditions can be combined in the WHERE clause using the AND and OR operators: `SELECT column1, column2, ... FROM table_name WHERE condition1 AND/OR condition2;`
6. The SELECT statement can also include an ORDER BY clause to sort the rows returned by the query: `SELECT column1, column2, ... FROM table_name ORDER BY column_name [ASC/DESC];`
7. The SELECT statement can be used to retrieve data from multiple tables using a JOIN operation: `SELECT column1, column2, ... FROM table_name1 JOIN table_name2 ON condition;`
8. The SELECT statement can include aggregate functions such as COUNT, SUM, AVG, MIN, and MAX to perform calculations on the data: `SELECT COUNT(column_name), SUM(column_name), AVG(column_name), MIN(column_name), MAX(column_name) FROM table_name;`
9. The SELECT statement can include a GROUP BY clause to group the rows returned by the query: `SELECT column1, column2, ... FROM table_name GROUP BY column_name;`
10. The SELECT statement can include a HAVING clause to filter the groups returned by the query: `SELECT column1, column2, ... FROM table_name GROUP BY column_name HAVING condition;`