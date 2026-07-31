### Joins

Joins are used in SQL to combine data from two or more tables. The tables are related by a common column, known as a key. There are several types of joins, including:

1. **Inner Join**: This join returns only the rows from both tables that satisfy the given join condition. In other words, it returns only the rows that have matching values in both tables.

2. **Left Outer Join**: This join returns all the rows from the left table and the matching rows from the right table. If there is no match, the result will contain NULL values for all columns of the right table.

3. **Right Outer Join**: This join returns all the rows from the right table and the matching rows from the left table. If there is no match, the result will contain NULL values for all columns of the left table.

4. **Full Outer Join**: This join returns all the rows from both tables. If there is no match, the result will contain NULL values for all columns of the table that does not have a matching row.

5. **Cross Join**: This join returns the Cartesian product of the two tables, i.e., it returns all possible combinations of rows from both tables.

6. **Self Join**: This join is used to join a table with itself. It is often used to find relationships within the same table.

These are the main types of joins used in SQL to combine data from two or more tables. Each type of join serves a specific purpose and can be used to achieve different results. It is important to understand the differences between the different types of joins in order to use them effectively in a database management system.