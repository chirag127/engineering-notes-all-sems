### Joins

- Joins are commands that combine rows from two or more tables, based on a related column between those tables  .
- Joins are useful when a user wants to extract data from tables that have one-to-many or many-to-many relationships .
- There are four main types of joins: inner join, left join, right join, and full join   .
- An inner join returns only the rows that match in both tables   .
- A left join returns all the rows from the left table, and the matching rows from the right table, or null if there is no match   .
- A right join returns all the rows from the right table, and the matching rows from the left table, or null if there is no match   .
- A full join returns all the rows from both tables, and null values for the columns that do not match    .
- The syntax for joins is as follows:

```sql
SELECT column_name(s)
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;
```

- The JOIN keyword can be replaced by INNER JOIN, LEFT JOIN, RIGHT JOIN, or FULL JOIN to specify the type of join .
- The ON clause specifies the join condition, which is the column or columns that are used to relate the tables  .
- The ORDER BY clause can be used to sort the result set by one or more columns .
- Here is an example of an inner join between two tables, Customers and Orders, based on the CustomerID column:

```sql
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;
```

- This query returns the customer name and order ID for each order that has a matching customer ID in both tables.