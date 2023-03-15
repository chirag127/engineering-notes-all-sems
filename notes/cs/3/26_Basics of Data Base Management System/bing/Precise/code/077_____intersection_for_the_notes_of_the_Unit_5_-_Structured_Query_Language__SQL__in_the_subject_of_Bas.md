### Intersection
- The `INTERSECT` operator in SQL is used to combine two `SELECT` statements, but returns rows only from the first `SELECT` statement that are identical to a row in the second `SELECT` statement.
- This means that it returns only the common rows between the two `SELECT` statements.
- The syntax for using the `INTERSECT` operator is as follows:
```
SELECT column1, column2, ...
FROM table1
INTERSECT
SELECT column1, column2, ...
FROM table2;
```
- The number and order of the columns must be the same in both `SELECT` statements, and the data types must be compatible.
- `INTERSECT` returns only distinct rows, meaning that if there are duplicate rows in the result, only one of them will be returned.
- If you want to return all rows, including duplicates, you can use the `UNION ALL` operator instead of `INTERSECT`.
- `INTERSECT` can be useful when you want to find common data between two tables. For example, you might use it to find customers who have placed an order in both the current month and the previous month.