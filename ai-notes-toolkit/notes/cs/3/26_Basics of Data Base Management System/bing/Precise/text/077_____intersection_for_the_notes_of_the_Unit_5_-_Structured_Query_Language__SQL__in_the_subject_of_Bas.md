### Intersection
- The `INTERSECT` operator in SQL is used to combine two `SELECT` statements, but returns rows only from the first `SELECT` statement that are identical to a row in the second `SELECT` statement.
- The `INTERSECT` operator returns only distinct rows that are in both result sets.
- The number and the order of the columns must be the same in both `SELECT` statements, and the data types must be compatible.
- The basic syntax of the `INTERSECT` operator is as follows:
```
SELECT column1, column2, ...
FROM table1
INTERSECT
SELECT column1, column2, ...
FROM table2;
```
- Here is an example that uses the `INTERSECT` operator to return the customers who have placed an order in both 2018 and 2019:
```
SELECT customer_id
FROM orders
WHERE order_date >= '2018-01-01' AND order_date < '2019-01-01'
INTERSECT
SELECT customer_id
FROM orders
WHERE order_date >= '2019-01-01' AND order_date < '2020-01-01';
```
- This query returns the `customer_id` of customers who have placed an order in both 2018 and 2019.