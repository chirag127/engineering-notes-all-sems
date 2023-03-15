### Joins

Joins are used to combine rows from two or more tables, based on a related column between them. There are several types of joins, including:

1. **Inner Join**: Returns only the rows from both tables where there is a match. If there is no match, no rows are returned.
2. **Left Join**: Returns all the rows from the left table and the matching rows from the right table. If there is no match, the result will still contain all rows from the left table, with NULL values in the columns of the right table.
3. **Right Join**: Returns all the rows from the right table and the matching rows from the left table. If there is no match, the result will still contain all rows from the right table, with NULL values in the columns of the left table.
4. **Full Outer Join**: Returns all the rows from both tables, with NULL values in the columns where there is no match.
5. **Cross Join**: Returns the Cartesian product of the two tables, i.e., all possible combinations of rows from both tables.

Joins are a fundamental concept in relational databases and are used to combine data from multiple tables in a meaningful way. They are typically used in SELECT, UPDATE, and DELETE statements.