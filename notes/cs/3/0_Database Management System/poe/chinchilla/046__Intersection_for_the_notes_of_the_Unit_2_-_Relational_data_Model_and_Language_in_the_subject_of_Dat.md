### Intersection

In the relational model, intersection is an operator that returns only the common rows between two tables. The result of the intersection operation is a new table that contains only the rows that exist in both tables. 

The syntax for intersection is as follows:

```
SELECT * 
FROM table1
INTERSECT
SELECT *
FROM table2;
```

Here are some important points to keep in mind about intersection:

- Both tables must have the same number of columns and the columns must have the same data type for the intersection to be valid.
- The order of the columns in the tables does not matter.
- The resulting table does not contain duplicate rows. If there are duplicate rows in either of the tables, they will be eliminated in the intersection operation.
- If there are null values in the tables, the intersection operation will ignore them. This means that if a row in one table has a null value in a column, and the corresponding row in the other table has a non-null value in that same column, the row will still be included in the result of the intersection.
- Intersection is a set operation, which means that the order of the rows in the resulting table is not guaranteed to be the same as the order in either of the input tables.

Here's an example to illustrate the use of intersection:

```
SELECT *
FROM employees
INTERSECT
SELECT *
FROM managers;
```

This query returns a table that contains only the rows that exist in both the employees and managers tables. The resulting table will have the same columns as both input tables, and will contain only the rows where an employee is also a manager.

In summary, intersection is a useful operator in the relational model that allows us to find only the common rows between two tables. It is important to keep in mind the rules and limitations of intersection when using it in SQL queries.