### Joins

Joins are used to combine rows from two or more tables based on a related column between them. Joining tables is one of the most common operations performed in a relational database system. There are different types of joins, which are discussed below.

1. Inner Join
   - Inner join returns only the matching rows between the two tables based on the specified condition.
   - Syntax: `SELECT * FROM table1 INNER JOIN table2 ON table1.column = table2.column;`

2. Left Join
   - Left join returns all the rows from the left table and matching rows from the right table. If there are no matching rows in the right table, null values are returned.
   - Syntax: `SELECT * FROM table1 LEFT JOIN table2 ON table1.column = table2.column;`

3. Right Join
   - Right join returns all the rows from the right table and matching rows from the left table. If there are no matching rows in the left table, null values are returned.
   - Syntax: `SELECT * FROM table1 RIGHT JOIN table2 ON table1.column = table2.column;`

4. Full Outer Join
   - Full outer join returns all the rows from both tables and null values where there is no match.
   - Syntax: `SELECT * FROM table1 FULL OUTER JOIN table2 ON table1.column = table2.column;`

5. Self Join
   - Self join is used to join a table to itself. It is useful when a table has a foreign key to itself.
   - Syntax: `SELECT * FROM table1 t1 INNER JOIN table1 t2 ON t1.column = t2.column;`

6. Cross Join
   - Cross join returns the Cartesian product of the two tables. It returns all possible combinations of rows between the tables.
   - Syntax: `SELECT * FROM table1 CROSS JOIN table2;`

7. Natural Join
   - Natural join returns all the rows from both tables where the column names match. It eliminates the duplicate column in the result.
   - Syntax: `SELECT * FROM table1 NATURAL JOIN table2;`

Joins are powerful tools for combining data from multiple tables. They allow us to create complex queries that retrieve data from multiple tables in a single query. It is important to understand the different types of joins and their syntax to use them effectively in database applications.