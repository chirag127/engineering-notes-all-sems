### Unions

- A union is a set operation that combines the results of two or more SELECT statements into a single result set.
- The SELECT statements must have the same number of columns, and the columns must have the same data types and be in the same order.
- The syntax for a union is as follows:
```
SELECT column1, column2, ...
FROM table1
UNION
SELECT column1, column2, ...
FROM table2;
```
- The UNION operator removes duplicate rows from the result set.
- If you want to include duplicate rows in the result set, use the UNION ALL operator instead of UNION.
- The UNION operator can be used to combine the results of multiple SELECT statements from different tables, as long as the data types and column order match.
- The UNION operator can also be used to combine the results of multiple SELECT statements from the same table, for example to combine the results of two different WHERE conditions.
- The result set of a UNION operation can be sorted using the ORDER BY clause. The ORDER BY clause must be placed after the last SELECT statement.
- The result set of a UNION operation can also be limited using the LIMIT clause. The LIMIT clause must be placed after the last SELECT statement.
