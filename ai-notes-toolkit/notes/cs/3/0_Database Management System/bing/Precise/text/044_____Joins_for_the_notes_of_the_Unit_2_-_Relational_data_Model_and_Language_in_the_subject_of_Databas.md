### Joins

Joins are used in SQL to combine data from two or more tables. The tables are related by a common column, also known as a key. The result of a join is a new table that contains all the columns from the tables being joined, and rows that satisfy the join condition.

There are several types of joins, including:

1. **Inner Join**: Returns only the rows from both tables that satisfy the join condition.
2. **Left Outer Join**: Returns all the rows from the left table and the matching rows from the right table. If there is no match, the result will contain NULL for all columns of the right table.
3. **Right Outer Join**: Returns all the rows from the right table and the matching rows from the left table. If there is no match, the result will contain NULL for all columns of the left table.
4. **Full Outer Join**: Returns all the rows from both tables. If there is no match, the result will contain NULL for all columns of the table without a matching row.
5. **Cross Join**: Returns the Cartesian product of the two tables, i.e., all possible combinations of rows from both tables.

Joins can be used to answer questions that require data from multiple tables. For example, to find the name and salary of all employees who work in a certain department, we can join the Employee and Department tables on the DepartmentID column, which is common to both tables.