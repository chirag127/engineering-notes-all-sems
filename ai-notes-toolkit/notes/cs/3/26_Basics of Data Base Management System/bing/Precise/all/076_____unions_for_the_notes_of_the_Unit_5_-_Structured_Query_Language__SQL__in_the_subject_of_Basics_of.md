### Unions

- The `UNION` operator is used to combine the results of two or more `SELECT` statements into a single result set.
- The `UNION` operator removes duplicate rows from the result set.
- The `UNION ALL` operator can be used to retain duplicate rows in the result set.
- The number and order of columns in the `SELECT` statements must be the same for the `UNION` operator to work.
- The data types of the corresponding columns in the `SELECT` statements must be compatible.

Example:

```
SELECT column1, column2 FROM table1
UNION
SELECT column1, column2 FROM table2;
```

This will return a result set that combines the results of the two `SELECT` statements, removing any duplicate rows.