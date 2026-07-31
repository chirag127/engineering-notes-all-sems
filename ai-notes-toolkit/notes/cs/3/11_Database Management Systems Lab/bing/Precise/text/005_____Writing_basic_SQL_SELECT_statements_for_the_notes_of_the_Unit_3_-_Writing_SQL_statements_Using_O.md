### Writing basic SQL SELECT statements for the notes of the Unit 3 - Writing SQL statements Using ORACLE /MYSQL in the subject of Database Management Systems Lab

1. The SELECT statement is used to retrieve data from a database table.
2. The basic syntax of the SELECT statement is as follows: `SELECT column1, column2, ... FROM table_name;`
3. The SELECT statement can be used to retrieve specific columns from a table by specifying the column names after the SELECT keyword.
4. The SELECT statement can also be used to retrieve all columns from a table by using the `*` wildcard character after the SELECT keyword: `SELECT * FROM table_name;`
5. The SELECT statement can be combined with the WHERE clause to filter the rows returned by the query: `SELECT column1, column2, ... FROM table_name WHERE condition;`
6. The SELECT statement can also be used to sort the rows returned by the query using the ORDER BY clause: `SELECT column1, column2, ... FROM table_name ORDER BY column_name [ASC|DESC];`
7. The SELECT statement can be used to retrieve data from multiple tables by using a JOIN clause: `SELECT column1, column2, ... FROM table1 JOIN table2 ON condition;`
8. The SELECT statement can be used to group rows and calculate aggregate values using the GROUP BY and HAVING clauses: `SELECT column1, aggregate_function(column2) FROM table_name GROUP BY column1 HAVING condition;`

These are some of the basic concepts and syntax for writing SQL SELECT statements using ORACLE/MYSQL in the subject of Database Management Systems Lab. It is important to practice writing and executing these statements to become proficient in using SQL to retrieve data from a database.