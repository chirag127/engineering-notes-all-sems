### Aggregate Functions

Aggregate functions are used to perform calculations on a set of values and return a single value. They are often used with the `GROUP BY` clause to group the result set by one or more columns. Here are some commonly used aggregate functions in SQL:

1. `COUNT`: Returns the number of rows in a table.
2. `SUM`: Returns the sum of all values in a column.
3. `AVG`: Returns the average of all values in a column.
4. `MIN`: Returns the minimum value in a column.
5. `MAX`: Returns the maximum value in a column.

These functions can be used with the `SELECT` statement to retrieve the desired result. For example, to find the total number of rows in a table, you can use the following query:

```SQL
SELECT COUNT(*) FROM table_name;
```

To find the sum of all values in a column, you can use the following query:

```SQL
SELECT SUM(column_name) FROM table_name;
```

Similarly, you can use the other aggregate functions to perform calculations on the data in a table. It is important to note that these functions ignore `NULL` values when performing calculations. If you want to include `NULL` values, you can use the `COALESCE` function to replace them with a default value.