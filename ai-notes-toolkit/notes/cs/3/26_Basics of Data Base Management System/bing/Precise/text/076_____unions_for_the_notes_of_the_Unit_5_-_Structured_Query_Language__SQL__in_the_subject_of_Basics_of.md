### Unions
- The `UNION` operator is used to combine the results of two or more `SELECT` statements into a single result set.
- The `UNION` operator removes duplicate rows from the result set.
- The `UNION ALL` operator can be used to retain duplicate rows in the result set.
- The number and order of columns in the `SELECT` statements must be the same for the `UNION` operator to work.
- The data types of the corresponding columns in the `SELECT` statements must be compatible.
- The `UNION` operator can be used to combine data from different tables, as long as the above conditions are met.
- The `UNION` operator can be used with the `ORDER BY` clause to sort the result set.
- The `UNION` operator can be used with the `LIMIT` clause to limit the number of rows returned in the result set.
- The `UNION` operator can be used with aggregate functions such as `SUM`, `COUNT`, `AVG`, `MAX`, and `MIN` to perform calculations on the combined result set.