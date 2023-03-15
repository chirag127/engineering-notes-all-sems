### Aggregate Functions

Aggregate functions are used in SQL to perform calculations on a set of values and return a single value. They are often used with the `GROUP BY` clause to group the result set by one or more columns. Here are some commonly used aggregate functions:

1. `COUNT`: Returns the number of rows in the specified column.
2. `SUM`: Returns the sum of all values in the specified column.
3. `AVG`: Returns the average of all values in the specified column.
4. `MIN`: Returns the minimum value in the specified column.
5. `MAX`: Returns the maximum value in the specified column.

Example:
```SQL
SELECT COUNT(*) FROM Customers;
```
This query returns the total number of rows in the `Customers` table.

```SQL
SELECT AVG(Price) FROM Products;
```
This query returns the average price of all products in the `Products` table.

```SQL
SELECT MIN(Price), MAX(Price) FROM Products;
```
This query returns the minimum and maximum price of all products in the `Products` table.

```SQL
SELECT COUNT(*), AVG(Price) FROM Products GROUP BY Category;
```
This query returns the number of products and the average price of products in each category.