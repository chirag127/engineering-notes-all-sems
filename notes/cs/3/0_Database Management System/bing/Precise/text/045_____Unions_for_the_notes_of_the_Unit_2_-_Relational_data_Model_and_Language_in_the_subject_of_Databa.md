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
- If you want to include duplicate rows in the result set, you can use the UNION ALL operator instead of UNION.
- The UNION operator can be used to combine the results of multiple SELECT statements from different tables, as long as the columns in the SELECT statements match in number, data type, and order.
- The UNION operator can also be used to combine the results of multiple SELECT statements from the same table, for example, to combine the results of two different WHERE clauses.
- The UNION operator is useful for combining data from multiple tables or for combining data from the same table based on different criteria.
- The result set of a UNION operation is sorted by default, but you can use the ORDER BY clause to specify a custom sort order.
- The UNION operator can be combined with other set operators, such as INTERSECT and EXCEPT, to perform more complex set operations.
