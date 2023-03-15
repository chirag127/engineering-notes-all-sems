### Unions
- The `UNION` operator is used to combine the result-set of two or more `SELECT` statements.
- Each `SELECT` statement within the `UNION` must have the same number of columns.
- The columns must also have similar data types.
- The columns in each `SELECT` statement must also be in the same order.
- The `UNION` operator selects only distinct values by default. To allow duplicate values, use the `UNION ALL` operator.
- Syntax:
```SQL
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```
- Example: The following SQL statement returns the cities (only distinct values) from both the "Customers" and the "Suppliers" table:
```SQL
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
```